"""
Project Atlas Logging
"""

import logging


def configure_logging():
    """Configure Atlas logging."""

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )
