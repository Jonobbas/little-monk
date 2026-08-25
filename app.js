const moods = {
  energised:{label:'Energised',message:'There is energy in you today. Give it one clear direction.',prompt:'What would make today feel meaningfully used?'},
  calm:{label:'Calm',message:'A quiet day. Notice what is helping you stay steady.',prompt:'What is worth protecting from this calm state?'},
  bored:{label:'Bored',message:'The sky feels flat. Curiosity may be the smallest door forward.',prompt:'What is one thing you could explore for ten minutes?'},
  stressed:{label:'Stressed',message:'There is rain in the inner climate. We do not have to solve everything at once.',prompt:'What is the one pressure that is taking the most space right now?'},
  angry:{label:'Angry',message:'The weather is intense. Notice it before acting from it.',prompt:'What happened just before the anger rose?'}
};

const $=id=>document.getElementById(id);
const climateCard=$('climateCard'),climateMessage=$('climateMessage'),climateBadge=$('climateBadge'),moodGrid=$('moodGrid'),chat=$('chat'),chatForm=$('chatForm'),chatInput=$('chatInput'),kaizenForm=$('kaizenForm'),kaizenInput=$('kaizenInput'),kaizenSaved=$('kaizenSaved');

const state=JSON.parse(localStorage.getItem('littleMonkState')||'{}');
state.entries=state.entries||[];
state.actions=state.actions||[];
state.outcomes=state.outcomes||[];
state.climateHistory=state.climateHistory||[];

function saveState(){localStorage.setItem('littleMonkState',JSON.stringify(state))}
function today(){return new Date().toISOString().slice(0,10)}
function addBubble(text,who='monk'){const b=document.createElement('div');b.className=`bubble ${who==='user'?'user-bubble':'monk-bubble'}`;b.textContent=text;chat.appendChild(b);chat.scrollTop=chat.scrollHeight}

function setMood(mood,announce=true){
  const c=moods[mood]||moods.calm;
  state.mood=mood;
  state.lastCheckIn=new Date().toISOString();
  climateCard.dataset.climate=mood;
  climateMessage.textContent=c.message;
  climateBadge.textContent=c.label;
  [...moodGrid.querySelectorAll('button')].forEach(b=>b.classList.toggle('active',b.dataset.mood===mood));
  const last=state.climateHistory.at(-1);
  if(!last||last.date!==today()||last.mood!==mood)state.climateHistory.push({date:today(),mood,at:new Date().toISOString()});
  state.climateHistory=state.climateHistory.slice(-90);
  if(announce)addBubble(c.prompt);
  saveState();
}

moodGrid.addEventListener('click',e=>{const b=e.target.closest('button[data-mood]');if(b)setMood(b.dataset.mood)});

function detectTheme(text){
  const l=text.toLowerCase();
  if(/work|office|meeting|deadline|project/.test(l))return'work';
  if(/sleep|tired|exhausted|rest/.test(l))return'recovery';
  if(/family|wife|husband|child|children|home/.test(l))return'family';
  if(/exercise|walk|yoga|gym|health/.test(l))return'body';
  if(/angry|frustrated|irritated/.test(l))return'anger';
  if(/stuck|confused|decision/.test(l))return'decision';
  return'reflection';
}

function patternInsight(){
  if(state.climateHistory.length<4)return null;
  const recent=state.climateHistory.slice(-7);
  const counts=recent.reduce((a,x)=>(a[x.mood]=(a[x.mood]||0)+1,a),{});
  const top=Object.entries(counts).sort((a,b)=>b[1]-a[1])[0];
  if(top&&top[1]>=3)return`I notice ${top[0]} has appeared ${top[1]} times in your recent check-ins. That may be a pattern worth watching.`;
  return null;
}

function localFallback(text){
  const mood=state.mood||'calm',l=text.trim().toLowerCase(),theme=detectTheme(text);
  const similar=state.entries.filter(e=>e.theme===theme).slice(-3);
  if(similar.length>=2)return`This connects with something you have returned to before: ${theme}. What is different about it today?`;
  if(/tired|exhausted|burnout|drained/.test(l))return'What can be reduced, postponed, or made smaller today?';
  if(/angry|irritated|frustrated|furious/.test(l))return'Before deciding what to do, what part is fact and what part is interpretation?';
  if(/confused|stuck|don't know|dont know/.test(l))return'Let us make it smaller. What is the next decision—not the whole journey?';
  if(/happy|great|excited|proud|good/.test(l))return'What specifically created that feeling, so we can remember what works for you?';
  if(mood==='stressed')return'Which part is under your control in the next 24 hours?';
  if(mood==='bored')return'Would action or curiosity help more right now? Name one tiny experiment.';
  if(mood==='energised')return'Where will this energy create the highest value today?';
  if(mood==='angry')return'What response would you respect yourself for tomorrow?';
  return'What does this tell you about what matters most right now?';
}

function buildMemoryContext(){
  const recentEntries=state.entries.slice(-8).map(e=>`${e.theme||'reflection'} | ${e.mood||'unknown'} | ${e.text}`);
  const reviewed=state.actions.filter(a=>a.status==='reviewed').slice(-6).map(a=>`Action: ${a.text} -> ${a.outcome||'unknown'}`);
  return [...recentEntries,...reviewed].slice(-10);
}

function outcomeSummary(){
  if(!state.outcomes.length)return'No reviewed actions yet.';
  const counts=state.outcomes.reduce((a,o)=>(a[o.result]=(a[o.result]||0)+1,a),{});
  return `${counts.helpful||0} helpful, ${counts.partly_helpful||0} partly helpful, ${counts.not_helpful||0} not helpful.`;
}

async function getAIReply(text){
  try{
    const response=await fetch('/api/chat',{
      method:'POST',
      headers:{'Content-Type':'application/json'},
      body:JSON.stringify({
        message:text,
        mood:state.mood||'calm',
        memories:buildMemoryContext(),
        action:state.kaizen?.text||null,
        outcomeSummary:outcomeSummary()
      })
    });
    if(!response.ok)throw new Error('AI endpoint unavailable');
    const data=await response.json();
    if(!data.reply)throw new Error('No AI reply');
    return data.reply;
  }catch(error){
    return localFallback(text);
  }
}

function captureOutcome(text){
  if(!state.pendingOutcomeId)return false;
  const l=text.toLowerCase();
  let result=null;
  if(/didn't help|didnt help|not help/.test(l))result='not_helpful';
  else if(/partly|somewhat|little/.test(l))result='partly_helpful';
  else if(/helped|worked|yes/.test(l))result='helpful';
  if(!result)return false;
  const action=state.actions.find(a=>a.id===state.pendingOutcomeId);
  if(action){
    action.status='reviewed';
    action.outcome=result;
    state.outcomes.push({actionId:action.id,result,moodBefore:action.mood,at:new Date().toISOString()});
    state.outcomes=state.outcomes.slice(-90);
  }
  delete state.pendingOutcomeId;
  saveState();
  setTimeout(()=>addBubble(result==='helpful'?'Good. I will remember that this kind of action helped you.':result==='partly_helpful'?'Useful. We will treat it as partial evidence, not a rule.':'Understood. I will remember that this approach did not help this time.'),220);
  return true;
}

chatForm.addEventListener('submit',async e=>{
  e.preventDefault();
  const text=chatInput.value.trim();
  if(!text)return;
  const wasOutcome=captureOutcome(text);
  addBubble(text,'user');
  state.entries.push({text,mood:state.mood||'calm',theme:detectTheme(text),at:new Date().toISOString()});
  state.entries=state.entries.slice(-100);
  saveState();
  chatInput.value='';
  if(wasOutcome)return;
  const thinking=document.createElement('div');
  thinking.className='bubble monk-bubble';
  thinking.textContent='…';
  chat.appendChild(thinking);
  chat.scrollTop=chat.scrollHeight;
  const reply=await getAIReply(text);
  thinking.remove();
  addBubble(reply);
});

kaizenForm.addEventListener('submit',e=>{
  e.preventDefault();
  const text=kaizenInput.value.trim();
  if(!text)return;
  const action={id:Date.now(),text,date:today(),mood:state.mood||'calm',status:'pending'};
  state.kaizen=action;
  state.actions.push(action);
  state.actions=state.actions.slice(-90);
  saveState();
  renderKaizen();
  addBubble(`I will remember this: “${text}”. When you return, I will ask what happened.`);
});

function renderKaizen(){
  if(!state.kaizen?.text)return;
  kaizenSaved.classList.remove('hidden');
  kaizenSaved.textContent=`Today: ${state.kaizen.text}`;
  kaizenInput.value='';
}

function askOutcome(){
  const pending=[...state.actions].reverse().find(a=>a.status==='pending'&&a.date<today());
  if(!pending)return;
  state.pendingOutcomeId=pending.id;
  addBubble(`Last time you chose: “${pending.text}”. Did it help? Reply with “helped”, “partly”, or “didn't help”.`);
}

setMood(state.mood||'calm',false);
renderKaizen();
if(state.entries.length){const last=state.entries.at(-1);addBubble(`Welcome back. Last time you wrote: “${last.text}”`)}
const insight=patternInsight();if(insight)addBubble(insight);
askOutcome();
saveState();