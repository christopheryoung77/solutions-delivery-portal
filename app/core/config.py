"""
Project Atlas
Sprint: 1.1A

Application Configuration
"""

from pathlib import Path
import secrets

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent


def get_version() -> str:
    """Read the Atlas version from the VERSION file."""
    version_file = PROJECT_ROOT / "VERSION"

    if version_file.exists():
        return version_file.read_text().strip()

    return "0.0.0-dev"


class Config:
    """Base configuration."""

    APP_NAME = "Project Atlas"
    APP_TITLE = "Solutions Delivery Portal"

    VERSION = get_version()

    SECRET_KEY = secrets.token_hex(32)

    DEBUG = True

    TEMPLATES_AUTO_RELOAD = True
