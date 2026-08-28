---
source_url: https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg-show-columns.html
---

# SHOW COLUMNS
<a name="querying-iceberg-show-columns"></a>

Shows the columns in a table.

## Synopsis
<a name="querying-iceberg-show-columns-synopsis"></a>

```
SHOW COLUMNS (FROM|IN) [{{db_name}}.]{{table_name}}
```

## Example
<a name="querying-iceberg-alter-table-change-column-example"></a>

```
SHOW COLUMNS FROM iceberg_table
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
