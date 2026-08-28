---
source_url: https://docs.aws.amazon.com/vpc/latest/tgw/add-source-multicast-group.html
---

# Register sources with a multicast group in AWS Transit Gateway
<a name="add-source-multicast-group"></a>

**Note**
This procedure is only required when you have set the **Static sources support** attribute to **enable**.

Use the following procedure to register sources with a multicast group. The source is the network interface that sends multicast traffic.

You need the following information before you add a source:
+ The ID of the multicast domain
+ The IDs of the sources' network interfaces
+ The multicast group IP address

**To register sources using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation pane, choose **Transit Gateway Multicast**.

1. Select the multicast domain, and then choose **Actions**, **Add group sources**.

1. For **Group IP address**, enter either the IPv4 CIDR block or IPv6 CIDR block to assign to the multicast domain.

1. Under **Choose network interfaces**, select the multicast senders' network interfaces.

1. Choose **Add sources**.

**To register sources using the AWS CLI**
Use the [register-transit-gateway-multicast-group-sources](https://docs.aws.amazon.com/cli/latest/reference/ec2/register-transit-gateway-multicast-group-sources.html) command.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
