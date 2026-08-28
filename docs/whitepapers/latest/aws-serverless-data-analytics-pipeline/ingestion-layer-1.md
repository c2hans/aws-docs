---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-serverless-data-analytics-pipeline/ingestion-layer-1.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Ingestion layer
<a name="ingestion-layer-1"></a>

 The ingestion layer in the presented serverless architecture is composed of a set of purpose-built AWS services to enable data ingestion from a variety of sources. Each of these services enables simple self-service data ingestion into the data lake landing zone and provides integration with other AWS services in the storage and security layers. Individual purpose-built AWS services match the unique connectivity, data format, data structure, and data velocity requirements of operational database sources, streaming data sources, and file sources.

## Operational database sources
<a name="operational-database-sources"></a>

 Typically, organizations store their operational data in various relational and NoSQL databases. [AWS Data Migration Service](https://aws.amazon.com/dms/) (AWS DMS) can connect to a variety of operational RDBMS and NoSQL databases and ingest their data into [Amazon Simple](https://aws.amazon.com/s3) [Storage Service](https://aws.amazon.com/s3) (Amazon S3) buckets in the data lake landing zone. With AWS DMS, you can first perform a one-time import of the source data into the data lake and replicate ongoing changes happening in the source database. AWS DMS encrypts S3 objects using [AWS Key Management Service](https://aws.amazon.com/kms) (AWS KMS) keys as it stores them in the data lake. AWS DMS is a fully managed, resilient service and provides a wide choice of instance sizes to host database replication tasks.

 [AWS Lake Formation](https://aws.amazon.com/lake-formation/) provides a scalable, serverless alternative, called blueprints, to ingest data from AWS native or on-premises database sources into the landing zone in the data lake. A Lake Formation blueprint is a predefined template that generates a data ingestion [AWS Glue workflow](https://aws.amazon.com/glue) based on input parameters such as source database, target Amazon S3 location, target dataset format, target dataset partitioning columns, and schedule. A blueprint-generated AWS Glue workflow implements an optimized and parallelized data ingestion pipeline consisting of crawlers, multiple parallel jobs, and triggers connecting them based on conditions. For more information, see [Integrating AWS Lake Formation with Amazon RDS for SQL Server](https://aws.amazon.com/blogs/big-data/integrating-aws-lake-formation-with-amazon-rds-for-sql-server/).

## Streaming data sources
<a name="streaming-data-sources"></a>

 The ingestion layer uses Amazon Data Firehose to receive streaming data from internal and external sources. With a few clicks, you can configure a Firehose API endpoint where sources can send streaming data. This streaming data can be clickstreams, application and infrastructure logs and monitoring metrics, and IoT data such as devices telemetry and sensor readings. Firehose does the following:
+  Buffers incoming streams
+  Batches, compresses, transforms, and encrypts the streams
+  Stores the streams as S3 objects in the landing zone in the data lake

 Firehose natively integrates with the security and storage layers and can deliver data to Amazon S3, [Amazon Redshift](https://aws.amazon.com/redshift/), and [Amazon OpenSearch Service](https://aws.amazon.com/elasticsearch-service/) (OpenSearch Service) for real-time analytics use cases. Firehose is serverless, requires no administration, and has a cost model where you pay only for the volume of data you transmit and process through the service. Firehose automatically scales to adjust to the volume and throughput of incoming data.

## File sources
<a name="file-sources"></a>

 Many applications store structured and unstructured data in files that are hosted on Network Attached Storage (NAS) arrays. Organizations also receive data files from partners and third-party vendors. Analyzing data from these file sources can provide valuable business insights.

## Internal file shares
<a name="internal-file-shares"></a>

 [AWS DataSync](https://aws.amazon.com/datasync) can ingest hundreds of terabytes and millions of files from NFS and SMB enabled NAS devices into the data lake landing zone. DataSync automatically handles scripting of copy jobs, scheduling and monitoring transfers, validating data integrity, and optimizing network utilization. DataSync can perform one-time file transfers and monitor and sync changed files into the data lake. DataSync is fully managed and can be set up in minutes.

### Partner data files
<a name="partner-data-files"></a>

 FTP is most common method for exchanging data files with partners. The [AWS Transfer Family](https://aws.amazon.com/aws-transfer-family/) is a serverless, highly available, and scalable service that supports secure FTP endpoints and natively integrates with Amazon S3. Partners and vendors transmit files using SFTP protocol, and the AWS Transfer Family stores them as S3 objects in the landing zone in the data lake. The AWS Transfer Family supports encryption using AWS KMS and common authentication methods including [*AWS Identity and Access Management*](https://aws.amazon.com/iam) (IAM) and Active Directory.

## Data APIs
<a name="data-apis"></a>

 Organizations today use SaaS and partner applications such as Salesforce, Marketo, and Google Analytics to support their business operations. Analyzing SaaS and partner data in combination with internal operational application data is critical to gaining 360- degree business insights. Partner and SaaS applications often provide API endpoints to share data.

### SaaS APIs
<a name="saas-apis"></a>

 The ingestion layer uses [Amazon AppFlow](https://aws.amazon.com/appflow/) to easily ingest SaaS applications data into the data lake. With a few clicks, you can set up serverless data ingestion flows in Amazon AppFlow. Your flows can connect to SaaS applications (such as Salesforce, Marketo, and Google Analytics), ingest data, and store it in the data lake. You can schedule Amazon AppFlow data ingestion flows or trigger them by events in the SaaS application. Ingested data can be validated, filtered, mapped, and masked before storing in the data lake. Amazon AppFlow natively integrates with authentication, authorization, and encryption services in the security and governance layer.

### Partner APIs
<a name="partner-apis"></a>

 To ingest data from partner and third-party APIs, organizations build or purchase custom applications that connect to APIs, fetch data, and create S3 objects in the landing zone by using [AWS SDKs](https://aws.amazon.com/tools/). These applications and their dependencies can be packaged into Docker containers and hosted on [AWS Fargate](https://aws.amazon.com/fargate/). Fargate is a serverless compute engine for hosting Docker containers without having to provision, manage, and scale servers. Fargate natively integrates with AWS security and monitoring services to provide encryption, authorization, network isolation, logging, and monitoring to the application containers.

 AWS Glue Python shell jobs also provide serverless alternative to build and schedule data ingestion jobs that can interact with partner APIs by using native, open-source, or partner-provided Python libraries. AWS Glue provides out-of-the-box capabilities to schedule singular Python shell jobs or include them as part of a more complex data ingestion workflow built on AWS Glue workflows.

### Third-party data sources
<a name="third-party-data-sources"></a>

 Your organization can gain a business edge by combining your internal data with third- party datasets such as historical demographics, weather data, and consumer behavior data. [AWS Data Exchange](https://aws.amazon.com/data-exchange/) provides a serverless way to find, subscribe to, and ingest third-party data directly into Amazon S3 buckets in the data lake landing zone. You can ingest a full third-party dataset and then automate detecting and ingesting revisions to that dataset. AWS Data Exchange is serverless and lets you find and ingest third-party datasets with a few clicks.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
