---
source_url: https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/accessingmetrics.html
---

# Accessing CloudWatch metrics
<a name="accessingmetrics"></a>

You can see Amazon File Cache metrics for Amazon CloudWatch Logs in many ways. You can view them through the CloudWatch console, or you can access them using the CloudWatch CLI or the CloudWatch API. The following procedures show you how to access the metrics using these various tools.

**To view metrics using the CloudWatch console**

1. Open the [CloudWatch console](https://console.aws.amazon.com/cloudwatch).

1. In the navigation pane, choose **Metrics**.

1. Select the **FSx** namespace.

1. (Optional) To view a metric, type its name in the search field.

1. (Optional) To filter by dimension, select **FileCacheId**.

**To access metrics from the AWS CLI**
+ Use the [`list-metrics`](https://docs.aws.amazon.com/cli/latest/reference/cloudwatch/list-metrics.html) command with the `--namespace "AWS/FSx"` namespace. For more information, see the [AWS CLI Command Reference](https://docs.aws.amazon.com/cli/latest/reference/).

**To access metrics from the CloudWatch API**
+ Call `[GetMetricStatistics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.html)`. For more information, see [Amazon CloudWatch API Reference](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FSx. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fsx` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
