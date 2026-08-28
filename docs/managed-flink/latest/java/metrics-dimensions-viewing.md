---
source_url: https://docs.aws.amazon.com/managed-flink/latest/java/metrics-dimensions-viewing.html
---

# View CloudWatch metrics
<a name="metrics-dimensions-viewing"></a>

You can view CloudWatch metrics for your application using the Amazon CloudWatch console or the AWS CLI.

**To view metrics using the CloudWatch console**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Metrics**.

1. In the **CloudWatch Metrics by Category** pane for Managed Service for Apache Flink, choose a metrics category.

1. In the upper pane, scroll to view the full list of metrics.

**To view metrics using the AWS CLI**
+ At a command prompt, use the following command.

  ```
  1. aws cloudwatch list-metrics --namespace "AWS/KinesisAnalytics" --region {{region}}
  ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed Service for Apache Flink. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-flink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
