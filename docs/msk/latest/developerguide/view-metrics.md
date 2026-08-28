---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/view-metrics.html
---

# Step 6: Use Amazon CloudWatch to view Amazon MSK metrics
<a name="view-metrics"></a>

In this step of [Getting Started Using Amazon MSK](getting-started.md), you look at the Amazon MSK metrics in Amazon CloudWatch.

**To view Amazon MSK metrics in CloudWatch**View metrics in CloudWatch

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Metrics**.

1. Choose the **All metrics** tab, and then choose **AWS/Kafka**.

1. To view broker-level metrics, choose **Broker ID, Cluster Name**. For cluster-level metrics, choose **Cluster Name**.

1. (Optional) In the graph pane, select a statistic and a time period, and then create a CloudWatch alarm using these settings.

**Next Step**

[Step 7: Delete the AWS resources created for this tutorial](delete-cluster.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
