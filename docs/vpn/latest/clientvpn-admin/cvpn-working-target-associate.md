---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-target-associate.html
---

# Associate a target network with an AWS Client VPN endpoint
<a name="cvpn-working-target-associate"></a>

You can associate one or more target networks (subnets) with a Client VPN endpoint using either the Amazon VPC Console or the AWS CLI. Before you associate a target network with a Client VPN endpoint, familiarize yourself with the requirements. See [Requirements for creating a target network](cvpn-working-target.md#cvpn-create-target-reqs).

**To associate a target network with a Client VPN endpoint (console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints**.

1. Select the Client VPN endpoint with which to associate the target network, choose **Target network associations**, and then choose **Associate target network**.

1. For **VPC**, choose the VPC in which the subnet is located. If you specified a VPC when you created the Client VPN endpoint or if you have previous subnet associations, it must be the same VPC.

1. For **Choose a subnet to associate**, choose the subnet to associate with the Client VPN endpoint.

1. Choose **Associate target network**.

**To associate a target network with a Client VPN endpoint (AWS CLI)**
Use the [associate-client-vpn-target-network](https://docs.aws.amazon.com/cli/latest/reference/ec2/associate-client-vpn-target-network.html) command.
