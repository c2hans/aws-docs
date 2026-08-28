---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-autoexpand-setup.html
---

# Set up automatic scaling for your Amazon MSK cluster
<a name="msk-autoexpand-setup"></a>

You can use the Amazon MSK console, the Amazon MSK API, or CloudFormation to implement automatic scaling for storage. CloudFormation support is available through [Application Auto Scaling](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html).

**Note**
You can't implement automatic scaling when you create a cluster. You must first create the cluster, and then create and enable an auto-scaling policy for it. However, you can create the policy while Amazon MSK service creates your cluster.

**Topics**
+ [Set up automatic scaling using the Amazon MSK AWS Management Console](msk-autoexpand-setup-console.md)
+ [Set up automatic scaling using the CLI](msk-autoexpand-setup-cli.md)
+ [Set up automatic-scaling for Amazon MSK using the API](msk-autoexpand-setup-api.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
