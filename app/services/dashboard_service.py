"""
Atlas Dashboard Service

Calculates dashboard KPIs.
"""

from app.repositories import WorkbookRepository
from app.core.constants import WORKSHEETS


class DashboardService:

    def __init__(self):

        self.repository = WorkbookRepository()

    def get_summary(self):

        summary = {}

        total = 0

        for key, sheet in WORKSHEETS.items():

            if key == "source":
                continue

            rows = len(
                self.repository.get_sheet(sheet)
            )

            summary[key] = rows

            total += rows

        summary["total_requests"] = total

        return summary
