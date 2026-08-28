---
source_url: https://docs.aws.amazon.com/vpc/latest/tgw/associate-attachment-to-domain.html
---

# Associating VPC attachments and subnets with a multicast domain in AWS Transit Gateway
<a name="associate-attachment-to-domain"></a>

Use the following procedure to associate a VPC attachment with a multicast domain. When you create an association, you can then select the subnets to include in the multicast domain.

Before you begin, you must create a VPC attachment on your transit gateway. For more information, see [Amazon VPC attachments in AWS Transit Gateway](tgw-vpc-attachments.md).

**To associate VPC attachments with a multicast domain using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation pane, choose **Transit Gateway Multicast**.

1. Select the multicast domain, and then choose **Actions**, **Create association**.

1. For **Choose attachment to associate**, select the transit gateway attachment.

1. For **Choose subnets to associate**, select the subnets to include in the multicast domain.

1. Choose **Create association**.

**To associate VPC attachments with a multicast domain using the AWS CLI**
Use the [associate-transit-gateway-multicast-domain](https://docs.aws.amazon.com/cli/latest/reference/ec2/associate-transit-gateway-multicast-domain.html) command.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
