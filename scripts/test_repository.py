from pprint import pprint

from app.repositories import WorkbookRepository


repo = WorkbookRepository()

pprint(repo.workbook_info())

print()

print(repo.get_sheet_names())

from pprint import pprint

from app.repositories import WorkbookRepository

repo = WorkbookRepository()

pprint(repo.workbook_info())

print("\nWorksheet Summary")
print("-" * 50)

for sheet in repo.get_sheet_names():

    df = repo.get_sheet(sheet)

    print(f"{sheet:<25} {len(df):>5} rows")
