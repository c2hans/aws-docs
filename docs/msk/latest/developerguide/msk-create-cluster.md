---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-create-cluster.html
---

# Create an MSK Provisioned cluster
<a name="msk-create-cluster"></a>

**Important**
You can't change the VPC for an MSK Provisioned cluster after you create the cluster.

Before you can create an MSK Provisioned cluster, you need to have an Amazon Virtual Private Cloud (VPC) and set up subnets within that VPC.

For Standard brokers in the US West (N. California) Region, you need two subnets in two different Availability Zones. In all other Regions where Amazon MSK is available, you can specify either two or three subnets. Your subnets must all be in different Availability Zones. For Express brokers, you need three subnets in three different Availability Zones. When you create an MSK Provisioned cluster, Amazon MSK distributes the broker nodes evenly over the subnets that you specify.

**Topics**
+ [Create an MSK Provisioned cluster using the AWS Management Console](create-cluster-console.md)
+ [Create a provisioned Amazon MSK cluster using the AWS CLI](create-cluster-cli.md)
+ [Create an MSK Provisioned cluster with a custom Amazon MSK configuration using the AWS CLI](create-cluster-cli-custom-config.md)
+ [Create an MSK Provisioned cluster using the Amazon MSK API](create-cluster-api.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
