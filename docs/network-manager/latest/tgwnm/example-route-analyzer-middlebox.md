---
source_url: https://docs.aws.amazon.com/network-manager/latest/tgwnm/example-route-analyzer-middlebox.html
---

# Example: Route analysis with a middlebox configuration
<a name="example-route-analyzer-middlebox"></a>

If you've configured a VPC to act as a middlebox appliance for inspecting traffic that flows to other parts of your network, you can indicate the location of the appliance in the route analysis. In the following example, the transit gateway has two VPC attachments and a VPN attachment. VPC A runs a firewall appliance (middlebox) that inspects the traffic that flows between the VPN connection and VPC B.

![Middlebox appliance](http://docs.aws.amazon.com/network-manager/latest/tgwnm/images/route-analyzer-middlebox.png)

 In the Route Analyzer, you can specify the location of the middlebox appliance as follows:

1. Under **Source**, specify the transit gateway and the VPN attachment. Specify an IP address from the range of the on-premises network, for example, `10.0.0.7`.

1. Under **Destination**, specify the transit gateway and the attachment for VPC B. Specify an IP address from the CIDR block of VPC B, for example, `172.31.0.8`.

1. For **Middlebox appliance?**, choose **Include**.

1. Run the route analysis.

1. For the **Middlebox appliance?** sections for the transit gateway attachment for VPC A, choose **Yes**.

   You can choose the ID of any resource in the path to view more information about that resource.

![Route analyzer results](http://docs.aws.amazon.com/network-manager/latest/tgwnm/images/nm-route-analyzer-middlebox.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
