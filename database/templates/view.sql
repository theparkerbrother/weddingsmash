DROP VIEW IF EXISTS public.organizations_view;

CREATE VIEW public.organizations_view
WITH (security_invoker = true)
AS
SELECT
    t.id,
    t.name,
    t.qb_id,
    to_char(t.created_at, 'YYYY-MM-DD HH24:MI') AS created_at,
    to_char(t.updated_at, 'YYYY-MM-DD HH24:MI') AS updated_at,
    cb.display_name AS created_by,
    ub.display_name AS updated_by
FROM public.organizations t
LEFT JOIN public.users cb ON t.created_by = cb.id
LEFT JOIN public.users ub ON t.updated_by = ub.id;