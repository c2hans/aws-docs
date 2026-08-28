---
source_url: https://docs.aws.amazon.com/vpc/latest/tgw/create-prefix-list-reference.html
---

# Create a route table prefix list reference in AWS Transit Gateway
<a name="create-prefix-list-reference"></a>

You can reference a prefix list in your transit gateway route table. A prefix list is a set of one or more CIDR block entries that you define and manage. You can use a prefix list to simplify the management of the IP addresses that you reference in your resources to route network traffic. For example, if you frequently specify the same destination CIDRs across multiple transit gateway route tables, you can manage those CIDRs in a single prefix list, instead of repeatedly referencing the same CIDRs in each route table. If you need to remove a destination CIDR block, you can remove its entry from the prefix list instead of removing the route from every affected route table.

When you create a prefix list reference in your transit gateway route table, each entry in the prefix list is represented as a route in your transit gateway route table.

For more information about prefix lists, see [Prefix lists](https://docs.aws.amazon.com/vpc/latest/userguide/managed-prefix-lists.html) in the *Amazon VPC User Guide*.

**To create a prefix list reference using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Transit Gateway Route Tables**.

1. Select the transit gateway route table.

1. Choose **Actions**, **Create prefix list reference**.

1. For **Prefix list ID**, choose the ID of the prefix list.

1.  For **Type**, choose if traffic to this prefix list should be allowed (**Active**) or dropped (**Blackhole**).

1. For **Transit gateway attachment ID**, choose the ID of the attachment to which to route traffic.

1. Choose **Create prefix list reference**.

**To create a prefix list reference using the AWS CLI**
Use the [create-transit-gateway-prefix-list-reference](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-transit-gateway-prefix-list-reference.html) command.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
