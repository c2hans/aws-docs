---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/spark-tuning-glue-emr/using-sql-window-functions.html
---

# Using SQL window functions instead of join and groupBy
<a name="using-sql-window-functions"></a>

[Window functions](https://spark.apache.org/docs/latest/sql-ref-syntax-qry-select-window.html) (Spark documentation) perform a calculation over a group of rows, called a *window*, that somehow relate to the current record. For example, they can be in the same partition or frame as the current row. Window functions are built into Spark, and they are similar to aggregate functions. *Aggregate functions, *such as `SUM` or `MAX`*,* operate on a group of rows and calculate a single return value for every group. Window functions are useful for processing tasks, such as calculating a moving average or accessing the value of rows based on the relative position of the current row.

The Spark `groupBy` function collects data into groups and performs aggregate functions on the grouped data. When you use `groupBy`, Spark partly aggregates the data first and then shuffles the reduced dataset. When you use window functions, the entire dataset is shuffled. Window functions can provide faster runtimes.

In very large datasets, if the cardinality of the column is large, then window functions are recommended. However, if the cardinality of the column is small, data aggregation is small, and the aggregated result can be broadcasted in the join.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
