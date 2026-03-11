"""
Sync endpoint for organizations.
POST /api/sync/organizations
"""


from flask import Blueprint
from app.utils.sync_auth import require_sync_key
from app.services.run_sync import run_sync
from app.services.validator_service import validate_record

bp = Blueprint("sync_organizations", __name__)
ENTITY = "organizations"

schema = {
    "qb_id": {"required": True},   # Quickbase record id
    "name": {"required": True},    # Organization name
    "owners": {"required": False}, # Owners of the organization
    "active": {"required": True},  # Active flag from source system
}


def validate_organization(record, index):
    return validate_record(record, index, schema)


@bp.route("/organizations", methods=["POST"])
@require_sync_key
def sync_organizations():
    """
    Sync endpoint for organizations.

    Route
    -----
    POST /api/sync/organizations

    Expected JSON body
    ------------------

    {
    "meta": {
        "source": "quickbase",
        "entity": "organizations",
        "event": "upsert"
    },
    "records": [
        {
        "qb_id": "1",
        "name": "Ivory Grove",
        "active": true
        }
    ]
    }

    Required headers
    ----------------

    x-sync-key: <SYNC_KEY>
    Content-Type: application/json

    Optional query params
    ---------------------

    dry_run=true

    Example curl request
    --------------------

    curl -X POST "http://127.0.0.1:5000/api/sync/organizations?dry_run=true" \
    -H "Content-Type: application/json" \
    -H "x-sync-key: YOUR_SYNC_KEY" \
    -d '{
        "meta": {
        "source": "quickbase",
        "entity": "organizations",
        "event": "upsert"
        },
        "records": [
        {
            "qb_id": "1",
            "name": "Ivory Grove",
            "active": true
        }
        ]
    }'

    Behavior
    --------

    - Records are upserted into the "organizations" table
    - Conflict field: qb_id
    - Unknown fields are ignored by validation
    """
    return run_sync(ENTITY, validate_organization)
