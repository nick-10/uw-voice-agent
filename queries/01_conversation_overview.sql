-- Conversation Overview
-- Total sessions, average messages per conversation, date range
SELECT
  COUNT(*) AS total_conversations,
  ROUND(AVG(message_count), 1) AS avg_messages_per_conversation,
  MIN(submitted_at) AS earliest_submission,
  MAX(submitted_at) AS latest_submission,
  SUM(message_count) AS total_messages
FROM `uw-voice-agents.voice_conversations.conversations`;
