---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/LogsAnomalyDetection-Metrics.html
---

# Metrics published by log anomaly detectors
<a name="LogsAnomalyDetection-Metrics"></a>

CloudWatch Logs publishes the **AnomalyCount** metric to CloudWatch metrics. This metric is published to the `AWS/Logs` namespace.

The **AnomalyCount** metric is published with the following dimensions:
+ **LogAnomalyDetector**– The name of the anomaly detector
+ **LogAnomalyPriority**– The priority level of the anomaly

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
