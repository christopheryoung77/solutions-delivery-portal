# Decision

Atlas models business entities independently of the data source.

## Reason

The current data source is Microsoft Excel.

The future data source will be PostgreSQL.

Business objects must remain independent of storage technology.

## Consequences

- Easier testing
- Cleaner architecture
- Future migration requires no UI changes
