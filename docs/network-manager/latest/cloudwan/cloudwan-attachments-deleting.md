---
source_url: https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-attachments-deleting.html
---

# Delete an AWS Cloud WAN core network attachment
<a name="cloudwan-attachments-deleting"></a>

You can delete any attachment from your core network. Deleted attachments can't be recovered. This section including the steps to delete an attachment using the AWS Cloud WAN console or by using the command line or API.

**To delete an attachment using the console**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global networks**.

1. On the **Global networks** page, choose the global network ID.

1. Under **Core network** in the navigation pane, choose **Attachments**.

1. Select the check box for the attachment that you want to delete.

1. Choose **Delete**.

1. Confirm that you want to delete the attachment by choosing **Delete** again.

   The attachment is removed from the **Attachments** page.

Use the command line or API to delete any of your core network attachments.

**To delete an attachment using the command line or API**
+ For a Connect, transit gateway route table, VPC, or Site-to-Site VPN attachment, see [delete-attachment](https://docs.aws.amazon.com/cli/latest/reference/networkmanager/delete-attachment.html).
+ For a Connect peer attachment, see [delete-transit-gateway-connect-peer](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-transit-gateway-connect-peer.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
