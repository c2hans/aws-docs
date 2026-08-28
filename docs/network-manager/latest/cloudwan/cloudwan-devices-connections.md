---
source_url: https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-devices-connections.html
---

# Create or delete a device connection in an AWS Cloud WAN global network
<a name="cloudwan-devices-connections"></a>

Create or delete a connection between two devices in your Cloud WAN global network.

**To create a connection**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global Networks**.

1. On the **Global networks** page, choose the global network ID.

1. In the navigation pane, choose **Devices**.

1. Choose the **Connections** tab, and then choose **Create connection**.

1. For the **Name** and **Description**, enter a name and optional description for the connection.

1. (Optional) For **Link**, choose a link to associate with the first device in the connection.

1. For **Connected device**, choose the ID of the second device in the connection.

1. (Optional) For **Connected link**, choose a link to associate with the second device in the connection.

1. Choose **Create connection**.

Delete the existing connection between two devices or delete a connection between two devices in your Cloud WAN global network.

**To delete a device connection**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global Networks**.

1. On the **Global networks** page, choose the global network ID.

1. In the navigation pane, choose **Devices**.

1. Choose the **Connections** tab.

1. In the **Connections** section, choose the check box of the connection you want to delete.

1. Choose **Delete**.

1. Choose **Delete** again to confirm you want to delete the connection.

   The connection is deleted immediately.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
