---
source_url: https://docs.aws.amazon.com/vpn/latest/s2svpn/view-elc-status.html
---

# Verify if AWS Site-to-Site VPN tunnel endpoint lifecycle control is enabled
<a name="view-elc-status"></a>

You can verify whether tunnel endpoint lifecycle control is enabled on an existing VPN tunnel by using the AWS Management Console or CLI.
+ If tunnel endpoint lifecycle control is disabled, and you want to enable it see [Enable tunnel endpoint lifecycle control](enable-elc.md).
+ If tunnel endpoint lifecycle control is enabled, and you want to disable it, see [Turn tunnel endpoint lifecycle control off](turn-elc-off.md).

**To verify if tunnel endpoint lifecycle control is enabled using the AWS Management Console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the left-side navigation pane, choose **Site-to-Site VPN Connections**.

1. Select the appropriate connection under **VPN connections**.

1. Select the **Tunnel details** tab.

1. In the tunnel details, look for **Tunnel Endpoint Lifecycle Control**, which will report whether the feature is **Enabled** or **Disabled**.

**To verify if tunnel endpoint lifecycle control is enabled using the AWS CLI**
Use the [describe-vpn-connections](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-vpn-connections.html) command to verify if tunnel endpoint lifecycle control is enabled.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
