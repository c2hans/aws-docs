---
source_url: https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg-drop-table.html
---

# DROP TABLE
<a name="querying-iceberg-drop-table"></a>

Drops an Iceberg table.

**Warning**
Because Iceberg tables are considered managed tables in Athena, dropping an Iceberg table also removes all the data in the table.

## Synopsis
<a name="querying-iceberg-drop-table-synopsis"></a>

```
DROP TABLE [IF EXISTS] [{{db_name}}.]{{table_name}}
```

## Example
<a name="querying-iceberg-drop-table-example"></a>

```
DROP TABLE iceberg_table
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
