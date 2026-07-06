from pprint import pprint

from app.providers import ExcelProvider


provider = ExcelProvider()

provider.connect()

pprint(provider.workbook_info())

provider.disconnect()
