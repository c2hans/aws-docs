---
source_url: https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/light-engine.html
---

# Light Engine
<a name="light-engine"></a>

The Light Engine is a complementary log analytics engine to the default OpenSearch Engine. It is designed for analyzing structured and infrequent logs, offering up to a 90% cost reduction. The Light Engine uses several AWS services, including Amazon Athena, AWS Glue, AWS Lambda, and AWS Step Functions, to achieve its scale and cost-effective performance.

## OpenSearch Engine vs. Light Engine
<a name="opensearch-engine-vs.-light-engine"></a>

We suggest using two engines to tackle real-world challenges. For mission-critical, high-performance, or essential workloads, opt for OpenSearch. Conversely, use Light Engine to save costs when handling secondary, less critical workloads that do not require the same level of performance.

The following table provides guidance for you to choose the appropriate analytics engine. For more assistance, consult an AWS Solutions Architect.

|  | OpenSearch Engine | Light Engine |
| --- | --- | --- |
|  **Ingest latency**  | Seconds \~ Minutes (depends on buffer layer type) | 5 minutes preceding |
|  **Query latency**  | Milliseconds \~ Seconds | Seconds \~ Minutes |
|  **Text search**  | Full-text | Fuzzy (the "Like" syntax of SQL) |
|  **Query language**  | DSL (Domain Specific Language) | SQL |
|  **Dashboards**  | OpenSearch Dashboards | Grafana |
|  **Alarm**  | Provided by OpenSearch Dashboards | Provided by Grafana |
|  **Access control**  | Field level | Table level |
|  **Sharing**  | Export data | Parquet files in Amazon S3 |
|  **Operational effort**  | High | Low |
|  **Schema**  | Semistructured | Structured |
|  **Cost**  | High | Low |
|  **Pricing model**  | Fixed; OpenSearch node types and counts, storage | On demand |

## Key components
<a name="key-components"></a>

 **Log Bucket**

A Log Bucket is an Amazon S3 bucket where you (or the log agent) deliver the raw logs to. The Log Bucket must reside in the same AWS account and Region as the solution you are implementing.

 **Staging Bucket**

The Staging Bucket is an Amazon S3 storage location that holds a small portion of the raw log files, which are copied from the Log Bucket. The solution then processes these raw log files in the Staging Bucket in batches.

 **Centralized Bucket**

The Centralized Bucket is an Amazon S3 storage location where Light Engine stores the partitioned, and compressed (in Apache Parquet format) log files. The schema and format are optimized for query by Light Engine.

 **Archive Bucket**

The Archive Bucket is an Amazon S3 storage location where Light Engine moves the data from the Centralized Bucket, and then use Amazon S3 Lifecycle policy to delete the logs.

 **Log Processor**

The Log Processor is triggered at a regular interval (default is 5 minutes) by Amazon EventBridge. It processes logs to accomplish the following tasks:
+ Process raw log files stored on Amazon S3 in batches, and transform them into Apache Parquet format.
+ Automatically partition all incoming data by time, Region, and other relevant attributes.
+ Calculate metrics of log data and save to the Centralized bucket.
+ Trigger Amazon SNS notifications when task execution fails.
+ Each Pipeline/Ingestion corresponds to an Amazon EventBridge rule that periodically triggers the log processor, for instance, every 5 minutes.

 **Log Merger**

The Log Merger periodically (default is once every day at 1:00AM UTC) merges small parquet format files into large parquet format files, and further improve the query performance. It accomplishes the following tasks:
+ Merge small files into files of a specified size, reduce the number of files, and reduce data storage.
+ Optimize the partition granularity and update the AWS AWS Glue Data Catalog to reduce the number of partitions.
+ Trigger Amazon SNS notifications when task execution fails.
+ Each pipeline corresponds to an Amazon EventBridge rule to periodically trigger log merger.

 **Log Archiver**

The Log Archiver manages the lifecycle of data stored in Amazon S3, and cleanup table partitions.
+ Move the expired data in Centralized to archived until the lifecycle rule deletes the files.
+ Update AWS AWS Glue Data Catalog and delete expired table partitions
+ Trigger Amazon SNS notifications when task execution fails.
+ Each pipeline corresponds to an Amazon EventBridge rule to periodically trigger log archive, for instance, every day at 1:00AM.

## Architecture Diagram
<a name="architecture-diagram-1"></a>

 **Light Engine architecture.**

![image14](https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image14.png)

The Light Engine runs the following workflow:

1. Logs are uploaded to an Amazon S3 bucket (Log Bucket). An event notification is sent to Amazon SQS using S3 Event Notifications when a new log file is created.

1. Amazon SQS triggers AWS Lambda to execute.

1. AWS Lambda copy log files from Log Bucket to Staging Bucket.

1. The Log Processor, scheduled by Amazon EventBridge, read logs from the Staging Bucket.

1. The Log Processor parses, calculates metrics (for AWS Service logs), compresses using zstd method, partitions, and saves the processed data in Parquet format into the Centralized Bucket.

1. Log Merger, scheduled by Amazon EventBridge, reads logs from the Centralized Bucket. It then merges small log files into larger ones, and saves them back to the Centralized Bucket. This process helps to optimize the storage, and improve the performance when querying.

1. Log Archiver, scheduled by Amazon EventBridge, periodically copies the log files to the Archive Bucket, and delete log files.

1. Log Archiver saves the copied log files to the Archived Bucket, and then uses the S3 Lifecycle to delete the logs according to the configurations.

1. Users query and visualize logs in Grafana, and Grafana uses Athena to query processed logs in Centralized Bucket.

   When any errors occur during data processing, notifications will be sent to the Simple Notification Service (Amazon SNS). You can configure Amazon SNS to deliver these notifications via SMS, email, or instant messaging, to be promptly informed of any issues that arise.
