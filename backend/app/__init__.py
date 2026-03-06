from flask import Flask
from dotenv import load_dotenv

from app.routes.health import bp as health_bp
from app.routes.organizations import bp as organizations_bp
from app.routes.sync.organizations import bp as sync_organizations_bp

def create_app():
    load_dotenv(override=True)
    import os

    app = Flask(__name__)

    app.register_blueprint(health_bp, url_prefix="/api")
    app.register_blueprint(organizations_bp, url_prefix="/api")
    app.register_blueprint(sync_organizations_bp, url_prefix="/api")

    return app