---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-target-apply.html
---

# Apply a security group to a target network in AWS Client VPN
<a name="cvpn-working-target-apply"></a>

When you create a Client VPN endpoint, you can specify the security groups to apply to the target network. When you associate the first target network with a Client VPN endpoint, we automatically apply the default security group of the VPC in which the associated subnet is located. For more information, see [Security groups](client-authorization.md#security-groups).

You can change the security groups for the Client VPN endpoint. The security group rules that you require depend on the kind of VPN access you want to configure. For more information, see [Scenarios and examples for Client VPN](how-it-works.md#scenario).

**To apply a security group to a target network (console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints**.

1. Select the Client VPN endpoint to which to apply the security groups.

1. Choose **Security Groups**, and then choose **Apply Security Groups**.

1. Select the appropriate security group(s) from **Security group IDs**.

1. Choose **Apply Security Groups**.

**To apply a security group to a target network (AWS CLI)**
Use the [apply-security-groups-to-client-vpn-target-network](https://docs.aws.amazon.com/cli/latest/reference/ec2/apply-security-groups-to-client-vpn-target-network.html) command.
