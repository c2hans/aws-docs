---
source_url: https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg-alter-table-drop-column.html
---

# ALTER TABLE DROP COLUMN
<a name="querying-iceberg-alter-table-drop-column"></a>

Drops a column from an existing Iceberg table.

## Synopsis
<a name="querying-iceberg-alter-table-drop-column-synopsis"></a>

```
ALTER TABLE [{{db_name}}.]{{table_name}} DROP COLUMN {{col_name}}
```

## Example
<a name="querying-iceberg-alter-table-drop-column-example"></a>

```
ALTER TABLE iceberg_table DROP COLUMN userid
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
