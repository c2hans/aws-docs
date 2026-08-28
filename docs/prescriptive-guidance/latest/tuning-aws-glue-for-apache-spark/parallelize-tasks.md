---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/tuning-aws-glue-for-apache-spark/parallelize-tasks.html
---

# Parallelize tasks
<a name="parallelize-tasks"></a>

To optimize performance, it's important to parallelize tasks for data loads and transformations. As we discussed in [Key topics in Apache Spark](key-topics-apache-spark.md), the number of resilient distributed dataset (RDD) partitions is important, because it determines the degree of parallelism. Each task that Spark creates corresponds to an RDD partition on a 1:1 basis. To achieve the best performance, you need to understand how the number of RDD partitions is determined and how that number is optimized.

If you do not have enough parallelism, the following symptoms will be recorded in [CloudWatch metrics](https://docs.aws.amazon.com/glue/latest/dg/monitoring-awsglue-with-cloudwatch-metrics.html) and the Spark UI.

## CloudWatch metrics
<a name="parallelize-metrics"></a>

Check the **CPU Load** and **Memory Utilization**. If some executors are not processing during a phase of your job, it's appropriate to improve parallelism. In this case, during the visualized timeframe, **Executor 1** was performing a task, but the remaining executors (2, 3, and 4) were not. You can infer that those executors were not assigned tasks by the Spark driver.

![Graph showing driver and only one executor.](http://docs.aws.amazon.com/prescriptive-guidance/latest/tuning-aws-glue-for-apache-spark/images/guide-img/ee14755c-1401-4ea5-afc7-732eb483b047/images/ae5f1f45-5e8e-4a81-b065-1b168ccfce5a.png)

## Spark UI
<a name="parallelize-spark"></a>

On the **Stage** tab in the Spark UI, you can see** **the* number of tasks *in a stage. In this case, Spark has performed only one task.

![""](http://docs.aws.amazon.com/prescriptive-guidance/latest/tuning-aws-glue-for-apache-spark/images/guide-img/ee14755c-1401-4ea5-afc7-732eb483b047/images/f09c19af-ae0c-4f59-900d-579ab263978f.png)

Additionally, the event timeline shows **Executor 1** processing one task. This means that the work in this stage was performed entirely on one executor, while the others were idle.

![Event timeline showing only one task.](http://docs.aws.amazon.com/prescriptive-guidance/latest/tuning-aws-glue-for-apache-spark/images/guide-img/ee14755c-1401-4ea5-afc7-732eb483b047/images/027e75e3-a7c5-4430-9e5f-c2fc2d8b2f0d.png)

If you observe these symptoms, try the following solutions for each data source.

### Parallelize data load from Amazon S3
<a name="parallelize-data-load-from-amazon-s3.14064b32-95ee-5345-97f8-4e4d8867f4bb"></a>

To parallelize data loads from Amazon S3, first check the default number of partitions. You can then manually determine a target number of partitions, but be sure to avoid having too many partitions.

#### Determine the default number of partitions
<a name="determine-the-default-number-of-partitions.83f21304-5b2e-5be8-a482-fa2df4610876"></a>

For Amazon S3, the initial number of Spark RDD partitions (each of which corresponds to a Spark task) is determined by features of your Amazon S3 dataset (for example, format, compression, and size). When you create an AWS Glue DynamicFrame or a Spark DataFrame from CSV objects stored in Amazon S3, the initial number of RDD partitions (`NumPartitions`) can be approximately calculated as follows:
+ Object size <= 64 MB: `NumPartitions = Number of Objects`
+ Object size > 64 MB: `NumPartitions = Total Object Size / 64 MB`
+ Unsplittable (gzip): `NumPartitions = Number of Objects`

As discussed in the [Reduce the amount of data scan](reduce-data-scan.md) section, Spark divides large S3 objects into splits that can be processed in parallel. When the object is larger than the split size, Spark splits the object and creates an RDD partition (and task) for each split. Spark's split size is based on your data format and runtime environment, but this is a reasonable starting approximation. Some objects are compressed using unsplittable compression formats such as gzip, so Spark cannot split them.

The `NumPartitions` value might vary depending on your data format, compression, AWS Glue version, number of AWS Glue workers, and Spark configuration.

For example, when you load a single 10 GB `csv.gz` object using a Spark DataFrame, the Spark driver will create only one RDD Partition (`NumPartitions=1`) because gzip is unsplittable. This results in a heavy load on one particular Spark executor and no tasks are assigned to the remaining executors, as described in following figure.

Check the actual number of tasks (`NumPartitions`) for the stage on the [Spark Web UI](https://docs.aws.amazon.com/glue/latest/dg/monitor-spark-ui.html) **Stage** tab, or run `df.rdd.getNumPartitions()` in your code to check the parallelism.

When encountering a 10 GB gzip file, examine whether the system generating that file can generate it in a splittable format. If this isn't an option, you might need to [scale cluster capacity](scale-cluster-capacity.md) to process the file. To run transforms efficiently on the data that you loaded, you will need to rebalance your RDD across the workers in your cluster by using repartition.

#### Manually determine a target number of partitions
<a name="manually-determine-a-target-number-of-partitions.957eca52-28d0-5224-8c44-bf6f4b4e0a76"></a>

Depending on the properties of your data and Spark's implementation of certain functionalities, you might end up with a low `NumPartitions` value even though the underlying work can still be parallelized. If `NumPartitions` is too small, run `df.repartition(N)` to increase the number of partitions so that the processing can be distributed across multiple Spark executors.

In this case, running `df.repartition(100)` will increase `NumPartitions` from 1 to 100, creating 100 partitions of your data, each with a task that can be assigned to the other executors.

The operation `repartition(N)` divides the entire data equally (10 GB / 100 partitions = 100 MB/partition), avoiding data skew to certain partitions.

|
|
| Note: When a shuffle operation such as `join` is run, the number of partitions is dynamically increased or decreased depending on the value of `spark.sql.shuffle.partitions` or `spark.default.parallelism`. This facilitates a more efficient exchange of data between Spark executors. For more information, see the [Spark documentation](https://spark.apache.org/docs/latest/configuration.html#runtime-sql-configuration). |
| --- |

Your goal when determining the target number of partitions is to maximize the use of the provisioned AWS Glue workers. The number of AWS Glue workers and the number of Spark tasks are related through the number of vCPUs. Spark supports one task for each vCPU core. In AWS Glue version 3.0 or later, you can calculate a target number of partitions by using the following formula.

```
# Calculate NumPartitions by WorkerType
numExecutors = (NumberOfWorkers - 1)
numSlotsPerExecutor =
  4 if WorkerType is G.1X
  8 if WorkerType is G.2X
  16 if WorkerType is G.4X
  32 if WorkerType is G.8X
NumPartitions = numSlotsPerExecutor * numExecutors

# Example: Glue 4.0 / G.1X / 10 Workers
numExecutors = ( 10 - 1 ) = 9  # 1 Worker reserved on Spark Driver
numSlotsPerExecutor       = 4  # G.1X has 4 vCpu core ( Glue 3.0 or later )
NumPartitions = 9  * 4    = 36
```

In this example, each G.1X worker provides four vCPU cores to a Spark executor (`spark.executor.cores = 4`). Spark supports one task for each vCPU Core, so G.1X Spark executors can run four tasks simultaneously (`numSlotPerExecutor`). This number of partitions makes full use of the cluster if tasks take an equal amount of time. However, some tasks will take longer than others, creating idle cores. If this happens, consider multiplying `numPartitions` by 2 or 3 to break up and efficiently schedule the bottleneck tasks.

#### Too many partitions
<a name="too-many-partitions.b4f8bbbc-48ef-5339-9547-46b3e9e3998a"></a>

An excessive number of partitions creates an excessive number of tasks. This causes a heavy load on the Spark driver because of overhead related to distributed processing, such as management tasks and data exchange between Spark executors.

If the number of partitions in your job is substantially larger than your target number of partitions, consider reducing the number of partitions. You can reduce partitions by using the following options:
+ If your file sizes are very small, use AWS Glue [groupFiles](https://docs.aws.amazon.com/glue/latest/dg/grouping-input-files.html). You can reduce the excessive parallelism resulting from the launch of an Apache Spark task to process each file.
+ Use `coalesce(N)` to merge partitions together. This is a low-cost process. When reducing the number of partitions, `coalesce(N)` is preferred over `repartition(N)`, because `repartition(N)` performs shuffle to distribute the amount of records in each partition equally. That increases costs and management overhead.
+ Use Spark 3.x Adaptive Query Execution. As discussed in the [Key topics in Apache Spark](key-topics-apache-spark.md) section, Adaptive Query Execution provides a function to automatically coalesce the number of partitions. You can use this approach when you can't know the number of partitions until you perform the execution.

### Parallelize data load from JDBC
<a name="parallelize-data-load-from-jdbc.7222269a-34e9-5687-9548-beea3c909ed1"></a>

The number of Spark RDD partitions is determined by configuration. Note that by default only a single task is run to scan an entire source dataset through a `SELECT` query.

Both AWS Glue DynamicFrames and Spark DataFrames support parallelized JDBC data load across multiple tasks. This is done by using `where` predicates to split one `SELECT` query into multiple queries. To parallelize reads from JDBC, configure the following options:
+ For AWS Glue DynamicFrame, set `hashfield` (or `hashexpression)` and `hashpartition`. To learn more, see [Reading from JDBC tables in parallel](https://docs.aws.amazon.com/glue/latest/dg/run-jdbc-parallel-read-job.html).

  ```
  connection_mysql8_options = {
      "url": "jdbc:mysql://XXXXXXXXXX.XXXXXXX.us-east-1.rds.amazonaws.com:3306/test",
      "dbtable": "medicare_tb",
      "user": "test",
      "password": "XXXXXXXXX",
      "hashexpression":"id",
      "hashpartitions":"10"
  }
  datasource0 = glueContext.create_dynamic_frame.from_options(
      'mysql',
      connection_options=connection_mysql8_options,
      transformation_ctx= "datasource0"
  )
  ```
+ For Spark DataFrame, set `numPartitions`, `partitionColumn`, `lowerBound`, and `upperBound`. To learn more, see [JDBC To Other Databases](https://spark.apache.org/docs/latest/sql-data-sources-jdbc.html).

  ```
  df = spark.read \
      .format("jdbc") \
      .option("url", "jdbc:mysql://XXXXXXXXXX.XXXXXXX.us-east-1.rds.amazonaws.com:3306/test") \
      .option("dbtable", "medicare_tb") \
      .option("user", "test") \
      .option("password", "XXXXXXXXXX") \
      .option("partitionColumn", "id") \
      .option("numPartitions", "10") \
      .option("lowerBound", "0") \
      .option("upperBound", "1141455") \
      .load()

  df.write.format("json").save("s3://bucket_name/Tests/sparkjdbc/with_parallel/")
  ```

### Parallelize data load from DynamoDB when using the ETL connector
<a name="parallelize-data-load-from-9999999999999999ddb--when-using-the-etl-connector.e6f934be-c173-51fd-b016-53981f65f4a0"></a>

The number of Spark RDD partitions is determined by the `dynamodb.splits` parameter. To parallelize reads from Amazon DynamoDB, configure the following options:
+ Increase the value of `dynamodb.splits`.
+ Optimize the parameter by following the formula explained in [Connection types and options for ETL in AWS Glue for Spark](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-connect.html#aws-glue-programming-etl-connect-dynamodb).

### Parallelize data load from Kinesis Data Streams
<a name="parallelize-data-load-from-kinesis-data-streams.1478b532-169b-589e-8a4e-0cefacaab945"></a>

The number of Spark RDD partitions is determined by the number of shards in the source Amazon Kinesis Data Streams data stream. If you have only a few shards in your data stream, there will be only a few Spark tasks. This can result in low parallelism in downstream processes. To parallelize reads from Kinesis Data Streams, configure the following options:
+ Increase the number of shards to obtain more parallelism when loading data from Kinesis Data Streams.
+ If your logic in the micro-batch is complex enough, consider repartitioning the data at the beginning of the batch, after dropping unneeded columns.

For more information, see [Best practices to optimize cost and performance for AWS Glue streaming ETL jobs](https://aws.amazon.com/blogs/big-data/best-practices-to-optimize-cost-and-performance-for-aws-glue-streaming-etl-jobs/).

### Parallelize tasks after data load
<a name="parallelize-tasks-after-data-load.4a5e6dba-44d3-58a5-9f32-d9fbf97974c7"></a>

To parallelize tasks after data load, increase the number of RDD partitions by using the following options:
+ Repartition data to generate a greater number of partitions, especially right after initial load if the load itself could not be parallelized.

  Call `repartition()` either on DynamicFrame or DataFrame, specifying the number of partitions. A good rule of thumb is two or three times the number of cores available.

  However, when writing a partitioned table, this can lead to an explosion of files (each partition can potentially generate a file into each table partition). To avoid this, you can repartition your DataFrame by column. This uses the table partition columns so the data is organized before writing. You can specify a higher number of partitions without getting small files on the table partitions. However, be careful to avoid data skew, in which some partition values end up with most of the data and delay the completion of the task.
+ When there are shuffles, increase the `spark.sql.shuffle.partitions` value. This also can help with any memory issues when shuffling.

  When you have more than 2,001 shuffle partitions, Spark uses a compressed memory format. If you have a number close to that, you might want to set the `spark.sql.shuffle.partitions` value over that limit to get the more efficient representation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
