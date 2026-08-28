---
source_url: https://docs.aws.amazon.com/vpc/latest/tgw/view-vpc-attachment.html
---

# View a VPC attachment in AWS Transit Gateway
<a name="view-vpc-attachment"></a>

**To view your VPC attachments using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation pane, choose **Transit Gateway Attachments**.

1. In the **Resource type** column, look for **VPC**. These are the VPC attachments.

1. Choose an attachment to view its details.

**To view your VPC attachments using the AWS CLI**
Use the [describe-transit-gateway-vpc-attachments](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-transit-gateway-vpc-attachments.html) command.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
