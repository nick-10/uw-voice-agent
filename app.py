"""FastAPI conversation controller — always-on mic with pause detection & interruption."""

import asyncio, json, os, re, traceback
from contextlib import asynccontextmanager
from datetime import datetime, timezone
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from google.cloud import storage as gcs
from google.adk import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from agent import agent
from speech_services import ContinuousTranscriber, synthesize
import database as db

session_service = InMemorySessionService()
runner = Runner(agent=agent, app_name="uw_voice_agent", session_service=session_service)
_adk_sessions: set[str] = set()

PAUSE_SECONDS = 1.5  # Wait this long after last final transcript before processing


@asynccontextmanager
async def lifespan(app: FastAPI):
    await db.init_db()
    yield

app = FastAPI(lifespan=lifespan)


async def _ensure_adk_session(user_id: str, session_id: str):
    key = f"{user_id}:{session_id}"
    if key not in _adk_sessions:
        await session_service.create_session(app_name="uw_voice_agent", user_id=user_id, session_id=session_id)
        _adk_sessions.add(key)


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


async def _generate_title(session_id: str, first_message: str):
    """Use Gemini to generate a ~3-word title for the session."""
    try:
        title_session_id = f"title_{session_id}"
        await session_service.create_session(
            app_name="uw_voice_agent", user_id="system", session_id=title_session_id
        )

        title_agent_runner = Runner(
            agent=agent, app_name="uw_voice_agent", session_service=session_service
        )

        prompt = f'Summarize this message in exactly 2-3 words as a conversation title. Return ONLY the title, nothing else. Message: "{first_message}"'
        title = ""
        async for event in title_agent_runner.run_async(
            user_id="system",
            session_id=title_session_id,
            new_message=types.UserContent(parts=[types.Part(text=prompt)]),
        ):
            if event.is_final_response() and event.content:
                for part in event.content.parts:
                    if part.text:
                        title += part.text

        title = title.strip().strip('"').strip("'")
        if title:
            await db.update_session_title(session_id, title)
    except Exception:
        traceback.print_exc()


# ─── REST API for chat history ───────────────────────────────────────────

@app.get("/api/sessions")
async def list_sessions():
    sessions = await db.get_sessions()
    return {"sessions": sessions}


@app.get("/api/sessions/{session_id}/messages")
async def get_session_messages(session_id: str):
    messages = await db.get_messages(session_id)
    return {"messages": messages}


@app.delete("/api/sessions/{session_id}")
async def delete_session(session_id: str):
    await db.delete_session(session_id)
    return {"ok": True}


GCS_BUCKET = os.environ.get("GCS_CONVERSATION_BUCKET", "uw-voice-agent-conversations")

@app.post("/api/sessions/{session_id}/submit")
async def submit_session(session_id: str):
    """Export conversation as JSON and upload to GCS bucket."""
    messages = await db.get_messages(session_id)
    if not messages:
        return {"error": "No messages in this session"}, 400

    sessions = await db.get_sessions(limit=200)
    session_meta = next((s for s in sessions if s["session_id"] == session_id), {})

    payload = {
        "session_id": session_id,
        "title": session_meta.get("title", "Untitled"),
        "submitted_at": datetime.now(timezone.utc).isoformat(),
        "message_count": len(messages),
        "messages": messages,
    }

    blob_name = f"conversations/{session_id}.json"
    try:
        client = gcs.Client()
        bucket = client.bucket(GCS_BUCKET)
        blob = bucket.blob(blob_name)
        blob.upload_from_string(
            json.dumps(payload, default=str),
            content_type="application/json",
        )
    except Exception as e:
        traceback.print_exc()
        return {"error": str(e)}

    gcs_uri = f"gs://{GCS_BUCKET}/{blob_name}"
    return {"ok": True, "gcs_uri": gcs_uri}


# ─── WebSocket chat endpoint ────────────────────────────────────────────

@app.websocket("/ws/chat")
async def ws_chat(ws: WebSocket):
    await ws.accept()

    # Create a new DB session for this connection
    db_session_id = await db.create_session()
    user_id = "web_user"

    # Use the DB session ID for ADK too
    adk_session_id = db_session_id
    await _ensure_adk_session(user_id, adk_session_id)

    # Tell the client what session they're in
    await _safe_send_text(ws, json.dumps({"type": "session_id", "session_id": db_session_id}))

    loop = asyncio.get_event_loop()
    transcriber: ContinuousTranscriber | None = None
    interrupted = asyncio.Event()
    agent_speaking = False
    accumulated_text = []
    debounce_task: asyncio.Task | None = None
    is_first_message = True

    async def handle_agent(transcript: str):
        """Send transcript to agent, stream TTS audio back sentence by sentence."""
        nonlocal agent_speaking, is_first_message
        interrupted.clear()
        agent_speaking = True
        await _safe_send_text(ws, json.dumps({"type": "response_start"}))

        # Save user message to DB
        await db.save_message(db_session_id, "user", transcript)

        # Generate title from first message (fire-and-forget)
        if is_first_message:
            is_first_message = False
            asyncio.create_task(_generate_title(db_session_id, transcript))

        agent_text = ""
        try:
            async for event in runner.run_async(
                user_id=user_id, session_id=adk_session_id,
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
            # Save agent message to DB
            await db.save_message(db_session_id, "agent", agent_text)

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
