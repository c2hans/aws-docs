---
source_url: https://docs.aws.amazon.com/network-manager/latest/tgwnm/deleting-a-connection.html
---

# Delete a connection using AWS Network Manager
<a name="deleting-a-connection"></a>

If you no longer need a connection, you can delete it.

**To delete a connection**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global Networks**.

1. On the **Global networks** page, choose the global network ID.

1. In the navigation pane, choose **Devices**, and select the device.

1. Choose **Connections**, and select the connection.

1. Choose **Delete**.

1. When prompted for confirmation, choose **Delete**.

**To delete a connection using the AWS CLI**
Use the [delete-connection](https://docs.aws.amazon.com/cli/latest/reference/networkmanager/delete-connection.html) command.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
