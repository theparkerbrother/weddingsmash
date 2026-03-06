import os
from functools import wraps
from flask import request, jsonify

def require_sync_key(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        expected = os.getenv("SYNC_API_KEY")
        if not expected:
            return jsonify({"error": "SYNC_API_KEY not set on server"}), 500

        provided = request.headers.get("X-Sync-Key")

        if not provided or provided != expected:
            return jsonify({"error": "unauthorized"}), 401

        return fn(*args, **kwargs)
    return wrapper