"""
Workbook Repository

Central access layer for the Atlas workbook.
"""

from app.providers import ExcelProvider


class WorkbookRepository:

    def __init__(self):

        self.provider = ExcelProvider()

        self.provider.connect()

    def get_sheet(self, sheet_name):

        return self.provider.get_sheet(sheet_name)

    def workbook_info(self):

        return self.provider.workbook_info()

    def get_sheet_names(self):

        return self.provider.workbook_info()["sheet_names"]
