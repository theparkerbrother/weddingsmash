from flask import Blueprint, request, jsonify
from app.utils.sync_auth import require_sync_key
from app.services.sync_service import run_sync
from app.services.validator_service import validate_record
from app.sync_config import SYNC_CONFIG

bp = Blueprint("sync_router", __name__)


@bp.route("", methods=["POST"])
@require_sync_key
def sync_router():
    payload = request.get_json(silent=True) or {}
    meta = payload.get("meta", {})
    entity = meta.get("entity")

    config = SYNC_CONFIG.get(entity)

    if not config:
        return jsonify({
            "error": f"Unsupported entity: {entity}"
        }), 400

    schema = config["schema"]

    def validate_entity(record, index):
        return validate_record(record, index, schema)

    return run_sync(
        config["table_name"],
        validate_entity,
        config.get("conflict_field", "qb_id")
    )