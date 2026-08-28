---
source_url: https://docs.aws.amazon.com/vpc/latest/tgw/create-tgw-route-table.html
---

# Create a transit gateway route table in AWS Transit Gateway
<a name="create-tgw-route-table"></a>

**To create a transit gateway route table using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation pane, choose **Transit Gateway Route Tables**.

1. Choose **Create transit gateway route table**.

1. (Optional) For **Name tag**, type a name for the transit gateway route table. This creates a tag with the tag key "Name", where the tag value is the name that you specify.

1. For **Transit gateway ID**, select the transit gateway for the route table.

1. Choose **Create transit gateway route table**.

**To create a transit gateway route table using the AWS CLI**
Use the [create-transit-gateway-route-table](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-transit-gateway-route-table.html) command.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
