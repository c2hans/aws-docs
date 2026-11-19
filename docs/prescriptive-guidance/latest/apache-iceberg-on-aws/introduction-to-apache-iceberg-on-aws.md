---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/introduction-to-apache-iceberg-on-aws.html
---

# Introduction to Apache Iceberg on AWS

## Data lake challenges that Iceberg addresses
<a name="data-lake-challenges-that-iceberg-addresses"></a>

The evolution of data storage has progressed from databases to data warehouses and data lakes, where each technology addresses unique business and data requirements. Traditional databases excelled at handling structured data and transactional workloads, but they faced performance challenges as data volumes increased. Data warehouses emerged to tackle performance and scalability issues, but like databases, they relied on proprietary formats within vertically integrated systems.

Data lakes offer one of the best options for storing data in terms of cost, scalability, and flexibility. You can use a data lake to retain large volumes of structured and unstructured data at a low cost, and use this data for different types of analytics workloads, from business intelligence reporting to big data processing, real-time analytics, machine learning, and generative artificial intelligence (AI), to help guide better decisions.

Despite these benefits, data lakes weren't initially designed with database-like capabilities. A data lake doesn't provide support for atomicity, consistency, isolation, and durability (ACID) processing semantics, which you might require to optimize and manage your data effectively at scale across hundreds or thousands of users by using many different technologies. Data lakes don't provide native support for the following functionality:
+ Performing efficient record-level updates and deletions as data changes in your business
+ Managing query performance as tables grow to millions of files and hundreds of thousands of partitions
+ Ensuring data consistency across multiple concurrent writers and readers
+ Preventing data corruption when write operations fail partway through the operation
+ Evolving table schemas over time without (partially) rewriting datasets

These challenges have become particularly prevalent in use cases such as handling change data capture (CDC) or use cases pertaining to privacy, deletion of data, and streaming data ingestion, which can result in sub-optimal tables.

Data lakes that use the traditional Hive-format tables support write operations only for entire files. This makes updates and deletes difficult to implement, time consuming, and costly. Moreover, concurrency controls and guarantees offered in ACID-compliant systems are needed to ensure data integrity and consistency.

These challenges leave users with a dilemma: choose between a fully integrated but proprietary platform, or opt for a vendor-neutral but resource-intensive, self-built data lake that requires constant maintenance and migration to realize its potential value.

To help overcome these challenges, Iceberg provides additional database-like functionality that simplifies the optimization and management overhead of data lakes, while still supporting storage on cost-effective systems such as [Amazon S3](https://aws.amazon.com/s3).

## Introduction to Apache Iceberg
<a name="introduction-to-apache-iceberg"></a>

Apache Iceberg is an open-source table format that provides features in data lake tables that were historically only available in databases or data warehouses. It's designed to scale from small tables to petabyte-sized datasets without sacrificing performance, making it well-suited for workloads of any size. Some of the main features of Iceberg tables are:
+ **Delete, update, and merge. **Iceberg supports standard SQL commands for data warehousing for use with data lake tables.
+ **Fast scan planning and advanced filtering.** Iceberg stores metadata such as partition and column-level statistics that can be used by engines to speed up planning and running queries.
+ **Full schema evolution.** Iceberg supports adding, dropping, updating, or renaming columns without side-effects.
+ **Partition evolution.** You can update the partition layout of a table as data volume or query patterns change. Iceberg supports changing the columns that a table is partitioned on, or adding columns to, or removing columns from, composite partitions.
+ **Hidden partitioning. **This feature prevents reading unnecessary partitions automatically. This eliminates the need for users to understand the table's partitioning details or to add extra filters to their queries.
+ **Version rollback.** Users can quickly correct problems by reverting to a pre-transaction state.
+ **Time travel.** Users can query a specific previous version of a table.
+ **Serializable isolation.** Table changes are atomic, so readers never see partial or uncommitted changes.
+ **Concurrent writers.** Iceberg uses optimistic concurrency to allow multiple transactions to succeed. In case of conflicts, one of the writers has to retry the transaction.
+ **Native maintenance capabilities.** Iceberg exposes built-in procedures to keep tables healthy over time, including compacting small files (optionally with sorting or z-ordering to co-locate related rows and improve data skipping at query time), rewriting manifests, expiring old snapshots, and removing orphan files. These operations run as standard SQL or engine procedures, so you don't need custom tooling to control storage growth and sustain query performance.
+ **Open file formats.** Iceberg supports multiple open source file formats, including [Apache Parquet](https://parquet.apache.org/), [Apache Avro](https://avro.apache.org/), and [Apache ORC](https://orc.apache.org/).
+ **Open catalog interface (Iceberg REST Catalog).** Iceberg defines an open REST specification for catalog operations such as creating tables, committing snapshots, and resolving metadata. Clients talk to the catalog over plain HTTP using the generic REST catalog client, with no catalog-specific SDKs, drivers, or JAR dependencies to bundle. Any engine that speaks the Iceberg REST protocol can work with any compliant catalog implementation, such as the AWS Glue Data Catalog.

In summary, data lakes that use the Iceberg format benefit from transactional consistency, speed, scale, and schema evolution. For more information about these and other Iceberg features, see the [Apache Iceberg documentation](https://iceberg.apache.org/docs/latest/).

### Business outcomes
<a name="business-outcomes.aca30ca6-7b68-5430-bd2b-83ed0aef9411"></a>

Translating the features above into what teams actually see day to day:
+ **Lower operational overhead.** Row-level `UPDATE`, `DELETE`, and `MERGE` replace the custom Spark jobs, partition rewrites, and manual reconciliation that Hive-format tables typically require for CDC, GDPR/CCPA deletions, and late-arriving data. Platform teams spend less time maintaining pipelines and more time delivering new data products.
+ **Lower query cost.** Partition and column-level statistics, hidden partitioning, and manifest-level pruning let engines skip files before reading them. File compaction further reduces scan overhead by merging many small files into fewer right-sized files, and compaction with sorting (z-order or sort-order-based) co-locates rows with similar values so that column min/max statistics prune even more files for selective queries. The same query scans less data and issues fewer S3 LIST/GET requests (thanks to Iceberg metadata), which directly reduces cost on consumption-priced query engines, lowers S3 request charges, and reduces runtime.
+ **Faster time to insight.** Schema and partition evolution are metadata-only operations, so adding a column or changing a partition layout no longer requires a multi-hour table rewrite or a coordinated downtime window. Analytics teams can respond to new requirements in minutes instead of days.
+ **Reduced risk and faster incident recovery.** Serializable isolation prevents readers from seeing partial writes, and version rollback turns a bad write or a corrupted upstream feed into a one-statement fix instead of a restore-from-backup operation.
+ **Simplified auditing and reproducibility.** Time travel lets you query the exact state of a table at any past snapshot or timestamp, so you can reproduce a report, investigate a data discrepancy, or satisfy regulatory audit requests without maintaining separate snapshot copies or point-in-time backups.
+ **No vendor lock-in.** Because Iceberg is an open table format with open file formats (Parquet, ORC, Avro) on your own S3 storage, the same tables are readable by AWS services such as Amazon Athena, Amazon EMR, AWS Glue, and Amazon Redshift, by open source engines such as Apache Spark, Apache Flink, Trino, DuckDB, and PyIceberg, and by third-party platforms. Teams can change engines or add new ones without migrating data.

## Iceberg table anatomy
<a name="iceberg-table-anatomy"></a>

Now that we've covered the main Iceberg capabilities, let's dive deeper into the details and design of an Iceberg table.

These capabilities are enabled by Iceberg's hierarchical layers of data and metadata files, which manage metadata intelligently to optimize query planning and execution.

The following diagram portrays the organization of an Iceberg table through two perspectives: the AWS services used to store the table and the file placement in Amazon S3.

![Iceberg table anatomy with Iceberg metadata layers on top of data files](https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/images/guide-img/ceffa39e-028d-47b6-a54a-6ef8526aee6a/images/f98a7441-6878-45a7-b905-842bba72d007.png)

As shown in the diagram, an Iceberg table consists of three main layers:
+ **Iceberg catalog**: The catalog holds the pointer to the current table metadata file and is what makes Iceberg commits atomic — every write commit is a compare-and-swap of that pointer to a new metadata file. Iceberg supports several catalog types (AWS Glue Data Catalog, Iceberg REST catalogs, Hive Metastore, ..). On AWS, the AWS Glue Data Catalog is the default choice for most workloads, and integrated services such as Amazon Athena, Amazon Redshift, Amazon EMR, and AWS Glue read and write Iceberg tables through it.
+ **Metadata layer**: A hierarchy of files that keeps track of the schema, partition specs, sort orders, and snapshot history of the table, plus per-file and per-column statistics that engines use to prune reads. These files are stored in Amazon S3 within the table's `metadata/` prefix.
  + **Table metadata file (JSON)**, one for each table commit operation (write, alter, rollback, and so on), records the whole table state at that point: the current snapshot ID, the list of snapshots (each pointing at a manifest list), the history of schemas, partition specs, and sort orders (with an indication of the current ones), and any named refs such as branches and tags.
  + **Manifest list (Avro)**, one per snapshot, contains one entry per manifest file that makes up the snapshot. Each entry carries manifest-level stats — most importantly the partition value ranges (per-partition-column min/max aggregated across every data file the manifest references), record counts, and added/deleted file counts. Query engines use those ranges to skip entire manifest files during scan planning when a query's partition filter doesn't overlap them, which is why scan planning stays fast as the table grows.
  + **Manifest files (Avro)** contain one record per data file, including its location, format, partition values, record count, size, and column-level statistics (value, null, and NaN counts, lower and upper bounds) that engines use to skip files during scan planning.
+ **Data layer**: This layer contains the files that queries actually scan. Data files can be stored in different formats, including [Apache Parquet](https://parquet.apache.org/), [Apache Avro](https://avro.apache.org/), and [Apache ORC](https://orc.apache.org/).
  + **Data files** contain the data records for the table.
  + **Delete files** encode row-level delete and update operations produced by merge-on-read writers. V2 tables use *positional* and *equality* delete files (see [delete formats](https://iceberg.apache.org/spec/#delete-formats) in the Iceberg spec). V3 tables replace positional delete files with **deletion vectors** stored in Puffin files, which are much more efficient at query time.

## Hosting Iceberg tables on AWS: self-managed vs. Amazon S3 Tables
<a name="hosting-iceberg-tables-on-aws-self-managed-vs-amazon-s3-tables"></a>

On AWS you can host Apache Iceberg tables as **self-managed Iceberg on Amazon S3** or in **Amazon S3 Tables**. Both use the same Iceberg table format; with Amazon S3 Tables, the heavy lifting (Iceberg table maintenance and replication) is managed for you.

For a side-by-side comparison covering storage, catalog, compaction, snapshot management, unreferenced file removal, table replication, transaction throughput, storage tiering, access control, and cost model, see [Hosting Iceberg tables on AWS: self-managed vs. Amazon S3 Tables](apache-iceberg-on-aws-self-managed-vs-s3-tables.md).

## AWS support for Apache Iceberg
<a name="aws-support-for-apache-iceberg"></a>

Apache Iceberg is supported by a wide range of AWS services. The following diagram depicts a simplified reference architecture of a data lake that's based on Iceberg.

![A simplified reference architecture of a data lake that's based on Iceberg](https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/images/guide-img/ceffa39e-028d-47b6-a54a-6ef8526aee6a/images/405ad614-a7e3-48ff-beea-26463a91f7e9.png)

The following AWS services provide native Iceberg integrations. There are additional AWS services that can interact with Iceberg, either indirectly or by packaging the Iceberg libraries.
+ [**Amazon S3**](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is the best place to build data lakes because of its durability, availability, scalability, security, compliance, and audit capabilities. Iceberg was designed and built to interact with Amazon S3 seamlessly, and provides support for many Amazon S3 features as listed in the [Iceberg documentation](https://iceberg.apache.org/docs/latest/aws/#s3-fileio). In addition, [Amazon S3 Tables](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables.html) deliver the first cloud object store with built-in Iceberg support and streamline storing tabular data at scale. With S3 Tables support for Iceberg, you can easily query your tabular data by using popular AWS and third-party query engines. Table buckets automate table maintenance (compaction, snapshot expiration, orphan-file cleanup) and expose Iceberg tables through an Iceberg REST catalog and, when integrated with AWS analytics services, through the AWS Glue Data Catalog under the `s3tablescatalog/<table-bucket-name>` federated catalog. See [Getting started with Amazon S3 Tables](getting-started-with-amazon-s3-tables.md).
+ [**Amazon EMR**](https://docs.aws.amazon.com/emr/) is a big data solution for petabyte-scale data processing, interactive analytics, and machine learning by using open source frameworks such as Apache Spark, Flink, Trino, and Hive. Amazon EMR can run on customized Amazon Elastic Compute Cloud (Amazon EC2) clusters, Amazon Elastic Kubernetes Service (Amazon EKS), AWS Outposts, or Amazon EMR Serverless. See [Working with Iceberg in Amazon EMR (Spark)](working-with-iceberg-in-amazon-emr-spark.md) and [Working with Iceberg tables by using Trino (Amazon EMR)](working-with-iceberg-tables-by-using-trino-amazon-emr.md).
+ [**Amazon Athena**](https://docs.aws.amazon.com/athena/latest/ug/what-is.html) is a serverless, interactive analytics service that's built on open source frameworks. It supports open-table and file formats and provides a simplified, flexible way to analyze petabytes of data where it lives. Athena provides native support for read, time travel, write, and DDL queries for Iceberg and uses the AWS Glue Data Catalog for the Iceberg metastore. See [Working with Iceberg tables by using Athena SQL queries](working-with-iceberg-tables-by-using-athena-sql-queries.md).
+ [**Amazon Redshift**](https://docs.aws.amazon.com/redshift/) is a petabyte-scale cloud data warehouse with provisioned and serverless deployment options. Amazon Redshift queries Iceberg tables cataloged in the AWS Glue Data Catalog (on Redshift Serverless and RG instance types with its own compute, on RA3 instance types through Redshift Spectrum), and creates and writes Iceberg tables in Amazon S3 and Amazon S3 Tables directly from SQL. Redshift materialized views can be defined on Iceberg tables. See [Working with Iceberg tables by using Amazon Redshift](working-with-iceberg-tables-by-using-amazon-redshift.md).
+ [**AWS Glue**](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html) is a serverless data integration service that makes it easier to discover, prepare, move, and integrate data from multiple sources for analytics, machine learning (ML), and application development. It is fully integrated with Iceberg. Specifically, you can perform read and write operations on Iceberg tables by using AWS Glue jobs, manage tables through the [AWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/start-data-catalog.html) (Hive metastore-compatible), discover and register tables automatically by using AWS Glue crawlers, and evaluate data quality in Iceberg tables through the AWS Glue Data Quality feature. The AWS Glue Data Catalog also supports collecting column statistics, calculating and updating the number of distinct values (NDVs) for each column in Iceberg tables, and automatic table optimizations (compaction, snapshot retention, orphan file deletion). AWS Glue also supports zero-ETL integrations from a list of AWS services and third-party applications into Iceberg tables. See [Working with Iceberg in AWS Glue](iceberg-glue.md).
+ [**Amazon Data Firehose**](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html) is a fully managed service for delivering real-time streaming data to destinations such as Amazon S3, Amazon Redshift, Amazon OpenSearch Service, Amazon OpenSearch Serverless, Splunk, Apache Iceberg tables, and any custom HTTP or HTTP endpoints owned by supported third-party service providers, including Datadog, Dynatrace, LogicMonitor, MongoDB, New Relic, Coralogix, and Elastic. With Firehose, you don't need to write applications or manage resources. You configure your data producers to send data to Firehose, and it automatically delivers the data to the destination that you specified. You can also configure Firehose to transform your data before delivering it. See [Working with Iceberg tables by using Amazon Data Firehose](iceberg-firehose.md).
+ [**Amazon Kinesis Data Streams**](https://docs.aws.amazon.com/streams/latest/dev/data-delivery-st.html) and [**Amazon MSK**](https://docs.aws.amazon.com/msk/latest/developerguide/msk-data-delivery-iceberg-supported-configs.html) (Express brokers) deliver streams directly as Iceberg tables on Amazon S3 Tables through streaming tables: no connector, Flink, or Spark job in between, with exactly-once delivery, inline compaction, and automatic registration in the AWS Glue Data Catalog. See [Streaming directly to Iceberg from Amazon Kinesis Data Streams and Amazon MSK](streaming-directly-to-iceberg-from-kinesis-and-msk.md).
+ [**Amazon Managed Service for Apache Flink**](https://docs.aws.amazon.com/managed-flink/latest/java/what-is.html) is a fully managed Amazon service that lets you use an Apache Flink application to process streaming data. It supports both reading from and writing to Iceberg tables, and enables real-time data processing and analytics.
+ [**Amazon SageMaker AI**](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html) supports the storage of feature sets in Amazon SageMaker AI Feature Store by using Iceberg format.
+ [**Amazon SageMaker Unified Studio**](https://aws.amazon.com/sagemaker/unified-studio/) is a unified development environment for data, analytics, and AI workflows, built on a lakehouse architecture that supports the Apache Iceberg table format as a first-class open format across analytics engines. It accesses Iceberg tables cataloged in the AWS Glue Data Catalog, querying them with engines such as Amazon Athena, Amazon EMR, Amazon Redshift, and AWS Glue (Apache Spark); the catalog also exposes an Iceberg REST API so that third-party and open-source engines like PyIceberg can connect to the same tables.
+ [**Amazon Elastic Container Service (Amazon ECS)**](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html) is a fully managed container orchestration service. You can run any Iceberg-compatible engine (e.g., [PyIceberg](iceberg-pyiceberg.md), or DuckDB) as a container on Amazon ECS to read and write Iceberg tables.
+ [**Amazon Elastic Kubernetes Service (Amazon EKS)**](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html) is a managed Kubernetes service. Iceberg-capable engines that ship as containers (e.g., [PyIceberg](iceberg-pyiceberg.md) or DuckDB sidecars) can read and write Iceberg tables from pods scheduled on Amazon EKS.
+ [**AWS Lambda**](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a serverless compute service that runs event-driven code on demand. It's a good fit for lightweight, bursty Iceberg reads and writes when paired with [PyIceberg](iceberg-pyiceberg.md) or DuckDB as the in-process Iceberg engine — for example, an HTTPS query endpoint served by DuckDB inside Lambda, or a scheduled/event based Iceberg ingest task built with PyIceberg.
+ [**AWS Lake Formation**](https://docs.aws.amazon.com/lake-formation/latest/dg/what-is-lake-formation.html) provides coarse and fine-grained access control permissions to access data, including Iceberg tables consumed by Athena or Amazon Redshift. To learn more about permissions support for Iceberg tables, see the [Lake Formation documentation](https://docs.aws.amazon.com/lake-formation/latest/dg/working-with-services.html).

The following sections of this guide explain how to integrate these AWS services with Apache Iceberg.

For detailed architecture references by use case see [Reference architectures](reference-architectures.md).
