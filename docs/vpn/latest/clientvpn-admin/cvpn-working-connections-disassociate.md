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
