---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/spark-tuning-glue-emr/using-partitioning-hints.html
---

# Using partitioning hints in Spark 3.0.0
<a name="using-partitioning-hints"></a>

Spark [partitioning hints](https://spark.apache.org/docs/latest/sql-ref-syntax-qry-select-hints.html#partitioning-hints) can help you tune performance and reduce the number of output files. Spark SQL supports partitioning hints, such as `COALESCE`, `REPARTITION`, and `REPARTITION_BY_RANGE`. These hints are similar to the Dataset APIs, such as `coalesce`, `repartition`, and `repartitionByRange`. The following hints help you control the number of output files in Spark SQL, which helps you tune performance:
+ **Coalesce** - Reduce the number of partitions to the specified number of partitions. A partition number is the only parameter of the `COALESCE` hint.
+ **Repartition** - Repartition to the specified number of partitions by using the specified partitioning expressions. The `REPARTITION` hint parameters are a partition number, column names, or both.
+ **Repartition by range** - Repartition to the specified number of partitions by using the specified partitioning expressions. Column names is a required parameter for the `REPARTITION_BY_RANGE` hint, and a partition number is optional.
+ **Rebalance** - Rebalance the query result output partitions so that every partition is a reasonable size. `REBALANCE` hint parameters are an initial partition number, column names, or both or neither.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
