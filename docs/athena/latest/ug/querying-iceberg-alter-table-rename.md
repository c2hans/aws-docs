---
source_url: https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg-alter-table-rename.html
---

# ALTER TABLE RENAME
<a name="querying-iceberg-alter-table-rename"></a>

Renames a table.

Because the table metadata of an Iceberg table is stored in Amazon S3, you can update the database and table name of an Iceberg managed table without affecting underlying table information.

## Synopsis
<a name="querying-iceberg-alter-table-rename-synopsis"></a>

```
ALTER TABLE [{{db_name}}.]{{table_name}} RENAME TO [{{new_db_name}}.]{{new_table_name}}
```

## Example
<a name="querying-iceberg-alter-table-rename-example"></a>

```
ALTER TABLE my_db.my_table RENAME TO my_db2.my_table2
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
