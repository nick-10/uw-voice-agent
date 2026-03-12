-- Full Transcript View
-- View the complete transcript of a specific conversation
-- Replace 'sample_001' with the session_id you want to view
SELECT
  c.title,
  m.role,
  m.content,
  m.timestamp
FROM `uw-voice-agents.voice_conversations.conversations` c,
  UNNEST(c.messages) AS m
WHERE c.session_id = 'sample_001'
ORDER BY m.timestamp;
