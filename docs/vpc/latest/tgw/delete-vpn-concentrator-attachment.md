---
source_url: https://docs.aws.amazon.com/vpc/latest/tgw/delete-vpn-concentrator-attachment.html
---

# Delete a VPN Concentrator attachment in AWS Transit Gateway
<a name="delete-vpn-concentrator-attachment"></a>

**Prerequisites**
+ All VPN connections on the VPN Concentrator must be deleted before you can delete the Concentrator attachment.
+ Ensure that you have updated your routing configurations to account for the removal of the VPN Concentrator and its associated VPN connections.

**To delete VPN connections on a VPN Concentrator using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation pane, choose **Site-to-Site VPN Connections**.

1. Identify the VPN connections associated with your VPN Concentrator by looking for the VPN Concentrator ID in the **Transit Gateway ID** column.

1. Select a VPN connection that you want to delete.

1. Choose **Actions**, **Delete**.

1. When prompted for confirmation, choose **Delete**.

1. Repeat steps 4-6 for each VPN connection associated with the VPN Concentrator.

**To delete a VPN Concentrator attachment using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation pane, choose **Transit Gateway Attachments**.

1. Select the VPN Concentrator attachment that you want to delete. Verify that no VPN connections are associated with this Concentrator.

1. Choose **Actions**, **Delete attachment**.

1. When prompted for confirmation, choose **Delete**.

The VPN Concentrator attachment enters the **Deleting** state and will be removed from your account. This process may take a few minutes to complete.

**To delete VPN connections on a VPN Concentrator using the AWS CLI**
Use the [delete-vpn-connection](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-vpn-connection.html) command for each VPN connection associated with the VPN Concentrator.

**To delete a VPN Concentrator attachment using the AWS CLI**
Use the [delete-vpn-concentrator](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-vpn-concentrator.html) command after all VPN connections have been deleted.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
