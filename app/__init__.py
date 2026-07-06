"""
Project Atlas

Application Factory
"""

from flask import Flask

from app.core.config import Config
from app.core.logging import configure_logging
from app.dashboard import dashboard_bp
from app.core.health import health_bp


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    configure_logging()

    app.register_blueprint(dashboard_bp)

    app.register_blueprint(health_bp)

    app.logger.info("Atlas started successfully")

    return app
