-- Response Length Analysis
-- Average agent response length per conversation (in characters)
SELECT
  c.session_id,
  c.title,
  ROUND(AVG(LENGTH(m.content)), 0) AS avg_agent_response_chars,
  MAX(LENGTH(m.content)) AS longest_response_chars,
  COUNT(*) AS agent_messages
FROM `uw-voice-agents.voice_conversations.conversations` c,
  UNNEST(c.messages) AS m
WHERE m.role = 'agent'
GROUP BY c.session_id, c.title
ORDER BY avg_agent_response_chars DESC;
