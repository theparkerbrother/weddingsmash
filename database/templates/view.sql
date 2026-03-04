CREATE OR REPLACE VIEW public.<table_name>_view
WITH (security_invoker = true)
AS
SELECT
    t.id,

    to_char(t.created_at, 'YYYY-MM-DD HH24:MI') AS created_at,
    to_char(t.updated_at, 'YYYY-MM-DD HH24:MI') AS updated_at,

    cb.display_name AS created_by,
    ub.display_name AS updated_by

FROM public.<table_name> t
LEFT JOIN public.users cb ON t.created_by = cb.id
LEFT JOIN public.users ub ON t.updated_by = ub.id;