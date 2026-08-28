---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/spark-tuning-glue-emr/using-the-spark-cbo.html
---

# Using the Spark cost-based optimizer
<a name="using-the-spark-cbo"></a>

Spark version 2.09 and later can use a cost-based optimizer (CBO). The CBO selects the cheapest execution plan for a query based on various table statistics. CBO tries to optimize the execution of the query with respect to CPU utilization and I/O, thus returning as quickly as possible. However, in most cases, data statistics are commonly absent, especially when statistics collection is even more expensive than the data processing. Even if the statistics are available, they are likely out of date. The following are best practices for using the CBO:
+ Collect statistics on all columns used in operations such as joins, filters, and group bys. This helps the optimizer make better decisions. Use `ANALYZE TABLE` to collect statistics.
+ Increase the frequency of statistics collection if data is rapidly changing. Outdated statistics can result in unoptimized plans.
+ Start with default CBO parameters and tune them only if needed. Aggressive optimizations can increase runtimes.
+ Verify if CBO is choosing optimal plans by forcing the optimized plan and comparing the performance. Enable optimizer logging to compare the plans.
+ For better optimizations, use CBO in combination with partitioning, bucketing, and data skew hints. Partitioning can help CBO to scale.
+ To detect plan regressions early, continuously monitor query performance after enabling CBO.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
