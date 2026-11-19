---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_VpcEndpoint.html
---

# VpcEndpoint

The VPC and subnets for the endpoints of a proxy mode firewall. You use this in `CreateFirewall`. Network Firewall creates the firewall endpoints and the firewall's NAT gateways in this VPC.

This differs from `VpcEndpointAssociation`, which defines additional endpoints for a firewall in other VPCs.

## Contents
<a name="API_VpcEndpoint_Contents"></a>

 ** SubnetMappings **   <a name="networkfirewall-Type-VpcEndpoint-SubnetMappings"></a>
The subnets where Network Firewall creates the firewall endpoints of a proxy mode firewall. Specify one subnet for each Availability Zone, and a NAT gateway mapping in each of those Availability Zones.
Type: Array of [SubnetMapping](API_SubnetMapping.md) objects
Required: Yes

 ** VpcId **   <a name="networkfirewall-Type-VpcEndpoint-VpcId"></a>
The ID of the VPC where Network Firewall creates the endpoints and NAT gateways of a proxy mode firewall.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^vpc-[0-9a-f]+$`
Required: Yes

## See Also
<a name="API_VpcEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/VpcEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/VpcEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/VpcEndpoint)
