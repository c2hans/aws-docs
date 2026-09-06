---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/spark-tuning-glue-emr/pruning-dynamic-partitions.html
---

# Pruning dynamic partitions
<a name="pruning-dynamic-partitions"></a>

Spark 3.0 and later includes Dynamic Partition Pruning (DPP). *Dynamic partition pruning* is an optimization technique in Spark that prevents scanning of unnecessary partitions when reading data. The following are some key things to know about DPP:
+ It examines the partition values requested in the query filters and predicates and determines which partitions are required to satisfy the query. Any partitions that are deemed unnecessary are automatically and transparently pruned.
+ DPP reduces processing time and resource utilization by skipping partitions that contain no applicable data. This helps Spark to focus only on relevant partitions.
+ It works with both static partitions and dynamically generated partitions that are added through insertions or incremental loads. Spark recognizes new partitions and can continue applying dynamic pruning.
+ DPP is completely transparent or invisible to developers. No special coding is needed to enable DPP. It occurs automatically behind the scenes as an optimization during query plan generation.

The following are some best practices to ensure DPP works efficiently:
+ Use predicate pushdown by applying filters early in your Spark data frame operations. This helps Spark to eliminate partitions early by using the partition metadata.
+ Collect statistics on your data by running `ANALYZE TABLE` frequently. This reduces column-level statistics that help Spark to more accurately determine which partitions can be ignored.
+ Avoid over-partitioning your data. Too many partitions can overload the driver node when it collects statistics. Aim for 10–100 partitions for each large table.
+ Repartition data frames before joins. This prevents shuffle joins that require moving all data and further optimizes the amount of data that is read.
+ Use consistent partition column types and naming across different tables being joined. This helps Spark better match partitions for join optimization.
+ Test queries with `EXPLAIN` to ensure DPP is being applied, and verify whether addition tuning is necessary.

In a *star schema*, tables are divided into two main types: *fact* tables and *dimension* tables. Dimension tables tend to be much smaller than fact tables. When joining a fact table to a dimension table, DPP optimizes the query plan. It creates a subquery from any filters that are applied to the dimension table. It broadcasts this subquery and builds a hash table from it. It then applies the hash table to the fact table's scan phase, before reading the fact table data. This helps DPP to reduce the amount of data that must be read from the larger fact table.

The following example query shows DPP in action. The query fetches the number of orders from the country (India) and includes an inner join between a fact table (`fact_orders`) and a dimension table (`nation`). The `fact_orders` table is partitioned by the column `o_nationkey`.

```
- "select n.n_name as country, count(1) as no_of_orders from fact_orders o join nation n on o.o_nationkey = n.n_nationkey where n.n_name = 'INDIA' group by n.n_name"
```

The following are the steps used in the `EXPLAIN` plan:

1. Scan the smaller dimension table (`nation`) and filter by column `n_name = 'INDIA'`.

1. Broadcast the results of the previous step.

1. Create a subquery that filters on the results from the first step.

1. Push it down as a `PartitionFilter` so that it only scans the fact table partitions that are needed, instead of a full table scan.

The following is the `EXPLAIN` plan for this DPP-optimized query.

```
== Physical Plan ==
AdaptiveSparkPlan isFinalPlan=true
+- == Final Plan ==
   *(4) HashAggregate(keys=[], functions=[count(1)], output=[count#208L])
   +- ShuffleQueryStage 3
      +- Exchange SinglePartition, ENSURE_REQUIREMENTS, [id=#353]
         +- *(3) HashAggregate(keys=[], functions=[partial_count(1)], output=[count#212L])
            +- *(3) HashAggregate(keys=[n_name#31], functions=[], output=[])
               +- ShuffleQueryStage 1
                  +- Exchange hashpartitioning(n_name#31, 36), ENSURE_REQUIREMENTS, [id=#315]
                     +- *(2) HashAggregate(keys=[n_name#31], functions=[], output=[n_name#31])
                        +- *(2) Project [n_name#31]
                           +- *(2) BroadcastHashJoin [cast(o_nationkey#145 as bigint)], [n_nationkey#32L], Inner, BuildRight, false
                              :- *(2) ColumnarToRow
                              :  +- FileScan parquet [o_nationkey#145] Batched: true, DataFilters: [], Format: Parquet, Location: InMemoryFileIndex[s3://aws-spark-tuning/fact_orders], PartitionFilters: [isnotnull(o_nationkey#145), dynamicpruningexpression(cast(o_nationkey#145 as bigint) IN dynamicp..., PushedFilters: [], ReadSchema: struct<>
                              :        +- SubqueryBroadcast dynamicpruning#210, 0, [n_nationkey#32L], [id=#200]
                              :           +- OutputAdapter [n_name#31, n_nationkey#32L]
                              :              +- AdaptiveSparkPlan isFinalPlan=true
                              :                 +- BroadcastQueryStage 2
                              :                    +- ReusedExchange [n_name#31, n_nationkey#32L], BroadcastExchange HashedRelationBroadcastMode(List(input[1, bigint, false]),false), [id=#233]
                              +- BroadcastQueryStage 0
                                 +- BroadcastExchange HashedRelationBroadcastMode(List(input[1, bigint, false]),false), [id=#233]
                                    +- *(1) Filter ((isnotnull(n_name#31) AND (n_name#31 = INDIA)) AND isnotnull(n_nationkey#32L))
                                       +- FileScan json [n_name#31,n_nationkey#32L] Batched: false, DataFilters: [isnotnull(n_name#31), (n_name#31 = INDIA), isnotnull(n_nationkey#32L)], Format: JSON, Location: InMemoryFileIndex[s3://aws-spark-tuning/input/demo/json/nation], PartitionFilters: [], PushedFilters: [IsNotNull(n_name), EqualTo(n_name,INDIA), IsNotNull(n_nationkey)], ReadSchema: struct<n_name:string,n_nationkey:bigint>
```

Even though there is no direct filter added on the `o_nationkey` column, because of the DPP feature, Spark automatically scans only those partitions that are needed, instead of the entire table.
