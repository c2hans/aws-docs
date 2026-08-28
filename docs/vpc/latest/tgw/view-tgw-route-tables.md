---
source_url: https://docs.aws.amazon.com/vpc/latest/tgw/view-tgw-route-tables.html
---

# View transit gateway route tables using AWS Transit Gateway
<a name="view-tgw-route-tables"></a>

**To view your transit gateway route tables using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation pane, choose **Transit Gateway Route Tables**.

1. (Optional) To find a specific route table or set of tables, enter all or part of the name, keyword, or attribute in the filter field.

1. Select the checkbox for a route table, or choose its ID, to display information about its associations, propagations, routes, and tags.

**To view your transit gateway route tables using the AWS CLI**
Use the [describe-transit-gateway-route-tables](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-transit-gateway-route-tables.html) command.

**To view the routes for a transit gateway route table using the AWS CLI**
Use the [search-transit-gateway-routes](https://docs.aws.amazon.com/cli/latest/reference/ec2/search-transit-gateway-routes.html) command.

**To view the route propagations for a transit gateway route table using the AWS CLI**
Use the [get-transit-gateway-route-table-propagations](https://docs.aws.amazon.com/cli/latest/reference/ec2/get-transit-gateway-route-table-propagations.html) command.

**To view the associations for a transit gateway route table using the AWS CLI**
Use the [get-transit-gateway-route-table-associations](https://docs.aws.amazon.com/cli/latest/reference/ec2/get-transit-gateway-route-table-associations.html) command.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
