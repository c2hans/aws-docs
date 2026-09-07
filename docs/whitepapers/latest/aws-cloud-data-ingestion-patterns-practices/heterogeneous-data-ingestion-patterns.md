---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-cloud-data-ingestion-patterns-practices/heterogeneous-data-ingestion-patterns.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Heterogeneous data ingestion patterns
<a name="heterogeneous-data-ingestion-patterns"></a>

## Heterogeneous data files ingestion
<a name="heterogeneous-data-files-ingestion"></a>

 This section covers use cases where you are looking to ingest the data and change the original file format and/or load it into a purpose-built data storage destination and/or perform transformations while ingesting data. The use case for this pattern usually falls under outside-in or inside-out data movement in the Modern Data architecture. Common use cases for inside-out data movement include loading the data warehouse storage (for example, Amazon Redshift) or data indexing solutions (for example, Amazon OpenSearch Service) from data lake storage.

 Common use cases for outside-in data movement are ingesting CSV files from on-premises to an optimized parquet format for querying or to merge the data lake with changes from the new files. These may require complex transformations along the way, which may involve processes like changing data types, performing lookups, cleaning, and standardizing data, and so on before they are finally ingested into the destination system. Consider the following tools for these use cases.

### Data extract, transform, and load (ETL)
<a name="data-extract-transform-and-load-etl"></a>

 [AWS Glue](https://aws.amazon.com/glue/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc) is a serverless data integration service that makes it easy to discover, prepare, and combine data for analytics, machine learning, and application development. It provides various mechanisms to perform extract, transform, and load (ETL) functionality. AWS Glue provides both visual and code-based interfaces to make data integration easier. Data engineers and ETL developers can visually create, run, and monitor ETL workflows with a few clicks in AWS Glue Studio.

 You can build event-driven pipelines for ETL with AWS Glue ETL. Refer to the following example.

![A diagram depicting AWS Glue ETL architecture.](https://docs.aws.amazon.com/whitepapers/latest/aws-cloud-data-ingestion-patterns-practices/images/aws-glue-etl.jpeg)

 You can use AWS Glue as a managed ETL tool to connect to your data centers for ingesting data from files while transforming data and then load the data into your data storage of choice in AWS (or example, Amazon S3 data lake storage or Amazon Redshift). For details on how to set up AWS Glue in a hybrid environment when you are ingesting data from on-premises data centers, refer to [How to access and analyze on-premises data stores using AWS Glue](https://aws.amazon.com/blogs/big-data/how-to-access-and-analyze-on-premises-data-stores-using-aws-glue/).

 AWS Glue supports various format options for files both as input and as output. These formats include avro, csv, ion, orc, and more. For a complete list of supported formats, refer to [Format Options for ETL Inputs and Outputs in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-format.html).

 AWS Glue provide various connectors to connect to the different source and destination targets. For a reference of all connectors and their usage as source or sink, refer to Connection Types and Options for ETL in AWS Glue.

 AWS Glue supports Python and Scala for programming your ETL. As part of the transformation, AWS Glue provides various transform classes for programming with both [PySpark](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-transforms.html) and [Scala](https://docs.aws.amazon.com/glue/latest/dg/glue-etl-scala-apis.html).

 You can use AWS Glue to meet the most complex data ingestion needs for your Modern Data architecture. Most of these ingestion workloads must be automated in enterprises and can follow a complex workflow. You can use [Workflows](https://docs.aws.amazon.com/glue/latest/dg/workflows_overview.html) in AWS Glue to achieve orchestration of AWS Glue workloads. For more complex workflow orchestration and automation, use [AWS Data Pipeline](https://aws.amazon.com/datapipeline/?nc2=h_ql_prod_an_dp).

### Using native tools to ingest data into data management systems
<a name="using-native-tools-to-ingest-data-into-data-management-systems"></a>

 AWS services may also provide native tools/APIs to ingest data from files into respective data management systems. For example, Amazon Redshift provides the COPY command which uses the Amazon Redshift massively parallel processing (MPP) architecture to read and load data in parallel from files in Amazon S3, from an Amazon DynamoDB table, or from text output from one or more remote hosts. For a reference to the Amazon Redshift COPY command, refer to [Using a COPY command to load data](https://docs.aws.amazon.com/redshift/latest/dg/t_Loading_tables_with_the_COPY_command.html). Note that the files need to follow certain formatting to be loaded successfully. For details, refer to Preparing your input data. You can use AWS Glue ETL to perform the required transformation to bring the input file in the right format.

 Amazon Keyspaces (for Apache Cassandra) is a scalable, highly available, managed Cassandra-compatible database service that provides a cqlsh copy command to load data into an Amazon Keyspaces table. For more details, including best practices and performance tuning, refer to Loading data into Amazon Keyspaces with cqlsh.

### Using third-party vendor tools
<a name="using-third-party-vendor-tools"></a>

 Many customers may already be using third-party vendor tools for ETL jobs in their data centers. Depending upon the access, scalability, skills, and licensing needs, customers can choose to use these tools to ingest files into the Modern Data architecture for various data movement patterns. Some third-party tools include MS SQL Server Integration Services (SSIS), IBM DataStage, and more. This whitepaper does not cover those options here. However, it is important to consider aspects like native connectors provided by these tools (for example, having connectors for Amazon S3, or Amazon Athena) as opposed to getting a connector from another third-party. Further considerations include security scalability, manageability, and maintenance of those options to meet your enterprise data ingestion needs.

## Streaming data ingestion
<a name="streaming-data-ingestion"></a>

 One of the core capabilities of a Modern Data architecture is the ability to ingest streaming data quickly and easily. Streaming data is data that is generated continuously by thousands of data sources, which typically send in the data records simultaneously, and in small sizes (order of Kilobytes). Streaming data includes a wide variety of data such as log files generated by customers using your mobile or web applications, ecommerce purchases, in-game player activity, information from social networks, financial trading floors, or geospatial services, and telemetry from connected devices or instrumentation in data centers.

 This data must be processed sequentially and incrementally on a record-by-record basis or over sliding time windows, and used for a wide variety of analytics including correlations, aggregations, filtering, and sampling. When ingesting streaming data, the use case may require to first load the data into your data lake before processing it, or it may need to be analyzed as it is streamed and stored in the destination data lake or purpose-built storage.

 Information derived from such analysis gives companies visibility into many aspects of their business and customer activity—such as service usage (for metering/billing), server activity, website clicks, and geo-location of devices, people, and physical goods—and enables them to respond promptly to emerging situations. For example, businesses can track changes in public sentiment on their brands and products by continuously analyzing social media streams and respond in a timely fashion as the necessity arises.

 AWS provides several options to work with streaming data. You can take advantage of the managed streaming data services offered by [Amazon Kinesis](https://aws.amazon.com/kinesis/) or deploy and manage your own streaming data solution in the cloud on [Amazon EC2](https://aws.amazon.com/ec2).

 AWS offers streaming and analytics managed services such as Amazon Kinesis Data [Firehose](https://aws.amazon.com/kinesis/data-firehose), [Amazon Kinesis Data Streams](https://aws.amazon.com/kinesis/data-streams/), [Amazon Managed Service for Apache Flink](https://aws.amazon.com/kinesis/data-analytics/), and [Amazon Managed Streaming for Apache Kafka](https://aws.amazon.com/msk/) (Amazon MSK).

 In addition, you can run other streaming data platforms, such as Apache Flume, Apache Spark Streaming, and Apache Storm, on Amazon EC2 and [Amazon EMR](https://aws.amazon.com/emr/).

### Amazon Data Firehose
<a name="amazon-kinesis-data-firehose"></a>

 Amazon Data Firehose is the easiest way to load streaming data into AWS. You can use [Firehose](https://aws.amazon.com/kinesis/data-firehose/) to quickly ingest real-time clickstream data and move the data into a central repository, such as Amazon S3, which can act as a data lake. Not only this, as you ingest data, you have the ability to transform the data as well as integrate with other AWS services and third-party services for use cases such as log analytics, IoT analytics, security monitoring, and more.

 Amazon Data Firehose is a fully managed service for delivering real-time streaming data directly to Amazon S3. Firehose automatically scales to match the volume and throughput of streaming data, and requires no ongoing administration. Firehose can also be configured to transform streaming data before it’s stored in Amazon S3. Its transformation capabilities include compression, encryption, data batching, and AWS Lambda functions.

 Firehose can compress data before it’s stored in Amazon S3. It currently supports GZIP, ZIP, and SNAPPY compression formats. GZIP is the preferred format because it can be used by Amazon Athena, Amazon EMR, and Amazon Redshift.

 Firehose encryption supports Amazon S3 server-side encryption with [AWS KMS](https://aws.amazon.com/kms/) for encrypting delivered data in Amazon S3. You can choose not to encrypt the data or to encrypt with a key from the list of AWS KMS keys that you own (refer to [Data Encryption with Amazon S3 and AWS KMS](https://docs.aws.amazon.com/whitepapers/latest/building-data-lakes/securing-protecting-managing-data.html#data-encryption-with-amazon-s3-and-aws-kms)). Firehose can concatenate multiple incoming records, and then deliver them to Amazon S3 as a single S3 object. This is an important capability because it reduces Amazon S3 transaction costs and transactions per second load.

 Finally, Firehose can invoke AWS Lambda functions to transform incoming source data and deliver it to Amazon S3. Common transformation functions include transforming Apache Log and Syslog formats to standardized JSON and/or CSV formats. The JSON and CSV formats can then be directly queried using Amazon Athena. If using a Lambda data transformation, you can optionally back up raw source data to another S3 bucket, as shown in the following figure.

![A diagram that depicts delivering real-time streaming data with Amazon Kinesis Data Firehose to Amazon S2 with optional backup.](https://docs.aws.amazon.com/whitepapers/latest/aws-cloud-data-ingestion-patterns-practices/images/firehose-to-s3.png)

### Sending data to an Amazon Data Firehose Delivery Stream
<a name="sending-data-to-an-amazon-kinesis-data-firehose-delivery-stream"></a>

 There are several options to send data to your delivery stream. AWS offers SDKs for many popular programming languages, each of which provides APIs for Firehose. AWS has also created a utility to help send data to your delivery stream.

#### Using the API
<a name="using-the-api"></a>

 The Firehose API offers two operations for sending data to your delivery stream: PutRecord sends one data record within one call, PutRecordBatch can send multiple data records within one call.

 In each method, you must specify the name of the delivery stream and the data record, or array of data records, when using the method. Each data record consists of a data BLOB that can be up to 1,000 KB in size and any kind of data.

 For detailed information and sample code for the Firehose API operations, refer to [Writing to a Firehose Delivery Stream Using the AWS SDK](https://docs.aws.amazon.com/firehose/latest/dev/writing-with-sdk.html).

#### Using the Amazon Kinesis Agent
<a name="using-the-amazon-kinesis-agent"></a>

 The Amazon Kinesis Agent is a stand-alone Java software application that offers an easy way to collect and send data to Kinesis Data Streams and Firehose. The agent continuously monitors a set of files and sends new data to your stream. The agent handles file rotation, checkpointing, and retry upon failures. It delivers all of your data in a reliable, timely, and simple manner. It also emits Amazon CloudWatch metrics to help you better monitor and troubleshoot the streaming process.

 You can install the agent on Linux-based server environments such as web servers, log servers, and database servers. After installing the agent, configure it by specifying the files to monitor and the destination stream for the data. After the agent is configured, it durably collects data from the files and reliably sends it to the delivery stream.

 The agent can monitor multiple file directories and write to multiple streams. It can also be configured to pre-process data records before they’re sent to your stream or delivery stream.

 If you’re considering a migration from a traditional batch file system to streaming data, it’s possible that your applications are already logging events to files on the file systems of your application servers. Or, if your application uses a popular logging library (such as Log4j), it is typically a straight-forward task to configure it to write to local files.

 Regardless of how the data is written to a log file, you should consider using the agent in this scenario. It provides a simple solution that requires little or no change to your existing system. In many cases, it can be used concurrently with your existing batch solution. In this scenario, it provides a stream of data to Kinesis Data Streams, using the log files as a source of data for the stream.

 In our example scenario, we chose to use the agent to send streaming data to the delivery stream. The source is on-premises log files, so forwarding the log entries to Firehose was a simple installation and configuration of the agent. No additional code was needed to start streaming the data.

![A diagram depicting Kinesis agent to monitor multiple fie directories.](https://docs.aws.amazon.com/whitepapers/latest/aws-cloud-data-ingestion-patterns-practices/images/kinesis-agent-1.png)

### Data transformation
<a name="data-transformation"></a>

 In some scenarios, you may want to transform or enhance your streaming data before it is delivered to its destination. For example, data producers might send unstructured text in each data record, and you may need to transform it to JSON before delivering it to Amazon OpenSearch Service.

 To enable streaming data transformations, Firehose uses an [AWS Lambda](https://aws.amazon.com/lambda/) function that you create to transform your data.

#### Data transformation flow
<a name="data-transformation-flow"></a>

 When you enable Firehose data transformation, Firehose buffers incoming data up to 3 MB or the buffering size you specified for the delivery stream, whichever is smaller. Firehose then invokes the specified Lambda function with each buffered batch asynchronously. The transformed data is sent from Lambda to Firehose for buffering. Transformed data is delivered to the destination when the specified buffering size or buffering interval is reached, whichever happens first. The following figure illustrates this process for a delivery stream that delivers data to Amazon S3.

![A diagram depicting a Kinesis Agent to monitor multiple file directories and write to Kinesis Data Firehose.](https://docs.aws.amazon.com/whitepapers/latest/aws-cloud-data-ingestion-patterns-practices/images/kinesis-agent-2.png)

### Amazon Kinesis Data Streams
<a name="amazon-kinesis-data-streams"></a>

 [Amazon Kinesis Data Streams](https://aws.amazon.com/kinesis/data-streams/) enables you to build your own custom applications that process or analyze streaming data for specialized needs. It can continuously capture and store terabytes of data per hour from hundreds of thousands of sources. You can use Kinesis Data Streams to run real-time analytics on high frequency event data such as stock ticker data, sensor data, and device telemetry data to gain insights in a matter of minutes versus hours or days.

 Kinesis Data Streams provide many more controls in terms of how you want to scale the service to meet high demand use cases, such as real-time analytics, gaming data feeds, mobile data captures, log and event data collection, and so on. You can then build applications that consume the data from Amazon Kinesis Data Streams to power real-time dashboards, generate alerts, implement dynamic pricing and advertising, and more. Amazon Kinesis Data Streams supports your choice of stream processing framework including Kinesis Client Library (KCL), Apache Storm, and Apache Spark Streaming.

![A diagram depicting custom real-time pipelines using stream-processing frameworks .](https://docs.aws.amazon.com/whitepapers/latest/aws-cloud-data-ingestion-patterns-practices/images/custom-rt-pipelines.png)

#### Sending data to Amazon Kinesis Data Streams
<a name="sending-data-to-amazon-kinesis-data-streams"></a>

 There are several mechanisms to send data to your stream. AWS offers SDKs for many popular programming languages, each of which provides APIs for Kinesis Data Streams. AWS has also created several utilities to help send data to your stream.

#### Amazon Kinesis Agent
<a name="amazon-kinesis-agent"></a>

 The Amazon Kinesis Agent can be used to send data to Kinesis Data Streams. For details on installing and configuring the Kinesis agent, refer to [Writing to Firehose Using Kinesis Agent](https://docs.aws.amazon.com/firehose/latest/dev/writing-with-agents.html).

#### Amazon Kinesis Producer Library (KPL)
<a name="amazon-kinesis-producer-library-kpl"></a>

 The KPL simplifies producer application development, allowing developers to achieve high write throughput to one or more Kinesis streams. The KPL is an easy-to-use, highly configurable library that you install on your hosts that generate the data that you want to stream to Kinesis Data Streams. It acts as an intermediary between your producer application code and the Kinesis Data Streams API actions.

 The KPL performs the following primary tasks:
+  Writes to one or more Kinesis streams with an automatic and configurable retry mechanism
+  Collects records and uses PutRecords to write multiple records to multiple shards per request
+  Aggregates user records to increase payload size and improve throughput
+  Integrates seamlessly with the Amazon Kinesis Client Library (KCL) to de- aggregate batched records on the consumer
+  Submits Amazon CloudWatch metrics on your behalf to provide visibility into producer performance

 The KPL can be used in either synchronous or asynchronous use cases. We suggest using the higher performance of the asynchronous interface unless there is a specific reason to use synchronous behavior. For more information about these two use cases and example code, refer to [Writing to your Kinesis Data Stream Using the KPL](https://docs.aws.amazon.com/streams/latest/dev/kinesis-kpl-writing.html).

### Using the Amazon Kinesis Client Library (KCL)
<a name="using-the-amazon-kinesis-client-library-kcl"></a>

 You can develop a consumer application for Kinesis Data Streams using the Kinesis Client Library (KCL). Although you can use the [Kinesis Streams API](https://docs.aws.amazon.com/streams/latest/dev/developing-producers-with-sdk.html) to get data from an Amazon Kinesis stream, we recommend using the design patterns and code for consumer applications provided by the KCL.

 The KCL helps you consume and process data from a Kinesis stream. This type of application is also referred to as a consumer. The KCL takes care of many of the complex tasks associated with distributed computing, such as load balancing across multiple instances, responding to instance failures, checkpointing processed records, and reacting to resharding. The KCL enables you to focus on writing record-processing logic.

 The KCL is a Java library; support for languages other than Java is provided using a multi-language interface. At run time, a KCL application instantiates a worker with configuration information, and then uses a record processor to process the data received from a Kinesis stream. You can run a KCL application on any number of instances. Multiple instances of the same application coordinate on failures and load- balance dynamically. You can also have multiple KCL applications working on the same stream, subject to throughput limits. The KCL acts as an intermediary between your record processing logic and Kinesis Streams.

 For detailed information on how to build your own KCL application, refer to [Developing KCL 1.x Consumers](https://docs.aws.amazon.com/streams/latest/dev/developing-consumers-with-kcl.html).

### Amazon Managed Streaming for Apache Kafka (Amazon MSK)
<a name="amazon-managed-streaming-for-apache-kafka-amazon-msk"></a>

 Amazon Managed Streaming for Apache Kafka (Amazon MSK) is a fully managed service that makes it easy for you to build and run applications that use Apache Kafka to process streaming data. Apache Kafka is an open-source platform for building real- time streaming data pipelines and applications. With Amazon MSK, you can use native Apache Kafka APIs to populate data lakes, stream changes to and from databases, and power machine learning and analytics applications. Amazon MSK is tailor made for use cases that require ultra-low latency (less than 20 milliseconds) and higher throughput through a single partition. With Amazon MSK, you can offload the overhead of maintaining and operating Apache Kafka to AWS which will result in significant cost savings when compared to running a self-hosted version of Apache Kafka.

![A diagram depicting Managed Kafka for storing streaming data in an Amazon S3 data lake.](https://docs.aws.amazon.com/whitepapers/latest/aws-cloud-data-ingestion-patterns-practices/images/managed-kafka.jpeg)

### Other streaming solutions in AWS
<a name="other-streaming-solutions-in-aws"></a>

 You can install streaming data platforms of your choice on Amazon EC2 and [Amazon EMR](https://aws.amazon.com/emr), and build your own stream storage and processing layers. By building your streaming data solution on Amazon EC2 and Amazon EMR, you can avoid the friction of infrastructure provisioning, and gain access to a variety of stream storage and processing frameworks. Options for streaming the data storage layer include [Amazon](https://aws.amazon.com/msk/) [MSK](https://aws.amazon.com/msk/) and [Apache Flume](https://flume.apache.org/). Options for streaming the processing layer include [Apache](https://spark.apache.org/streaming/) [Spark Streaming](https://spark.apache.org/streaming/) and [Apache Storm](https://storm.apache.org/).

![A diagram that depicts moving data to AWS using Amazon EMR.](https://docs.aws.amazon.com/whitepapers/latest/aws-cloud-data-ingestion-patterns-practices/images/aws-using-emr.png)

## Relational data ingestion
<a name="relational-data-ingestion"></a>

 One of common scenarios for [Modern Data architecture](https://aws.amazon.com/blogs/big-data/harness-the-power-of-your-data-with-aws-analytics/) is where customers move relational data from on-premises data centers into the AWS Cloud or from within the AWS Cloud into managed relational database services offered by AWS, such as [Amazon Relational Database Service](https://aws.amazon.com/rds/) (Amazon RDS), and Amazon Redshift – a cloud data warehouse. This pattern can be used for both onboarding the data into [Modern Data Architecture on AWS](https://aws.amazon.com/big-data/datalakes-and-analytics/data-lake-house/) and/or migrating data from commercial relational database engines into [Amazon RDS](https://aws.amazon.com/rds/). Also, AWS provides managed services for loading and migrating relational data from Oracle or SQL Server databases to [Amazon RDS](https://aws.amazon.com/rds/) and [Amazon Aurora](https://aws.amazon.com/rds/aurora) – a fully managed relational database engine that’s compatible with MySQL and PostgreSQL.

 Customers migrating into Amazon RDS and Amazon Aurora managed database services gain benefits of operating and scaling a database engine without extensive administration and licensing requirements. Also, customers gain access to features such as backtracking where relational databases can be backtracked to a specific time, without restoring data from a backup, [restoring database cluster to a specified time](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PIT.html), and avoiding database licensing costs.

 Customers with data in on-premises warehouse databases gain benefits by moving the data to Amazon Redshift – a cloud data warehouse database that simplifies administration and scalability requirements.

 The data migration process across heterogeneous database engines is a two-step process:

1.  [Assessment and Schema Conversion](https://aws.amazon.com/dms/schema-conversion-tool/)

1.  [Loading of data into AWS managed database services](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_BestPractices.html)

 Once data is onboarded, you can decide whether to maintain a copy with up-to-date changes of a database in support of modern data architecture or cut-over applications to use the managed database for both application needs and Lake House architecture.

### Schema Conversion Tool
<a name="schema-conversion-tool"></a>

 AWS Schema Conversion Tool (AWS SCT) is used to facilitate heterogeneous database assessment and migration by automatically converting the source database schema and code objects to a format that’s compatible with the target database engine. The custom code that it converts includes views, stored procedures, and functions. Any code that SCT cannot convert automatically is flagged for manual conversion.

![A diagram that depicts the AWS Schema Conversion Tool.](https://docs.aws.amazon.com/whitepapers/latest/aws-cloud-data-ingestion-patterns-practices/images/schema-conversion-tool.jpeg)

### AWS Database Migration Service (AWS DMS)
<a name="aws-database-migration-service-aws-dms"></a>

 AWS Database Migration Service (AWS DMS) is used to perform initial data load from on-premises database engine into target (Amazon Aurora). After the ingestion load is completed, depending on whether you need an on-going replication, AWS DMS or other migration and [change data capture](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Task.CDC.html) (CDC) solutions can be used for propagating the changes (deltas) from a source to the target database.

 Network connectivity in a form of [Site-to-Site VPN](https://aws.amazon.com/vpn/) or AWS Direct Connect between on- premises data centers and the AWS Cloud must be established and sized accordingly to ensure secure and realizable data transfer for both initial and ongoing replications.

 When loading large databases, especially in cases when there is a low bandwidth connectivity between the on-premises data center and AWS Cloud, it’s recommended to use [AWS Snowball Edge](https://aws.amazon.com/snowball) or similar data storage devices for shipping data to AWS. Such physical devices are used for securely copying and shipping the data to AWS Cloud.

 Once devices are received by AWS, the data is securely loaded into [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3) and then ingested into an [Amazon Aurora](https://aws.amazon.com/rds/aurora) database engine. **N**etwork connectivity must be sized accordingly to that data can be initially loaded in a timely manner, and ongoing CDC does not incur latency lag.

![A diagram depicting AWS Database Migration Service.](https://docs.aws.amazon.com/whitepapers/latest/aws-cloud-data-ingestion-patterns-practices/images/database-migration-service.jpeg)

 When moving data from on-premises databases or storing data in the cloud, security and access control of the data is an important aspect that must be accounted for in any architecture. AWS services use Transport Level Security (TLS) for securing data in transit. For securing data at rest, AWS offers a large number of encryption options for encrypting data automatically using [AWS provided keys](https://aws.amazon.com/kms/), customer provided keys, and even using [Hardware Security Module](https://aws.amazon.com/cloudhsm/) (HSM). Once data is loaded in AWS and securely stored, the pattern must account for providing controlled and auditable access to the data at the right level of granularity. In AWS, a combination of [AWS Identity and Access Management](https://aws.amazon.com/iam/) (IAM) and [AWS Lake Formation](https://aws.amazon.com/lake-formation) services can be used to achieve this requirement.

### Ingestion between relational and non-relational data stores
<a name="ingestion-between-relational-and-non-relational-data-stores"></a>

 Many organizations consider migrating from commercial relational data stores to non- relational data stores to align with the application and analytics modernization strategies. These AWS customers modernize their applications with [microservices](https://aws.amazon.com/microservices/) architecture. In cases of microservices architecture, customers choose to implement separate datastores for each microservice that is highly available and can scale to meet the demand. In regard to analytics modernization strategies s, in many situations these customers move their data around the perimeter of the Modern Data architecture from one purpose-built store like a relational database to a non-relational database and from a non-relational to a relational data store to derive insights from their data.

 In addition, relational database management systems (RDBMSs) require up-front schema definition, and changing the schema later is very expensive. There are many use cases where it’s very difficult to anticipate the database schema upfront that the business will eventually need. Therefore, RDBMS backends may not be appropriate for applications that work with a variety of data. However, NoSQL databases (like document databases) have dynamic schemas for unstructured data, and you can store data in many ways. They can be column-oriented, document-oriented, graph-based, or organized as a key-value store. The following section illustrates the ingestion pattern for these use cases.

### Migrating or ingesting data from a relational data store to NoSQL data store
<a name="migrating-or-ingesting-data-from-a-relational-data-store-to-nosql-data-store"></a>

 Migrating from commercial relational databases like Microsoft SQL Server or Oracle to [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) is challenging because of their difference in schema. There are many different schema design considerations [when moving from relational databases to NoSQL databases](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SQLtoNoSQL.html).

![A diagram that depicts migrating data from a relational data store to NoSQL data store .](https://docs.aws.amazon.com/whitepapers/latest/aws-cloud-data-ingestion-patterns-practices/images/migrating-to-nosql.jpeg)

 You can use [AWS Database Migration Service](https://aws.amazon.com/dms/) (AWS DMS) to migrate your data to and from the most widely used commercial and open-source databases. It supports homogeneous and heterogeneous migrations between different database platforms.

 AWS DMS supports migration to a [DynamoDB table as a target](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.DynamoDB.html). You use object mapping to migrate your data from a source database to a target DynamoDB table.

 Object mapping enables you to determine where the source data is located in the target. You can also create a DMS task that captures the ongoing changes from the source database and apply these to DynamoDB as target. This task can be full load plus change data capture (CDC) or CDC only.

 One of the key challenges when refactoring to Amazon DynamoDB is identifying the access patterns and building the data model. There are many [best practices for designing and architecting with Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/best-practices.html). AWS provides NoSQL Workbench for Amazon DynamoDB. NoSQL Workbench is a cross-platform client-side GUI application for modern database development and operations and is available for Windows, macOS, and Linux. NoSQL Workbench is a unified visual IDE tool that provides data modeling, data visualization, and query development features to help you design, create, query, and manage DynamoDB tables.

### Migrating or ingesting data from a relational data store to a document DB (such as Amazon DocumentDB [with MongoDB compatibility])
<a name="migrating-or-ingesting-data-from-a-relational-data-store-to-a-document-db-such-as-amazon-documentdb-with-mongodb-compatibility"></a>

 [Amazon DocumentDB](https://aws.amazon.com/documentdb/) (with [MongoDB](https://aws.amazon.com/documentdb/what-is-mongodb/) compatibility) is a fast, scalable, highly available, and fully managed document database service that supports MongoDB workloads. As a document database, Amazon DocumentDB makes it easy to store, query, and index [JSON](https://aws.amazon.com/documentdb/what-is-json/) data.

 In this scenario, converting the relational structures to documents can be complex and may require building complex data pipelines for transformations. [Amazon Database Migration Services](https://aws.amazon.com/dms/) (AWS DMS) can simplify the process of the migration and replicate ongoing changes.

 [AWS DMS maps database objects to Amazon DocumentDB](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.DocumentDB.html) in the following ways:
+  A relational database, or database schema, maps to an Amazon DocumentDB database.
+  Tables within a relational database map to collections in Amazon DocumentDB.
+  Records in a relational table map to documents in Amazon DocumentDB. Each document is constructed from data in the source record.

![A diagram that depicts migrating data from a relational data store to DocumentDB.](https://docs.aws.amazon.com/whitepapers/latest/aws-cloud-data-ingestion-patterns-practices/images/migrating-to-documentdb.jpeg)

 AWS DMS reads records from the source endpoint, and constructs JSON documents based on the data it reads. For each JSON document, AWS DMS determines an \_id field to act as a unique identifier. It then writes the JSON document to an Amazon DocumentDB collection, using the \_id field as a primary key.

### Migrating or ingesting data from a document DB (such as Amazon DocumentDB [with MongoDB compatibility] to a relational database
<a name="migrating-or-ingesting-data-from-a-document-db-such-as-amazon-documentdb-with-mongodb-compatibility-to-a-relational-database"></a>

 AWS DMS supports Amazon DocumentDB (with MongoDB compatibility) as a database source. You can use AWS DMS to migrate or replicate changes from Amazon DocumentDB to relational database such as Amazon Redshift for data warehousing use cases. [Amazon Redshift](https://aws.amazon.com/redshift/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc) is a fully managed, petabyte-scale data warehouse service in the cloud. AWS DMS supports two migration modes when using DocumentDB as a source, document mode and table mode.

 In [document mode](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.DocumentDB.html), the JSON documents from DocumentDB are migrated as is. So, when you use a relational database as a target, the data is a single column named \_doc in a target table. You can optionally set the extra connection attribute extractDocID to true to create a second column named "\_id" that acts as the primary key. If you use change data capture (CDC), set this parameter to true except when using Amazon DocumentDB as the target.

 In [table mode](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.DocumentDB.html), AWS DMS transforms each top-level field in a DocumentDB document into a column in the target table. If a field is nested, AWS DMS flattens the nested values into a single column. AWS DMS then adds a key field and data types to the target table's column set.

 The change streams feature in Amazon DocumentDB (with MongoDB compatibility) provides a time-ordered sequence of change events that occur within your cluster’s collections. You can read events from a change stream using AWS DMS to implement many different use cases, including the following:
+  Change notification
+  Full-text search with [Amazon OpenSearch Service](https://aws.amazon.com/elasticsearch-service/) (OpenSearch Service)
+  Analytics with [Amazon Redshift](https://aws.amazon.com/redshift/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc)

 After change streams are enabled, you can create a migration task in AWS DMS that migrates existing data and at the same time replicates ongoing changes. AWS DMS continues to capture and apply changes even after the bulk data is loaded. Eventually, the source and target databases synchronize, minimizing downtime for a migration.

 During a database migration when Amazon Redshift is the target for data warehousing use cases, AWS DMS first moves data to an Amazon S3 bucket. When the files reside in an Amazon S3 bucket, AWS DMS then transfers them to the proper tables in the Amazon Redshift data warehouse.

![A diagram that depicts Migrating data from NoSQL store to Amazon Redshift .](https://docs.aws.amazon.com/whitepapers/latest/aws-cloud-data-ingestion-patterns-practices/images/migrating-to-redshift.jpeg)

 AWS Database Migration Service supports both full load and change processing operations. AWS DMS reads the data from the source database and creates a series of comma-separated value (`.csv`) files. For full-load operations, AWS DMS creates files for each table. AWS DMS then copies the table files for each table to a separate folder in Amazon S3. When the files are uploaded to Amazon S3, AWS DMS sends a [COPY command](https://docs.aws.amazon.com/redshift/latest/dg/r_COPY.html) and the data in the files are copied into Amazon Redshift. For change- processing operations, AWS DMS copies the net changes to the .csv files. AWS DMS then uploads the net change files to Amazon S3 and copies the data to Amazon Redshift.

### Migrating or ingesting data from a document DB (such as Amazon Document DB [with MongoDB compatibility]) to Amazon OpenSearch Service
<a name="migrating-or-ingesting-data-from-a-document-db-such-as-amazon-document-db-with-mongodb-compatibility-to-amazon-elasticsearch-service"></a>

 Taking the same approach as AWS DMS support for Amazon DocumentDB (with MongoDB) as a database source, you can migrate or replicate changes from Amazon DocumentDB to [Amazon OpenSearch Service](https://aws.amazon.com/elasticsearch-service/) as the target.

 In OpenSearch Service, you work with indexes and documents. An *index* is a collection of documents, and a *document* is a JSON object containing scalar values, arrays, and other objects. OpenSearch Service provides a JSON-based query language, so that you can query data in an index and retrieve the corresponding documents. When AWS DMS creates indexes for a target endpoint for OpenSearch Service, it creates one index for each table from the source endpoint.

 AWS DMS supports multithreaded full load to increase the speed of the transfer, and multithreaded CDC load to improve the performance of CDC. For the task settings and prerequisites that are required to be configured for these modes, refer to [Using an Amazon OpenSearch Service cluster as a target for AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Elasticsearch.html).

![A diagram that depicts migrating data from Amazon DocumentDB store to Amazon OpenSearch Service.](https://docs.aws.amazon.com/whitepapers/latest/aws-cloud-data-ingestion-patterns-practices/images/migrating-to-opensearch.png)
