-- User vs Agent Talk Ratio
-- Compare user messages to agent messages per conversation
SELECT
  c.session_id,
  c.title,
  COUNTIF(m.role = 'user') AS user_messages,
  COUNTIF(m.role = 'agent') AS agent_messages,
  ROUND(COUNTIF(m.role = 'user') / GREATEST(COUNTIF(m.role = 'agent'), 1), 2) AS user_to_agent_ratio
FROM `uw-voice-agents.voice_conversations.conversations` c,
  UNNEST(c.messages) AS m
GROUP BY c.session_id, c.title
ORDER BY user_to_agent_ratio DESC;
