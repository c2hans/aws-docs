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
