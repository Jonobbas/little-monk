export default async function handler(req, res) {
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });

  const apiKey = process.env.OPENAI_API_KEY;
  if (!apiKey) return res.status(503).json({ error: 'AI service is not configured yet.' });

  const { message, mood, memories = [], action, outcomeSummary } = req.body || {};
  if (!message) return res.status(400).json({ error: 'Message is required.' });

  const memoryText = memories.slice(-8).map((m, i) => `${i + 1}. ${m}`).join('\n') || 'No prior memories available.';

  const system = `You are Little Monk, a calm AI personal growth companion.\n\nMission: help the user become 1% better through reflection, memory, pattern awareness, and one small useful action.\n\nStyle: warm, concise, observant, non-judgmental. Ask thoughtful questions more often than giving lectures. Use the flow Observe -> Locate -> Soften -> Advance.\n\nDo not diagnose mental-health conditions, claim certainty about the user's psychology, or present yourself as a therapist. If there is evidence from memory, refer to it carefully as a pattern or possibility, not a fact about the person's identity.\n\nCurrent inner climate: ${mood || 'unknown'}\nCurrent daily action: ${action || 'none'}\nOutcome history summary: ${outcomeSummary || 'none yet'}\nRelevant memories:\n${memoryText}\n\nRespond in 2-5 sentences. If possible, end with one useful reflective question or one very small next action.`;

  try {
    const response = await fetch('https://api.openai.com/v1/chat/completions', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${apiKey}`
      },
      body: JSON.stringify({
        model: process.env.OPENAI_MODEL || 'gpt-4.1-mini',
        temperature: 0.7,
        messages: [
          { role: 'system', content: system },
          { role: 'user', content: message }
        ]
      })
    });

    const data = await response.json();
    if (!response.ok) return res.status(response.status).json({ error: data?.error?.message || 'AI request failed.' });

    const reply = data?.choices?.[0]?.message?.content?.trim();
    return res.status(200).json({ reply });
  } catch (error) {
    return res.status(500).json({ error: 'Unable to reach the AI service.' });
  }
}
