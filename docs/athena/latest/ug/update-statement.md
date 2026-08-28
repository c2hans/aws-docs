---
source_url: https://docs.aws.amazon.com/athena/latest/ug/update-statement.html
---

# UPDATE
<a name="update-statement"></a>

Updates rows in an Apache Iceberg table. `UPDATE` is transactional and is supported only for Apache Iceberg tables. The statement works only on existing rows and cannot be used to insert or append a row.

## Synopsis
<a name="update-statement-synopsis"></a>

To update the rows in an Iceberg table, use the following syntax.

```
UPDATE [{{db_name}}.]{{table_name}} SET xx=yy[,...] [WHERE {{predicate}}]
```

For more information and examples, see the `UPDATE` section of [Update Iceberg table data](querying-iceberg-updating-iceberg-table-data.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
