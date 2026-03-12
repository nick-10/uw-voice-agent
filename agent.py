"""ADK Agent definition — Gemini 3.0 Flash via Vertex AI."""

from google.adk import Agent

agent = Agent(
    name="uw_voice_assistant",
    model="gemini-2.5-flash-lite",
    description="A helpful voice-based conversational assistant.",
    instruction=(
        "You are a friendly, concise voice assistant. "
        "Keep responses short and conversational since the user is speaking to you. "
        "Avoid markdown, bullet points, or long lists — respond as you would in a natural conversation."
    ),
)
