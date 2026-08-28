---
source_url: https://docs.aws.amazon.com/vpc/latest/tgw/tgw-replace-static-route.html
---

# Replace a static route in AWS Transit Gateway
<a name="tgw-replace-static-route"></a>

Replace a static route in a transit gateway route table with a different static route.

**To replace a static route using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation pane, choose **Transit Gateway Route Tables**.

1. Choose the route that you want to replace in the route table.

1. In the details section, choose the **Routes** tab.

1. Choose **Actions**, **Replace static route**.

1. For the **Type**, choose either **Active** or **Blackhole**.

1. From the **Choose attachment** drop-down, choose the transit gateway that will replace the current one in the route table.

1. Choose **Replace static route**.

**To replace a static route using the AWS CLI**
Use the [replace-transit-gateway-route](https://docs.aws.amazon.com/cli/latest/reference/ec2/replace-transit-gateway-route.html) command.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
