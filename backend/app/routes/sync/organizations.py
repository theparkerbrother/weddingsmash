from flask import Blueprint
from app.utils.sync_auth import require_sync_key
from app.services.sync_service import run_sync
from app.services.validator_service import validate_record

bp = Blueprint("sync_organizations", __name__)

organization_schema = {
    "qb_id": {"required": True},
    "name": {"required": True},
}

def validate_organization(record, index):
    return validate_record(record, index, organization_schema)

@bp.route("/sync/organizations", methods=["POST"])
@require_sync_key
def sync_organizations():
    return run_sync("organizations", validate_organization)