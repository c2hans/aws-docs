---
source_url: https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/service-log-analytics-pipeline.html
---

# Service log analytics pipeline
<a name="service-log-analytics-pipeline"></a>

Centralized Logging with OpenSearch supports log analysis for AWS services, such as Amazon S3 Access Logs, and Application Load Balancer access logs. For a complete list of supported AWS services, refer to [Supported AWS Services](supported-aws-services.md).

This solution ingests different AWS service logs using different workflows.

**Note**
Centralized Logging with OpenSearch supports [cross-account log ingestion](cross-account-ingestion.md). If you want to ingest logs from the same account, the resources in the **Sources** group will be in the same account as your Centralized Logging with OpenSearch account. Otherwise, they will be in another AWS account.

## Logs through Amazon S3
<a name="logs-through-amazon-s3"></a>

Many AWS services support delivering logs to Amazon S3 directly, or through other services. The workflow supports three scenarios:

 **Scenario 1: Logs to Amazon S3 directly (OpenSearch Engine)**

In this scenario, the service directly delivers logs to Amazon S3. This architecture is applicable to the following log sources:
+ AWS CloudTrail logs (delivers to Amazon S3)
+ Application Load Balancer access logs
+ AWS WAF logs
+ Amazon CloudFront standard logs
+ Amazon S3 Access Logs
+ AWS Config logs
+ VPC Flow Logs (delivers to Amazon S3)

 **Amazon S3 based service log pipeline architecture.**

![image2](https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image2.png)

The log pipeline runs the following workflow:

1. AWS services are configured to deliver logs to Amazon S3 bucket (Log Bucket).

1. (Option A) An event notification is sent to Amazon EventBridge when a new log file is created.

   (Option B) An event notification is sent to Amazon SQS using [S3 Event Notifications](https://docs.aws.amazon.com/AmazonS3/latest/userguide/NotificationHowTo.html) when a new log file is created.

1. (Option A) Amazon EventBridge initiates the *Log Processor* Lambda function.

   (Option B) OpenSearch Ingestion Service consumes the SQS messages.

1. The Log Processor Lambda function reads and processes the log files.

1. The Log Processor Lambda function ingests the logs into the Amazon OpenSearch Service.

1. Logs that fail to be processed are exported to Amazon S3 bucket (Backup Bucket).

 **Scenario 2: Logs to Amazon S3 via Kinesis Data Firehose (OpenSearch Engine)**

In this scenario, the service cannot deliver their logs to Amazon S3 directly. The logs are sent to Amazon CloudWatch, and Amazon Data Firehose is used to subscribe the logs from CloudWatch Log Group and then redeliver the logs to Amazon S3. This architecture is applicable to the following log sources:
+ AWS Lambda logs

 **Depicts Amazon S3 (via Firehose) based service log pipeline architecture**

![image3](https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image3.png)

The log pipeline runs the following workflow:

1. AWS services logs are configured to deliver logs to Amazon CloudWatch Logs, and Amazon Data Firehose are used to subscribe and store logs in Amazon S3 bucket (Log Bucket).

1. An event notification is sent to Amazon SQS using S3 Event Notifications when a new log file is created.

1. Amazon SQS initiates the Log Processor Lambda function to run.

1. The Log Processor Lambda function reads and processes the log files.

1. The Log Processor Lambda function ingests the logs into the Amazon OpenSearch Service.

1. Logs that fail to be processed are exported to Amazon S3 bucket (Backup Bucket).

 **Scenario 3: Logs to Amazon S3 by calling AWS service API (OpenSearch Engine)**

In this scenario, a helper Lambda function periodically invokes AWS service APIs to download log files and save them to an S3 bucket. This architecture is applicable to the following log sources:
+ Amazon RDS
+ AWS WAF (Sampled logs)

 **Depicts API call-based service log pipeline architecture**

![arch service api](https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/arch-service-api.png)

The log pipeline runs the following workflow:

1. Amazon EventBridge periodically triggers the AWS Lambda function. Every 5 mins by default.

1. The AWS Lambda function invokes the appropriate AWS service API to download the log files.

1. The downloaded log files are stored in an Amazon S3 bucket.

1. An event notification is sent to Amazon EventBridge when a new log file is created.

1. Upon receiving the notification, Amazon EventBridge triggers the Log Processor Lambda function.

1. The Log Processor Lambda function reads and processes the log files.

1. The Log Processor Lambda function ingests the processed logs into the Amazon OpenSearch Service for analysis.

1. The Log Processor Lambda function exports any logs that fail to process to a designated Amazon S3 bucket (Backup Bucket) for later review.

 **Scenario 4: Logs to Amazon S3 directly (Light Engine)**

In this scenario, the service directly sends logs to Amazon S3. This architecture is applicable to the following log sources:
+ Amazon CloudFront standard logs
+ AWS CloudTrail logs (delivers to Amazon S3)
+ Application Load Balancer access logs
+ AWS WAF logs
+ VPC Flow Logs (delivers to Amazon S3)

 **Amazon S3 based service log pipeline architecture.**

![image4](https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image4.png)

The log pipeline runs the following workflow:

1. AWS services are configured to deliver logs to the Amazon S3 bucket (Log Bucket).

1. An event notification is sent to Amazon SQS using S3 Event Notifications when a new log file is created.

1. Amazon SQS initiates the Log Processor Lambda function to run.

1. AWS Lambda retrieves the log file from the Log Bucket.

1. AWS Lambda uploads the log file to the Staging Bucket.

1. The Log Processor Lambda function, AWS Step Functions, processes raw log files stored in the staging bucket in batches.

1. The Log Processor Lambda function converts raw log files to Apache Parquet format, automatically partitions all incoming data based on criteria including time and Region, calculates relevant metrics, and stores the results in the Centralized Bucket.

## Logs through Amazon Kinesis Data Streams
<a name="logs-through-amazon-kinesis-data-streams"></a>

Some AWS services support delivering logs to Amazon Kinesis Data Streams. The workflow supports two scenarios:

 **Scenario 1: Logs to Kinesis Data Streams directly (OpenSearch Engine)**

In this scenario, the service directly delivers logs to Amazon Kinesis Data Streams. This architecture is applicable to the following log sources:
+ Amazon CloudFront real-time logs

 **Amazon Kinesis Data Streams based service log pipeline architecture.**

![image5](https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image5.png)

**Warning**
This solution does not support cross-account ingestion for CloudFront real-time logs.

The log pipeline runs the following workflow:

1. AWS services are configured to deliver logs to Amazon Kinesis Data Streams.

1. Amazon Kinesis Data Streams trigger AWS Lambda to execute.

1. AWS Lambda read, parse, and process logs from Kinesis Data Streams, and upload to Amazon OpenSearch Service.

1. Logs that fail to be processed are exported to Amazon S3 bucket (Backup Bucket).

 **Scenario 2: Logs to Kinesis Data Streams via CloudWatch Logs (OpenSearch Engine)**

In this scenario, the service delivers the logs to CloudWatch Logs, and then CloudWatch Logs redeliver the logs in real-time to Kinesis Data Streams using subscription. This architecture is applicable to the following log sources:
+ AWS CloudTrail logs (delivers to CloudWatch Logs)
+ VPC Flow Logs (delivers to CloudWatch Logs)

 **Amazon Kinesis Data Streams (via CloudWatch Logs) based service log pipeline architecture.**

![image6](https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image6.png)

The log pipeline runs the following workflow:

1. AWS Services logs are configured to write logs Amazon CloudWatch Logs.

1. Logs are redelivered to Kinesis Data Streams via CloudWatch Logs subscription.

1. Kinesis Data Streams initiates the AWS Lambda (Log Processor) to execute.

1. The Log Processor processes and ingests the logs into the Amazon OpenSearch Service.

1. Logs that fail to be processed are exported to Amazon S3 bucket (Backup Bucket).

For cross-account ingestion, the AWS Services store logs on Amazon CloudWatch log group in the member account, and other resources remain in the main account.
