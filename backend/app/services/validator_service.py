def validate_record(record, index, schema):
    """
    Generic validator:
    - record must be a dict
    - required fields must be present/non-empty
    - returns (clean_record, error_or_None)
    - clean_record includes only schema fields (prevents unexpected columns)
    """

    if not isinstance(record, dict):
        return None, {
            "index": index,
            "record": record,
            "error": "record must be an object"
        }

    clean = {}

    for field, rules in schema.items():
        required = rules.get("required", False)
        allow_empty = rules.get("allow_empty", False)

        value = record.get(field)

        # Missing required field
        if required and value is None:
            return None, {
                "index": index,
                "record": record,
                "error": f"{field} is required"
            }

        # Empty string check (common for QB exports)
        if required and isinstance(value, str) and value.strip() == "" and not allow_empty:
            return None, {
                "index": index,
                "record": record,
                "error": f"{field} is required"
            }

        # If provided, include in clean output
        if value is not None:
            clean[field] = value

    return clean, None