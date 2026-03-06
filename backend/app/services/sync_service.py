from flask import request, jsonify
from app.services.supabase import get_supabase_client
from app.services.sync_log_service import log_sync_event


def normalize_payload(payload):
    if isinstance(payload, dict):
        return [payload]
    if isinstance(payload, list):
        return payload
    return None


def run_sync(entity_name, validate_fn, conflict_field="qb_id"):
    payload = request.get_json(silent=True)

    if payload is None:
        return jsonify({"error": "Invalid or missing JSON body"}), 400

    records = normalize_payload(payload)

    if records is None:
        return jsonify({"error": "Body must be an object or array"}), 400

    dry_run = request.args.get("dry_run", "false").lower() == "true"

    valid_records = []
    errors = []

    for i, rec in enumerate(records):

        try:
            clean, err = validate_fn(rec, i)

            if err:
                errors.append(err)
            else:
                valid_records.append(clean)

        except Exception as e:
            errors.append({
                "index": i,
                "record": rec,
                "error": f"validator exception: {str(e)}"
            })

    client = get_supabase_client()

    result = None

    if not dry_run and valid_records:
        result = (
            client
            .table(entity_name)
            .upsert(valid_records, on_conflict=conflict_field)
            .execute()
        )

    if len(valid_records) == 0:
        status = "failed"
    elif len(errors) == 0:
        status = "success"
    else:
        status = "partial"

    response = {
        "status": status,
        "received": len(records),
        "upserted": len(valid_records),
        "failed": len(errors),
        "errors": errors
    }

    if dry_run:
        response["dry_run"] = True

    if not dry_run and result:
        response["data"] = result.data

    log_sync_event(
        entity=entity_name,
        dry_run=dry_run,
        received_count=len(records),
        valid_count=len(valid_records),
        failed_count=len(errors),
        status=status,
        errors=errors,
        meta={}
    )

    return jsonify(response), 200