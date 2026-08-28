---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/tuning-aws-glue-for-apache-spark/key-topics-apache-spark.html
---

# Key topics in Apache Spark
<a name="key-topics-apache-spark"></a>

This section explains Apache Spark basic concepts and key topics for tuning AWS Glue for Apache Spark performance. It's important to understand these concepts and topics before discussing real-world tuning strategies.

## Architecture
<a name="spark-architecture"></a>

The Spark driver is mainly responsible for splitting your Spark application up into tasks that can be accomplished on individual workers. The Spark driver has the following responsibilities:
+ Running `main()` in your code
+ Generating execution plans
+ Provisioning Spark executors in conjunction with cluster manager, which manages resources on the cluster
+ Scheduling tasks and requesting tasks for Spark executors
+ Managing task progress and recovery

You use a `SparkContext` object to interact with the Spark driver for your job run.

A Spark executor is a worker for holding data and running tasks that are passed from the Spark driver. The number of Spark executors will go up and down with the size of your cluster.

![Spark driver, cluster manager, and worker node connections with JVM executors in the worker nodes.](http://docs.aws.amazon.com/prescriptive-guidance/latest/tuning-aws-glue-for-apache-spark/images/guide-img/ee14755c-1401-4ea5-afc7-732eb483b047/images/9f657149-094c-46cd-915e-1d2771abb382.png)

|
|
| Note: A Spark executor has multiple slots so that multiple tasks to be processed in parallel. Spark supports one task for each virtual CPU (vCPU) core by default. For example, if an executor has four CPU cores, it can run four concurrent tasks. |
| --- |

## Resilient distributed dataset
<a name="distributed-dataset"></a>

Spark does the complex job of storing and tracking large data sets across Spark executors. When you write code for Spark jobs, you don't need to think about the details of storage. Spark provides the *resilient distributed dataset (RDD)* abstraction, which is a collection of elements that can be operated on in parallel and can be partitioned across the Spark executors of the cluster.

The following figure shows the difference in how to store data in memory when a Python script is run in its typical environment and when it's run in the Spark framework (*PySpark*).

![Python val [1,2,3 N], Apache Spark rdd = sc.parallelize[1,2,3 N].](http://docs.aws.amazon.com/prescriptive-guidance/latest/tuning-aws-glue-for-apache-spark/images/guide-img/ee14755c-1401-4ea5-afc7-732eb483b047/images/2ac4d7ef-1c19-4744-a619-66e4126b1b53.png)

+ **Python** – Writing `val = [1,2,3...N]` in a Python script keeps the data in memory on the single machine where the code is running.
+ **PySpark** – Spark provides the RDD data structure to load and process data distributed across memory on multiple Spark executors. You can generate an RDD with code such as `rdd = sc.parallelize[1,2,3...N]`, and Spark can automatically distribute and hold data in memory across multiple Spark executors.

  In many AWS Glue jobs, you use RDDs through AWS Glue *DynamicFrames* and Spark *DataFrames*. These are abstractions that allow you to define the schema of data in an RDD and perform higher-level tasks with that additional information. Because they use RDDs internally, data is transparently distributed and loaded to multiple nodes in following code:
  + DynamicFrame

    ```
    dyf= glueContext.create_dynamic_frame.from_options(
        's3', {"paths": [ "s3://<YourBucket>/<Prefix>/"]},
        format="parquet",
        transformation_ctx="dyf"
    )
    ```
  + DataFrame

    ```
    df = spark.read.format("parquet")
        .load("s3://<YourBucket>/<Prefix>")
    ```

An RDD has following features:
+ RDDs consist of data divided into multiple parts called *partitions*. Each Spark executor stores one or more partitions in memory, and the data is distributed across multiple executors.
+ RDDs are *immutable*, meaning they can't be changed after they're created. To change a DataFrame, you can use *transformations*, which are defined in the following section.
+ RDDs replicate data across available nodes, so they can automatically recover from node failures.

### Lazy evaluation
<a name="lazy-evaluation.0485d35a-1ce7-5c1a-b566-7758866c4c10"></a>

RDDs support two types of operations: *transformations*, which create a new dataset from an existing one, and *actions*, which return a value to the driver program after running a computation on the dataset.
+ **Transformations** – Because RDDs are *immutable, *you can change them only by using a transformation.

  For example, `map` is a transformation that passes each dataset element through a function and returns a new RDD representing the results. Notice that the `map` method doesn't return an output. Spark stores the abstract transformation for the future, rather than letting you interact with the result. Spark will not act on transformations until you call an action*.*
+ **Actions** – Using transformations, you build up your logical transformation plan. To initiate the computation, you run an action such as `write`, `count`, `show`, or `collect`.

  All transformations in Spark are *lazy*, in that they don't compute their results right away. Instead, Spark remembers a series of transformations applied to some base dataset, such as Amazon Simple Storage Service (Amazon S3) objects. The transformations are computed only when an action requires a result to be returned to the driver. This design enables Spark to run more efficiently. For example, consider the situation where a dataset created through the `map` transformation is consumed only by a transformation that substantially reduces the number of rows, such as `reduce`. You can then pass the smaller dataset that has undergone both transformations to the driver, instead of passing the larger mapped dataset.

## Terminology of Spark applications
<a name="terms"></a>

This section covers Spark application terminology. The Spark driver creates an *execution plan* and controls the behavior of applications in several abstractions. The following terms are important for development, debugging, and performance tuning with the Spark UI.
+ ***Application*** – Based on a Spark session (Spark context). Identified by a unique ID such as `<application_XXX>`.
+ ***Jobs*** – Based on the actions** **created** **for an RDD. A job consists of one or more *stages*.
+ ***Stages*** – Based on the *shuffles*** **created** **for an RDD. A stage consists of one or more tasks. The shuffle is Spark's mechanism for redistributing data so that it's grouped differently across RDD partitions. Certain transformations, such as `join()`, require a shuffle. Shuffle are discussed in more detail in the [Optimize shuffles](optimize-shuffles.md) tuning practice.
+ ***Tasks*** – A task is the minimum unit of processing scheduled by Spark. Tasks are created for each RDD partition, and the number of tasks is the maximum number of simultaneous executions in the stage.

![Execution plan with jobs, stages, shuffle, and tasks.](http://docs.aws.amazon.com/prescriptive-guidance/latest/tuning-aws-glue-for-apache-spark/images/guide-img/ee14755c-1401-4ea5-afc7-732eb483b047/images/a2a098e4-f0ba-413a-8137-d5f84c11909d.png)

|
|
| Note: Tasks are the most important thing to consider when optimizing parallelism. The number of tasks scales with the number of RDD partitions. |
| --- |

### Parallelism
<a name="parallelism.eb41d3f9-8a87-5bdd-9201-f56cd4d1d3b2"></a>

Spark parallelizes tasks for loading and transforming data.

Consider an example where you perform distributed processing of access log files (named `accesslog1 ... accesslogN`) on Amazon S3. The following diagram shows the distributed-processing flow.

![""](http://docs.aws.amazon.com/prescriptive-guidance/latest/tuning-aws-glue-for-apache-spark/images/guide-img/ee14755c-1401-4ea5-afc7-732eb483b047/images/802eab1b-c287-40e0-a105-963f2eeed72d.png)

1. The Spark driver creates an execution plan for distributed processing across many Spark executors.

1. The Spark driver assigns tasks each executor based on the execution plan. By default, the Spark driver creates RDD partitions (each corresponding to a Spark task) for each S3 object (`Part1 ... N`). Then the Spark driver assigns tasks to each executor.

1. Each Spark task downloads its assigned S3 object and stores it in memory in the RDD partition. In this way, multiple Spark executors download and process their assigned task in parallel.

For more details about the initial number of partitions and optimization, see the [Parallelize tasks](parallelize-tasks.md) section.

### Catalyst optimizer
<a name="catalyst-optimizer.bc77b2d3-c13c-5e3c-ae9b-d726abc56131"></a>

Internally, Spark uses an engine called [Catalyst optimizer](https://www.databricks.com/glossary/catalyst-optimizer) to optimize execution plans. Catalyst has a query optimizer that you can use when running high-level Spark APIs, such as [Spark SQL](https://spark.apache.org/docs/latest/sql-programming-guide.html#sql), [DataFrame, and Datasets](https://spark.apache.org/docs/latest/sql-programming-guide.html#datasets-and-dataframes), as described in the following diagram.

![Logical plan goes throuh Catalyst optimizer, which outputs an optimized plan that is sent to RDDs.](http://docs.aws.amazon.com/prescriptive-guidance/latest/tuning-aws-glue-for-apache-spark/images/guide-img/ee14755c-1401-4ea5-afc7-732eb483b047/images/7b5448fb-a635-41f6-bf95-0fbc0d4489c7.png)

Because the Catalyst optimizer doesn't work directly with the RDD API, the high-level APIs are generally faster than the low-level RDD API. For complex joins, the Catalyst optimizer can significantly improve performance by optimizing the job run plan. You can see the optimized plan of your Spark job on the **SQL** tab of the Spark UI.

#### Adaptive Query Execution
<a name="adaptive-query-execution.7b52835b-20b9-5c95-91b9-39bf03fb4a6a"></a>

The Catalyst optimizer performs runtime optimization through a process called *Adaptive Query Execution*. Adaptive Query Execution uses runtime statistics to re-optimize the run plan of the queries while your job is running. Adaptive Query Execution offers several solutions to performance challenges, including coalescing post-shuffle partitions, converting sort-merge join to broadcast join, and skew join optimization, as described in the following sections.

Adaptive Query Execution is available in AWS Glue 3.0 and later, and it's enabled by default in AWS Glue 4.0 (Spark 3.3.0) and later. Adaptive Query Execution can be turned on and off by using `spark.conf.set("spark.sql.adaptive.enabled", "true")` in your code.

#### Coalescing post-shuffle partitions
<a name="coalescing-post-shuffle-partitions.ad4074c9-4ad0-50ed-aa79-822b97a2872d"></a>

This feature reduces RDD partitions (coalesce) after each shuffle based on the `map` output statistics. It simplifies the tuning of the shuffle partition number when running queries. You don't need to set a shuffle partition number to fit your dataset. Spark can pick the proper shuffle partition number at runtime after you have a large enough initial number of shuffle partitions.

Coalescing post-shuffle partitions is enabled when both `spark.sql.adaptive.enabled` and `spark.sql.adaptive.coalescePartitions.enabled` are set to true. For more information, see the [Apache Spark documentation](https://spark.apache.org/docs/latest/sql-performance-tuning.html#coalescing-post-shuffle-partitions).

#### Converting sort-merge join to broadcast join
<a name="converting-sort-merge-join-to-broadcast-join.4019bf8a-83a5-58d4-8a8f-b0f1b0b501c9"></a>

This feature recognizes when you are joining two datasets of substantially different size, and it adopts a more efficient join algorithm based on that information. For more details, see the [Apache Spark documentation](https://spark.apache.org/docs/latest/sql-performance-tuning.html#converting-sort-merge-join-to-broadcast-join). Join strategies are discussed in the [Optimize shuffles](optimize-shuffles.md) section.

#### Skew join optimization
<a name="skew-join-optimization.e7577526-94a1-56bc-91d0-255a2b16d585"></a>

Data skew is one of the most common bottlenecks for Spark jobs. It describes a situation in which data is skewed to specific RDD partitions (and consequently, specific tasks), which delays the overall processing time of the application. This can often downgrade the performance of join operations. The skew join optimization feature dynamically handles skew in sort-merge joins by splitting (and replicating if needed) skewed tasks into roughly even-sized tasks.

This feature is enabled when `spark.sql.adaptive.skewJoin.enabled` is set to true. For more details, see the [Apache Spark documentation](https://spark.apache.org/docs/latest/sql-performance-tuning.html#optimizing-skew-join). Data skew is discussed further in the [Optimize shuffles](optimize-shuffles.md) section.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
