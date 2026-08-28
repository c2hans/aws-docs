---
source_url: https://docs.aws.amazon.com/vpc/latest/tgw/delete-vpn-attachment.html
---

# Delete a VPN attachment in AWS Transit Gateway
<a name="delete-vpn-attachment"></a>

**To delete a VPN attachment using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation pane, choose **Transit Gateway Attachments**.

1. Select the VPN attachment.

1. Choose the resource ID of the VPN connection to navigate to the **VPN Connections** page.

1. Choose **Actions**, **Delete**.

1. When prompted for confirmation, choose **Delete**.

**To delete a VPN attachment using the AWS CLI**
Use the [delete-vpn-connection](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-vpn-connection.html) command.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
