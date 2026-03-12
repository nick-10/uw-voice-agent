-- Recent Conversations
-- Last 20 conversations with titles, message counts, and timestamps
SELECT
  session_id,
  title,
  message_count,
  submitted_at
FROM `uw-voice-agents.voice_conversations.conversations`
ORDER BY submitted_at DESC
LIMIT 20;
