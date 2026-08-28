---
source_url: https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/cost.html
---

# Cost
<a name="cost"></a>

**Important**
The following cost estimations are examples and may vary depending on your environment.

You will be responsible for the cost of the AWS services used when running the solution. The main factors affecting the solution cost include:
+ Log analytics engine selection
+ Type of logs to be ingested
+ Volume of logs to be ingested/processed
+ Size of the log message
+ Location of logs
+ Additional features

As of this revision, the following examples demonstrate the cost estimation of 10/100/1000 GB daily log ingestion for running this solution with default settings in the US East (N. Virginia) Region. The cost formulation depends on the type of log analytics engine. The solution console can manage both OpenSearch Engine and Light Engine, and the solution console cost remains the same.

## Using OpenSearch Engine
<a name="using-opensearch-engine"></a>

This section describes the cost when choosing OpenSearch Engine. It is composed of [Amazon OpenSearch Service Cost](#amazon-opensearch-cost), [Processing Cost](#processing-cost), and [Additional Features Cost](#additional-features-cost).

### Amazon OpenSearch Service Cost
<a name="amazon-opensearch-cost"></a>
+  **OD**: On Demand
+  **AURI\_1**: All Upfront Reserved Instance 1 Year
+  **Tiering**: The days stored in each tier. For example, 7H \+ 23W \+ 60C indicates that the log is stored in hot tier for 7 days, warm tier for 23 days, and cold tier for 60 days.
+  **Replica**: The number of shard replicas.

| Daily log Volume (GB) | Retention (days) | Tiering | Replica | OD Monthly (USD) | AURI\_1 Monthly (USD) | Dedicated Master | Data Node | Amazon EBS (GB) | UltraWarm Nodes | UltraWarm/Cold Amazon S3 Storage (GB) | OD cost per GB (USD) | AURI\_1 cost per GB ($) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10 | 30 | 30H | 0 | 216.28 | 158.54 | N/A | c6g.large[2] | 380 | N/A | 0 | 0.72093 | 0.52847 |
| 10 | 30 | 30H | 1 | 289.35 | 223.94 | N/A | m6g.large[2] | 760 | N/A | 0 | 0.9645 | 0.74647 |
| 100 | 30 | 7H \+ 23W | 0 | 989.49 | 825.97 | m6g.large[3] | m6g.large[2] | 886 | medium[2] | 0 | 0.32983 | 0.27532 |
| 100 | 30 | 7H \+ 23W | 1 | 1295.85 | 1066.92 | m6g.large[3] | m6g.large[4] | 1772 | medium[2] | 0 | 0.43195 | 0.35564 |
| 100 | 90 | 7H \+ 23W \+ 60C | 0 | 1133.49 | 969.97 | m6g.large[3] | m6g.large[2] | 886 | medium[2] | 8300 | 0.12594 | 0.10777 |
| 100 | 90 | 7H \+ 23W \+ 60C | 1 | 1439.85 | 1210.92 | m6g.large[3] | m6g.large[4] | 1772 | medium[2] | 8300 | 0.15998 | 0.13455 |
| 100 | 180 | 7H \+ 23W \+ 150C | 0 | 1349.49 | 1185.97 | m6g.large[3] | m6g.large[2] | 886 | medium[2] | 17300 | 0.07497 | 0.06589 |
| 100 | 180 | 7H \+ 23W \+ 150C | 1 | 1655.85 | 1426.92 | m6g.large[3] | m6g.large[4] | 1772 | medium[2] | 17300 | 0.09199 | 0.07927 |
| 1000 | 30 | 7H \+ 23W | 0 | 6101.15 | 5489.48 | m6g.large[3] | r6g.xlarge[6] | 8856 | medium[15] | 23000 | 0.20337 | 0.18298 |
| 1000 | 30 | 7H \+ 23W | 1 | 8759.49 | 7635.8 | m6g.large[3] | r6g.2xlarge[6] | 17712 | medium[15] | 23000 | 0.29198 | 0.25453 |
| 1000 | 90 | 7H \+ 23W \+ 60C | 0 | 8027.33 | 7245.45 | m6g.large[3] | r6g.xlarge[6] | 8856 | medium[15] | 83000 | 0.08919 | 0.0805 |
| 1000 | 90 | 7H \+ 23W \+ 60C | 1 | 10199.49 | 9075.8 | m6g.large[3] | r6g.2xlarge[6] | 17712 | medium[15] | 83000 | 0.11333 | 0.10084 |
| 1000 | 180 | 7H \+ 23W \+ 150C | 0 | 9701.15 | 9089.48 | m6g.large[3] | r6g.xlarge[6] | 8856 | medium[15] | 173000 | 0.0539 | 0.0505 |
| 1000 | 180 | 7H \+ 23W \+ 150C | 1 | 12644.19 | 11420.86 | m6g.large[3] | r6g.2xlarge[6] | 17712 | medium[15] | 173000 | 0.07025 | 0.06345 |

### Processing Cost
<a name="processing-cost"></a>

 **Log ingestion through Amazon S3**

This section is applicable to:
+ AWS service logs, including Amazon S3 Access Logs, CloudFront standard logs, CloudTrail logs (Amazon S3), Application Load Balancer access logs, AWS WAF logs, VPC Flow Logs (Amazon S3), AWS Config logs, Amazon RDS/Aurora logs, and AWS Lambda Logs.
+ Application Logs that use Amazon S3 as a data buffer.

Assumptions:
+ The logs stored in Amazon S3 are in gzip format.
+ A 4MB compressed log file in Amazon S3 is roughly 100 MB in raw log size.
+ A Lambda with 1 GB memory takes about 26 seconds to process a 4 MB compressed log file, namely 260 milliseconds (ms) per MB raw logs.
+ The maximum compressed log file size is 5 MB.
+ Ingesting logs from Amazon S3 will incur Amazon SQS and Amazon S3 request fees, which are very low, or usually within the AWS Free Tier.

You have N GB raw log per day, and the daily cost estimation is as follows:

When you use AWS Lambda as a log processor:
+ Lambda Cost = 260 ms per MB x 1024 MB x N GB/day x $0.0000000167 per ms
+ Amazon S3 Storage Cost = $0.023 per GB x NGB/day x 4% (compression)

When you use OpenSearch Ingestion as a log processor:
+ OSI Pipeline Cost = $0.24 per OCU per hour
+ The maximum amount of Amazon S3 data 1 OCU can handle is around 20MB/s

The total estimated monthly cost for ingesting logs is:

 **Total Monthly Cost (Lambda as processor)** = (Lambda Cost \+ Amazon S3 Storage Cost) x 30 days

| Daily Log Volume | Daily Lambda Cost (USD) | Daily Amazon S3 Storage Cost (USD) | Monthly Cost (USD) |
| --- | --- | --- | --- |
| 10 | 0.044 | 0.009 | 1.610 |
| 100 | 0.445 | 0.092 | 16.099 |
| 1000 | 4.446 | 0.920 | 160.986 |
| 5000 | 22.23 | 4.600 | 804.900 |

 **Total Monthly Cost (OpenSearch Ingestion as processor)** = (OpenSearch Ingestion Cost \+ Amazon S3 Storage Cost) x 30 days

| Daily Log Volume | Daily Lambda Cost (USD) | Daily Amazon S3 Storage Cost (USD) | Monthly Cost (USD) |
| --- | --- | --- | --- |
| 10 | 5.760 | 0.001 | 173.1 |
| 100 | 5.760 | 0.009 | 175.5 |
| 1000 | 11.52 | 0.920 | 373.2 |
| 5000 | 34.56 | 4.600 | 1174.8 |

For Amazon RDS/Aurora logs and AWS Lambda Logs that deliver to CloudWatch Logs, apart from the Amazon S3 and Lambda costs listed previously, there is the additional cost of using Firehose (KDF) to subscribe to the CloudWatch Logs Stream and put them into an Amazon S3 bucket, and KDF is charging for a 5KB increment (less than 5KB per record is billed as 5KB).

Assuming Log size is 0.2 KB per record, then the daily KDF cost is estimated as follows:
+ Firehose Cost = $0.029 per GB x N GB/day x (5KB/0.2 KB)

For example, for 1GB logs per day, the extra monthly cost of KDF is $21.75.

**Important**
If you want to save costs charged by Firehose, make sure you activate logs only when needed. For example, you can choose not to activate Amazon RDS general logs unless required.

 **Log ingestion through Amazon Kinesis Data Streams**

This section is applicable to:
+ AWS Services Logs including CloudFront real-time logs, CloudTrail logs (delivers to CloudWatch Logs), and VPC Flow Logs (delivers to CloudWatch Logs).
+ Application Logs that use Amazon Kinesis Data Streams as the log buffer.

**Important**
The cost estimation does not include the logging cost of service. For example, CloudFront real-time logs are charged based on the number of log lines generated ($0.01 for every 1,000,000 log lines). There are also log delivery to CloudWatch charges for CloudTrail and VPC Flow Logs that enabled CloudWatch Logging. Check the service pricing for more details.

The cost estimation is based on the following assumptions and facts:
+ The average log message size is 1 KB.
+ The daily log volume is L GB.
+ The Lambda processor memory is 1024 MB.
+ Every Lambda invocation processes 1 MB logs.
+ One Lambda invocation processes one shard of Kinesis, and Lambda can scale up to more concurrent invocations to process multiple shards.
+ The Lambda runtime to process log less than 5 MB is 500ms.
+ 30% additional shards are provided to handle traffic jitter.
+ One Kinesis shard intake log size is = 1 MB /second x 3600 seconds per hour x 24 hours x 0.7 = 60.48 GB/day.
+ The desired Kinesis Shard number S is = Round\_up\_to\_next\_integer(Daily log volume L / 60.48).

Based on the preceding assumptions, here is the daily cost estimation formula:
+ Kinesis Shard Hour Cost = $0.015 / shard hour x 24 hours per day x S shards
+ Kinesis PUT Payload Unit Cost = $0.014 per million units x 1 million per GB x L GB per day
+ Lambda Cost = $0.0000000167 per 1ms x 500 ms per invocation x 1,000 invocations per GB x L GB per day

 **Total Monthly Cost** = (Kinesis Shard Hour Cost \+ Kinesis PUT Payload Unit Cost \+ Lambda Cost) x 30 days

| Daily Log Volume (GB) | Shards | Daily Kinesis Shard Hour Cost (USD) | Daily Kinesis PUT Payload Unit Cost (USD) | Daily Lambda Cost (USD) | Monthly Cost (USD) |
| --- | --- | --- | --- | --- | --- |
| 10 | 1 | 0.36 | 0.14 | 0.0835 | 17.505 |
| 100 | 2 | 0.72 | 1.4 | 0.835 | 88.65 |
| 1000 | 17 | 6.12 | 14 | 8.35 | 854.1 |

### Additional Features Cost
<a name="additional-features-cost"></a>

**Note**
You will not be charged if you do not use the additional features in the Centralized Logging with OpenSearch console.

 **Access Proxy**

If you deploy the [Access Proxy](access-proxy.md) through Centralized Logging with OpenSearch, additional charges will apply. The total cost varies depending on the instance type and number of instances. As of this revision, the following are two examples for the cost estimation in the US East (N. Virginia) Region.

 *Example 1: Instance Type - t3.nano, Instance Number - 2*
+ EC2 cost = t3.nano 1Y RI All Upfront price $26.28 x 2 / 12 months = $4.38/month
+ Amazon EBS Cost = Amazon EBS $0.1 GB/month x 8 GB x 2 = $1.6/month (The Amazon EBS attached to the EC2 instance is 8 GB)
+ Elastic Load Balancing Cost = $0.0225 per APPLICATION LOAD BALANCER-hour x 720 hours/month = $16.2/month

 **Total Monthly Cost** = $4.38 EC2 Cost \+ $1.6 Amazon EBS Cost \+ $16.2 Elastic Load Balancing Cost = **$22.18**

 *Example 2: Instance Type - t3.large, Instance Number - 2*
+ EC2 Cost = t3.large 1Y RI All Upfront $426.612 x 2 / 12 months = $71.1/month
+ Amazon EBS Cost = $0.1 GB/month x 8 GB x 2 = $1.6/month (The Amazon EBS attached to the EC2 instance is 8 GB)
+ Elastic Load Balancing Cost = $0.0225 per APPLICATION LOAD BALANCER-hour x 720 hours/month = $16.2/month

 **Total Monthly Cost** = $71.1 EC2 Cost \+ $1.6 Amazon EBS Cost \+ $16.2 Elastic Load Balancing Cost = **$88.9**

 **Amazon OpenSearch Service Alarms**

If you deploy the [alarms](pipeline-alarms-monitoring-and-logs.md#pipeline-alarms) through Centralized Logging with OpenSearch, the [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing) will apply.

 **Pipeline Alarms**

| Log Type | Alarm Count | Number of Standard Resolution Alarm Metrics | Monthly Cost per Ingestion per Pipeline |
| --- | --- | --- | --- |
| AWS Service logs | 4 | 0.1 USD | 0.4 USD |
| Application logs | 5 | 0.1 USD | 0.5 USD |

 **Pipeline Monitoring**

 **Log processor**

Assumptions:
+ Deployment in the US East (N. Virginia) Region (us-east-1)
+ A processor Lambda will be triggered every 60 seconds. The monthly metric put request number is 60 (requests) x 24 (hours) x 30 (days) = 43,200
+ PutMetricData: 43,200 requests x 0.00001 USD = 0.432 USD
+ There are 4 metrics for Service Logs (total logs, failed logs, loaded logs, excluded logs) and 3 metrics (total logs, failed logs, loaded logs) for Application logs
+ Amazon CloudWatch Logs API = PutMetricData x Number of Metrics
+ Amazon CloudWatch Logs Metric = Number of Metrics x 0.3

| Log Type | Monthly Metric Put Request Number | Number of Metrics | Amazon CloudWatch Logs API | Amazon CloudWatch Logs Metric | Monthly Cost Per Source/Per Pipeline |
| --- | --- | --- | --- | --- | --- |
| AWS Service logs | 43,200 | 4 | 1.728 USD | 1.2 USD | 2.928 USD |
| Application logs | 43,200 | 3 | 1.296 USD | 0.9 USD | 2.196 USD |

Fluent Bit

Assumptions:
+ Deployment in the US East (N. Virginia) Region (us-east-1)
+ There are 7 metrics: `FluentBitOutputProcRecords`, `FluentBitOutputProcBytes`, `FluentBitOutputDroppedRecords`, `FluentBitOutputErrors`, `FluentBitOutputRetriedRecords`, `FluentBitOutputRetriesFailed`, `FluentBitOutputRetries`. For more information, refer to the [Monitoring](pipeline-alarms-monitoring-and-logs.md#monitoring) section.
+ Number of Metrics requested: an interval of 60 seconds to put logs from Fluent Bit to Amazon CloudWatch (60 requests in an hour). Monthly put requests are 60 (requests) x 24 (hours) x 30 (days) = 43,200
+ PutMetricData: 43,200 requests x 0.00001 USD = 0.432 USD
+ CloudWatch Logs API = PutMetricData x Number of Metrics x Number of Instances
+ CloudWatch Logs Metric = Number of Metrics x 0.3

| Number of EC2 Instances / EKS Nodes | Amazon CloudWatch Logs API | Amazon CloudWatch Logs Log Storage and Ingested (Calculated by AWS Pricing Calculator) | Amazon CloudWatch Logs Metric | Monthly Cost Per Source/Per Pipeline |
| --- | --- | --- | --- | --- |
| 1 | 3.024 USD | 0.04 USD | 2.1 USD | 5.164 USD |
| 10 | 30.24 USD | 0.35 USD | 2.1 USD | 32.69 USD |
| 100 | 302.4 USD | 3.53 USD | 2.1 USD | 308.03 USD |

## Using Light Engine
<a name="using-light-engine"></a>

The pricing model of Light Engine is on demand. The cost varies on the raw log volume and the query log volume processed per day. The following provides monthly cost estimation in three scenarios:
+ 10 GB raw log, and query 50 GB per day
+ 100 GB raw log, and query 500 GB per day
+ 1TB raw log, and query 1TB per day

| Amazon Service | Monthly Cost (USD) Raw log: 10GB daily Query: 50GB daily | Monthly Cost (USD) Raw log: 100GB daily Query: 300GB daily | Monthly Cost (USD) Raw log: 1TB daily Query: 1TB daily |
| --- | --- | --- | --- |
| Amazon S3 | $1.49 | $19.98 | $148.99 |
| AWS Lambda | $0.37 | $0.73 | $1.10 |
| Amazon SQS | $0.00 | $0.00 | $0.00 |
| Amazon DynamoDB | $3.79 | $3.79 | $3.79 |
| AWS Step Functions | $8.07 | $16.14 | $26.90 |
| Amazon SNS | $0.18 | $0.18 | $0.18 |
| Amazon Athena | $7.25 | $43.51 | $148.54 |
| Amazon EC2 | $29.20 | $29.20 | $29.20 |
|  **Total**  |  **$50.35**  |  **$113.53**  |  **$358.70**  |

## Solution Console Cost
<a name="solution-console-cost"></a>

**Note**
AWS Step Functions, Amazon CloudWatch, AWS Systems Manager, and Amazon EventBridge are all within AWS Free Tier.

A web console is created automatically when you deploy the solution. Assume the visits to the console are 3,000 times in a month (30 days), it will incur the following cost:

| Service | Monthly Cost (USD) |
| --- | --- |
| Amazon CloudFront (1GB Data Transfer Out to internet and 1GB Data Transfer Out to Origin) | 0.25 |
| Amazon S3 | 0.027 |
| Amazon Cognito | 0.05 |
| AWS AppSync | 0.01 |
| Amazon DynamoDB | 1.00 |
| AWS Lambda | 0.132 |
|  **Total**  |  **1.469**  |

## View cost in Cost Explorer
<a name="view-cost-in-cost-explorer"></a>

You can view the spending of the entire solution, or at the pipeline level. All pipelines provisioned through the web console will, by default, have the `CLOSolutionCostAnalysis` tag associated with them. When creating a log pipeline, you have the option to input additional tags, and those tags will be propagated to all resources associated with that pipeline. You can then use the tag to view the cost of a specific pipeline or a group of pipelines with the same tag.

To enable this function, you must activate user-defined cost allocation tags first, and then view the cost in [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/).

 **Step 1: Activate user-defined cost allocation tags**

For tags to appear on your billing reports, you must activate them. Your user-defined cost allocation tags represent the tag key, which you activate in the Billing and Cost Management console. Once you activate or deactivate the tag key, it will affect all tag values that share the same tag key. A tag key can have multiple tag values. For more information, see the [AWS Billing and Cost Management and Cost Management API Reference](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_UpdateCostAllocationTagsStatus.html).

1. Sign in to the AWS Management [Console and open the AWS Billing and Cost Management and Cost Management console](https://console.aws.amazon.com/billing/).

1. In the navigation pane, choose **Cost allocation tags**.

1. Select the tag key **CLOSolutionCostAnalysis** to activate.

1. Choose **Activate**.

**Note**
After you create and apply user-defined tags to your resources, it can take up to 24 hours for the tag keys to appear on your cost allocation tags page for activation.

For an example of how tag keys appear in your billing report with cost allocation tags, see [Viewing a cost allocation report](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/configurecostallocreport.html#allocation-viewing).

 **Step 2: View Cost Explorer dashboard**

1. Sign in to the AWS Management Console and open the [AWS Billing and Cost Management and Cost Management console](https://console.aws.amazon.com/billing/).

1. In the navigation pane, choose **Cost Explorer**.

1. Choose **Tag** as the displayed Dimension and select the specific tag **CLOSolutionCostAnalysis** to filter.

1. If your activated tag is absent in the dropdown list, this is because the activation process is still in progress. It can take up to 24 hours for tag keys to activate. Try later.

 **New cost and usage report example bar graph.**

![image16](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image16.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Centralized Logging with OpenSearch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
