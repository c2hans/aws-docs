---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_NatGatewayCreateMapping.html
---

# NatGatewayCreateMapping
<a name="API_NatGatewayCreateMapping"></a>

A NAT gateway that Network Firewall creates for a proxy mode firewall in one Availability Zone. You use this in `CreateFirewall` and `AssociateSubnets`.

To create a public NAT gateway, specify `AllocationIds`, and one `PrivateIps` address for each Elastic IP address. To create a private NAT gateway, specify only `PrivateIps`. You must specify at least one of them. Each Elastic IP address and private IP address can appear only once in a request.

The NAT gateway is a resource in your account. To change its IP addresses, use Amazon EC2 NAT gateway actions.

## Contents
<a name="API_NatGatewayCreateMapping_Contents"></a>

 ** SubnetId **   <a name="networkfirewall-Type-NatGatewayCreateMapping-SubnetId"></a>
The ID of the subnet where Network Firewall creates the NAT gateway. The subnet must be in the firewall's VPC and can't be one of the firewall endpoint subnets. Each mapping must be in a different Availability Zone.
Type: String
Required: Yes

 ** AllocationIds **   <a name="networkfirewall-Type-NatGatewayCreateMapping-AllocationIds"></a>
The allocation IDs of the Elastic IP addresses for a public NAT gateway, from 1 to 8. For each allocation ID, specify one address in `PrivateIps`. If you don't specify this, Network Firewall creates a private NAT gateway.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 32 items.
Required: No

 ** PrivateIps **   <a name="networkfirewall-Type-NatGatewayCreateMapping-PrivateIps"></a>
The private IPv4 addresses of the NAT gateway. The addresses must be in the subnet that you specify and can't be the subnet's reserved addresses.
For a public NAT gateway, you must specify exactly one address for each Elastic IP address in `AllocationIds`, even if you specify only one. For a private NAT gateway, specify from 1 to 8 addresses. The first address is the primary address.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 32 items.
Required: No

## See Also
<a name="API_NatGatewayCreateMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/NatGatewayCreateMapping)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/NatGatewayCreateMapping)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/NatGatewayCreateMapping)
