"""Google Cloud Speech-to-Text (continuous streaming) and Text-to-Speech."""

import asyncio, os, queue, threading, time
from google.cloud import speech, texttospeech

PROJECT_ID = os.environ.get("GOOGLE_CLOUD_PROJECT", "uw-voice-agents")


class ContinuousTranscriber:
    """Continuous STT that auto-restarts streams. Designed for always-on mic."""

    def __init__(self, loop: asyncio.AbstractEventLoop):
        self._audio_q: queue.Queue[bytes | None] = queue.Queue()
        self.results: asyncio.Queue[dict | None] = asyncio.Queue()
        self._stop = threading.Event()
        self._loop = loop
        self._thread = threading.Thread(target=self._run_loop, daemon=True)
        self._thread.start()

    def feed(self, chunk: bytes):
        self._audio_q.put(chunk)

    def stop(self):
        self._stop.set()
        self._audio_q.put(None)
        asyncio.run_coroutine_threadsafe(self.results.put(None), self._loop)

    def _audio_gen(self):
        while not self._stop.is_set():
            try:
                chunk = self._audio_q.get(timeout=0.1)
            except queue.Empty:
                continue
            if chunk is None:
                break
            yield speech.StreamingRecognizeRequest(audio_content=chunk)

    def _run_loop(self):
        """Keep restarting STT streams (they timeout after ~5 min)."""
        while not self._stop.is_set():
            try:
                self._run_stream()
            except Exception:
                pass
            if not self._stop.is_set():
                time.sleep(0.2)

    def _run_stream(self):
        client = speech.SpeechClient()
        config = speech.StreamingRecognitionConfig(
            config=speech.RecognitionConfig(
                encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
                sample_rate_hertz=16000,
                language_code="en-US",
            ),
            interim_results=True,
        )
        for resp in client.streaming_recognize(config=config, requests=self._audio_gen()):
            if self._stop.is_set():
                break
            for result in resp.results:
                if result.alternatives:
                    asyncio.run_coroutine_threadsafe(
                        self.results.put({"text": result.alternatives[0].transcript, "is_final": result.is_final}),
                        self._loop,
                    )


def synthesize(text: str) -> bytes:
    """Convert text to MP3 audio bytes using Cloud Text-to-Speech."""
    client = texttospeech.TextToSpeechClient()
    resp = client.synthesize_speech(
        input=texttospeech.SynthesisInput(text=text),
        voice=texttospeech.VoiceSelectionParams(language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL),
        audio_config=texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3),
    )
    return resp.audio_content
