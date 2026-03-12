-- Search Conversations by Keyword
-- Find conversations containing a specific keyword in any message
-- Replace 'financial' with your search term
SELECT
  c.session_id,
  c.title,
  m.role,
  m.content
FROM `uw-voice-agents.voice_conversations.conversations` c,
  UNNEST(c.messages) AS m
WHERE LOWER(m.content) LIKE '%financial%'
ORDER BY c.submitted_at DESC;
