---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/spark-tuning-glue-emr/architecture.html
---

# Architecture
<a name="architecture"></a>

The following diagram depicts the architecture of the solution described in this guide. An AWS Glue job reads data from an [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) bucket, which is a cloud-based object storage service that helps you store, protect, and retrieve data. You can initiate the AWS Glue Spark job through the AWS Management Console, [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html), or the AWS Glue API. The AWS Glue Spark job processes the raw data in an Amazon S3 bucket and then stores the processed data in a different bucket.

![AWS Glue with Spark processing raw data in an Amazon S3 bucket](https://docs.aws.amazon.com/prescriptive-guidance/latest/spark-tuning-glue-emr/images/guide-img/03a14f27-75e9-4b79-afab-d8b743354a10/images/a4e34dfd-155f-44fc-bf54-2a47b9112de9.png)

For example purposes, this guide describes a basic [AWS Glue Spark job](https://docs.aws.amazon.com/glue/latest/dg/etl-jobs-section.html), which is written in Python and Spark (PySpark). This AWS Glue job is used to demonstrate best practices for Spark SQL tuning. Although this guide focuses on AWS Glue, the best practices in this guide also apply to [Amazon EMR Spark jobs](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/jobs-spark.html).

The following diagram depicts the lifecycle of a Spark SQL query. The Spark Catalyst Optimizer generates a query plan. A *query plan* is a series of steps, like instructions, that are used to access the data in a SQL relational database system. To develop a performance-optimized Spark SQL query plan, the first step is to view the `EXPLAIN` plan, interpret the plan, and then tune the plan. You can use the Spark user interface (UI) or the Spark History Server to visualize the plan.

![Lifecycle of a Spark query to create a resilient distributed dataset (RDD)](https://docs.aws.amazon.com/prescriptive-guidance/latest/spark-tuning-glue-emr/images/guide-img/03a14f27-75e9-4b79-afab-d8b743354a10/images/a3a3d9b8-2f46-4203-8162-8eeb52bdae8d.png)

Spark Catalyst Optimizer converts the initial query plan into an optimized query plan as follows:

1. **Analysis and declarative APIs** – The analysis phase is the first step. The *unresolved logical plan*, where objects referenced in the SQL query are not known or not matched to an input table, is generated with unbound attributes and data types. The Spark Catalyst Optimizer then applies a set of rules to build a logical plan. The SQL parser can generate an SQL Abstract Syntax Tree (AST) and provide this as an input for the logical plan. The input might also be also be a data frame or dataset object that is constructed by using an API. The following table shows when you should use SQL, data frames, or datasets.

<table>
<tbody>
</tbody>
</table>

   For more information about the types of inputs, review the following:
   + A dataset API provides a **typed** version. This reduces performance because of heavy reliance on user-defined lambda functions. RDD or datasets are statically typed. For example, when you define an RDD, you need to explicitly provide the schema definition.
   + A data frame API provides **untyped** relational operations. Data frames are dynamically typed. Similar to RDD, when you define a data frame, the schema stays the same. The data is still structured. However, this information is only available at runtime. This allows the compiler to write SQL-like statements and define new columns on the fly. For example, it can append columns to an existing data frame without needing to define a new class for every operation.
   + A Spark SQL query is evaluated for syntax and analysis errors during runtime, which provides faster runtimes.

1. **Catalog** –** **Spark SQL uses Apache Hive Metastore (HMS) to manage the metadata of persistent relational entities, such as databases, tables, columns, and partitions.

1. **Optimization** –** **The optimizer rewrites the query plan by using heuristics and cost. It does the following to produce an optimized logical plan:

   1. Prunes columns

   1. Pushes down predicates

   1. Reorders joins

1. **Physical plans and the planner** – Spark Catalyst Optimizer converts the logical plan to a set of physical plans. This means it converts the *what* to *how.*

1. **Selected physical plans ­**– Spark Catalyst Optimizer selects the most cost-effective physical plan.

1. **Optimized query plan** – Spark SQL runs the performance-optimized and cost-optimized query plan. Spark Memory Management tracks the memory usage and distributes memory between tasks and operators. The Spark Tungsten engine can substantially improve the memory and CPU efficiency for Spark applications. It also implements binary data model processing, and it operates directly on binary data. This bypasses the need for deserialization and significantly reduces the overhead associated with data conversion and deserialization.
