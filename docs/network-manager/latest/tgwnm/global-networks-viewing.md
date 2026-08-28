---
source_url: https://docs.aws.amazon.com/network-manager/latest/tgwnm/global-networks-viewing.html
---

# View a global network using AWS Global Networks for Transit Gateways
<a name="global-networks-viewing"></a>

View the details of your global network and information about the network objects in your global network.

**To view your global network information**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global Networks**.

1. On the **Global networks** page, choose the global network ID.

1. The **Overview** page displays an inventory of the objects in both your core network and transit gateway network. To view details about the global network resource (such as its ARN), choose **Details**. For more information about the other pages on the dashboard, see [Access transit gateway network dashboards using AWS Network Manager](nm-monitoring-console.md).

**To view global network details using the AWS CLI**
Use the [describe-global-networks](https://docs.aws.amazon.com/cli/latest/reference/networkmanager/describe-global-networks.html) command.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
