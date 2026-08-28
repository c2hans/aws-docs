---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-connections-view.html
---

# View AWS Client VPN client connections
<a name="cvpn-working-connections-view"></a>

You can view the active Client VPN connections using either the Amazon VPC Console or the AWS CLI.

**To view Client VPN client connections (console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints**.

1. Select the Client VPN endpoint for which to view client connections.

1. Choose the **Connections** tab. The **Connections** tab lists all active and terminated client connections.

**To view Client VPN client connections (AWS CLI)**
Use the [describe-client-vpn-connections](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-client-vpn-connections.html) command.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
