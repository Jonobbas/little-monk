# Little Monk Agent — Current Status and Milestone Roadmap

**Audit date:** 10 October 2026  
**Purpose:** Establish actual product and code status, then guide a safe, sustainable build for the Create AI Agents Championship and a 100-person feedback pilot.  
**Source of truth proposed:** Jonobbas/little-monk for the agent product and code; Jonobbas/little-monk-website for the brand, journals, books, and campaign pages.

## 1. Executive status

Little Monk already has a developed product model and a polished browser beta. Its core promise and journey are clear:

> Notice your inner climate → name what you need → reflect → choose one small action → review what happened → adapt.

The model has a sound human-control principle: the user remains the authority on their experience, and the system supports reflection and planning rather than diagnosis or therapy.

The current system is at **polished product prototype / founding beta**, not yet at **authenticated multi-user AI agent**. The product and several web builds have progressed further than the core public GitHub repository. The immediate work is to connect the live experience to the source-controlled build, then complete authentication, protected persistence, the agent workflow, and the feedback loop.

## 2. What was inspected

### Product and live web surfaces

- [Little Monk brand site](https://little-monk.uk/) currently promotes *The Space Between*, the 30-day journal based on Ma, alongside the quote library, Meet Little Monk, and Teen Ikigai pages. It is a brand and product site, not the current login-based agent.
- [Little Monk Founding Beta](https://little-monk-app.jonobbas.chatgpt.site/) exposes Today, Goal Focus, Insights, The idea, Practice, Wisdom, Research, Roadmap, and Feedback. The Today flow includes Inner Climate and need selections. Its privacy copy says reflections stay on the device; optional anonymous usage counts exclude journal text, mood, goals, names, and device identifiers.
- The beta’s public [product approach](https://little-monk-app.jonobbas.chatgpt.site/approach), [practice model](https://little-monk-app.jonobbas.chatgpt.site/practice), [research notes](https://little-monk-app.jonobbas.chatgpt.site/research), and [roadmap](https://little-monk-app.jonobbas.chatgpt.site/roadmap) clearly describe the loop, user control, research limits, and staged introduction of agency. The research page says cited behavior-change research informs design but does not establish that Little Monk itself improves wellbeing or long-term progress.

### GitHub

- [Jonobbas/little-monk](https://github.com/Jonobbas/little-monk) is public, on main, with a single branch and no releases. The latest commit inspected was 25 August 2026. It contains a browser prototype, a GitHub Pages workflow, an AI API handler, a Supabase schema, visual assets, and separate poster-production work.
- [Jonobbas/little-monk-website](https://github.com/Jonobbas/little-monk-website) is private and contains the brand/marketing site, journal funnel, and an older rule-based app prototype. Its latest inspected changes were 1 September 2026, primarily for The Space Between and FlowCraft. It is not the source for the current Founding Beta.
- The current Founding Beta at little-monk-app.jonobbas.chatgpt.site is not visibly represented as a synchronized build in either repository. Capture its product model and feature set in GitHub before adding more functionality.

## 3. GitHub implementation findings

### Already present

- The public app repository has a responsive browser UI and localStorage-based history, actions, outcomes, and climate data.
- api/chat.js is a server-side OpenAI Chat Completions handler. It defaults to gpt-4.1-mini, accepts a message, mood, action, outcome summary, and a client-supplied memories array, and returns a short reflection.
- The prompt already encodes useful boundaries: warm, concise, non-judgmental, no diagnosis, and careful treatment of inferred patterns.
- supabase/schema.sql defines profiles, check-ins, reflections, actions, outcomes, and memories, and enables Row Level Security.
- DEPLOY_AI.md describes a future Observe → Store → Retrieve → Reflect → Action → Follow-up → Outcome → Update-memory loop and correctly recommends one orchestrator, not a multi-agent swarm.

### Not yet complete

- Supabase RLS is enabled, but the schema says explicit policies tied to auth.uid() still need to be added. It is not ready for real multi-user journal storage.
- The AI handler does not authenticate callers, connect to Supabase, retrieve memory server-side, or write actions and outcomes. Memories are supplied by the browser, so retrieval is not yet trusted or user-scoped.
- The handler does not define request throttling, per-user usage limits, structured tool permissions, an error-reporting pipeline, or an evaluation set.
- The GitHub Pages workflow deploys static files. DEPLOY_AI.md instead describes a Vercel serverless route; the production deployment path for the AI endpoint is unresolved. The latest Pages workflow also fails at `actions/configure-pages@v5` because GitHub Pages is not enabled/configured for Actions in this repository (GitHub API returns 404). Enable/configure Pages or remove the deployment workflow after selecting the canonical host, then verify a green deploy.
- The polished current beta, public app repository, and brand site are separate implementations. Continuing feature work before choosing a canonical source risks further drift.
- The public README does not explain the current agent, local setup, environment variables, tests, deployment, or product boundaries.

## 4. Product decisions for the first multi-user beta

1. **Keep the existing model.** Do not redesign Little Monk’s philosophy or rebuild the polished journey from zero.
2. **Select one first audience.** Start with adults who want help turning a meaningful personal or work goal into a realistic next action. Keep minors out of the first data-collecting beta.
3. **Keep the first use case narrow.** Deliver one complete cycle: check-in, clarification, reflection, user-selected action, saved commitment, follow-up, outcome review, and weekly adjustment.
4. **Use one orchestrator.** The agent may use a small, explicit set of backend tools. Do not introduce multi-agent orchestration during this MVP.
5. **Keep external actions permissioned.** No email, calendar, device, or messaging actions in the first beta. The agent proposes actions and saves a commitment only after the user confirms.
6. **Use personal memory, not indiscriminate transcript ingestion.** Store entries under the authenticated user. Retrieve only a small, relevant, user-scoped set of approved memories. Use summaries first; add vector/embedding retrieval only if tests show that structured retrieval misses useful context.
7. **Keep the local-only beta as a fallback.** Users must know whether their session is local-only or account-backed.

## 5. Target architecture

### User experience

Retain the current Today / Goal Focus / Review / Insights flow. Add clear sign-up, consent, account-backed saving, memory controls, and feedback states. Distinguish user-authored entries from AI-generated summaries or hypotheses.

### Authentication and data

Use the existing Supabase direction unless a short implementation spike shows it cannot meet the prototype requirements:

- Supabase Auth provides user identity.
- Every user-owned record references the authenticated user.
- Apply and test RLS policies based on auth.uid() for every user-owned table.
- Include user-controlled export and deletion before inviting external testers.
- Keep feedback and operational error events separate from private reflection content.
- Keep API keys and service-role credentials out of browser code.

Supabase documents integration between Auth and Row Level Security. Its current Free plan lists 50,000 monthly active users and 500 MB database storage, ample in scale for an initial 100-person pilot, subject to current operational limits and plan terms: https://supabase.com/pricing and https://supabase.com/docs/guides/auth

### AI runtime and cost

The current handler uses an OpenAI API key with separate usage-based billing. ChatGPT, Gemini, and Claude subscriptions do not automatically include runtime API calls from Little Monk.

For a free-first pilot, evaluate Cloudflare Workers AI as the model runtime because the Little Monk domains already use Cloudflare. Its current docs list a free allocation of 10,000 Neurons per day; usage above that requires a paid plan and some models are excluded from the free plan. Add per-user request limits, a daily usage cap, a visible fallback response, and usage monitoring before inviting testers. Recheck current terms and model availability before launch: https://developers.cloudflare.com/workers-ai/platform/pricing/

Keep the model provider behind one small adapter and record the selected model and prompt version. Do not switch providers or rewrite the product prompt during an active feedback cohort unless a safety or reliability issue requires it.


### Shared knowledge bank and individual fit

Maintain two distinct context layers:

- **Shared knowledge bank:** source records, concise paraphrased notes, principles, evidence limits, and links to the source. This is common product knowledge; it contains no participant journal entries.
- **Private user memory:** only that person’s consented goals, preferences, constraints, accepted/rejected suggestions, and outcomes. Keep it access-controlled and deletable with their account.

For every source, record title/author, publication or source date, type, URL/identifier, access/rights status, population and setting where relevant, methods, key finding or principle, limitations, evidence class, tags, reviewer and review date. Preserve disagreements and context rather than collapsing diverse Japanese practices into one universal rule.

Use a transparent evidence rubric: peer-reviewed reviews and well-designed empirical studies can support bounded empirical claims; other research can inform design with stated limitations; Japanese philosophical/traditional principles and books can inform reflection and practice design but are not clinical or causal evidence by themselves; participant stories are experiential input and hypothesis generators, not population-level proof. Keep citations attached to each knowledge card and to the recommendation that uses it.

Personalize by matching a person’s stated goal, preferences, constraints, and their own past feedback/outcomes to candidate practices. Phrase fit as a tentative hypothesis (for example, “This may fit because you said…”) and invite correction. Update it only from user-confirmed feedback and observed outcomes; do not claim deterministic prediction, diagnose, or infer sensitive traits. Evaluate whether the suggestion was relevant and useful for that individual.

For books and articles, store bibliographic metadata and original paraphrased notes with citations. Do not ingest or redistribute full copyrighted text without permission or a suitable license. Initial register and review workflow: [Knowledge Bank Register](LITTLE_MONK_KNOWLEDGE_BANK_REGISTER.md).

### Feedback and errors

- Collect explicit feedback through the existing feedback entry point.
- Send compact error events with a correlation ID, app version, route, and error category.
- Do not log journal text, mood details, goal text, passwords, tokens, or full prompts by default.
- Offer a separate, clearly consented diagnostic report if a tester wants to share a failed interaction.
- Keep tester contact details separate from private reflections and use them only for the stated beta purpose.
- Record each issue, its frequency, decision, and the release that addressed it.

## 6. Milestones and acceptance gates

Dates are planning targets. A milestone is complete only when its exit checks pass. If a gate slips, reduce scope before extending work into late nights.

| Milestone | Target window | Work | Exit gate |
|---|---|---|---|
| **M0 — Consolidate the product and sources** | 12–18 Oct | Capture the Founding Beta UX, product contract, and feature inventory in this repo. Mark the brand site and old prototypes as separate. Select this repository as agent source of truth; record the current beta as reference build. Create the source register, evidence rubric, and first review queue from sources already listed in the beta. | Versioned product brief; one canonical repo; current flow notes; source schema and evidence labels in place; seed sources explicitly marked pending verification. |
| **M1 — Secure accounts and storage** | 19 Oct–1 Nov | Connect Auth to the schema; add user references and RLS policies; verify all reads/writes are user-scoped; add consent, export, and deletion. | Two test users cannot read or alter one another’s records; signed-out access is blocked; export/deletion work; keys remain server-side. |
| **M2 — Connect the grounded agent loop** | 2–8 Nov | Connect the model runtime to the UI through an authenticated server endpoint. Retrieve relevant source-grounded knowledge cards and approved user-scoped summaries as separate context. Add a small tool set: read relevant memory, propose a cited practice with a clear rationale, save confirmed action, review outcome, update approved summary. | One end-to-end scenario works from check-in to follow-up, persists across sessions, and passes the evaluation set. Tested guidance traces to a reviewed source card or is clearly labeled an exploratory hypothesis; users can correct fit; no unapproved tool writes. |
| **M3 — Closed alpha and operational feedback** | 9–15 Nov | Test with founders and 5–10 trusted adults. Verify account boundaries, fallback behavior, quota handling, accessibility, error events, feedback, and deletion. Fix critical trust/safety and data-separation defects. | No critical data-isolation issue; failures are traceable without logging private journal text; testers can submit feedback. |
| **M4 — 100-person pilot** | 16 Nov–13 Dec | Invite in controlled batches (10 → 25 → 50 → up to 100). Ask users to try the loop for seven days; keep a four-week cohort where possible. Review activation, confirmed actions, reviews, returns, qualitative usefulness, misunderstandings, and willingness to use again. Treat feedback-derived patterns as candidate patterns; review them against context and research before changing shared guidance or making public claims. | Up to 100 invited testers; internal evidence summary; feedback classified by frequency and severity; candidate patterns have provenance and human review; changes tied to observed issues. |
| **M5 — Competition package** | 7–15 Dec | Prepare the live prototype, concise pitch deck, and demo video. Show one realistic agent journey, memory and permission boundaries, user feedback, and a credible path from pilot to product. | All assets work from a clean session; demo has a fallback recording; claims match evidence; package ready by 15 Dec. |
| **M6 — Post-submission hardening** | Jan–May 2027, if continuing | Use organizer feedback to improve reliability, evaluation, security, and business case. Add native app or external integrations only when pilot evidence supports them. Prepare a fully working live demonstration if selected for later rounds. | Reliable, tested product flow and a live demo that does not depend on a fragile setup or unsupported claim. |

**Competition date note:** the 7 October Dubai Government launch announcement says registration closes in December and asks for a prototype, pitch deck, and demo video. The Dubai Chambers page’s FAQ says registration closes in December, while its displayed timeline places registration close and submission in January. To avoid relying on inconsistent dates, prepare the package by 15 December and check the participant portal for the binding deadline: https://www.protocol.dubai.ae/en/media-listing/news-events/hamdan-bin-mohammed-launches-create-ai-agents-championship-to-inspire-transformative-ideas-for-global-good/ and https://www.dubaichambercommerce.com/en/web/dubai-chamber-of-digital-economy/create-ai-agents

## 7. Pilot measures

Use the previously selected engagement targets as directional gates, not promises of impact:

- 70% of invited testers complete a first check-in.
- 50% save or confirm a small action.
- 30% return within seven days.
- At least five testers say they would consider paying and explain what value they would pay for.
- Capture at least one useful example and one important criticism per tester who completes an interview.
- Track errors and privacy concerns separately; cross-user data exposure is a stop-ship issue.

Do not present anonymous event counts as unique users or as proof that advice improved wellbeing. Combine product events with voluntary interviews and self-reported outcomes.

## 8. Weekly work rhythm

The build must progress without taking over sleep or family time.

- **Target:** 6–8 focused hours a week.
- **Two weekday sessions:** 90 minutes each, preferably after 7:30 PM.
- **One Sunday session:** up to 3 hours for integration, testing, and planning.
- Each session starts with one named task and ends with a commit, a short progress note, and the next action.
- Use a hard stop at the planned end time. Do not begin a new feature near bedtime.
- Keep a “not now” list for voice, calendar/device connections, multi-agent design, native apps, and extra dashboards until user evidence calls for them.
- If a milestone slips, cut optional features; do not borrow sleep from the next day.

## 9. First three actions

1. Add a current-state brief to this repo that captures the Founding Beta’s live flow and records which repository code matches it.
2. Populate and review the knowledge bank register, beginning with the six references already listed on the live Research page; verify metadata, methods, limitations, relevance, and rights before using any source to support product claims.
3. Reconcile the deployment path: choose one canonical UI source, one server runtime, and one database environment; document each URL and purpose, and resolve the failing Pages workflow.
4. Add a cross-user data-isolation test before opening authenticated storage to external testers.

## Sources checked

- Live Little Monk brand site: https://little-monk.uk/
- Live Founding Beta: https://little-monk-app.jonobbas.chatgpt.site/
- Product model and research notes: https://little-monk-app.jonobbas.chatgpt.site/approach · https://little-monk-app.jonobbas.chatgpt.site/practice · https://little-monk-app.jonobbas.chatgpt.site/research · https://little-monk-app.jonobbas.chatgpt.site/roadmap
- Agent repository: https://github.com/Jonobbas/little-monk
- Brand/website repository: https://github.com/Jonobbas/little-monk-website
- Supabase pricing and Auth docs: https://supabase.com/pricing · https://supabase.com/docs/guides/auth
- Cloudflare Workers AI pricing: https://developers.cloudflare.com/workers-ai/platform/pricing/
