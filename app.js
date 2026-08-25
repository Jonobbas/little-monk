const moods = {
  energised: {
    label: 'Energised',
    message: 'There is energy in you today. Give it one clear direction.',
    prompt: 'What would make today feel meaningfully used?'
  },
  calm: {
    label: 'Calm',
    message: 'A quiet day. Notice what is helping you stay steady.',
    prompt: 'What is worth protecting from this calm state?'
  },
  bored: {
    label: 'Bored',
    message: 'The sky feels flat. Curiosity may be the smallest door forward.',
    prompt: 'What is one thing you could explore for ten minutes?'
  },
  stressed: {
    label: 'Stressed',
    message: 'There is rain in the inner climate. We do not have to solve everything at once.',
    prompt: 'What is the one pressure that is taking the most space right now?'
  },
  angry: {
    label: 'Angry',
    message: 'The weather is intense. Notice it before acting from it.',
    prompt: 'What happened just before the anger rose?'
  }
};

const climateCard = document.getElementById('climateCard');
const climateMessage = document.getElementById('climateMessage');
const climateBadge = document.getElementById('climateBadge');
const moodGrid = document.getElementById('moodGrid');
const chat = document.getElementById('chat');
const chatForm = document.getElementById('chatForm');
const chatInput = document.getElementById('chatInput');
const kaizenForm = document.getElementById('kaizenForm');
const kaizenInput = document.getElementById('kaizenInput');
const kaizenSaved = document.getElementById('kaizenSaved');

const state = JSON.parse(localStorage.getItem('littleMonkState') || '{}');

function saveState() {
  localStorage.setItem('littleMonkState', JSON.stringify(state));
}

function addBubble(text, who = 'monk') {
  const bubble = document.createElement('div');
  bubble.className = `bubble ${who === 'user' ? 'user-bubble' : 'monk-bubble'}`;
  bubble.textContent = text;
  chat.appendChild(bubble);
  chat.scrollTop = chat.scrollHeight;
}

function setMood(mood, announce = true) {
  const config = moods[mood] || moods.calm;
  state.mood = mood;
  state.lastCheckIn = new Date().toISOString();
  climateCard.dataset.climate = mood;
  climateMessage.textContent = config.message;
  climateBadge.textContent = config.label;

  [...moodGrid.querySelectorAll('button')].forEach(btn => {
    btn.classList.toggle('active', btn.dataset.mood === mood);
  });

  if (announce) addBubble(config.prompt, 'monk');
  saveState();
}

moodGrid.addEventListener('click', (event) => {
  const button = event.target.closest('button[data-mood]');
  if (!button) return;
  setMood(button.dataset.mood);
});

function mentorReply(text) {
  const mood = state.mood || 'calm';
  const clean = text.trim();
  const lower = clean.toLowerCase();

  if (/tired|exhausted|burnout|drained/.test(lower)) {
    return 'What can be reduced, postponed, or made smaller today?';
  }
  if (/angry|irritated|frustrated|furious/.test(lower)) {
    return 'Before deciding what to do, what part is fact and what part is interpretation?';
  }
  if (/confused|stuck|don't know|dont know/.test(lower)) {
    return 'Let us make it smaller. What is the next decision—not the whole journey?';
  }
  if (/happy|great|excited|proud|good/.test(lower)) {
    return 'Good. What specifically created that feeling, so you can repeat it deliberately?';
  }
  if (mood === 'stressed') return 'Which part is under your control in the next 24 hours?';
  if (mood === 'bored') return 'Would action or curiosity help more right now? Name one tiny experiment.';
  if (mood === 'energised') return 'Where will this energy create the highest value today?';
  if (mood === 'angry') return 'What response would you respect yourself for tomorrow?';
  return 'What does this tell you about what matters most to you right now?';
}

chatForm.addEventListener('submit', (event) => {
  event.preventDefault();
  const text = chatInput.value.trim();
  if (!text) return;

  addBubble(text, 'user');
  state.entries = state.entries || [];
  state.entries.push({ text, mood: state.mood || 'calm', at: new Date().toISOString() });
  state.entries = state.entries.slice(-50);
  saveState();
  chatInput.value = '';

  window.setTimeout(() => addBubble(mentorReply(text), 'monk'), 350);
});

kaizenForm.addEventListener('submit', (event) => {
  event.preventDefault();
  const text = kaizenInput.value.trim();
  if (!text) return;
  state.kaizen = { text, date: new Date().toISOString().slice(0, 10) };
  saveState();
  renderKaizen();
});

function renderKaizen() {
  if (!state.kaizen?.text) return;
  kaizenSaved.classList.remove('hidden');
  kaizenSaved.textContent = `Today: ${state.kaizen.text}`;
  kaizenInput.value = '';
}

setMood(state.mood || 'calm', false);
renderKaizen();

if (state.entries?.length) {
  const last = state.entries[state.entries.length - 1];
  addBubble(`Welcome back. Last time you wrote: “${last.text}”`, 'monk');
}
