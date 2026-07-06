from flask import Blueprint
from flask import jsonify
from flask import current_app

health_bp = Blueprint("health", __name__)


@health_bp.route("/health")
def health():

    return jsonify(
        {
            "application": current_app.config["APP_NAME"],
            "version": current_app.config["VERSION"],
            "environment": "development",
            "status": "healthy",
        }
    )
