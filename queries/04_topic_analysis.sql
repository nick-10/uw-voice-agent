-- Topic Analysis
-- Group conversations by title to identify common topics
SELECT
  title,
  COUNT(*) AS conversation_count,
  ROUND(AVG(message_count), 1) AS avg_messages
FROM `uw-voice-agents.voice_conversations.conversations`
GROUP BY title
ORDER BY conversation_count DESC;
