---
source_url: https://docs.aws.amazon.com/network-manager/latest/tgwnm/working-with-route-analyzer.html
---

# Perform a route analysis
<a name="working-with-route-analyzer"></a>

Perform a route analysis of your AWS global network. You can only use Route Analyzer using the AWS Global Networks for Transit Gateways console.

**To analyze your routes**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global Networks**.

1. On the **Global networks** page, choose the global network ID.

1. In the navigation pane, choose **Transit Gateway network**.

1. The **Overview** page opens by default, showing information about your transit gateways.

1. Choose the **Route Analyzer** tab.

1. Under **Source**, do the following:
   + Choose the transit gateway and the transit gateway attachment.
   + For **IP address**, enter a source IPv4 or IPv6 address.

1. Under **Destination**, do the following:
   + Choose the transit gateway and the transit gateway attachment.
   + For **IP address**, enter a target IPv4 or IPv6 address.

1. (Optional) To analyze the return path, ensure that you enable **Include return path in results**. If enabled, you must specify an IP address under **Source**.

1. To specify middlebox appliances in the routing path, choose **Middlebox appliance?**. We store this information for use in future analyses. You can update your middlebox appliances later on as needed.

1. Choose **Run route analysis**.

1. The results are displayed under **Results of route analysis**. If you specified **Middlebox appliance?**, choose **Yes **or **No** for each of the attachments to indicate the location of the appliances and to complete the route analysis.

   You can choose the ID of any of the resources in the path to view more information about the resources.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
