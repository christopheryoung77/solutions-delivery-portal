"""
Excel Provider

Provides read-only access to the Atlas workbook.
"""

from pathlib import Path
import logging

import pandas as pd

from app.core.config import Config
from .base_provider import BaseProvider

logger = logging.getLogger(__name__)


class ExcelProvider(BaseProvider):

    def __init__(self):

        self.workbook_path = Path(Config.WORKBOOK_PATH)
        self.workbook = None

    def connect(self):

        if not self.workbook_path.exists():
            raise FileNotFoundError(self.workbook_path)

        logger.info("Opening workbook: %s", self.workbook_path)

        self.workbook = pd.ExcelFile(self.workbook_path)

        logger.info(
            "Workbook contains %s worksheets",
            len(self.workbook.sheet_names),
        )

    def disconnect(self):

        self.workbook = None

    def workbook_info(self):

        return {
            "path": str(self.workbook_path),
            "sheet_count": len(self.workbook.sheet_names),
            "sheet_names": self.workbook.sheet_names,
        }

    def get_sheet(self, sheet_name):

        return pd.read_excel(
            self.workbook_path,
            sheet_name=sheet_name,
        )
