# BigQuery Queries for Voice Agent Analytics

These queries work against the external table `uw-voice-agents.voice_conversations.conversations`
which reads JSON files from `gs://uw-voice-agent-conversations/conversations/`.

## Setup
- **Project:** `uw-voice-agents`
- **Dataset:** `voice_conversations`
- **Table:** `conversations` (external, auto-reads from GCS)

## Usage
Run any query in the BigQuery console, Colab Enterprise, or `bq` CLI.
New conversations appear automatically when submitted from the voice agent UI.
