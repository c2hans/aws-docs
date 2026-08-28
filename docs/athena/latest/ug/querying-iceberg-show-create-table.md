---
source_url: https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg-show-create-table.html
---

# SHOW CREATE TABLE
<a name="querying-iceberg-show-create-table"></a>

Displays a `CREATE TABLE` DDL statement that can be used to recreate the Iceberg table in Athena. If Athena cannot reproduce the table structure (for example, because custom table properties are specified in the table), an UNSUPPORTED error is thrown.

## Synopsis
<a name="querying-iceberg-show-create-table-synopsis"></a>

```
SHOW CREATE TABLE [{{db_name}}.]{{table_name}}
```

## Example
<a name="querying-iceberg-show-create-table-example"></a>

```
SHOW CREATE TABLE iceberg_table
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
