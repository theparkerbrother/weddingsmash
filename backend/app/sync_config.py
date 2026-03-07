SYNC_CONFIG = {
    "organizations": {
        "table_name": "organizations",
        "conflict_field": "qb_id",
        "schema": {
            "qb_id": {"required": True},
            "name": {"required": True},
            "active": {"required": True}
        }
    },

    # future entities
    # "projects": { ... }
}