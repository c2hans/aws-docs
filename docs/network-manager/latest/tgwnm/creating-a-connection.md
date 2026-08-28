---
source_url: https://docs.aws.amazon.com/network-manager/latest/tgwnm/creating-a-connection.html
---

# Create a connection using AWS Network Manager
<a name="creating-a-connection"></a>

Create a connection between two existing devices in your global network.

**To create a connection**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global Networks**.

1. On the **Global networks** page, choose the global network ID.

1. In the navigation pane, choose **Devices**, and choose the ID of the device.

1. Choose **Connections**, and then choose **Create connection**.

1. For **Name** and **Description**, enter a name and description for the connection.

1. (Optional) For **Link**, choose a link to associate with the first device in the connection.

1. For **Connected device**, choose the ID of the second device in the connection.

1. (Optional) For **Connected link**, choose a link to associate with the second device in the connection.

1. Choose **Create connection**.

**To create a connection using the AWS CLI**
Use the [create-connection](https://docs.aws.amazon.com/cli/latest/reference/networkmanager/create-connection.html) command.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
