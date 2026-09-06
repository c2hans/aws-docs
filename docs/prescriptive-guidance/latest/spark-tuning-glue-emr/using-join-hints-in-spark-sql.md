---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/spark-tuning-glue-emr/using-join-hints-in-spark-sql.html
---

# Using join hints in Spark SQL
<a name="using-join-hints-in-spark-sql"></a>

With Spark 3.0, you can specify the type of join algorithm that you want Spark to use at runtime. The join strategy hints, `BROADCAST`, `MERGE`, `SHUFFLE_HASH`, and `SHUFFLE_REPLICATE_NL`, instruct Spark to use the hinted strategy on each specified relation when joining them with another relation. This section discusses the join strategy hints in detail.

## BROADCAST
<a name="broadcast"></a>

In a *Broadcast Hash* join, one of the datasets is significantly smaller than the other. Because the smaller dataset can fit in memory, it is broadcasted to all of the executors in the cluster. After the data is broadcasted, a standard hash join is performed. A Broadcast Hash join happens in two steps:
+ **Broadcast ** – The smaller dataset is broadcasted to all executors within the cluster.
+ **Hash join** – The smaller dataset is hashed across all of the executors and then joined with the larger dataset.

There is no `sort` or `merge` operation. When joining large fact tables with smaller dimension tables used to perform a star schema join, Broadcast Hash is the fastest join algorithm. The following example demonstrates how a Broadcast Hash join works. The join side with the hint is broadcasted, regardless of the size limit specified in the `spark.sql.autoBroadcastJoinThreshold` property*.* If both sides of the join have broadcast hints, the one with the smaller size (based on stats) is broadcast. The default value for the `spark.sql.autoBroadcastJoinThreshold` property is 10 MB. This configures the maximum size, in bytes, for a table that is broadcast to all worker nodes when performing a join.

The following examples provide the query, physical `EXPLAIN` plan, and the time taken for the query to run. The query requires less processing time if you use the `BROADCASTJOIN` hint to force a broadcast join, as shown in the second example `EXPLAIN` plan.

```
SQL Query : select table1.id,table1.col,table2.id,table2.int_col from table1 join table2 on table1.id = table2.id

== Physical Plan ==
AdaptiveSparkPlan isFinalPlan=false
  +- SortMergeJoin [id#80L], [id#95L], Inner
       :- Sort [id#80L ASC NULLS FIRST], false, 0
       :  +- Exchange hashpartitioning(id#80L, 36), ENSURE_REQUIREMENTS, [id=#725]
       :     +- Filter isnotnull(id#80L)
       :        +- Scan ExistingRDD[id#80L,col#81]
  +- Sort [id#95L ASC NULLS FIRST], false, 0
      +- Exchange hashpartitioning(id#95L, 36), ENSURE_REQUIREMENTS, [id=#726]
         +- Filter isnotnull(id#95L)
            +- Scan ExistingRDD[id#95L,int_col#96L]

Number of records processed: 799541
Querytime : 21.87715196 seconds
```

```
SQL Query :
select /*+ BROADCASTJOIN(table1)*/ table1.id,table1.col,table2.id,table2.int_col from table1 join table2 on table1.id = table2.id

Physical Plan ==
AdaptiveSparkPlan isFinalPlan=false\n
  +- BroadcastHashJoin [id#271L], [id#286L], Inner, BuildLeft, false
 :- BroadcastExchange HashedRelationBroadcastMode(List(input[0, bigint,   false]),false), [id=#955]
       :  +- Filter isnotnull(id#271L)
       :     +- Scan ExistingRDD[id#271L,col#272]
               +- Filter isnotnull(id#286L)
                 +- Scan ExistingRDD[id#286L,int_col#287L]

Number of records processed: 799541
Querytime : 15.35717314 seconds
```

## MERGE
<a name="merge"></a>

The *Shuffle Sort Merge* join is preferred when both datasets are large and cannot fit into memory. As the name indicates, this join involves the following three phases:
+ **Shuffle phase** – Both of the datasets in the join query are shuffled.
+ **Sort phase** – The records are sorted by the join key on both sides.
+ **Merge phase** – Both sides of the join condition are iterated, based on the join key.

The follow image shows a Directed Acyclic Graph (DAG) visualization of a Shuffle Sort Merge join. Both of the tables are read in the first two stages. In the next stage (stage 17), they are shuffled, sorted, and then merged together at the end.

|
|
| Note: Some of the stages in this image show as *skipped* because those steps were completed in previous stages. That data was cached or persisted for use in these stages. |
| --- |

![A DAG visualization of a Shuffle Sort Merge join](http://docs.aws.amazon.com/prescriptive-guidance/latest/spark-tuning-glue-emr/images/guide-img/03a14f27-75e9-4b79-afab-d8b743354a10/images/04e27c46-259e-4a03-bc47-ae7f81666754.png)

The following is a physical plan that indicates a Sort Merge join.

```
== Physical Plan ==
AdaptiveSparkPlan isFinalPlan=false
  +- SortMergeJoin [id#320L], [id#335L], Inner
       :- Sort [id#320L ASC NULLS FIRST], false, 0
       :  +- Exchange hashpartitioning(id#320L, 36), ENSURE_REQUIREMENTS, [id=#1018]
       :    +- Filter isnotnull(id#320L)
       :     +- Scan ExistingRDD[id#320L,col#321]
               +- Sort [id#335L ASC NULLS FIRST], false, 0
                +- Exchange hashpartitioning(id#335L, 36), ENSURE_REQUIREMENTS, [id=#1019]
                  +- Filter isnotnull(id#335L)
                   +- Scan ExistingRDD[id#335L,int_col#336L]
```

## SHUFFLE\_HASH
<a name="shuffle-hash"></a>

The *Shuffle Hash* join, as the name indicates, works by shuffling both datasets. The same keys from both sides end up in the same partition or task. After the data is shuffled, the smallest of the two datasets is hashed into buckets, and then a hash join is performed within the partition. A Shuffle Hash join is different from a Broadcast Hash join because the entire dataset is not broadcasted. A Shuffle Hash join is divided into two phases:
+ **Shuffle phase** – Both of the datasets are shuffled.
+ **Hash join phase** – The smaller side of data is hashed, bucketed, and then hash joined with the larger side in all of the partitions.

Sorting is not needed with Shuffle Hash joins inside of the partitions. The following image shows the phases of the Shuffle Hash join. The data is read initially, then it's shuffled across, and then a hash is created and used for the join.

![Phases of the Shuffle Hash join: Scan JSON read data, exchange, ShuffleHashJoin, and Hash Aggregate](http://docs.aws.amazon.com/prescriptive-guidance/latest/spark-tuning-glue-emr/images/guide-img/03a14f27-75e9-4b79-afab-d8b743354a10/images/68a58fcd-a1b7-45d2-815f-da3590fcc721.png)

By default, the optimizer chooses Shuffle Hash join when the Broadcast Hash join cannot be used. Based on the Broadcast Hash join threshold size (`spark.sql.autoBroadcastJoinThreshold`) and the number of shuffle partitions (`spark.sql.shuffle.partitions`) chosen, it uses the Shuffle Hash join when the single partition of the logical SQL is small enough to build a local hash table.

## SHUFFLE\_REPLICATE\_NL
<a name="shuffle-replicate-nl"></a>

The *Shuffle-and-Replicate Nested Loop* join, also known as a *Cartesian Product *join, works very similar to a Broadcast Hash join, except the dataset is not broadcasted.

In this join algorithm, *shuffle *doesn't refer to a true shuffle because records with the same keys aren't sent to the same partition. Instead, the entire partition from both datasets are copied over the network. When the partitions from the datasets are available, a Nested Loop join is performed. If there are `X` number of records in the first dataset and `Y` number of records in the second dataset in each partition, each record in the second dataset is joined with every record in the first dataset. This continues in a loop `X × Y` times in every partition.
