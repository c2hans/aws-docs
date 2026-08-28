---
source_url: https://docs.aws.amazon.com/glue/latest/dg/delete-column-stats.html
---

# Deleting column statistics
<a name="delete-column-stats"></a>

You can delete column statistics using the [DeleteColumnStatisticsForTable](https://docs.aws.amazon.com/glue/latest/webapi/API_DeleteColumnStatisticsForTable.html) API operation or AWS CLI. The following example shows how to delete column statistics using AWS Command Line Interface (AWS CLI).

```
aws glue delete-column-statistics-for-table \
    --database-name '{{database_name}}' \
    --table-name '{{table_name}}' \
    --column-name '{{column_name}}'
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
