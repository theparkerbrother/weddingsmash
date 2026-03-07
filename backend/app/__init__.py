from flask import Flask
from dotenv import load_dotenv

from app.routes.health import bp as health_bp
from app.routes.organizations import bp as organizations_bp
from app.routes.sync import sync_bp
from app.routes.sync_router import bp as sync_router_bp


def create_app():
    load_dotenv(override=True)
    
    app = Flask(__name__)

    app.register_blueprint(health_bp, url_prefix="/api")
    app.register_blueprint(organizations_bp, url_prefix="/api")
    app.register_blueprint(sync_bp, url_prefix="/api/sync")
    app.register_blueprint(sync_router_bp, url_prefix="/api/sync-router")

    return app