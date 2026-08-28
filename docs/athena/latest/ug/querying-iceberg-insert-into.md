---
source_url: https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg-insert-into.html
---

# INSERT INTO
<a name="querying-iceberg-insert-into"></a>

Inserts data into an Iceberg table. Athena Iceberg `INSERT INTO` is charged the same as current `INSERT INTO` queries for external Hive tables by the amount of data scanned. To insert data into an Iceberg table, use the following syntax, where {{query}} can be either `VALUES (val1, val2, ...)` or `SELECT (col1, col2, …) FROM [{{db_name}}.]{{table_name}} WHERE {{predicate}}`. For SQL syntax and semantic details, see [INSERT INTO](insert-into.md).

```
INSERT INTO [{{db_name}}.]{{table_name}} [(col1, col2, …)] {{query}}
```

The following examples insert values into the table `iceberg_table`.

```
INSERT INTO iceberg_table VALUES (1,'a','c1')
```

```
INSERT INTO iceberg_table (col1, col2, ...) VALUES (val1, val2, ...)
```

```
INSERT INTO iceberg_table SELECT * FROM another_table
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Athena. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query athena` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
