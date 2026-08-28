---
source_url: https://docs.aws.amazon.com/vpc/latest/tgw/disable-tgw-route-propagation.html
---

# Disable route propagation in AWS Transit Gateway
<a name="disable-tgw-route-propagation"></a>

Remove a propagated route from a route table attachment.

**To disable route propagation using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation pane, choose **Transit Gateway Route Tables**.

1. Select the route table to delete the propagation from.

1. On the lower part of the page, choose the **Propagations** tab.

1. Select the attachment and then choose **Delete propagation**.

1. When prompted for confirmation, choose **Delete propagation**.

**To disable route propagation using the AWS CLI**
Use the [disable-transit-gateway-route-table-propagation](https://docs.aws.amazon.com/cli/latest/reference/ec2/disable-transit-gateway-route-table-propagation.html) command.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
