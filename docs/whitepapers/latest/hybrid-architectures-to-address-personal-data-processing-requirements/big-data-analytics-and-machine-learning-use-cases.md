---
source_url: https://docs.aws.amazon.com/whitepapers/latest/hybrid-architectures-to-address-personal-data-processing-requirements/big-data-analytics-and-machine-learning-use-cases.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# 2.1 Big Data, analytics, and machine learning use cases
<a name="big-data-analytics-and-machine-learning-use-cases"></a>

 Requirements addressed:
+  **REQ1** (data residency)
+  **REQ3** (data access controls)
+  **REQ4** (availability and durability)

 AWS services – [Amazon Redshift](https://aws.amazon.com/redshift/), [AWS Glue](https://aws.amazon.com/glue/), [Amazon EMR](https://aws.amazon.com/emr/), [Amazon S3](https://aws.amazon.com/s3/), [AWS DataSync](https://aws.amazon.com/datasync/), [Amazon Athena](https://aws.amazon.com/athena/), [Amazon Kinesis](https://aws.amazon.com/kinesis/), [Amazon Managed Streaming for Apache Kafka](https://aws.amazon.com/msk/) (Amazon MSK), [AWS Database Migration Service](https://aws.amazon.com/dms/), and [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/)

![Amazon analytics and machine learning at the data lake](http://docs.aws.amazon.com/whitepapers/latest/hybrid-architectures-to-address-personal-data-processing-requirements/images/analytics-and-MA-data-lake.png)

 Amazon analytics and machine learning at the data lake

 Requirements **REQ2** (data protection) and **Customer-REQ1** (reliable connectivity) can be met through complimentary use of architecture 1.1: [Hybrid network connectivity from a data center to the AWS Cloud.](hybrid-network-connectivity-from-a-data-center-to-the-aws-cloud.md)

 Scalability and durability of services, as well as the pay-as-you-go model, make many customers choose AWS for their analytics and ML workloads. When data residency is required, hybrid architectures can be used for analytics and ML cases as well. In this example:

1.  The data source layer consists any kind of data sources, such as relational databases (Oracle, MySQL, PostgreSQL), enterprise applications (SAP, CRM), S3-compatible object storages (Ceph, MinIO, Eucaliptus), and Hadoop Distributed File System (HDFS), located on-premises.

1.  Export from relational databases is done by [AWS Database Migration Service](https://aws.amazon.com/dms/) (AWS DMS) with a full load (one-time export) or change data capture (continued date export) options, which transfers data into an Amazon S3 data lake to build a highly available and scalable data lake solution. AWS DMS can migrate data from the most widely used commercial and open-source databases.

1.  Amazon S3-compatible object storages and enterprise applications export data as files, and store it in shared folders on Network File System (NFS) or Server Message Block (SMB) file servers.

1.  AWS DataSync agents transfer data files from shared folders to AWS DataSync. DataSync optionally performs data integrity verification and puts files into the Amazon S3 data lake.

1.  Customers with local HDFS can use a DataSync agent to replicate data into the Amazon S3 data lake as described in the previous step, or use the [S3DistCp](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/UsingEMR_s3distcp.html) command to copy large amounts of data from HDFS to S3 directly. The command for S3DistCp in Amazon EMR version 4.0 and later is s3-dist-cp, which you can add as a step in a cluster, or at the command line. S3DistCp can also be run in a local Hadoop cluster. Additional information can be found in the [DistCp Guide](https://hadoop.apache.org/docs/stable/hadoop-distcp/DistCp.html).

1.  Another data flow from devices and applications, located anywhere, for near real-time data ingestion (such as streaming data) can be performed with [Amazon Data Firehose](https://aws.amazon.com/kinesis/data-firehose/) or [Amazon MSK](https://aws.amazon.com/msk/) (through various Kafka Connect connectors) and stored in the Amazon S3 data lake, or processed in near real-time with [Amazon Managed Service for Apache Flink](https://aws.amazon.com/kinesis/data-analytics/).

1.  From any location (on-premises or remote), customers can use Amazon ML services such as [Amazon SageMaker AI Studio](https://aws.amazon.com/sagemaker/studio/) to build and train ML models for any use case with fully managed cloud infrastructure, tools, and workflows. Amazon SageMaker AI lets you use data, stored in the Amazon S3 data lake, to train, tune, and validate ML models. Compiled models could be stored in Amazon S3 object storage and deployed at AWS endpoints, or downloaded and deployed locally.

1.  [AWS Glue](https://aws.amazon.com/glue/) is used to catalog the data and store it in Apache Hive metastore compatible format.

1.  Query data with [Amazon Athena](https://aws.amazon.com/athena/), [Amazon EMR Spark jobs](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/jobs-spark.html), and/or [Amazon Redshift Spectrum](https://docs.aws.amazon.com/redshift/latest/dg/c-using-spectrum.html), which lets you analyze data in Amazon S3 using standard SQL.

 Data residency requirement allows to collect, store, and process data at on-premises data center first, then copy, export, or back up data to the AWS Cloud (**REQ1**).

 The Amazon S3 data lake provides a permissions model, to control access to stored data *and* metadata, that describes that data. This approach addresses the *data access controls* requirement (**REQ3**).

 Using an Amazon S3 data lake to build a highly available and scalable data lake solution addresses the *data availability and durability* requirement (**REQ4**).

 For more information about data lakes and analytics on AWS, refer to [Analytics on AWS](https://aws.amazon.com/big-data/datalakes-and-analytics/?nc=sn&loc=1). For information on different approaches to move data into a data lake in AWS, refer to [Data Lakes on AWS](https://aws.amazon.com/products/storage/data-lake-storage/). For information on hybrid ML scenarios, refer to [Hybrid Machine Learning](https://docs.aws.amazon.com/whitepapers/latest/hybrid-machine-learning/hybrid-machine-learning.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
