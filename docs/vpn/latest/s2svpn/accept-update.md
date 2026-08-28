---
source_url: https://docs.aws.amazon.com/vpn/latest/s2svpn/accept-update.html
---

# Accept an AWS Site-to-Site VPN tunnel maintenance update
<a name="accept-update"></a>

When a maintenance update is available, you can accept it using the AWS Management Console or CLI. You can choose to accept the Site-to-Site VPN tunnel maintenance update at a time that's convenient for you. Once you accept the maintenance update it will be deployed.

**Note**
If you don't accept the maintenance update, AWS will automatically deploy it during a regular maintenance update cycle.

**To accept an available maintenance update using the AWS Management Console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the left-side navigation pane, choose **Site-to-Site VPN Connections**.

1. Select the appropriate connection under **VPN connections**.

1. Choose **Actions**, then **Replace VPN Tunnel**.

1. Select the specific tunnel that you want to replace by choosing the appropriate **VPN tunnel outside IP address**.

1. Choose **Replace**.

**To accept an available maintenance update using the AWS CLI**
Use the [replace-vpn-tunnel](https://docs.aws.amazon.com/cli/latest/reference/ec2/replace-vpn-tunnel.html) command to accept an available maintenance update.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
