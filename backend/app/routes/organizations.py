from flask import Blueprint, request, jsonify
from app.services.supabase import get_supabase_client

bp = Blueprint("organizations", __name__)

@bp.route("/organizations", methods=["GET"])
def get_organizations():

    client = get_supabase_client()

    result = client.table("organizations").select("*").limit(5).execute()

    return jsonify(result.data)


@bp.route("/organizations", methods=["POST"])
def create_organization():

    data = request.json

    if not data:
        return jsonify({"error": "No JSON body provided"}), 400

    client = get_supabase_client()

    result = client.table("organizations").insert(data).execute()

    return jsonify(result.data), 201