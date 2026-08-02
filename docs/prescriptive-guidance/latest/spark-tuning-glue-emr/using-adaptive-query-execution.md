---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/spark-tuning-glue-emr/using-adaptive-query-execution.html
---

# Using Adaptive Query Execution
<a name="using-adaptive-query-execution"></a>

Spark 3.0 and later includes an additional layer of optimization that is called [Adaptive Query Execution (AQE)](https://spark.apache.org/docs/latest/sql-performance-tuning.html#adaptive-query-execution). It optimizes queries based upon the metrics that are collected during query runtime. It uses the runtime statistics to pick the most efficient execution plan. This feature is enabled by default in Apache Spark version 3.2.0 and later. You can turn it off by setting the Spark configuration to `spark.sql.adaptive.enabled=false`. AQE has three primary features: coalescing post-shuffle partitions, converting sort-merge joins to broadcast joins, and optimizing skew joins.
