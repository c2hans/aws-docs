---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-connections-disassociate.html
---

# Terminate an AWS Client VPN client connection
<a name="cvpn-working-connections-disassociate"></a>

You can terminate a Client VPN client connection using the Amazon VPC Console or the AWS CLI.

**To terminate a Client VPN client connection (console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints**.

1. Select the Client VPN endpoint to which the client is connected, and choose **Connections**.

1. Select the connection to terminate, choose **Terminate Connection**, and then choose **Terminate Connection** again to confirm the termination.

**To terminate a Client VPN client connection (AWS CLI)**
Use the [terminate-client-vpn-connections](https://docs.aws.amazon.com/cli/latest/reference/ec2/terminate-client-vpn-connections.html) command.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
