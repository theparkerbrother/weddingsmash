from flask import Blueprint
from .organizations import bp as organizations_bp

sync_bp = Blueprint("sync", __name__)

sync_bp.register_blueprint(organizations_bp)