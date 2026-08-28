---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-create-cluster-tiered-storage-console.html
---

# Create a Amazon MSK cluster with tiered storage with the AWS Management Console
<a name="msk-create-cluster-tiered-storage-console"></a>

This process describes how to create a tiered storage Amazon MSK cluster using the AWS Management Console.

1. Open the Amazon MSK console at [https://console.aws.amazon.com/msk/](https://console.aws.amazon.com/msk/).

1. Choose **Create cluster**.

1. Choose **Custom create** for tiered storage.

1. Specify a name for the cluster.

1. In the **Cluster type**, select **Provisioned**.

1. Choose an Amazon Kafka version that supports tiered storage for Amazon MSK to use to create the cluster.

1. Specify a size of broker other than **kafka.t3.small**.

1. Select the number of brokers that you want Amazon MSK to create in each Availability Zone. The minimum is one broker per Availability Zone, and the maximum is 30 brokers per cluster.

1. Specify the number of zones that brokers are distributed across.

1. Specify the number of Apache Kafka brokers that are deployed per zone.

1. Select **Storage options**. This includes **Tiered storage and EBS storage** to enable tiered storage mode.

1. Follow the remaining steps in the cluster creation wizard. When complete, **Tiered storage and EBS storage** appears as the cluster storage mode in the **Review and create** view.

1. Select **Create cluster**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
