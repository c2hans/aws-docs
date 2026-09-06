---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/rel_monitor_aws_resources_notification_aggregation.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# REL06-BP02 Define and calculate metrics (Aggregation)
<a name="rel_monitor_aws_resources_notification_aggregation"></a>

 Store log data and apply filters where necessary to calculate metrics, such as counts of a specific log event, or latency calculated from log event timestamps.

 Amazon CloudWatch and Amazon S3 serve as the primary aggregation and storage layers. For some services, such as AWS Auto Scaling and Elastic Load Balancing, default metrics are provided by default for CPU load or average request latency across a cluster or instance. For streaming services, such as VPC Flow Logs and AWS CloudTrail, event data is forwarded to CloudWatch Logs and you need to define and apply metrics filters to extract metrics from the event data. This gives you time series data, which can serve as inputs to CloudWatch alarms that you define to trigger alerts.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>
+  Define and calculate metrics (Aggregation). Store log data and apply filters where necessary to calculate metrics, such as counts of a specific log event, or latency calculated from log event timestamps
  +  Metric filters define the terms and patterns to look for in log data as it is sent to CloudWatch Logs. CloudWatch Logs uses these metric filters to turn log data into numerical CloudWatch metrics that you can graph or set an alarm on.
    +  [Searching and Filtering Log Data](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/MonitoringLogData.html)
  +  Use a trusted third party to aggregate logs.
    +  Follow the instructions of the third party. Most third-party products integrate with CloudWatch and Amazon S3.
  +  Some AWS services can publish logs directly to Amazon S3. If your main requirement for logs is storage in Amazon S3, you can easily have the service producing the logs send them directly to Amazon S3 without setting up additional infrastructure.
    +  [Sending Logs Directly to Amazon S3](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Sending-Logs-Directly-To-S3.html)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Amazon CloudWatch Logs Insights Sample Queries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-examples.html)
+  [Debugging with Amazon CloudWatch Synthetics and AWS X-Ray](https://aws.amazon.com/blogs/devops/debugging-with-amazon-cloudwatch-synthetics-and-aws-x-ray/)
+  [One Observability Workshop](https://observability.workshop.aws/)
+  [Searching and Filtering Log Data](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/MonitoringLogData.html)
+  [Sending Logs Directly to Amazon S3](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Sending-Logs-Directly-To-S3.html)
+  [The Amazon Builders' Library: Instrumenting distributed systems for operational visibility](https://aws.amazon.com/builders-library/instrumenting-distributed-systems-for-operational-visibility/)
