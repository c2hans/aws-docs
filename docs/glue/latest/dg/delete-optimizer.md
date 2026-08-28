---
source_url: https://docs.aws.amazon.com/glue/latest/dg/delete-optimizer.html
---

# Deleting an optimizer
<a name="delete-optimizer"></a>

You can delete an optimizer and associated metadata for the table using AWS CLI or AWS API operation.

Run the following AWS CLI command to delete optimization history for a table. You need to specify the optimizer `type` along with the catalog ID, database name and table name. The acceptable values are: `compaction`, `retention`, and `orphan_file_deletion`.

```
aws glue delete-table-optimizer \
  --catalog-id {{123456789012}} \
  --database-name {{iceberg_db}} \
  --table-name {{iceberg_table}} \
  --type {{compaction}}
```

 Use `DeleteTableOptimizer` operation to delete an optimizer for a table.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
