---
source_url: https://docs.aws.amazon.com/decision-guides/latest/decision-guides/analytics-on-aws-how-to-choose.html
---

# Choosing an AWS analytics service

**Taking the first step**

|  |  |
| --- |--- |
| **Purpose** | Help determine which AWS analytics services are the best fit for your organization. |
| **Last updated** | November 19, 2026 |
| **Covered services** |  +  [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/getting-started.html) <br />+  [AWS Clean Rooms](https://docs.aws.amazon.com/clean-rooms/latest/userguide/what-is.html#first-time-user) <br />+   [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html) <br />+  [Amazon DataZone](https://docs.aws.amazon.com/datazone/latest/userguide/getting-started.html) <br />+  [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-gs.html) <br />+  [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/setting-up.html) <br />+  [Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/examples.html) <br />+  [AWS Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/getting-started-setup.html) <br />+  [Amazon Managed Service for Apache Flink](https://docs.aws.amazon.com/managed-flink/latest/java/what-is.html) <br />+  [Amazon Managed Streaming for Apache Kafka](https://docs.aws.amazon.com/msk/latest/developerguide/getting-started.html) <br />+  [Amazon Managed Workflows for Apache Airflow](https://docs.aws.amazon.com/mwaa/latest/userguide/what-is-mwaa.html) <br />+  [Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/gsg.html) <br />+  [AWS Quick Sight](https://docs.aws.amazon.com/quick/latest/userguide/quick-sight-getting-started.html) <br />+  [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/gsg/new-user.html) <br />+  [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/GetStartedWithS3.html) <br />+  [Amazon SageMaker](https://docs.aws.amazon.com/next-generation-sagemaker/)   |

## Introduction
<a name="intro"></a>

Organizations collect data from operational databases, business applications, files, and continuous event streams, and they need to turn that data into reports, dashboards, real-time insights, and inputs for machine learning (ML) and generative AI. AWS offers analytics services for each step: bringing data in, storing it, processing and transforming it, querying it, visualizing it, and governing who can access it.

**Many of these services overlap, by design.** The same job can often be done in more than one way:
+ **SQL on data in Amazon S3** can run in Amazon Athena, in Amazon Redshift through Redshift Spectrum, or with Trino on Amazon EMR.
+ **Apache Spark processing** can run in AWS Glue, Amazon EMR, or Athena for Apache Spark.
+ **Replicating operational data without pipelines** is available through zero-ETL integrations in both Amazon Redshift and AWS Glue.
+ **Federated query** is available in both Athena and Amazon Redshift.
+ **Stream processing** can run in Amazon Managed Service for Apache Flink, as Apache Flink on Amazon EMR, or as AWS Glue streaming ETL.
+ **Apache Iceberg tables** work with Amazon EMR, Athena, Amazon Redshift, AWS Glue, and Amazon SageMaker, so different engines can work on the same copy of data.

Because of this overlap, choosing a service is less about finding the single service that can do a job and more about finding the one that fits how you work. The most important factors are:
+ **How your teams work:** SQL, code, or visual tools.
+ **How much infrastructure you want to manage:** serverless, or clusters that you configure.
+ **How quickly you need results:** batch, interactive, or streaming.
+ **Where your data lives today:** operational databases, software as a service (SaaS) applications, Amazon S3, or event streams.

You don't have to choose between individual services and a unified experience. Amazon SageMaker Unified Studio brings tools from Amazon EMR, AWS Glue, Amazon Redshift, Amazon Bedrock, and Amazon SageMaker Studio into one environment for SQL analytics, big data processing, and model development. Many architectures use several of the services in this guide together.

**How to use this guide**

1. **Understand** the jobs that analytics architectures perform and which AWS services perform each one.

1. **Consider** the criteria that change which service fits your workload.

1. **Choose** a starting service for each of your needs, and see when an alternative is a better fit.

1. **Use** the getting-started resources for the services you choose.

1. **Explore** reference architectures, solutions, and other resources.

[![AWS Videos](https://img.youtube.com/vi/9Y1bwAmx0Do/0.jpg)](https://www.youtube.com/watch?v=9Y1bwAmx0Do&t=397s)

This eight-minute excerpt is from a one-hour presentation by Sirish Chandrasekaran and Rick Sears at re:Invent 2024. It provides an overview of how a fictional company, Maxdome, uses SageMaker Unified Studio AI and analytics to unlock data insights.

## Understand AWS analytics services
<a name="understand"></a>

Most analytics architectures do the same set of jobs: bring data in, store it, process and transform it, query it, analyze streams as they arrive, present results, and govern access. Many AWS services overlap. Several of them can do the same job in different ways, such as with SQL or code, serverless or on clusters you configure, and in batch or in real time. The following diagram shows the AWS analytics services that this guide covers. The tabs that follow are organized by job. Each one lists the services in this guide that do that job, and explains how.

![Diagram showing the AWS analytics services](https://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/analytics-services.png)

This guide covers the following services, organized by the job they do:
+ **Unified analytics and AI**: Amazon SageMaker Unified Studio and Amazon SageMaker.
+ **Ingest and replicate data**: Amazon Redshift, AWS Glue, Amazon Kinesis Data Streams, Amazon Managed Streaming for Apache Kafka, and Amazon Data Firehose.
+ **Process and transform data**: AWS Glue, Amazon EMR, Amazon Athena, and Amazon Managed Workflows for Apache Airflow.
+ **Query data**: Amazon Athena, Amazon Redshift, Amazon EMR, and Amazon OpenSearch Service.
+ **Process streaming data**: Amazon Managed Service for Apache Flink, Amazon EMR, AWS Glue, and Amazon Redshift.
+ **Store data in data lakes and data warehouses**: Amazon Simple Storage Service and Amazon Redshift.
+ **Visualize and search data**: AWS Quick Sight and Amazon OpenSearch Service.
+ **Govern and collaborate**: Amazon SageMaker Catalog, AWS Lake Formation, and AWS Clean Rooms.

------
#### [ Unified analytics and AI ]

[Amazon SageMaker Unified Studio](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/getting-started.html) provides an integrated environment for using your data and tools for analytics and AI. You can discover data and work with familiar AWS analytics and machine learning services for model development, generative AI, big data processing, and SQL analytics, assisted by Amazon Q Developer. It brings together tools that were previously in separate studios and query editors in Amazon EMR, AWS Glue, Amazon Redshift, Amazon Bedrock, and Amazon SageMaker Studio.

The [lakehouse architecture of Amazon SageMaker](https://docs.aws.amazon.com/sagemaker-lakehouse-architecture/latest/userguide/lakehouse-how.html) organizes data into catalogs. You can create new catalogs to store data in Amazon S3 or Redshift Managed Storage. You can also connect existing sources as catalogs. *Federated catalogs* connect to sources such as Amazon Redshift, Amazon DynamoDB, Amazon DocumentDB, Amazon Aurora MySQL and PostgreSQL, MySQL, PostgreSQL, SQL Server, Oracle, Snowflake, Google BigQuery, and Microsoft Azure SQL, so you can query them in place with fine-grained permissions managed through AWS Lake Formation.

------
#### [ Ingest and replicate data ]

**Zero-ETL integrations** replicate data from operational and application sources into analytics destinations, so you don't have to build and maintain pipelines.
+ **[Amazon Redshift zero-ETL integrations](https://docs.aws.amazon.com/redshift/latest/mgmt/zero-etl-using.html)** replicate data into an Amazon Redshift data warehouse from Amazon Aurora MySQL, Aurora PostgreSQL, Amazon DynamoDB, Amazon RDS for MySQL, Amazon RDS for Oracle, Amazon RDS for PostgreSQL, Oracle Database@AWS, applications (including Salesforce, Salesforce Marketing Cloud Account Engagement, SAP, ServiceNow, Instagram ads, Meta ads, and Zendesk), and self-managed MySQL, PostgreSQL, SQL Server, and Oracle.
+ **[AWS Glue zero-ETL integrations](https://docs.aws.amazon.com/glue/latest/dg/zero-etl-using.html)** replicate data from Amazon DynamoDB, Oracle Database@AWS, third-party applications (Facebook Ads, Instagram Ads, Salesforce, Salesforce Marketing Cloud Account Engagement, SAP OData, ServiceNow, Zendesk, and Zoho CRM), and self-managed Oracle, SQL Server, MySQL, and PostgreSQL. Targets are general purpose Amazon S3 buckets, Amazon S3 Tables, and Redshift Managed Storage through the lakehouse architecture of SageMaker, and Amazon Redshift data warehouses. Self-managed database sources can replicate only to an Amazon Redshift data warehouse.

**AWS Glue ETL** is the choice when data must be transformed before analysis. Zero-ETL provides service-managed replication with no custom logic. AWS Glue ETL lets you write transformation logic, combine sources, apply data quality rules, and cleanse or aggregate data. Source connections can be reused between AWS Glue ETL and AWS Glue zero-ETL. For more information, see [Simplify data integration with AWS Glue and zero-ETL to Amazon SageMaker Lakehouse](https://aws.amazon.com/blogs/big-data/simplify-data-integration-with-aws-glue-and-zero-etl-to-amazon-sagemaker-lakehouse/) on the AWS Big Data Blog. AWS Glue connects to a wide range of AWS, database, and SaaS sources.

**Streaming ingestion services** capture data continuously as it's produced:
+ [Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/introduction.html) collects and processes large streams of data records in real time. Applications read records from a data stream and can send results to dashboards, alerts, or other AWS services.
+ [Amazon Managed Streaming for Apache Kafka](https://docs.aws.amazon.com/msk/latest/developerguide/what-is-msk.html) (Amazon MSK) is a fully managed service for building and running applications that use Apache Kafka. It runs open-source versions of Apache Kafka, so existing Kafka applications, tools, and plugins work without changes.
+ [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html) delivers streaming data to destinations without consumer applications that you write. Destinations include Amazon S3, Amazon Redshift, Amazon OpenSearch Service, OpenSearch Service Serverless, Apache Iceberg tables, and HTTP endpoints and third-party providers such as Coralogix, Datadog, Dynatrace, Elastic, and Grafana Cloud.
+ [Amazon Redshift streaming ingestion](https://docs.aws.amazon.com/redshift/latest/dg/materialized-view-streaming-ingestion-getting-started.html) loads streaming data directly into Amazon Redshift materialized views from Amazon Kinesis Data Streams, Amazon MSK, Apache Kafka, and Confluent Cloud, without staging it in Amazon S3.

------
#### [ Process and transform data ]
+ [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html) is a serverless data integration service for discovering, preparing, moving, and integrating data from multiple sources. Its core capability is ETL. With AWS Glue Studio, you can [visually build ETL jobs](https://docs.aws.amazon.com/glue/latest/dg/author-job-glue.html) that run on the Apache Spark–based serverless engine of AWS Glue, without writing code. AWS Glue Data Quality recommends rules, detects anomalies with machine learning, and provides more than 25 built-in rule types.
+ [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-what-is-emr.html) runs open-source frameworks such as Apache Spark, Apache Hive, Trino, and Apache Flink. You can deploy it on Amazon EC2, on Amazon EKS, on AWS Outposts, or as EMR Serverless. [Amazon EMR Serverless](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/emr-serverless.html) runs applications that use frameworks such as Spark and Hive without clusters to configure, optimize, secure, or operate.
+ [Amazon Athena for Apache Spark](https://docs.aws.amazon.com/athena/latest/ug/notebooks-spark.html) runs Spark applications interactively without planning, configuring, or managing resources, and scales automatically on demand. You can use notebooks in the Athena console or Amazon SageMaker Unified Studio, or Spark Connect–compatible clients.
+ [Amazon Managed Workflows for Apache Airflow](https://docs.aws.amazon.com/mwaa/latest/userguide/what-is-mwaa.html) (Amazon MWAA) orchestrates data pipelines and workflows with Apache Airflow. It scales Airflow workers automatically within limits you set. [Amazon MWAA Serverless](https://docs.aws.amazon.com/mwaa/latest/mwaa-serverless-userguide/what-is-mwaa-serverless.html) is a deployment option that removes environment management and charges only for workflow run time.

------
#### [ Query data ]
+ [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html) runs ad hoc SQL queries on data in Amazon S3 without loading it, in formats such as CSV, JSON, Apache Parquet, and Apache ORC. It can run read, time travel, write, and data definition language (DDL) queries on Apache Iceberg tables. **Athena Federated Query** uses data source connectors that run on Lambda to query other sources. Prebuilt connectors include Amazon CloudWatch Logs, Amazon DynamoDB, Amazon DocumentDB, Amazon OpenSearch Service, and JDBC-compliant sources such as MySQL, PostgreSQL, and Amazon Redshift. You can write custom connectors with the Athena Query Federation SDK.
+ [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/welcome.html) is a fully managed, petabyte-scale data warehouse, available as provisioned clusters or as Redshift Serverless, which scales compute automatically and charges only when the warehouse is in use. **Amazon Redshift Spectrum** queries structured and semi-structured data in Amazon S3 without loading it into Amazon Redshift tables. **Federated queries** query live data in Amazon RDS for PostgreSQL, Amazon Aurora PostgreSQL, Amazon RDS for MySQL, and Aurora MySQL, and combine it with data in Amazon Redshift and Amazon S3. **Amazon Q generative SQL** in query editor v2 helps you write SQL from natural language.
+ **Trino on Amazon EMR** runs ANSI SQL–compliant interactive queries, most commonly complex SQL on large datasets in Amazon S3. For more information, see [Trino](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-trino.html) in the Amazon EMR documentation.
+ [Amazon OpenSearch Service direct query](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/direct-query-s3-overview.html) analyzes data in Amazon S3 without first copying it into OpenSearch. It requires OpenSearch 2.13 or later and the AWS Glue Data Catalog.

------
#### [ Process streaming data ]
+ [Amazon Managed Service for Apache Flink](https://docs.aws.amazon.com/managed-flink/latest/java/what-is.html) processes and analyzes streaming data with Java, Scala, Python, or SQL for time-series analytics, real-time dashboards, and metrics.
+ **Apache Flink on Amazon EMR** runs real-time stream processing as a YARN application on transient or long-running clusters, with connectors for sources including Amazon Kinesis Data Streams and Apache Kafka. For more information, see [Apache Flink](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-flink.html) in the Amazon EMR documentation.
+ **AWS Glue streaming ETL** runs continuous jobs on Apache Spark Structured Streaming. It ingests from Amazon Kinesis Data Streams, Apache Kafka, and Amazon MSK, then cleans and transforms the data and loads it into Amazon S3 or JDBC data stores. For more information, see [AWS Glue components](https://docs.aws.amazon.com/glue/latest/dg/components-overview.html).
+ **Amazon Redshift streaming ingestion** (see *Ingest and replicate data*) makes streams queryable in the data warehouse, and you can filter and aggregate in the materialized-view definition.

------
#### [ Store data in data lakes and data warehouses ]
+ [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) (Amazon S3) is the foundation for data lakes on AWS. **Amazon S3 Tables** store tabular data in Apache Iceberg format in table buckets, which provide higher transactions per second and better query throughput than self-managed tables in general purpose buckets.
+ **Apache Iceberg** is supported by Amazon EMR, Amazon Athena, Amazon Redshift, AWS Glue, and Amazon SageMaker, so multiple engines can work with the same tables. For more information, see [Modern data lakes](https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/data-lakes.html) in *Using Apache Iceberg on AWS*.
+ **Amazon Redshift** stores structured and semi-structured data in a managed data warehouse (see *Query data*).

------
#### [ Visualize and search data ]
+ [AWS Quick Sight](https://docs.aws.amazon.com/quick/latest/userguide/what-is.html) is the interactive data visualization and business intelligence capability of AWS Quick. You can connect to data sources, build dashboards, and embed analytics in applications. Supported sources include Amazon Athena, Amazon Aurora, Amazon OpenSearch Service, Amazon Redshift, Amazon Redshift Spectrum, Amazon S3, Amazon S3 Tables, Google BigQuery, and many relational databases.
+ [Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html) supports log analytics workloads, such as monitoring application performance, troubleshooting errors, and analyzing user behavior from logs. Direct query analyzes data in Amazon S3 without copying it (see *Query data*).

------
#### [ Govern and collaborate ]
+ [Amazon SageMaker Catalog](https://docs.aws.amazon.com/datazone/latest/userguide/sagemaker-datazone.html), built on Amazon DataZone, centrally manages data assets. You can catalog, search, and discover data, generate metadata with generative AI, and enforce access policies with a single permission model in Amazon SageMaker Unified Studio. The Amazon DataZone guide explains when to use SageMaker or Amazon DataZone.
+ [AWS Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/data-filtering.html) manages fine-grained permissions on AWS Glue Data Catalog tables, including column-level, row-level, and cell-level security through data filters. AWS Glue, Amazon Athena, Amazon Redshift Spectrum, and Amazon EMR honor Lake Formation permissions.
+ [AWS Clean Rooms](https://docs.aws.amazon.com/clean-rooms/latest/userguide/what-is.html) lets companies analyze combined datasets without sharing raw data. When you run queries, AWS Clean Rooms reads data from its original location. Collaborators control queries with analysis rules and can turn on differential privacy through a custom analysis rule.

------

## Consider criteria for AWS analytics services
<a name="consider"></a>

The following criteria are the ones most likely to change which AWS analytics service you choose. For each one, consider your current workload and how you expect it to grow. Most organizations end up using several services, so you might apply these criteria separately to each part of your pipeline.

------
#### [ Where your data comes from and what form it's in ]

Your data sources narrow your options more than any other factor.
+ **Operational databases and SaaS applications.** If your data is in databases such as Amazon Aurora, Amazon RDS, or Amazon DynamoDB, or in applications such as Salesforce, SAP, ServiceNow, or Zendesk, check whether a zero-ETL integration supports your source. Amazon Redshift and AWS Glue both offer zero-ETL integrations, and their supported sources and targets differ. If no zero-ETL integration covers your source, or you need to transform data on the way in, AWS Glue provides connections to a wide range of AWS, database, and SaaS sources.
+ **Files in Amazon S3.** If your data is already in Amazon S3 in formats such as CSV, JSON, Apache Parquet, or Apache ORC, you can query it in place with [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html) without loading it. Amazon Redshift Spectrum can also query data in Amazon S3 without loading it into Amazon Redshift tables.
+ **Event streams.** If data arrives continuously, such as clickstreams, application logs, or IoT telemetry, you need a streaming ingestion service such as [Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/introduction.html) or [Amazon MSK](https://docs.aws.amazon.com/msk/latest/developerguide/what-is-msk.html). If your teams already use Apache Kafka, Amazon MSK runs open-source Kafka, so existing applications and tools work without changes.
+ **Data you can't or don't want to move.** If data must stay in its source system, use federated query. Athena Federated Query uses connectors to query relational, non-relational, object, and custom data sources. Amazon Redshift federated queries work with Amazon RDS and Aurora PostgreSQL and MySQL.
+ **Semi-structured data.** Athena queries semi-structured formats such as JSON in Amazon S3. Amazon Redshift stores and queries semi-structured data natively with the SUPER data type.

------
#### [ How quickly you need results ]

Decide whether each workload is batch, interactive, or streaming. Different services fit each one.
+ **Batch.** Scheduled jobs that process large volumes of data periodically, such as nightly ETL. AWS Glue ETL jobs and Amazon EMR are common choices, orchestrated with Amazon Managed Workflows for Apache Airflow. For jobs that aren't time-sensitive, AWS Glue offers a flexible execution class, while the standard class suits time-sensitive workloads that need fast startup.
+ **Interactive.** Analysts and dashboards that expect answers in seconds. Amazon Athena runs ad hoc SQL on Amazon S3, and Amazon Redshift serves repeated queries from many users. With concurrency scaling, Amazon Redshift supports thousands of concurrent users and queries with consistently fast performance. For interactive Spark, Athena for Apache Spark runs without resources to manage and scales on demand.
+ **Streaming.** Data processed continuously as it arrives. Options include Amazon Managed Service for Apache Flink, Apache Flink on Amazon EMR, and AWS Glue streaming ETL. To query streaming data in your data warehouse, Amazon Redshift streaming ingestion loads streams directly into materialized views, without staging data in Amazon S3.
+ **Near real-time replication.** If you need fresh copies of operational data rather than continuous stream processing, zero-ETL integrations replicate changes after an initial load.

------
#### [ How your teams prefer to work ]

The skills and tools your teams already use are often the deciding factor between services that overlap.
+ **SQL.** Analysts who work in SQL can use Amazon Athena or Amazon Redshift. Trino on Amazon EMR is also ANSI SQL–compliant. In Amazon Redshift, Amazon Q generative SQL helps write queries from natural language.
+ **Code (Python, Scala, Java).** Data engineers who write Spark code can use AWS Glue, Amazon EMR, or Athena for Apache Spark. Stream processing in Amazon Managed Service for Apache Flink supports Java, Scala, Python, and SQL.
+ **Visual tools.** AWS Glue Studio lets you build ETL jobs visually without writing Spark code. Business users can explore data in AWS Quick Sight dashboards and ask questions in natural language in AWS Quick.
+ **Mixed teams.** If data engineers, analysts, and data scientists need to work on the same data, Amazon SageMaker Unified Studio brings SQL analytics, big data processing, and model development into one environment.

------
#### [ How much infrastructure you want to manage ]

Many analytics services offer both serverless and provisioned options. Serverless options remove capacity planning. Provisioned options give you more control over configuration, performance tuning, and cost for steady workloads.

| Job | Serverless options | Options with more configuration control |
| --- | --- | --- |
| SQL on the data lake | Amazon Athena | Trino on Amazon EMR |
| Data warehouse | Amazon Redshift Serverless | Amazon Redshift provisioned clusters |
| Spark and big data processing | AWS Glue, EMR Serverless, Athena for Apache Spark | Amazon EMR on Amazon EC2, on Amazon EKS, or on AWS Outposts |
| Stream ingestion | Amazon Kinesis Data Streams on-demand mode, Amazon MSK Serverless, Amazon Data Firehose | Amazon Kinesis Data Streams provisioned mode, Amazon MSK provisioned clusters |
| Workflow orchestration | Amazon MWAA Serverless | Amazon MWAA provisioned |
| Search and log analytics | OpenSearch Service Serverless | Amazon OpenSearch Service domains |

A serverless option fits when workloads are variable or unpredictable, or when you don't have dedicated staff to operate clusters. For example, Amazon Kinesis Data Streams on-demand mode scales automatically with no capacity planning. A provisioned option fits when you need specific instance types or framework versions. Amazon EMR, for example, lets you select instance types and purchasing options.

------
#### [ Open formats and multi-engine access ]

If different teams use different engines on the same data, store it in an open table format. Apache Iceberg is supported by Amazon EMR, Amazon Athena, Amazon Redshift, AWS Glue, and Amazon SageMaker. Athena supports read, time travel, write, and DDL queries on Iceberg tables.
+ **Amazon S3 Tables** store data in Iceberg format in table buckets, which provide higher transactions per second and better query throughput than self-managed tables in general purpose buckets.
+ **The lakehouse architecture of SageMaker** organizes data from Amazon S3, Amazon Redshift, databases, and applications into catalogs, and mounts them as databases in Amazon Redshift so they can be queried together.
+ **The AWS Glue Data Catalog** stores table metadata that Athena uses to find and query data in Amazon S3.

------
#### [ Governance and access control ]

Decide where access policies are defined and how fine-grained they need to be.
+ **Central catalog and discovery.** [Amazon SageMaker Catalog](https://docs.aws.amazon.com/datazone/latest/userguide/sagemaker-datazone.html), built on Amazon DataZone, lets users catalog, search, and discover data and enforce access policies with one permission model.
+ **Fine-grained permissions on data lake tables.** [AWS Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/data-filtering.html) provides column-level, row-level, and cell-level security through data filters. AWS Glue, Amazon Athena, Amazon Redshift Spectrum, and Amazon EMR honor Lake Formation permissions. Check which engines your teams use and confirm that each one is integrated.
+ **Federated sources.** Federated catalogs in the lakehouse architecture of SageMaker apply fine-grained permissions at the catalog, database, table, and column levels, managed centrally through Lake Formation. Supported sources include Amazon Redshift, Amazon DynamoDB, Amazon DocumentDB, Aurora, MySQL, PostgreSQL, SQL Server, Oracle, Snowflake, Google BigQuery, and Microsoft Azure SQL.
+ **Sharing with other organizations.** If you need to analyze data with partners without sharing raw data, [AWS Clean Rooms](https://docs.aws.amazon.com/clean-rooms/latest/userguide/what-is.html) reads data from its original location when you run queries, without moving it out of AWS. Analysis rules enforce query and output controls, and differential privacy can be turned on through a custom analysis rule.

------
#### [ Network security ]

If your security requirements prohibit traffic over the public internet, confirm that each service supports private connectivity. For example, Amazon Athena, AWS Glue, and Amazon Redshift support interface Amazon VPC endpoints powered by AWS PrivateLink. Check the security chapter of each service's documentation for its encryption options and network controls.

------
#### [ Cost model ]

Analytics services are priced differently. Match the pricing model to your usage pattern.

| Service | How you pay | Fits best when |
| --- | --- | --- |
| Amazon Athena | Per query, based on data scanned, or through capacity reservations that provide dedicated processing capacity in Data Processing Units (DPUs). You can use both in the same account. | Ad hoc or intermittent queries |
| Amazon Redshift Serverless | Compute in Redshift Processing Units (RPUs), with no charges while the warehouse is idle. Reservations of RPUs for one year offer discounts of up to 24 percent. | Variable warehouse workloads |
| AWS Glue | Per DPU for the time a job runs, with no charge for startup or shutdown. One DPU provides 4 vCPUs and 16 GB of memory. | Scheduled or event-driven ETL |
| Amazon EMR Serverless | For the vCPU, memory, and storage your applications use. | Spark and Hive jobs without cluster management |
| Amazon EMR on Amazon EC2 | For the instances in your cluster. Task nodes, which don't store HDFS data, are well suited to Spot Instances. | Long-running or highly tuned clusters |

To reduce data lake query costs, partition data and store it in compressed, columnar formats so that queries scan less data. For current prices, see each service's pricing page.

------

## Choose AWS analytics services
<a name="choose"></a>

Many AWS analytics services share capabilities. For example, Amazon Athena, Amazon Redshift, and Amazon EMR can all run SQL on data in Amazon S3, and AWS Glue, Amazon EMR, and Athena can all run Apache Spark. The right choice depends on how your teams prefer to work (SQL, code, or visual tools), how much infrastructure you want to manage (serverless or clusters you configure), how quickly you need results (batch, interactive, or streaming), and where your data lives today.

Each entry that follows describes a common need. It names the service to start with, other services that support the same need, and when to choose them. A single architecture often uses several of these services together.

**Choosing an analytics service by need**

| Your need | Start with | Also consider | When to choose |
| --- | --- | --- | --- |
| Build analytics and AI in one environment | [Amazon SageMaker Unified Studio](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/getting-started.html) | Individual services, for teams that work within one service | Start here for one environment spanning model development, generative AI, big data processing, and SQL analytics. Use individual services when a team works within one. |
| Query data in your data lake with SQL | [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html) | [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/welcome.html), [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-what-is-emr.html) (Trino) | Athena for serverless SQL on Amazon S3, paying per query. Amazon Redshift when many users query at once or you join lake and warehouse tables. Trino on Amazon EMR for an ANSI SQL engine on clusters you configure. |
| Run a data warehouse for business intelligence (BI) and reporting | Amazon Redshift | Amazon Athena | Amazon Redshift for a managed, petabyte-scale warehouse. Athena when queries are ad hoc or infrequent and data is already in Amazon S3. |
| Transform data and build ETL pipelines | [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html) | Amazon EMR, Athena for Apache Spark, [Amazon Managed Workflows for Apache Airflow](https://docs.aws.amazon.com/mwaa/latest/userguide/what-is-mwaa.html) (orchestration) | AWS Glue for serverless visual ETL. Amazon EMR for open-source frameworks with instance control. Athena for Apache Spark for interactive notebooks. Amazon Managed Workflows for Apache Airflow to orchestrate pipelines. |
| Replicate operational and SaaS data without building pipelines | Zero-ETL integrations (AWS Glue, Amazon Redshift) | AWS Glue ETL, when you need transformations | Zero-ETL to make operational and application data available without pipelines. AWS Glue ETL when data must be transformed first. |
| Query data where it lives | Federated query (Amazon Athena, Amazon Redshift) | Lakehouse architecture of SageMaker | Federated query to analyze data in place without copying it. Lakehouse architecture of SageMaker to catalog and govern federated sources centrally. |
| Ingest streaming data | [Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/introduction.html), [Amazon MSK](https://docs.aws.amazon.com/msk/latest/developerguide/what-is-msk.html) | [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html), Amazon Redshift streaming ingestion | Amazon Kinesis Data Streams for real-time collection; Amazon MSK when you use Apache Kafka. Amazon Data Firehose to deliver streams without consumer applications; Amazon Redshift streaming ingestion for low-latency data in the warehouse. |
| Process streaming data | [Amazon Managed Service for Apache Flink](https://docs.aws.amazon.com/managed-flink/latest/java/what-is.html) | Amazon EMR (Flink), AWS Glue streaming ETL | Amazon Managed Service for Apache Flink for stream processing in Java, Scala, Python, or SQL. Flink on Amazon EMR to run alongside other cluster applications; AWS Glue streaming ETL for Apache Spark Structured Streaming. |
| Visualize data and ask questions in natural language | [AWS Quick Sight](https://docs.aws.amazon.com/quick/latest/userguide/what-is.html) | None | AWS Quick Sight for visualization and BI; ask questions in natural language in Quick. |
| Analyze logs and search data | [Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html) | None | Amazon OpenSearch Service for log analytics; direct query analyzes Amazon S3 data without copying it into OpenSearch. |
| Govern access to data | [Amazon SageMaker Catalog](https://docs.aws.amazon.com/datazone/latest/userguide/sagemaker-datazone.html) (built on Amazon DataZone) | [AWS Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/data-filtering.html) | Amazon SageMaker Catalog to catalog and enforce a single permission model. AWS Lake Formation for column-, row-, or cell-level permissions on AWS Glue Data Catalog tables. |
| Collaborate with partners without sharing raw data | [AWS Clean Rooms](https://docs.aws.amazon.com/clean-rooms/latest/userguide/what-is.html) | None | AWS Clean Rooms to analyze combined datasets without sharing raw data; enforce controls with analysis rules and optional differential privacy. |

## Use AWS analytics services
<a name="use"></a>

The following resources help you start with each service in this guide. For each service, the getting-started resource comes first, followed by resources for the capabilities discussed in the Understand and Choose sections. Services are listed alphabetically.

------
#### [ Amazon Athena ]
+ **Get started**

  Use Athena to create a table based on sample data stored in Amazon S3, query the table, and check the results.

  [Get started with Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/getting-started.html)
+ **Work with Apache Iceberg tables**

  Run read, time travel, write, and DDL queries on Iceberg tables, and create Iceberg tables for use in Athena.

  [Query Apache Iceberg tables](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg.html)

  [Create Iceberg tables](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg-creating-tables.html)
+ **Available data source connectors**

  Find the prebuilt connectors you can use with Athena Federated Query to query data outside Amazon S3.

  [View the available connectors](https://docs.aws.amazon.com/athena/latest/ug/connectors-available.html)
+ **Use Apache Spark in Amazon Athena**

  Run Spark applications interactively in Athena without planning, configuring, or managing resources.

  [Use Apache Spark in Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/notebooks-spark.html)
+ **Use the AWS Glue Data Catalog to connect to your data**

  Learn how Athena uses the AWS Glue Data Catalog to store and find table metadata.

  [Use the AWS Glue Data Catalog to connect to your data](https://docs.aws.amazon.com/athena/latest/ug/data-sources-glue.html)

------
#### [ AWS Clean Rooms ]
+ **Setting up AWS Clean Rooms**

  Set up an AWS account and service roles for AWS Clean Rooms.

  [Set up AWS Clean Rooms](https://docs.aws.amazon.com/clean-rooms/latest/userguide/setting-up.html)
+ **Creating a collaboration**

  Create a collaboration and invite other members to analyze data together.

  [Create a collaboration](https://docs.aws.amazon.com/clean-rooms/latest/userguide/create-collaboration.html)
+ **AWS Clean Rooms Differential Privacy**

  Turn on differential privacy with a custom analysis rule to protect data in query results.

  [Learn about differential privacy](https://docs.aws.amazon.com/clean-rooms/latest/userguide/differential-privacy.html)
+ **Best practices for data collaborations**

  Configure analysis rules to enforce query controls and query output controls.

  [Review the best practices](https://docs.aws.amazon.com/clean-rooms/latest/userguide/best-practices.html)

------
#### [ Amazon Data Firehose ]
+ **Tutorial: Create a Firehose stream from console**

  Use the AWS Management Console or an AWS SDK to create a Firehose stream to your chosen destination.

  [Create a Firehose stream](https://docs.aws.amazon.com/firehose/latest/dev/basic-create.html)

------
#### [ Amazon DataZone ]
+ **Getting started with Amazon DataZone**

  Set up Amazon DataZone and walk through its basic workflows.

  [Get started with Amazon DataZone](https://docs.aws.amazon.com/datazone/latest/userguide/getting-started.html)
+ **When to use SageMaker versus Amazon DataZone**

  Understand how Amazon SageMaker Catalog, built on Amazon DataZone, relates to Amazon DataZone, and which to use.

  [Compare SageMaker and Amazon DataZone](https://docs.aws.amazon.com/datazone/latest/userguide/sagemaker-datazone.html)

------
#### [ Amazon EMR ]
+ **Tutorial: Getting started with Amazon EMR**

  Set up a cluster to process and analyze data with big data frameworks.

  [Get started with Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-gs.html)
+ **Getting started with Amazon EMR Serverless**

  Deploy a sample Spark or Hive workload on EMR Serverless.

  [Get started with EMR Serverless](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/getting-started.html)
+ **Getting started with Amazon EMR on Amazon EKS**

  Deploy a Spark application on a virtual cluster.

  [Get started with Amazon EMR on Amazon EKS](https://docs.aws.amazon.com/emr/latest/EMR-on-EKS-DevelopmentGuide/getting-started.html)
+ **Open-source frameworks on Amazon EMR**

  Use Flink for stream processing, Trino for interactive SQL, and Iceberg tables on Amazon EMR.

  [Apache Flink on Amazon EMR](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-flink.html)

  [Trino on Amazon EMR](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-trino.html)

  [Iceberg on Amazon EMR](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-iceberg.html)

------
#### [ AWS Glue ]
+ **Getting started with AWS Glue**

  Set up AWS Glue, including the permissions it needs.

  [Get started with AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/setting-up.html)
+ **Starting visual ETL jobs in AWS Glue Studio**

  Create an ETL job visually in AWS Glue Studio.

  [Start a visual ETL job](https://docs.aws.amazon.com/glue/latest/dg/edit-nodes-chapter.html)
+ **Streaming ETL jobs in AWS Glue**

  Create ETL jobs that run continuously and consume data from streaming sources.

  [Create a streaming ETL job](https://docs.aws.amazon.com/glue/latest/dg/add-job-streaming.html)
+ **Zero-ETL integrations**

  Find supported zero-ETL sources and targets, and configure an integration.

  [Learn about zero-ETL integrations](https://docs.aws.amazon.com/glue/latest/dg/zero-etl-using.html)

  [Configure a target for a zero-ETL integration](https://docs.aws.amazon.com/glue/latest/dg/zero-etl-target.html)
+ **AWS Glue Data Quality**

  Get recommended data quality rules and detect anomalies in your data.

  [Learn about AWS Glue Data Quality](https://docs.aws.amazon.com/glue/latest/dg/glue-data-quality.html)
+ **Getting started with the AWS Glue Data Catalog**

  Create your first AWS Glue Data Catalog, with an Amazon S3 bucket as your data source.

  [Get started with the AWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/start-data-catalog.html)

------
#### [ Amazon Kinesis Data Streams ]
+ **Getting started tutorials for Amazon Kinesis Data Streams**

  Work through tutorials for ingesting and consuming data with Amazon Kinesis Data Streams.

  [Explore the getting-started tutorials](https://docs.aws.amazon.com/streams/latest/dev/examples.html)
+ **Choose the right mode to stream in**

  Compare on-demand and provisioned capacity modes.

  [Compare capacity modes](https://docs.aws.amazon.com/streams/latest/dev/how-do-i-size-a-stream.html)

------
#### [ AWS Lake Formation ]
+ **Getting started with Lake Formation**

  Complete the setup tasks for Lake Formation.

  [Get started with Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/getting-started-setup.html)
+ **Data filtering and cell-level security**

  Use data filters for column-level, row-level, and cell-level security.

  [Set up data filtering](https://docs.aws.amazon.com/lake-formation/latest/dg/data-filtering.html)
+ **AWS service integrations with Lake Formation**

  See which AWS analytics services honor Lake Formation permissions.

  [View the service integrations](https://docs.aws.amazon.com/lake-formation/latest/dg/service-integrations.html)

------
#### [ Amazon Managed Service for Apache Flink ]
+ **Get started with Amazon Managed Service for Apache Flink**

  Learn the fundamental concepts and create an application with the DataStream API or the Table API.

  [Get started with the DataStream API](https://docs.aws.amazon.com/managed-flink/latest/java/getting-started.html)

  [Get started with the Table API](https://docs.aws.amazon.com/managed-flink/latest/java/gs-table.html)

------
#### [ Amazon MSK ]
+ **Setting up Amazon MSK**

  Complete the tasks required before you use Amazon MSK for the first time.

  [Set up Amazon MSK](https://docs.aws.amazon.com/msk/latest/developerguide/before-you-begin.html)
+ **What is Amazon MSK Serverless?**

  Learn about the serverless cluster type for Amazon MSK.

  [Learn about Amazon MSK Serverless](https://docs.aws.amazon.com/msk/latest/developerguide/serverless.html)

------
#### [ Amazon MWAA ]
+ **Get started with Amazon MWAA**

  Set up an environment with an Amazon VPC, DAG files, and supporting files.

  [Get started with Amazon MWAA](https://docs.aws.amazon.com/mwaa/latest/userguide/get-started.html)
+ **Quick start tutorial**

  Use an AWS CloudFormation template to create the resources for an Amazon MWAA environment.

  [Follow the quick start tutorial](https://docs.aws.amazon.com/mwaa/latest/userguide/quick-start.html)

------
#### [ OpenSearch Service ]
+ **Getting started with Amazon OpenSearch Service**

  Create and work with an OpenSearch Service domain.

  [Get started with Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/gsg.html)
+ **Tutorial: Getting started with OpenSearch Service Serverless**

  Create an OpenSearch Service Serverless search collection.

  [Get started with OpenSearch Service Serverless](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-getting-started.html)
+ **Directly querying Amazon S3 data**

  Analyze data in Amazon S3 from OpenSearch Service without copying it.

  [Set up direct query](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/direct-query-s3-overview.html)

------
#### [ AWS Quick Sight ]
+ **Getting started with AWS Quick Sight**

  Create your first analysis and dashboard in Quick Sight, the data visualization and analysis component of AWS Quick.

  [Get started with AWS Quick Sight](https://docs.aws.amazon.com/quick/latest/userguide/quick-sight-getting-started.html)
+ **Supported data sources**

  Find the data sources that you can connect to Quick Sight.

  [View the supported data sources](https://docs.aws.amazon.com/quick/latest/userguide/supported-data-sources.html)

------
#### [ Amazon Redshift ]
+ **Get started with Redshift Serverless data warehouses**

  Create a Redshift Serverless data warehouse, load sample data, and run queries.

  [Get started with Redshift Serverless](https://docs.aws.amazon.com/redshift/latest/gsg/new-user-serverless.html)
+ **Create a zero-ETL integration**

  Replicate data from a supported source into Amazon Redshift.

  [Create a zero-ETL integration](https://docs.aws.amazon.com/redshift/latest/mgmt/zero-etl-setting-up.create-integration.html)
+ **Streaming ingestion to a materialized view**

  Ingest data from Amazon Kinesis Data Streams or Apache Kafka sources directly into Amazon Redshift.

  [Set up streaming ingestion](https://docs.aws.amazon.com/redshift/latest/dg/materialized-view-streaming-ingestion.html)
+ **Querying data with federated queries**

  Query live data in Amazon RDS and Aurora databases from Amazon Redshift.

  [Query data with federated queries](https://docs.aws.amazon.com/redshift/latest/dg/federated-overview.html)
+ **Conduct a proof of concept for Amazon Redshift**

  Plan and run a proof of concept for your workload.

  [Conduct a proof of concept](https://docs.aws.amazon.com/redshift/latest/dg/proof-of-concept-playbook.html)

------
#### [ Amazon S3 ]
+ **Getting started with Amazon S3**

  Create a bucket and work with the objects in it.

  [Get started with Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/GetStartedWithS3.html)
+ **Tutorial: Getting started with Amazon S3 Tables**

  Create a table bucket and integrate table buckets in your Region with AWS analytics services.

  [Get started with Amazon S3 Tables](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-getting-started.html)

------
#### [ Amazon SageMaker ]
+ **Setting up Amazon SageMaker Unified Studio**

  Configure Amazon SageMaker Unified Studio, including authentication through AWS IAM Identity Center.

  [Set up Amazon SageMaker Unified Studio](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/setting-up.html)
+ **Getting started with the lakehouse architecture of Amazon SageMaker**

  Find relevant datasets, run SQL queries, and complete other common tasks in the lakehouse.

  [Get started with the lakehouse architecture](https://docs.aws.amazon.com/sagemaker-lakehouse-architecture/latest/userguide/lakehouse-get-started.html)
+ **How the lakehouse architecture of Amazon SageMaker works**

  Understand how the lakehouse organizes data from different sources into catalogs.

  [Learn how the lakehouse architecture works](https://docs.aws.amazon.com/sagemaker-lakehouse-architecture/latest/userguide/lakehouse-how.html)

------

## Explore ways to use AWS analytics services
<a name="explore"></a>

------
#### [ Reference architectures ]
+ **Modern Data Analytics Reference Architecture on AWS**

  Follow how data is collected from enterprise sources, SaaS applications, devices, logs, and streams, then ingested, stored, processed, and analyzed with AWS analytics services.

  [View the reference architecture](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/modern-data-analytics-on-aws/modern-data-analytics-on-aws.html)
+ **Architecture Best Practices for Analytics and Big Data**

  Browse reference architectures, diagrams, and best practices for analytics in the AWS Architecture Center.

  [Browse the Architecture Center on the AWS website](https://aws.amazon.com/architecture/analytics-big-data/)

------
#### [ Architecture guidance ]
+ **Data Analytics Lens – AWS Well-Architected Framework**

  Apply customer-proven best practices for designing well-architected analytics workloads.

  [Read the Data Analytics Lens](https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/analytics-lens.html)
+ **Using Apache Iceberg on AWS**

  Learn how to work with Iceberg tables across Amazon EMR, AWS Glue, Amazon Athena, and Amazon Redshift.

  [Read the guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/introduction.html)
+ **Build Modern Data Streaming Architectures on AWS**

  Design architectures to ingest, process, and analyze high-velocity data in real time.

  [Read the whitepaper](https://docs.aws.amazon.com/whitepapers/latest/build-modern-data-streaming-analytics-architectures/build-modern-data-streaming-analytics-architectures.html)
+ **What is the lakehouse architecture of Amazon SageMaker?**

  Understand how the lakehouse unifies data across Amazon S3 data lakes and Amazon Redshift data warehouses.

  [Learn about the lakehouse architecture](https://docs.aws.amazon.com/sagemaker-lakehouse-architecture/latest/userguide/what-is-smlh.html)

------
#### [ Solutions and guidance ]
+ **Guidance for Data Lakes on AWS**

  Deploy an automatically configured, event-driven, serverless data lake that ingests, stores, processes, and analyzes data with data governance.

  [Explore the guidance](https://docs.aws.amazon.com/solutions/data-lakes-on-aws/)
+ **Guidance for Scalable Analytics Using Apache Druid on AWS**

  Deploy Apache Druid on AWS for scalable, highly available, real-time analytics on large data volumes.

  [Explore the guidance](https://docs.aws.amazon.com/solutions/scalable-analytics-using-apache-druid-on-aws/)
+ **Solutions for Analytics**

  Browse curated solutions for analytics use cases in the AWS Solutions Library.

  [Browse the Solutions Library on the AWS website](https://aws.amazon.com/solutions/analytics/)

------
#### [ Blogs ]
+ **AWS Big Data Blog**

  Read posts on specific analytics use cases, new features, and architecture patterns.

  [Read the AWS Big Data Blog on the AWS website](https://aws.amazon.com/blogs/big-data/)

------
