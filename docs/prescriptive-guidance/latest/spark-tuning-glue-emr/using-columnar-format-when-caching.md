---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/spark-tuning-glue-emr/using-columnar-format-when-caching.html
---

# Using columnar format when caching
<a name="using-columnar-format-when-caching"></a>

Spark SQL has the ability to cache tables in-memory in a columnar format. `spark.catalog.cacheTable("tableName")` or `dataFrame.cache()` function calls can be used to cache tables in an in-memory columnar format. The Spark SQL engine then scans only the required columns and automatically tunes the compression to reduce memory and CPU usage. You can use `spark.catalog.uncacheTable("tableName")` or `dataFrame.unpersist()` to remove the table from memory.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
