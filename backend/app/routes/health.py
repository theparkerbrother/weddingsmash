from flask import Blueprint, jsonify
import os

APP_ENV = os.getenv("APP_ENV", "UNKNOWN")

bp = Blueprint("health", __name__)

@bp.route("/health", methods=["GET"])
def health():
    return jsonify({
        "environment": APP_ENV,
        "status": "ok"
    }), 200