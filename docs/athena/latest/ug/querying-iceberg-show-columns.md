---
source_url: https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg-show-columns.html
---

# SHOW COLUMNS

Shows the columns in a table.

## Synopsis
<a name="querying-iceberg-show-columns-synopsis"></a>

```sql
SHOW COLUMNS (FROM|IN) [{{db_name}}.]{{table_name}}
```

## Example
<a name="querying-iceberg-alter-table-change-column-example"></a>

```sql
SHOW COLUMNS FROM iceberg_table
```
