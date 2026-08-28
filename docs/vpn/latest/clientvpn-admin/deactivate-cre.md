---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/deactivate-cre.html
---

# Deactivate Client Route Enforcement from an AWS Client VPN endpoint
<a name="deactivate-cre"></a>

You can deactivate Client Route Enforcement on Client VPN endpoints using either the console or the AWS CLI.

**To deactivate Client Route Enforcement using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN endpoints**.

1. Choose the Client VPN endpoint that you want to modify, choose **Actions**, and then choose **Modify Client VPN endpoint**.

1. Scroll down the page to the **Other parameters** section.

1. Turn off **Client Route Enforcement**.

1. Choose **Modify Client VPN endpoint**.

**To deactivate Client Route Enforcement using the AWS CLI**
+ Use the [modify-client-vpn-endpoint](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-client-vpn-endpoint.html) command.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
