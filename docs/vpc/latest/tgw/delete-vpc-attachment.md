---
source_url: https://docs.aws.amazon.com/vpc/latest/tgw/delete-vpc-attachment.html
---

# Delete a VPC attachment in AWS Transit Gateway
<a name="delete-vpc-attachment"></a>

**To delete a VPC attachment using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation pane, choose **Transit Gateway Attachments**.

1. Select the VPC attachment.

1. Choose **Actions**, **Delete transit gateway attachment**.

1. When prompted, enter **delete** and choose **Delete**.

**To delete a VPC attachment using the AWS CLI**
Use the [delete-transit-gateway-vpc-attachment](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-transit-gateway-vpc-attachment.html) command.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
