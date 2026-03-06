from flask import Blueprint

sync_bp = Blueprint("sync", __name__)

# Import route modules so they register with this blueprint
from . import organizations  # noqa