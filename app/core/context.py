"""
Atlas Context Processors
"""

from flask import current_app


def inject_globals():
    """Inject global template variables."""

    return {
        "atlas": {
            "application": current_app.config["APP_NAME"],
            "title": current_app.config["APP_TITLE"],
            "version": current_app.config["VERSION"],
            "user": {
                "name": "Christopher Young",
                "role": "Solutions Architect",
            },
        }
    }
