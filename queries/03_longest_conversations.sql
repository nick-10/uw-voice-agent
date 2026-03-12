-- Longest Conversations
-- Top 10 conversations by message count
SELECT
  session_id,
  title,
  message_count,
  submitted_at
FROM `uw-voice-agents.voice_conversations.conversations`
ORDER BY message_count DESC
LIMIT 10;
