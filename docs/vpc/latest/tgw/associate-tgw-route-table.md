---
source_url: https://docs.aws.amazon.com/vpc/latest/tgw/associate-tgw-route-table.html
---

# Associate a transit gateway route table in AWS Transit Gateway
<a name="associate-tgw-route-table"></a>

You can associate a transit gateway route table with a transit gateway attachment.

**To associate a transit gateway route table using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation pane, choose **Transit Gateway Route Tables**.

1. Select the route table.

1. In the lower part of the page, choose the **Associations** tab.

1. Choose **Create association**.

1. Choose the attachment to associate and then choose **Create association**.

**To associate a transit gateway route table using the AWS CLI**
Use the [associate-transit-gateway-route-table](https://docs.aws.amazon.com/cli/latest/reference/ec2/associate-transit-gateway-route-table.html) command.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
