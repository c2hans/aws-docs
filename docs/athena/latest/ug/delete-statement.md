---
source_url: https://docs.aws.amazon.com/athena/latest/ug/delete-statement.html
---

# DELETE
<a name="delete-statement"></a>

Deletes rows in an Apache Iceberg table. `DELETE` is transactional and is supported only for Apache Iceberg tables.

## Synopsis
<a name="delete-statement-synopsis"></a>

To delete the rows from an Iceberg table, use the following syntax.

```
DELETE FROM [{{db_name}}.]{{table_name}} [WHERE {{predicate}}]
```

For more information and examples, see the `DELETE` section of [Update Iceberg table data](querying-iceberg-updating-iceberg-table-data.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
