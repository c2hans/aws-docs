---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations-Services.html
---

# AWS services where investigations are supported

You can launch investigations from telemetry data (such as CloudWatch metrics, alarms, and logs), review generated anomaly signals, and explore hypotheses on investigations. CloudWatch investigations work best when helping you with automated troubleshooting guidance on the AWS services listed below:
+ Amazon API Gateway
+ AWS AppSync
+ Amazon Data Firehose
+ Amazon DynamoDB
+ Amazon EBS<sup>1</sup>
+ Amazon EC2<sup>1</sup>
+ Amazon ECS on Amazon EC2<sup>2</sup>
+ Amazon ECS on Fargate<sup>2</sup>
+ Amazon EKS<sup>3</sup>
+ Amazon Kinesis Data Streams
+ AWS Lambda
+ Amazon OpenSearch Service
+ Amazon RDS<sup>4</sup>
+ Amazon S3
+ Amazon SNS
+ Amazon SQS
+ AWS Step Functions

The list of services will continue to be expanded over time. CloudWatch investigations uses a wide range of data sources to determine dependency relationships and plan analysis paths, including telemetry data configurations, service configurations, and observed relationships through CloudWatch Application Signals and X-Ray. Where none of the above is available, CloudWatch investigations will attempt to infer dependency relationships through co-occurring telemetry anomalies.

**Best practice setup**

While CloudWatch investigations will continue to analyze telemetry data and provide suggestions without the following features enabled, for optimal quality and performance for CloudWatch investigations, we recommend you complete the following steps:
+ <sup>1</sup>For both Amazon EC2 and Amazon EBS, update your CloudWatch agent to version 1.30049.1 or later. For more information, see [Collect metrics, logs, and traces using the CloudWatch agent](Install-CloudWatch-Agent.md).
+ <sup>2</sup>For Amazon ECS, enable CloudWatch Container Insights. For more information, see [Container Insights for Amazon ECS](deploy-container-insights-ECS.md).
+ <sup>3</sup>For Amazon EKS, enable CloudWatch Container Insights and configure Amazon EKS Access Entries. For more information, see [Container Insights for Amazon EKS](ContainerInsights.md) and [Integration with Amazon EKS](EKS-Integration.md).
+ <sup>4</sup>For Amazon RDS, enable CloudWatch Database Insights in the **Advanced mode**. For more information, see [Turning on the Advanced mode of Database Insights for Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_DatabaseInsights.TurningOnAdvanced.html) in the *Aurora User Guide*.
+ Enable CloudWatch Application Signals and X-Ray. For more information, see [Application Signals](CloudWatch-Application-Monitoring-Sections.md) and [What is AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html).
