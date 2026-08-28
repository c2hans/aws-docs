---
source_url: https://docs.aws.amazon.com/vpc/latest/tgw/delete-client-vpn-attachment.html
---

# Delete a Client VPN attachment in AWS Transit Gateway
<a name="delete-client-vpn-attachment"></a>

**To delete a Client VPN attachment using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation pane, choose **Transit gateways**.

1. Choose **Transit gateway attachments**.

1. Select the Client VPN attachment that you want to delete.

1. Choose **Actions**, **Delete transit gateway attachment**.

1. When prompted for confirmation, enter **delete** and choose **Delete**.

The Client VPN attachment enters the **Deleting** state and will be removed from your account. This process may take some time to complete.

**To delete a Client VPN attachment using the AWS CLI**
Use the [delete-transit-gateway-client-vpn-attachment](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-transit-gateway-client-vpn-attachment.html) command.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
