from flask import Flask
from dotenv import load_dotenv

from app.routes.health import bp as health_bp
from app.routes.sync import sync_bp

def create_app():
    load_dotenv(override=True)
    
    app = Flask(__name__)

    app.register_blueprint(health_bp, url_prefix="/api")
    app.register_blueprint(sync_bp, url_prefix="/api/sync")

    return app