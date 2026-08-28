---
source_url: https://docs.aws.amazon.com/network-manager/latest/tgwnm/deregister-tgw.html
---

# Deregister a transit gateway using AWS Network Manager
<a name="deregister-tgw"></a>

Deregister a transit gateway from a global network using either the Network Manager console or using the CLI. Once deregistered, you can re-register this transit gateway with the same global network or with a different global network.

**To deregister a transit gateway**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global Networks**.

1. On the **Global networks** page, choose the global network ID.

1. In the navigation pane, choose **Transit gateways**.

1. Select your transit gateway, and choose **Deregister**.

**To deregister a transit gateway using the AWS CLI**
Use the [deregister-transit-gateway](https://docs.aws.amazon.com/cli/latest/reference/networkmanager/deregister-transit-gateway.html) command.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
