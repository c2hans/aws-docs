---
source_url: https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/application-log-analytics-pipeline.html
---

# Application log analytics pipeline
<a name="application-log-analytics-pipeline"></a>

Centralized Logging with OpenSearch supports log analysis for application logs, such as NGINX/Apache HTTP Server logs or custom application logs.

**Note**
Centralized Logging with OpenSearch supports [cross-account log ingestion](cross-account-ingestion.md). If you want to ingest logs from the same account, the resources in the **Sources** group will be in the same account as your Centralized Logging with OpenSearch account. Otherwise, they will be in another AWS account.

## Logs from Amazon EC2 / Amazon EKS
<a name="logs-from-amazon-ec2-amazon-eks"></a>

Centralized Logging with OpenSearch supports collecting logs from Amazon EC2 instances or Amazon EKS clusters. The workflow supports two scenarios.

 **Scenario 1: Using OpenSearch Engine**

 **Application log pipeline architecture for EC2/EKS.**

![arch app ec2eks](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/arch-app-ec2eks.png)

The log pipeline runs the following workflow:

1. Fluent Bit works as the underlying log agent to collect logs from application servers and send them to an optional Log Buffer, or ingest into OpenSearch domain directly.

1. (Option A) The Log Buffer sends events to Amazon EventBridge.

   (Option B) The Log Buffer sends events to Amazon SQS.

1. (Option A) Amazon EventBridge triggers the Log Processor Lambda function to execute.

   (Option B) Amazon SQS triggers the OpenSearch Ingestion Service to execute.

1. The AWS Lambda function or OpenSearch Ingestion Service reads and processes the log records.

1. The AWS Lambda function or OpenSearch Ingestion Service ingests the logs into the OpenSearch domain.

1. Logs that fail to be processed are exported to an Amazon S3 bucket (Backup Bucket).

 **Scenario 2: Using Light Engine**

 **Application log pipeline architecture for EC2/EKS.**

![image8](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image8.png)

The log pipeline runs the following workflow:

1.  [Fluent Bit](https://fluentbit.io/) works as the underlying log agent to collect logs from application servers and send them to a Log Bucket.

1. An event notification is sent to Amazon SQS using S3 Event Notifications when a new log file is created.

1. Amazon SQS initiates AWS Lambda to execute.

1. AWS Lambda load the log file from the Log Bucket.

1. AWS Lambda put the log file to the Staging Bucket.

1. The Log Processor, AWS Step Functions, processes raw log files stored in the staging bucket in batches.

1. The Log Processor converts raw log files to Apache Parquet format and automatically partitions all incoming data based on criteria including time and Region.

## Logs from Amazon S3
<a name="logs-from-amazon-s3"></a>

Centralized Logging with OpenSearch supports collecting logs from Amazon S3 buckets. The workflow supports three scenarios:

 **Scenario 1: Using OpenSearch Engine (Ongoing)**

In this scenario, the solutions continuously read and parse logs whenever you upload a log file to the specified Amazon S3 location.

 **Application log pipeline architecture for Amazon S3.**

![image9](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image9.png)

The log pipeline runs the following workflow:

1. User uploads logs to an Amazon S3 bucket (Log Bucket).

1. An event notification is sent to Amazon EventBridge when a new log file is created.

1. Amazon EventBridge initiates AWS Lambda (Log Processor) to execute.

1. The Log Processor reads and processes log files.

1. The Log Processor ingests the processed logs into the OpenSearch domain.

1. Logs that fail to be processed are exported to an Amazon S3 bucket (Backup Bucket).

 **Scenario 2: Using OpenSearch Engine (One-time)**

In this scenario, the solution scans existing log files stored in the specified Amazon S3 location and ingests them into the log analytics engine in a single operation.

 **Application log pipeline architecture for Amazon S3.**

![image10](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image10.png)

The log pipeline runs the following workflow:

1. User uploads logs to an Amazon S3 bucket (Log Bucket).

1. Amazon ECS Task iterates log files in the Log Bucket.

1. Amazon ECS Task sends the log location to an Amazon EventBridge.

1. Amazon EventBridge initiates AWS Lambda to execute.

1. The Log Processor reads and parses log files.

1. The Log Processor ingests the processed logs into the OpenSearch domain.

1. Logs that fail to be processed are exported to an Amazon S3 bucket (Backup Bucket).

 **Scenario 3: Using Light Engine (Ongoing)**

 **Application log pipeline architecture for Amazon S3.**

![image11](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image11.png)

The log pipeline runs the following workflow:

1. Logs are uploaded to an Amazon S3 bucket (Log bucket).

1. An event notification is sent to Amazon SQS using S3 Event Notifications when a new log file is created.

1. Amazon SQS initiates AWS Lambda.

1. AWS Lambda copies objects from the Log bucket.

1. AWS Lambda output the copied objects to the Staging bucket.

1. AWS Step Functions periodically trigger Log Processor to process raw log files stored in the staging bucket in batches.

1. The Log Processor converts them into Apache Parquet format and automatically partitions all incoming data based on criteria including time and Region.

## Logs from Syslog Client
<a name="logs-from-syslog-client"></a>

**Important**
Make sure your Syslog generator/sender’s subnet is connected to Centralized Logging with OpenSearch’s **two** private subnets. You may need to use [VPC Peering Connection](https://docs.aws.amazon.com/vpc/latest/peering/working-with-vpc-peering.html) or [Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) to connect these VPCs.
The Network Load Balancer together with the Amazon ECS containers in the architecture diagram will be provisioned only when you create a Syslog ingestion and be automated deleted when there is no Syslog ingestion.

 **Scenario 1: Using OpenSearch Engine**

 **Application log pipeline architecture for Syslog.**

![image12](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image12.png)

1. Syslog client (like [Rsyslog](https://www.rsyslog.com/)) sends logs to a Network Load Balancer in Centralized Logging with OpenSearch’s private subnets, and the Network Load Balancer routes to the Amazon ECS containers running Syslog servers.

1.  [Fluent Bit](https://fluentbit.io/) works as the underlying log agent in the Amazon ECS service to parse logs, and send them to an optional Log Buffer, or ingest into OpenSearch domain directly.

1. The Log Buffer sends messages to Amazon EventBridge.

1. Amazon EventBridge triggers the Log Processor Lambda function to run.

1. The Log Processor Lambda function reads and processes the log records and ingests the logs into the OpenSearch domain.

1. Logs that fail to be processed are exported to an Amazon S3 bucket (Backup Bucket).

 **Scenario 2: Using Light Engine**

 **Application log pipeline architecture for Syslog.**

![image13](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image13.png)

1. Syslog client (like Rsyslog) send logs to a Network Load Balancer in Centralized Logging with OpenSearch’s private subnets, and the Network Load Balancer routes to the Amazon ECS containers running Syslog servers.

1. Fluent Bit works as the underlying log agent in the Amazon ECS Service to parse logs, and send them to an optional Log Buffer, or ingest into OpenSearch domain directly.

1. An event notification is sent to Amazon SQS using S3 Event Notifications when a new log file is created.

1. Amazon SQS initiates AWS Lambda.

1. AWS Lambda copies objects from the Log bucket.

1. AWS Lambda output the copied objects to the Staging bucket

1. AWS Step Functions periodically trigger Log processor to process raw log files stored in the staging bucket in batches.

1. The Log Processor converts them into Apache Parquet format and automatically partitions all incoming data based on criteria including time and Region.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Centralized Logging with OpenSearch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
