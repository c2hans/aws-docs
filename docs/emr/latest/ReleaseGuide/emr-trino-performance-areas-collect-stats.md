---
source_url: https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-trino-performance-areas-collect-stats.html
---

# Collect and Utilize table statistics
<a name="emr-trino-performance-areas-collect-stats"></a>

 Collecting table statistics allows Trino’s cost-based optimizer to make informed decisions about join orders, filter pushdown, and partition pruning, resulting in better performance.

You can use the `ANALYZE` command to collect statistics for Hive or Iceberg tables:

```
ANALYZE sales;
```

Collecting statistics on wide tables can be taxing on resources. We recommend specifying a subset of columns that are used in joins, in filters, or in grouping operations.

This is another helpful command. It displays current statistics for a table to verify if statistics are up to date.

```
show stats for table_name;
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
