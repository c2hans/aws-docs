---
source_url: https://docs.aws.amazon.com/vpc/latest/tgw/tgw-peering-add-route.html
---

# Add a route to a transit gateway route table using AWS Transit Gateway
<a name="tgw-peering-add-route"></a>

To route traffic between the peered transit gateways, you must add a static route to the transit gateway route table that points to the transit gateway peering attachment. The owner of the accepter transit gateway must also add a static route to their transit gateway's route table.

**To create a static route using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation pane, choose **Transit Gateway Route Tables**.

1. Select the route table for which to create a route.

1. Choose **Actions**, **Create static route**.

1. On the **Create static route** page, enter the CIDR block for which to create the route. For example, specify the CIDR block of a VPC that's attached to the peer transit gateway.

1. Choose the peering attachment for the route.

1. Choose **Create static route**.

**To create a static route using the AWS CLI**
Use the [create-transit-gateway-route](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-transit-gateway-route.html) command.

**Important**
After you create the route, the transit gateway peering attachment must already be associated with the transit gateway route table. For more information, see [Associate a transit gateway route table in AWS Transit Gateway](associate-tgw-route-table.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
