---
source_url: https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-devices-connect-peer.html
---

# Associate or disassociate a Connect peer link in an AWS Cloud WAN global network
<a name="cloudwan-devices-connect-peer"></a>

Associate or disassociate a Connect peer device link association in your Cloud WAN global network.

You can only associate one link with a Connect peer. If a link is already associated with a Connect peer, and you want to use that link with another Connect peer, you must first disassociate the link the Connect peer it's associated with.

**To create a Connect peer association**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global Networks**.

1. On the **Global networks** page, choose the global network ID.

1. In the navigation pane, choose **Devices**.

1. Choose the link for the device **ID** that you want to create an on-premises association for.

1. Choose the **Connect peer** tab.

1. Choose **Associate**.

1. Choose the on-premises **Connect peer**.

1. (Optional) Choose the **Link** used for the connection.

1. Choose **Create Connect peer association**.

   The link is available to use immediately.

**To disassociate a Connect peer association**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global Networks**.

1. On the **Global networks** page, choose the global network ID.

1. In the navigation pane, choose **Devices**.

1. Choose the device **ID** link.

1. Choose the **Connect peer** tab.

1. Choose the check box for the Connect peer that you want to disassociate.

1. Choose **Disassociate**.

   Disassociation occurs immediately.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
