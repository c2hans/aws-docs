---
source_url: https://docs.aws.amazon.com/whitepapers/latest/building-data-lakes/data-ingestion-methods.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Data ingestion methods
<a name="data-ingestion-methods"></a>

 A core capability of a data lake architecture is the ability to quickly and easily ingest multiple types of data:
+ Real-time streaming data and bulk data assets, from on-premises storage platforms.
+ Structured data generated and processed by legacy on-premises platforms - mainframes and data warehouses.
+ Unstructured and semi-structured data – images, text files, audio and video, and graphs).

AWS provides services and capabilities to ingest different types of data into your data lake built on Amazon S3 depending on your use case. This section provides an overview of various ingestion services.

## Amazon Kinesis Data Firehose
<a name="amazon-kinesis-firehose"></a>

[Amazon Data Firehose](https://aws.amazon.com/kinesis/data-firehose/) is part of the Kinesis family of services that makes it easy to collect, process, and analyze real-time streaming data at any scale. Firehose is a fully managed service for delivering real-time streaming data directly to data lakes (Amazon S3), data stores, and analytical services for further processing. Firehose automatically scales to match the volume and throughput of streaming data, and requires no ongoing administration. Firehose can also be configured to transform streaming data before it’s stored in a data lake built on Amazon S3. Its transformation capabilities include compression, encryption, data batching, and Lambda functions. Firehose integrates with [Amazon Kinesis Data Streams](https://aws.amazon.com/kinesis/data-streams/) and [Amazon Managed Streaming for Apache Kafka](https://aws.amazon.com/msk/) to deliver the streaming data into destinations, such as Amazon S3, [Amazon Redshift](https://aws.amazon.com/redshift/), [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/the-elk-stack/what-is-opensearch/), and third-party solutions such as [Splunk](https://www.splunk.com/).

Firehose can convert your input JSON data to Apache Parquet and Apache ORC before storing the data into your data lake built on Amazon S3. Parquet and Orc being columnar data formats, help save space and allow faster queries on the stored data compared to row-based formats such as JSON. Firehose can compress data before it’s stored in Amazon S3. It currently supports GZIP, ZIP, and SNAPPY compression formats. GZIP is the preferred format because it can be used by Amazon Athena, [Amazon EMR](https://aws.amazon.com/emr/), and Amazon Redshift.

Firehose also allows you to invoke Lambda functions to perform transformations on the input data. Using Lambda blueprints, you can transform the input comma-separated values (CSV), structured text, such as Apache Log and Syslog formats, into JSON first. You can optionally store the source data to another S3 bucket. The following figure illustrates the data flow between Firehose and different destinations.

Firehose also provides the ability to group and partition the target files using custom prefixes such as dates for S3 objects. This facilitates faster querying by the use of the partitioning and incremental processing further with the same feature.

![Delivering real-time streaming data with Kinesis Data Firehose to different destinations with optional backup](http://docs.aws.amazon.com/whitepapers/latest/building-data-lakes/images/storage-best-practices2.png)

Firehose also natively integrates with Amazon Managed Service for Apache Flink which provides you with an efficient way to analyze and transform streaming data using Apache Flink and SQL applications. Apache Flink is an open-source framework and engine for processing streaming data using Java and Scala. Using Managed Service for Apache Flink, you can develop applications to perform time series analytics, feed real-time dashboards, and create real-time metrics. You can also use Managed Service for Apache Flink for transforming the incoming stream and create a new data stream that can be written back into Firehose before it is delivered to a destination.

Finally, Firehose encryption supports Amazon S3 server-side encryption with [AWS Key Management Service](https://aws.amazon.com/kms/) (AWS KMS) for encrypting delivered data in your data lake built on Amazon S3. You can choose not to encrypt the data or to encrypt the data with a key from the list of AWS KMS keys that you own (refer to the [**Data encryption with Amazon S3 and AWS KMS**](securing-protecting-managing-data.md#data-encryption-with-amazon-s3-and-aws-kms) section of this document). Firehose can concatenate multiple incoming records, and then deliver them to Amazon S3 as a single S3 object.

This is an important capability because it reduces the load of Amazon S3 transaction costs and transactions per second. You can grant your application access to send data to Firehose using AWS Identity and Access Management (IAM). Using IAM, you can also grant Firehose access to S3 buckets, Amazon Redshift cluster, or Amazon OpenSearch Service cluster. You can also use Kinesis Data Firehose with virtual private cloud (VPC) endpoints (AWS PrivateLink). AWS PrivateLink is an AWS technology that enables private communication between AWS services using an elastic network interface with private IPs in your Amazon VPC.

## AWS Snow Family
<a name="aws-snowball"></a>

[AWS Snow Family](https://aws.amazon.com/snow/), comprised of AWS Snowball Edge, AWS Snowball Edge, and AWS Snowmobile, offers hardware devices of varying capacities for movement of data from on-premises locations to AWS. The devices also offer cloud computing capabilities at the edge for the applications that need to perform computations closer to the source of the data. Using Snowball Edge you can transfer data generated continuously from sensors, IoT devices, and machines, to the AWS Cloud. Snowball Edge features 8 TB of storage. Snowball Edge and Snowmobile are used to transfer massive amounts of data up to 100 PB.

Snowball moves terabytes of data into your data lake built on Amazon S3. You can use it to transfer databases, backups, archives, healthcare records, analytics datasets, historic logs, IoT sensor data, and media content, especially in situations where network conditions hinder transfer of large amounts of data both into and out of AWS.

AWS Snow Family uses physical storage devices to transfer large amounts of data between your on-premises data centers and your data lake built on Amazon S3. You can use [AWS Storage Optimized Snowball Edge](https://aws.amazon.com/snowball/features/) to securely and efficiently migrate bulk data from on-premises storage platforms and Hadoop clusters. Snowball Edge supports encryption and uses AES-256-bit encryption. Encryption keys are never shipped with the Snowball device, so the data transfer process is highly secure.

Data is transferred from the Snowball Edge device to your data lake built on Amazon S3 and stored as S3 objects in their original or native format. Snowball Edge also has a Hadoop Distributed File System (HDFS) client, so data may be migrated directly from Hadoop clusters into an S3 bucket in its native format. Snowball Edge devices can be particularly useful for migrating terabytes of data from data centers and locations with intermittent internet access.

## AWS Glue
<a name="aws-storage-gateway"></a>

[AWS Glue](https://aws.amazon.com/glue/) is a fully managed serverless ETL service that makes it easier to categorize, clean, transform, and reliably transfer data between different data stores in a simple and cost-effective way. The core components of AWS Glue consists of a central metadata repository known as [AWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/components-overview.html) which is a drop-in replacement for an Apache Hive metastore (refer to the [**Catalog and search**](data-cataloging.md) section of this document for more information) and an ETL job system that automatically generates Python and Scala code and manages ETL jobs. The following figure depicts the high-level architecture of an AWS Glue environment.

![Architecture of an AWS Glue environment](http://docs.aws.amazon.com/whitepapers/latest/building-data-lakes/images/storage-best-practices3.png)

To ETL the data from source to target, you create a job in AWS Glue, which involves the following steps:

1. Before you can run an ETL job, define a crawler and point it to the data source to identify the table definition and the metadata required to run the ETL job. The metadata and the table definitions are stored in the Data Catalog. The data source can be an AWS service, such as Amazon RDS, Amazon S3, Amazon DynamoDB, or Kinesis Data Streams, as well as a third-party JDBC-accessible database. Similarly, a data target can be an AWS service, such as Amazon S3, Amazon RDS, and Amazon DocumentDB (with MongoDB compatibility), as well as a third-party JDBC-accessible database.

1. Either provide a script to perform the ETL job, or AWS Glue can generate the script automatically.

1. Run the job on-demand or use the scheduler component that helps in initiating the job in response to an event and schedule at a defined time.

1. When the job is run, the script extracts the data from the source, transforms the data, and finally loads the data into the data target.

## AWS DataSync
<a name="aws-datasync"></a>

[AWS DataSync](https://aws.amazon.com/datasync/) is an online data transfer service that helps in moving data between on-premises storage systems and AWS storage services, as well as between different AWS storage services. You can automate the data movement between on-premises Network File Systems (NFS), Server Message Block (SMB), or a self-managed object store to your data lake built on Amazon S3. DataSync allows data encryption and data integrity validation to ensure safe and secure transfer of data. DataSync also has support for an HDFS connector to read directly from on-premises Hadoop clusters and replicate your data to your data lake built on Amazon S3.

## AWS Transfer Family
<a name="aws-transfer-family"></a>

[AWS Transfer Family](https://aws.amazon.com/aws-transfer-family/) is a fully managed and secure transfer service that helps you to move files into and out of AWS storage services (for example, your data lake built on Amazon S3 storage and [Amazon Elastic File System](https://aws.amazon.com/efs/) (Amazon EFS) Network File System (NFS)). AWS Transfer Family supports Secure Shell (SSH) File Transfer Protocol (FTP), FTP Secure (FTPS), and FTP. You can use AWS Transfer Family to ingest data into your data lakes built on Amazon S3 from third parties, such as vendors and partners, to perform an internal transfer within the organization, and distribute subscription-based data to customers.

## Storage Gateway
<a name="aws-storage-gateway2"></a>

[Storage Gateway](https://aws.amazon.com/storagegateway/) can be used to integrate legacy on-premises data processing platforms with a data lake built on Amazon S3. The File Gateway configuration of Storage Gateway offers on-premises devices and applications a network file share through an NFS connection. Files written to this mount point are converted to objects stored in Amazon S3 in their original format without any proprietary modification. This means that you can integrate applications and platforms that don’t have native Amazon S3 capabilities—such as on-premises lab equipment, mainframe computers, databases, and data warehouses—with S3 buckets, and then use analytical tools such as Amazon EMR or Amazon Athena to process this data.

## Apache Hadoop distributed copy command
<a name="apache-hadoop-distributed-copy-command"></a>

Amazon S3 natively supports distributed copy (DistCp), which is a standard Apache Hadoop data transfer mechanism. This allows you to run DistCp jobs to transfer data from an on-premises Hadoop cluster to an S3 bucket. The command to transfer data is similar to the following:

`hadoop distcp hdfs://source-folder s3a://destination-bucket`

## Direct Connect
<a name="aws-direct-connect2"></a>

[Direct Connect](https://aws.amazon.com/directconnect/) establishes a dedicated network connection between your on-premises internal network and AWS. Direct Connect links the internal network to an Direct Connect location over a standard Ethernet fiber optic cable. Using the dedicated connection, you can create virtual interface directly with Amazon S3, which can be used to securely transfer data from on-premises into a data lake built on Amazon S3 for analysis.

## AWS Database Migration Service
<a name="aws-database-migration-service"></a>

[AWS Database Migration Service](https://aws.amazon.com/dms/) (AWS DMS) facilitates the movement of data from various data stores such as relational databases, NoSQL databases, data warehouses, and other data stores into AWS. AWS DMS allows one-time migration and ongoing replication (change data capture) to keep the source and target data stores in sync. Using AWS DMS, you can use Amazon S3 as a target for the supported database sources. AWS DMS task for Amazon S3 writes both full load migration and change data capture (CDC) in a comma separated value (CSV) format by default.

You can also write the data into Apache Parquet format (parquet) for more compact storage and faster query options. Both CSV and parquet formats are favorable for in-place querying using services such as Amazon Athena and Amazon Redshift Spectrum (refer to the [**In-place querying**](in-place-querying.md) section of this document for more information). As mentioned earlier, Parquet format is recommended for analytical querying. It is useful to use AWS DMS to migrate databases from on-premises to or across different AWS accounts to your data lake built on Amazon S3 during initial data transfer or on a regular basis.
