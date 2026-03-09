create extension if not exists pgcrypto;

insert into auth.users (
    id,
    aud,
    role,
    email,
    encrypted_password,
    email_confirmed_at,
    raw_app_meta_data,
    raw_user_meta_data,
    created_at,
    updated_at
)
values (
    'f1d8fd7b-6f77-4603-9443-f64dcf6d9fe4',
    'authenticated',
    'authenticated',
    'system@weddingsmash.local',
    extensions.crypt(
        'system-user-not-loginable',
        extensions.gen_salt('bf')
    ),
    now(),
    '{}'::jsonb,
    '{}'::jsonb,
    now(),
    now()
)
on conflict (id) do nothing;

insert into public.users (
    id,
    display_name
)
values (
    'f1d8fd7b-6f77-4603-9443-f64dcf6d9fe4',
    'Smash Magic'
)
on conflict (id) do nothing;