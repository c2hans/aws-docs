---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search-ingesting-span-log-groups.html
---

# Spans
<a name="CloudWatch-Transaction-Search-ingesting-span-log-groups"></a>

 Spans sent to X-Ray are ingested and managed in a log group called `aws/spans`. This topic describes which CloudWatch Logs features are available for transaction spans.

**Available features**
 The following CloudWatch Logs features are available for transaction spans.
+  [Metric filters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/MonitoringLogData.html) – Use metric filters to extract custom metrics from spans.
+  [Subscriptions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Subscriptions.html) – Use subscriptions to access a real-time feed of span events from CloudWatch Logs.
+  [Log anomaly detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/LogsAnomalyDetection.html) – Use log anomaly detection to establish a baseline for spans sent to the `aws/spans` log group.
+  [Contributor Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights.html) – Use Contributor Insights to analyze span data and create a time series displaying contributor data.

**Unsupported features**
 The following are features not supported for transaction spans.
+  Spans cannot be sent to CloudWatch Logs with the `PutLogEvents` API.
+  Span data cannot be [enriched or transformed](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html).

**Note**
 Span ingestion is charged separately from log ingestion. For information about pricing, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
