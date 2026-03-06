from app.services.supabase import get_supabase_client

def log_sync_event(
    *,
    entity: str,
    dry_run: bool,
    received_count: int,
    valid_count: int,
    failed_count: int,
    status: str,
    errors: list,
    meta: dict | None = None
):
    """
    Best-effort logging. Should never break the sync endpoint.
    Audit fields are filled by DB trigger.
    """
    try:
        client = get_supabase_client()
        payload = {
            "entity": entity,
            "dry_run": dry_run,
            "received_count": received_count,
            "valid_count": valid_count,
            "failed_count": failed_count,
            "status": status,
            "errors": errors,
            "meta": meta or {}
        }
        client.table("sync_events").insert(payload).execute()
    except Exception:
        pass