-- Little Monk v0.2 structured memory schema
create extension if not exists pgcrypto;

create table if not exists profiles (
  id uuid primary key,
  display_name text,
  created_at timestamptz default now()
);

create table if not exists checkins (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null,
  mood text not null check (mood in ('energised','calm','bored','stressed','angry')),
  note text,
  created_at timestamptz default now()
);

create table if not exists reflections (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null,
  content text not null,
  theme text,
  mood text,
  created_at timestamptz default now()
);

create table if not exists actions (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null,
  action_text text not null,
  mood_before text,
  status text default 'pending' check (status in ('pending','reviewed','cancelled')),
  created_at timestamptz default now()
);

create table if not exists outcomes (
  id uuid primary key default gen_random_uuid(),
  action_id uuid references actions(id) on delete cascade,
  user_id uuid not null,
  result text not null check (result in ('helpful','partly_helpful','not_helpful')),
  note text,
  mood_after text,
  created_at timestamptz default now()
);

create table if not exists memories (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null,
  kind text not null,
  summary text not null,
  confidence numeric default 0.5,
  source_ref text,
  created_at timestamptz default now(),
  updated_at timestamptz default now()
);

create index if not exists checkins_user_created_idx on checkins(user_id, created_at desc);
create index if not exists reflections_user_created_idx on reflections(user_id, created_at desc);
create index if not exists actions_user_created_idx on actions(user_id, created_at desc);
create index if not exists outcomes_user_created_idx on outcomes(user_id, created_at desc);
create index if not exists memories_user_updated_idx on memories(user_id, updated_at desc);

-- Enable RLS before production and add policies tied to auth.uid().
alter table profiles enable row level security;
alter table checkins enable row level security;
alter table reflections enable row level security;
alter table actions enable row level security;
alter table outcomes enable row level security;
alter table memories enable row level security;
