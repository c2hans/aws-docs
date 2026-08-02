---
source_url: https://docs.aws.amazon.com/whitepapers/latest/big-data-analytics-options/amazon-emr.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Amazon EMR
<a name="amazon-emr"></a>

 [Amazon EMR](https://aws.amazon.com/elasticmapreduce/) is the industry-leading cloud big data platform for processing vast amounts of data using open source tools such as [Apache Spark](https://aws.amazon.com/emr/features/spark/), [Apache Hive](https://aws.amazon.com/emr/features/hive/), [Apache HBase](https://aws.amazon.com/emr/features/hbase/), [Apache Flink](https://aws.amazon.com/blogs/big-data/use-apache-flink-on-amazon-emr/), [Apache Hudi](https://aws.amazon.com/emr/features/hudi/), and [Presto](https://aws.amazon.com/emr/features/presto/). Amazon EMR makes it easy to set up, operate, and scale your big data environments by automating time-consuming tasks like provisioning capacity and tuning clusters. With EMR you can run petabyte-scale analysis at [less than half of the cost](https://pages.awscloud.com/Gated-IDC-The-Economic-Benefits-of-Migrating-Apache-Spark-and-Hadoop-to-Amazon-EMR.html) of traditional on-premises solutions and [over 3x faster](https://aws.amazon.com/blogs/big-data/amazon-emr-introduces-emr-runtime-for-apache-spark/) than standard Apache Spark. You can run workloads on Amazon EC2 instances, on Amazon EKS clusters, or on-premises using EMR on AWS Outposts.

Amazon EMR does all the work involved with provisioning, managing, and maintaining the infrastructure and software of a [Hadoop](https://hadoop.apache.org/) cluster. Amazon EMR now supports [Amazon EC2 M6g instances](https://aws.amazon.com/ec2/instance-types/m6/) to deliver the best price performance for cloud workloads. Amazon EC2 M6g instances are powered by [AWS Graviton2](https://aws.amazon.com/ec2/graviton/) processors that are custom designed by AWS, utilizing 64-bit [Arm Neoverse](https://www.arm.com/solutions/infrastructure) cores. Amazon EMR provides up to 35% lower cost and up to 15% improved performance for Spark workloads on Graviton2-based instances versus previous generation instances.

## Ideal usage patterns
<a name="ideal-usage-patterns-emr"></a>

 Amazon EMR’s flexible framework reduces large processing problems and data sets into smaller jobs and distributes them across many compute nodes in a Hadoop cluster. This capability lends itself to many usage patterns with big data analytics. Here are a few examples:
+  Log processing and analytics
+  Large ETL data movement
+  Risk modeling and threat analytics
+  Ad targeting and click stream analytics
+  Genomics
+  Predictive analytics
+  Ad hoc data mining and analytics

 For more information, see the [documentation for Amazon EMR](https://aws.amazon.com/emr/).

## Cost model
<a name="cost-model-emr"></a>

 With Amazon EMR, you can launch a persistent cluster that stays up indefinitely, or a temporary cluster that ends after the analysis is complete. In either scenario, you pay only for the hours the cluster is up.

 Amazon EMR supports a variety of Amazon EC2 instance types (standard, high CPU, high memory, high I/O, and so on) and all Amazon EC2 pricing options (On-Demand, Reserved, and Spot). When you launch an Amazon EMR cluster (also called a "job flow"), you choose how many and what type of Amazon EC2 instances to provision. The Amazon EMR price is in addition to the Amazon EC2 price.

For more information, see [Amazon EMR pricing.](https://aws.amazon.com/elasticmapreduce/pricing/)

## Performance
<a name="performance-emr"></a>

 Amazon EMR performance is driven by the type of EC2 instances on which you choose to run your cluster, and how many you chose to run your analytics. You should choose an instance type suitable for your processing requirements, with sufficient memory, storage, and processing power. With the introduction of Graviton2 instances, you can see improved performance of up to 15% relative to equivalent previous generation instances. For more information about EC2 instance specifications, see [Amazon EC2 Instance Types](https://aws.amazon.com/ec2/instance-types/).

An important consideration when you create an EMR cluster is how you configure Amazon EC2 instances. EC2 instances in an EMR cluster are organized into node types.

The [node types in Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-master-core-task-nodes.html) are as follows:
+ **Primary node** — A node that manages the cluster by running software components to coordinate the distribution of data and tasks among other nodes for processing. The primary node tracks the status of tasks and monitors the health of the cluster. Every cluster has a primary node, and it's possible to create a single-node cluster with only the primary node.
+ **Core node** — A node with software components that run tasks and store data in the Hadoop Distributed File System (HDFS) on your cluster. Multi-node clusters have at least one core node.
+ **Task node** — A node with software components that only runs tasks and does not store data in HDFS. Task nodes are optional.

## Durability and availability
<a name="durability-and-availability-emr"></a>

 By default, Amazon EMR is fault tolerant for core node failures and continues job execution if a dependent node goes down. Amazon EMR will also provision a new node when a core node fails. However, Amazon EMR will not replace nodes if all nodes in the cluster are lost.

You can monitor the health of nodes and replace failed nodes with Amazon CloudWatch. When you launch an Amazon EMR cluster, you can choose to have one or three primary nodes in your cluster. Launching a cluster with three primary nodes is only supported by Amazon EMR version 5.23.0 and later. EMR can take advantage of EC2 placement groups to ensure primary nodes are placed on distinct underlying hardware to further improve cluster availability.

For more information, see [EMR integration with EC2 placement groups](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-ha-placementgroup.html).

## Scalability and elasticity
<a name="scalability-and-elasticity-emr"></a>

With Amazon EMR, it's easy to [resize a running cluster](https://aws.amazon.com/blogs/big-data/best-practices-for-resizing-and-automatic-scaling-in-amazon-emr/). You can add core nodes which hold the HDFS at any time to increase your processing power and increase the HDFS storage capacity (and throughput). Additionally, you can use Amazon S3 natively, or using EMRFS along with or instead of local HDFS, which enables you to decouple your memory and compute from your storage providing greater flexibility and cost efficiency.

You can also add and remove task nodes at any time which can process Hadoop jobs, but do not maintain HDFS. Some customers add hundreds of instances to their clusters when their batch processing occurs, and remove the extra instances when processing completes. For example, you may not know how much data your clusters will be handling in six months, or you may have spiky processing needs.

 With Amazon EMR, you don't need to guess your future requirements or provision for peak demand because you can easily add or remove capacity at any time.

You can add all new clusters of various sizes and remove them at any time with a few clicks in the console or by a [programmatic](https://docs.aws.amazon.com/emr/latest/APIReference/API_Operations.html) API call.

Additionally, you can configure instance fleets for a cluster to choose a wide variety of provisioning options for EC2 instances. With instance fleets you can specify target capacities on On-Demand Instances, and Spot Instances within each fleet. Amazon EMR tries to provide the capacity you need with the best mix of capacity and price based on your selection of Availability Zones.

While a cluster is running, if Amazon EC2 reclaims a Spot Instance because of a price increase, or an instance fails, Amazon EMR tries to replace the instance with any of the instance types that you specify. This makes it easier to regain capacity if a node is lost for any reason.

## Interfaces
<a name="interfaces-emr"></a>

 Amazon EMR supports many tools on top of [Hadoop](https://hadoop.apache.org/) that can be used for big data analytics and each has their own interfaces. Here is a brief summary of the most popular options:

### Hive
<a name="hive-emr"></a>

 [Hive](https://hive.apache.org/) is an open source data warehouse and analytics package that runs on top of Hadoop. Hive is operated by Hive QL, a SQL-based language, which enables users to structure, summarize, and query data. Hive QL goes beyond standard SQL, adding first-class support for map/reduce functions and complex extensible user-defined data types like JSON and Thrift. This capability allows processing of complex and unstructured data sources such as text documents and log files.

 Hive allows user extensions via user-defined functions written in Java. Amazon EMR has made numerous improvements to Hive, including direct integration with DynamoDB and Amazon S3. For example, with Amazon EMR you can load table partitions automatically from S3, you can write data to tables in S3 without using temporary files, and you can access resources in S3, such as scripts for custom map and/or reduce operations and additional libraries.

For more information, see [Apache Hive](https://docs.aws.amazon.com/ElasticMapReduce/latest/ReleaseGuide/emr-hive.html) in the *Amazon EMR Release Guide*.

### Pig
<a name="pig-emr"></a>

[Pig](https://pig.apache.org/) is an open-source analytics package that runs on top of Hadoop. Pig is operated by Pig Latin, an SQL-like language which enables users to structure, summarize, and query data. Pig Latin also adds first-class support for map and reduce functions and complex extensible user-defined data types. This capability allows processing of complex and unstructured data sources such as text documents and log files.

Pig allows user extensions via user-defined functions written in Java. Amazon EMR has made numerous improvements to Pig, including the ability to use multiple file systems (normally, Pig can only access one remote file system), the ability to load customer JARs and scripts from S3 (such as “`REGISTER s3://my-bucket/piggybank.jar`”), and additional functionality for String and DateTime processing.

For more information, see [Apache Pig](https://docs.aws.amazon.com/ElasticMapReduce/latest/ReleaseGuide/emr-pig.html) in the *Amazon EMR Release Guide*.

### Spark
<a name="spark-emr"></a>

[Spark](https://spark.apache.org/) is an open-source data analytics engine built on Hadoop with the fundamentals for in-memory MapReduce. Spark provides additional speed for certain analytics and is the foundation for other power tools such as Shark (SQL driven data warehousing), Spark Streaming (streaming applications), GraphX (graph systems) and MLlib (machine learning).

EMR features [Amazon EMR runtime for Apache Spark](https://aws.amazon.com/blogs/big-data/amazon-emr-introduces-emr-runtime-for-apache-spark/), a performance-optimized runtime environment for Apache Spark that is active by default on Amazon EMR clusters. Amazon EMR runtime for Apache Spark can be over 3x faster than clusters without the EMR runtime, and has 100% API compatibility with standard Apache Spark. This improved performance means your workloads run faster and saves you compute costs, without making any changes to your applications.

For more information, see [Apache Spark on Amazon EMR](https://aws.amazon.com/emr/details/spark/) .

### HBase
<a name="hbase-emr"></a>

[HBase](https://hbase.apache.org/) is an open-source, non-relational, distributed database modeled after Google's [Bigtable](https://cloud.google.com/bigtable). It was developed as part of Apache Software Foundation's Hadoop project and runs on top of Hadoop Distributed File System (HDFS) to provide BigTable-like capabilities for Hadoop. HBase provides you a fault-tolerant, efficient way of storing large quantities of sparse data using column-based compression and storage. In addition, HBase provides fast lookup of data, because data is stored in-memory instead of on disk.

HBase is optimized for sequential write operations, and it is highly efficient for batch inserts, updates, and deletes. HBase works seamlessly with Hadoop, sharing its file system and serving as a direct input and output to Hadoop jobs. HBase also integrates with Apache Hive, enabling SQL-like queries over HBase tables, joins with Hive-based tables, and support for Java Database Connectivity (JDBC). With Amazon EMR, you can back up HBase to Amazon S3 (full or incremental, manual or automated) and you can restore from a previously created backup.

For more information, see [Apache HBase](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hbase.html) in the *Amazon EMR Release Guide*.

### Presto
<a name="presto-emr"></a>

[Presto](https://prestodb.io/) is an open-source distributed SQL query engine optimized for low-latency, ad hoc analysis of data. It supports the ANSI SQL standard, including complex queries, aggregations, joins, and window functions. Presto can process data from multiple data sources, including HDFS and Amazon S3.

### Hudi
<a name="hudi"></a>

[Apache Hudi](https://hudi.apache.org/) is an open-source data management framework used to simplify incremental data processing and data pipeline development by providing record-level insert, update, upsert, and delete capabilities. *Upsert* refers to the ability to insert records into an existing dataset if they do not already exist or to update them if they do. By efficiently managing how data is laid out in S3, Hudi allows data to be ingested and updated in near-real-time. Hudi carefully maintains metadata of the actions performed on the dataset to help ensure that the actions are atomic and consistent. Hudi is integrated with [Apache Spark](https://aws.amazon.com/emr/features/spark/), [Apache Hive](https://hive.apache.org/), and [Presto](https://prestodb.github.io/). In Amazon EMR release versions 6.1.0 and later, Hudi is also integrated with [Trino](https://trino.io/) (PrestoSQL).

### Kinesis Connector
<a name="kinesis-connector-emr"></a>

 The [Kinesis Connector](https://docs.aws.amazon.com/kinesisanalytics/latest/java/how-connectors.html) enables EMR to directly read and query data from Kinesis Data Streams. You can perform batch processing of Kinesis streams using existing Hadoop tools such as Hive, Pig, [MapReduce](https://en.wikipedia.org/wiki/MapReduce), [Hadoop Streaming](https://hadoop.apache.org/docs/r1.2.1/streaming.html), and Cascading. Some use cases enabled by this integration are:
+  **Streaming log analysis** — You can analyze streaming web logs to generate a list of top ten error types every few minutes by Region, browser, and access domains.
+  **Complex data processing workflows **— You can join Kinesis stream with data stored in Amazon S3, Dynamo DB tables, and HDFS. You can write queries that join clickstream data from Kinesis with advertising campaign information stored in a DynamoDB table to identify the most effective categories of ads that are displayed on particular websites.
+  **Ad-hoc queries** — You can periodically load data from Kinesis into HDFS and make it available as a local [Impala table](https://impala.apache.org/docs/build/html/topics/impala_tables.html) for fast, interactive, analytic queries.

### Other third-party tools
<a name="other-third-party-tools-emr"></a>

Amazon EMR also supports a variety of other popular applications and tools in the Hadoop system, such as [R](https://www.rstudio.com/) (statistics), [Mahout](https://mahout.apache.org/) (machine learning),[ Ganglia](https://docs.amazonaws.cn/en_us/emr/latest/ReleaseGuide/emr-ganglia.html) (monitoring), [Accumulo](https://accumulo.apache.org/) (secure NoSQL database), [Hue](https://gethue.com/) (user interface to analyze Hadoop data), [HCatalog](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-hcatalog.html) (table and storage management), and more.

Additionally, you can install your own software on top of Amazon EMR to help solve your business needs. AWS provides the ability to quickly move large amounts of data from S3 to HDFS, from HDFS to S3, and between S3 buckets using Amazon EMR’s [S3DistCp,](https://docs.aws.amazon.com/ElasticMapReduce/latest/DeveloperGuide/UsingEMR_s3distcp.html) an extension of the open source tool [DistCp](https://hadoop.apache.org/docs/current/hadoop-distcp/DistCp.html) that uses MapReduce to efficiently move large amounts of data.

You can optionally use the EMR File System (EMRFS), an implementation of HDFS which allows Amazon EMR clusters to store data on S3. You can enable S3 server-side and client-side encryption.

### EMR Studio
<a name="emr-studio"></a>

[EMR Studio](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio.html) is an integrated development environment (IDE) that makes it easy for data scientists and data engineers to develop, visualize, and debug data engineering and data science applications written in R, Python, Scala, and PySpark.

EMR Studio provides fully managed [Jupyter](https://jupyter.org/) Notebooks, and tools like [Spark](https://spark.apache.org/) UI and [YARN Timeline Service](https://hadoop.apache.org/docs/current/hadoop-yarn/hadoop-yarn-site/TimelineServer.html) to simplify debugging. Data scientists and analysts can install custom kernels and libraries, collaborate with peers using code repositories such as GitHub and BitBucket, or run parameterized notebooks as part of scheduled workflows using orchestration services like [Apache Airflow](https://airflow.apache.org/) or Amazon Managed Workflows for Apache Airflow. Administrators can set up EMR Studio such that analysts can run their applications on existing EMR clusters, or create new clusters using pre-defined CloudFormation templates for EMR.

## Anti-patterns
<a name="anti-patterns-emr"></a>

 Amazon EMR has the following anti-pattern:
+  **Small datasets** – Amazon EMR is built for massive parallel processing; if your data set is small enough to run quickly on a single machine, in a single thread, the added overhead to map and reduce jobs may not be worth it for small datasets that can easily be processed in memory on a single system. Amazon EMR or a relational database running on Amazon EMR may be a better option for workloads with stringent requirements.
