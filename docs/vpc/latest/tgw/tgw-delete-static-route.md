---
source_url: https://docs.aws.amazon.com/vpc/latest/tgw/tgw-delete-static-route.html
---

# Delete a static route in AWS Transit Gateway
<a name="tgw-delete-static-route"></a>

Delete static routes from a transit gateway route table.

**To delete a static route using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation pane, choose **Transit Gateway Route Tables**.

1. Select the route table for which to delete the route, and choose **Routes**.

1. Choose the route to delete.

1. Choose **Delete static route**.

1. In the confirmation box, choose **Delete static route**.

**To delete a static route using the AWS CLI**
Use the [delete-transit-gateway-route](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-transit-gateway-route.html) command.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
