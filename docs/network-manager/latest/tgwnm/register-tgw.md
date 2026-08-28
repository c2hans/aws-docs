---
source_url: https://docs.aws.amazon.com/network-manager/latest/tgwnm/register-tgw.html
---

# Register a transit gateway using AWS Network Manager
<a name="register-tgw"></a>

Register a transit gateway created using Amazon Virtual Private Cloud with your AWS global network using either the Network Manager console or using the CLI. You cannot register a transit gateway with more than one global network.

**To register a transit gateway**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global Networks**.

1. On the **Global networks** page, choose the global network ID.

1. In the navigation pane, choose **Transit gateways**., and then choose **Register transit gateway**.

1. (Optional) If your account is enabled for multi-account access, from the **Select account** dropdown list choose the account you want to register transit gateways from.

   The **Select transit gateway to register** section populates with that account's transit gateways.

1. Choose one or more transit gateways, and then choose **Register transit gateway**.

**To register a transit gateway using the AWS CLI**
Use the [register-transit-gateway](https://docs.aws.amazon.com/cli/latest/reference/networkmanager/register-transit-gateway.html) command.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
