---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/hyperscale-aurora-mysql/parameter-tuning.html
---

# Parameter tuning
<a name="parameter-tuning"></a>

Apart from the connection-related parameters, there are a handful of parameters that you can tune to improve the performance your Amazon Aurora MySQL-Compatible Edition cluster when faced with hypergrowth. When changing any database parameter, it's important to use the following best practices:
+ Change one parameter at time so that you can measure the impact of the change.
+ Some parameters might require a warmup period to manifest their effect after they are changed. Consider this when you observe and measure the performance of your Aurora MySQL-Compatible cluster.
+ Avoid incorrect parameter values, which could prevent the database instance from starting-up.

These parameters include:
+ `sync_binlog`
+ `table_open_cache`
+ `innodb_sync_array_size`
+ `innodb_flush_log_at_trx_commit`
+ `autocommit`
+ `tmp_table_size`
+ `max_heap_table_size`

For guidelines on configuring these parameters, see [Aurora MySQL configuration parameters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Reference.ParameterGroups.html), [Recommendations for MySQL features in Aurora MySQ](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.BestPractices.FeatureRecommendations.html)L, and [Temporary table behavior in Aurora MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/ams3-temptable-behavior.html) in the AWS documentation.
