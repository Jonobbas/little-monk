# Little Monk v0.2 — Real AI + Persistent Memory Setup

The repository is now prepared for a real server-side LLM endpoint and a structured memory database.

## 1. Deploy on a host with serverless functions

GitHub Pages can serve the static UI, but it cannot securely hold an OpenAI API key or run `/api/chat`.

Use a serverless host such as Vercel for the AI-enabled build.

Required environment variables:

- `OPENAI_API_KEY`
- `OPENAI_MODEL` (optional; defaults to `gpt-4.1-mini` in the current prototype)

Never put API keys in `app.js`, `index.html`, or any public repository file.

## 2. Create the database

Create a Supabase project and run:

`supabase/schema.sql`

This creates structured tables for:

- profiles
- check-ins / Inner Climate
- reflections
- daily Kaizen actions
- intervention outcomes
- derived memories

The schema enables row-level security. Before real users are added, authentication and explicit RLS policies tied to `auth.uid()` must be configured.

## 3. Current data flow

Browser -> `/api/chat` -> OpenAI API

The browser sends only a limited memory context, current Inner Climate, daily action, and summarized intervention outcomes. The server keeps the API key secret.

Until cloud persistence is wired in, the current browser app keeps its history in localStorage. If `/api/chat` is unavailable, it falls back to the original rule-based mentor so the PoC still works.

## 4. Next engineering milestone

Wire Supabase Auth + database writes so each interaction follows:

Observe -> Store -> Retrieve relevant memory -> AI reflection -> One action -> Follow-up -> Outcome -> Update memory.

Do not add a multi-agent swarm yet. Start with one Little Monk orchestrator. Add specialist pattern/memory/evaluation agents later only if measured tests show better outcomes.

## 5. Safety and privacy

Little Monk is a personal-growth companion, not a therapist or diagnostic system. Do not infer or store medical diagnoses. Provide clear consent, deletion controls, data export, and minimal-data defaults before inviting external beta users.
