"""FastAPI conversation controller — always-on mic with pause detection & interruption."""

import asyncio, json, re, traceback
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from google.adk import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from agent import agent
from speech_services import ContinuousTranscriber, synthesize

app = FastAPI()
session_service = InMemorySessionService()
runner = Runner(agent=agent, app_name="uw_voice_agent", session_service=session_service)
_sessions: set[str] = set()

PAUSE_SECONDS = 1.5  # Wait this long after last final transcript before processing


async def _ensure_session(user_id: str, session_id: str):
    key = f"{user_id}:{session_id}"
    if key not in _sessions:
        await session_service.create_session(app_name="uw_voice_agent", user_id=user_id, session_id=session_id)
        _sessions.add(key)


def _split_sentences(text: str) -> list[str]:
    parts = re.split(r'(?<=[.!?])\s+', text)
    return [p for p in parts if p.strip()]


async def _safe_send_text(ws: WebSocket, data: str):
    try:
        await ws.send_text(data)
    except Exception:
        pass


async def _safe_send_bytes(ws: WebSocket, data: bytes):
    try:
        await ws.send_bytes(data)
    except Exception:
        pass


@app.websocket("/ws/chat")
async def ws_chat(ws: WebSocket):
    await ws.accept()
    user_id, session_id = "default", "default"
    await _ensure_session(user_id, session_id)

    loop = asyncio.get_event_loop()
    transcriber: ContinuousTranscriber | None = None
    interrupted = asyncio.Event()
    agent_speaking = False
    accumulated_text = []
    debounce_task: asyncio.Task | None = None

    async def handle_agent(transcript: str):
        """Send transcript to agent, stream TTS audio back sentence by sentence."""
        nonlocal agent_speaking
        interrupted.clear()
        agent_speaking = True
        await _safe_send_text(ws, json.dumps({"type": "response_start"}))

        agent_text = ""
        try:
            async for event in runner.run_async(
                user_id=user_id, session_id=session_id,
                new_message=types.UserContent(parts=[types.Part(text=transcript)]),
            ):
                if interrupted.is_set():
                    break
                if event.is_final_response() and event.content:
                    for part in event.content.parts:
                        if part.text:
                            agent_text += part.text
        except Exception as e:
            traceback.print_exc()
            await _safe_send_text(ws, json.dumps({"type": "error", "message": str(e)}))

        if agent_text and not interrupted.is_set():
            await _safe_send_text(ws, json.dumps({"type": "response_text", "text": agent_text}))
            for sentence in _split_sentences(agent_text):
                if interrupted.is_set():
                    break
                try:
                    audio = await asyncio.to_thread(synthesize, sentence)
                    if not interrupted.is_set():
                        await _safe_send_bytes(ws, audio)
                except Exception:
                    traceback.print_exc()

        agent_speaking = False
        await _safe_send_text(ws, json.dumps({"type": "response_end"}))

    async def debounce_and_process():
        """Wait for pause, then process accumulated transcripts."""
        nonlocal accumulated_text
        await asyncio.sleep(PAUSE_SECONDS)
        if accumulated_text:
            full_text = " ".join(accumulated_text)
            accumulated_text = []
            if len(full_text.strip()) > 2:
                await handle_agent(full_text.strip())

    async def process_stt_results():
        """Continuously read STT results, accumulate with debounce."""
        nonlocal debounce_task, accumulated_text, agent_speaking
        while True:
            result = await transcriber.results.get()
            if result is None:
                break
            await _safe_send_text(ws, json.dumps({"type": "transcript", **result}))

            if result["is_final"] and len(result["text"].strip()) > 2:
                # If agent is currently speaking, interrupt it
                if agent_speaking:
                    interrupted.set()
                    accumulated_text = []
                    await asyncio.sleep(0.1)  # Let interruption propagate

                accumulated_text.append(result["text"])
                # Reset debounce timer
                if debounce_task:
                    debounce_task.cancel()
                debounce_task = asyncio.create_task(debounce_and_process())

    try:
        while True:
            msg = await ws.receive()
            if msg["type"] == "websocket.disconnect":
                break
            elif msg.get("bytes"):
                if transcriber is None:
                    transcriber = ContinuousTranscriber(loop)
                    asyncio.create_task(process_stt_results())
                transcriber.feed(msg["bytes"])
            elif msg.get("text"):
                data = json.loads(msg["text"])
                if data.get("type") == "interrupt":
                    interrupted.set()
                    accumulated_text = []
    except WebSocketDisconnect:
        pass
    finally:
        if transcriber:
            transcriber.stop()
        if debounce_task:
            debounce_task.cancel()


app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8010)
