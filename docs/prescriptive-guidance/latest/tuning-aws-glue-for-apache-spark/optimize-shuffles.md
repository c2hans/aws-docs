---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/tuning-aws-glue-for-apache-spark/optimize-shuffles.html
---

# Optimize shuffles
<a name="optimize-shuffles"></a>

Certain operations, such as `join()` and `groupByKey()`, require Spark to perform a shuffle. The shuffle is Spark's mechanism for redistributing data so that it's grouped differently across RDD partitions. Shuffling can help remediate performance bottlenecks. However, because shuffling typically involves copying data between Spark executors, the shuffle is a complex and costly operation. For example, shuffles generate the following costs:
+ Disk I/O:
  + Generates a large number of intermediate files on disk.
+ Network I/O:
  + Needs many network connections (Number of connections = `Mapper × Reducer`).
  + Because records are aggregated to new RDD partitions that might be hosted on a different Spark executor, a substantial fraction of your dataset might move between Spark executors over the network.
+ CPU and memory load:
  + Sorts values and merges sets of data. These operations are planned on the executor, placing a heavy load on the executor.

Shuffle is one of the most substantial factors in degraded performance of your Spark application. While storing the intermediate data, it can exhaust space on the executor's local disk, which causes the Spark job to fail.

You can assess your shuffle performance in CloudWatch metrics and in the Spark UI.

## CloudWatch metrics
<a name="shuffle-metrics"></a>

If the **Shuffle Bytes Written** value is high compared with **Shuffle Bytes Read**, your Spark job might use [shuffle operations](https://spark.apache.org/docs/latest/rdd-programming-guide.html#shuffle-operations) such as `join()` or `groupByKey()`.

![Data Shuffle Across Executors (Bytes) graph showing a spike in shuffle bytes written.](https://docs.aws.amazon.com/prescriptive-guidance/latest/tuning-aws-glue-for-apache-spark/images/guide-img/ee14755c-1401-4ea5-afc7-732eb483b047/images/2e033b62-cdff-4bb0-9bea-b8529167c960.png)

## Spark UI
<a name="shuffle-spark"></a>

On the **Stage** tab of the Spark UI, you can check the **Shuffle Read Size / Records** values. You can also see it on the **Executors** tab.

In the following screenshot, each executor exchanges approximately 18.6GB/4020000 records with the shuffle process, for a total shuffle read size of about 75 GB).

The **Shuffle Spill (Disk)** column shows a large amount of data spill memory to disk, which might cause a full disk or a performance issue.

![""](https://docs.aws.amazon.com/prescriptive-guidance/latest/tuning-aws-glue-for-apache-spark/images/guide-img/ee14755c-1401-4ea5-afc7-732eb483b047/images/fda93bf5-86f4-47b7-b04d-b1141ec6b987.png)

If you observe these symptoms and the stage takes too long when compared to your performance goals, or it fails with `Out Of Memory` or `No space left on device` errors, consider the following solutions.

### Optimize the join
<a name="optimize-the-join.2a878fa6-989b-5d6b-8c42-c666f9287ab8"></a>

The `join()` operation, which joins tables, is the most commonly used shuffle operation, but it's often a performance bottleneck. Because join is a costly operation, we recommend not using it unless it's essential to your business requirements. Double-check that you are making efficient use of your data pipeline by asking the following questions:
+ Are you recomputing a join that is also performed in other jobs you can reuse?
+ Are you joining to resolve foreign keys to values that aren't used by the consumers of your output?

After you confirm that your join operations are essential to your business requirements, see the following options for optimizing your join in a way that meets your requirements.

#### Use pushdown before join
<a name="use-pushdown-before-join.57acc1fc-9d18-5d9f-aac2-acda8c378419"></a>

Filter out unnecessary rows and columns in the DataFrame before performing a join. This has the following advantages:
+ Reduces the amount of data transfer during shuffle
+ Reduces the amount of processing in the Spark executor
+ Reduces the amount of data scan

```
# Default
df_joined  = df1.join(df2, ["product_id"])

# Use Pushdown
df1_select = df1.select("product_id","product_title","star_rating").filter(col("star_rating")>=4.0)
df2_select = df2.select("product_id","category_id")
df_joined  = df1_select.join(df2_select, ["product_id"])
```

#### Use DataFrame Join
<a name="use-dataframe-join.0edca4c0-ab79-5d64-a64d-3ad83e8b51d0"></a>

Try using a [Spark high-level API](https://archive.apache.org/dist/spark/docs/3.3.0/sql-programming-guide.html) such as SparkSQL, DataFrame, and Datasets instead of the RDD API or DynamicFrame join. You can convert DynamicFrame to DataFrame with a method call such as `dyf.toDF()`. As discussed in the [Key topics in Apache Spark](key-topics-apache-spark.md) section, these join operations internally take advantage of query optimization by the Catalyst optimizer.

#### Shuffle and broadcast hash joins and hints
<a name="shuffle-and-broadcast-hash-joins-and-hints.584e2935-be49-5bc7-8ff2-b9e28b6787ca"></a>

Spark supports two types of join: shuffle join and broadcast hash join. A broadcast hash join doesn't require shuffling, and it can require less processing than a shuffle join. However, it's applicable only when joining a small table to a large one. When joining a table that can fit in the memory of a single Spark executor, consider using a broadcast hash join.

The following diagram shows the high-level structure and steps of a broadcast hash join and a shuffle join.

![Broadcast join with direct connections between tables and joined table, and shuffle join with two shuffle phases in between the tables and joined table.](https://docs.aws.amazon.com/prescriptive-guidance/latest/tuning-aws-glue-for-apache-spark/images/guide-img/ee14755c-1401-4ea5-afc7-732eb483b047/images/09eae7f2-2f0f-4f42-8aec-39b27baf77fb.png)

The details of each join are as follows:
+ Shuffle join:
  + The shuffle hash join joins two tables without sorting and distributes the join between the two tables. It's suitable for joins of small tables that can be stored in the Spark executor's memory.
  + The sort-merge join distributes the two tables to be joined by key and sorts them before joining. It's suitable for joins of large tables.
+ Broadcast hash join:
  + A broadcast hash join pushes the smaller RDD or table to each of the worker nodes. Then it does a map-side combine with each partition of the larger RDD or table.

    It's suitable for joins when one of your RDDs or tables can fit in memory or can be made to fit in memory. It's beneficial to do a broadcast hash join when possible, because it doesn't require a shuffle. You can use a join hint to request a broadcast join from Spark as follows.

    ```
    # DataFrame
    from pySpark.sql.functions import broadcast
    df_joined= df_big.join(broadcast(df_small), right_df[key] == left_df[key], how='inner')

    -- SparkSQL
    SELECT /*+ BROADCAST(t1) /  FROM t1 INNER JOIN t2 ON t1.key = t2.key;
    ```

    For more information about join hints, see [Join hints](https://spark.apache.org/docs/latest/sql-ref-syntax-qry-select-hints.html#join-hints).

In AWS Glue 3.0 and later, you can take advantage of broadcast hash joins automatically by enabling [Adaptive Query Execution](https://spark.apache.org/docs/latest/sql-performance-tuning.html#adaptive-query-execution) and additional parameters. Adaptive Query Execution converts a sort-merge join to a broadcast hash join when the runtime statistics of either join side is smaller than the adaptive broadcast hash join threshold.

In AWS Glue 3.0, you can enable Adaptive Query Execution by setting `spark.sql.adaptive.enabled=true`. Adaptive Query Execution is enabled by default in AWS Glue 4.0.

You can set additional parameters related to shuffles and broadcast hash joins:
+ `spark.sql.adaptive.localShuffleReader.enabled`
+ `spark.sql.adaptive.autoBroadcastJoinThreshold`

For more information about related parameters, see [Converting sort-merge join to broadcast join](https://archive.apache.org/dist/spark/docs/3.3.0/sql-performance-tuning.html#converting-sort-merge-join-to-broadcast-join).

In AWS Glue 3.0 and or later, you can use other join hints for shuffle to tune your behavior.

```
-- Join Hints for shuffle sort merge join
SELECT /*+ SHUFFLE_MERGE(t1) /  FROM t1 INNER JOIN t2 ON t1.key = t2.key;
SELECT /*+ MERGEJOIN(t2) /  FROM t1 INNER JOIN t2 ON t1.key = t2.key;
SELECT /*+ MERGE(t1) /  FROM t1 INNER JOIN t2 ON t1.key = t2.key;

-- Join Hints for shuffle hash join
SELECT /*+ SHUFFLE_HASH(t1) /  FROM t1 INNER JOIN t2 ON t1.key = t2.key;

-- Join Hints for shuffle-and-replicate nested loop join
SELECT /*+ SHUFFLE_REPLICATE_NL(t1) /  FROM t1 INNER JOIN t2 ON t1.key = t2.key;
```

#### Use bucketing
<a name="use-bucketing.900f023c-0377-5b0d-b2d7-6977693cbdfc"></a>

*The sort-merge join *requires two phases, shuffle and sort, and then merge. These two phases can overload the Spark executor and cause OOM and performance issues when some of the executors are merging and others are sorting simultaneously. In such cases, it might be possible to efficiently join by using [bucketing](https://spark.apache.org/docs/latest/sql-data-sources-load-save-functions.html#bucketing-sorting-and-partitioning). Bucketing will pre-shuffle and pre-sort your input on join keys, and then write that sorted data to an intermediary table. The cost of the shuffle and sort steps can be reduced when joining large tables by defining the sorted intermediary tables in advance.

![Sort-merge join has the additional shuffle and sort steps.](https://docs.aws.amazon.com/prescriptive-guidance/latest/tuning-aws-glue-for-apache-spark/images/guide-img/ee14755c-1401-4ea5-afc7-732eb483b047/images/ce03432b-a979-40da-ae19-0f7084968f38.png)

Bucketed tables are useful for the following:
+ Data joined frequently over the same key, such as `account_id`
+ Loading daily cumulative tables, such as base and delta tables that could be bucketed on a common column

You can create a bucketed table by using the following code.

```
df.write.bucketBy(50, "account_id").sortBy("age").saveAsTable("bucketed_table")
```

#### Repartition DataFrames on join keys before the join
<a name="repartition-dataframes-on-join-keys-before-the-join.3f968490-7b62-55d4-b55a-e20f5953830a"></a>

To repartition the two DataFrames on the join keys before the join, use the following statements.

```
df1_repartitioned = df1.repartition(N,"join_key")
df2_repartitioned = df2.repartition(N,"join_key")
df_joined  = df1_repartitioned.join(df2_repartitioned,"product_id")
```

This will partition two (still separate) RDDs on the join key before initiating the join. If the two RDDs are partitioned on the same key with the same partitioning code, RDD records that your plan to join together will have a high likelihood of being co-located on the same worker before shuffling for the join. This might improve performance by reducing network activity and data skew during the join.

### Overcome data skew
<a name="overcome-data-skew.06c12491-eaae-597f-adc7-df511a192920"></a>

Data skew is one of the most common causes of a bottleneck for Spark jobs. It occurs when data isn't uniformly distributed across RDD partitions. This causes tasks for that partition to take much longer than others, delaying the overall processing time of the application.

To identify data skew, assess the following metrics in the Spark UI:
+ On the **Stage** tab in the Spark UI, examine the **Event Timeline** page. You can see an uneven distribution of tasks in the following screenshot. Tasks that are distributed unevenly or are taking too long to run can indicate data skew.
![Executor computing time is much longer for one task than for the others.](https://docs.aws.amazon.com/prescriptive-guidance/latest/tuning-aws-glue-for-apache-spark/images/guide-img/ee14755c-1401-4ea5-afc7-732eb483b047/images/1ceb4119-615b-42be-b563-83b3b66d703f.png)
+ Another important page is **Summary Metrics**, which shows statistics for Spark tasks. The following screenshot shows metrics with percentiles for **Duration**, **GC Time**, **Spill (memory)**, **Spill (disk)**, and so on.
![Summary Metrics table with the Duration row highlighted.](https://docs.aws.amazon.com/prescriptive-guidance/latest/tuning-aws-glue-for-apache-spark/images/guide-img/ee14755c-1401-4ea5-afc7-732eb483b047/images/58037157-4a0f-4847-89f4-1a279a214068.png)

  When the tasks are evenly distributed, you will see similar numbers in all the percentiles. When there is data skew, you will see very biased values in each percentile. In the example, task duration is less than 13 seconds in **Min**, **25th percentile**, **Median**, and **75th percentile**. While the **Max** task processed 100 times more data than the **75th percentile**, its duration of 6.4 minutes is about 30 times longer. It means that at least one task (or up to 25 percent of the tasks) took far longer than the rest of the tasks.

If you see data skew, try the following:
+ If you use AWS Glue 3.0, enable Adaptive Query Execution by setting `spark.sql.adaptive.enabled=true`. Adaptive Query Execution is enabled by default in AWS Glue 4.0.

  You can also use Adaptive Query Execution for data skew introduced by joins by setting the following related parameters:
  + `spark.sql.adaptive.skewJoin.skewedPartitionFactor`
  + `spark.sql.adaptive.skewJoin.skewedPartitionThresholdInBytes`
  + `spark.sql.adaptive.advisoryPartitionSizeInBytes=128m (128 mebibytes or larger should be good)`
  + `spark.sql.adaptive.coalescePartitions.enabled=true (when you want to coalesce partitions)`

  For more information, see the [Apache Spark documentation](https://spark.apache.org/docs/latest/sql-performance-tuning.html#optimizing-skew-join).
+ Use keys with a large range of values for the join keys. In a shuffle join, partitions are determined for each hash value of a key. If a join key's cardinality is too low, the hash function is more likely to do a bad job of distributing your data across partitions. Therefore, if your application and business logic support it, consider using a higher cardinality key or a composite key.

  ```
  # Use Single Primary Key
  df_joined = df1_select.join(df2_select, ["primary_key"])

  # Use Composite Key
  df_joined = df1_select.join(df2_select, ["primary_key","secondary_key"])
  ```

### Use cache
<a name="use-cache.218cea4d-1154-5856-867b-509408d386ce"></a>

When you use repetitive DataFrames, avoid additional shuffle or computation by using `df.cache()` or `df.persist()` to cache the calculation results in each Spark executor's memory and on disk. Spark also supports persisting RDDs on disk or replicating across multiple nodes ([storage level](https://spark.apache.org/docs/latest/rdd-programming-guide.html#rdd-persistence)).

For example, you can persist the DataFrames by adding `df.persist()`. When the cache is no longer needed, you can use `unpersist` to discard the cached data.

```
df = spark.read.parquet("s3://<Bucket>/parquet/product_category=Books/")
df_high_rate = df.filter(col("star_rating")>=4.0)
df_high_rate.persist()

df_joined1 = df_high_rate.join(<Table1>, ["key"])
df_joined2 = df_high_rate.join(<Table2>, ["key"])
df_joined3 = df_high_rate.join(<Table3>, ["key"])
...
df_high_rate.unpersist()
```

### Remove unneeded Spark actions
<a name="remove-unneeded-spark-actions.76b48a98-8c72-5f69-b973-a3fb3c7656f5"></a>

Avoid running unnecessary actions such as `count`, `show` , or `collect`. As discussed in the [Key topics in Apache Spark](key-topics-apache-spark.md) section, Spark is lazy. Each transformed RDD might be recomputed each time you run an action on it. When you use many Spark actions, multiple source accesses, task calculations, and shuffle runs for each action are being called.

If you don't need `collect()` or other actions in your commercial environment, consider removing them.

|
|
| Note: Avoid using Spark `collect()` in commercial environments as much as possible. The `collect()` action returns all the results of a calculation in the Spark executor to the Spark driver, which might cause the Spark driver to return an OOM error. To avoid an OOM error, Spark sets `spark.driver.maxResultSize = 1GB` by default, which limits the maximum data size returned to the Spark driver to 1 GB. |
| --- |
