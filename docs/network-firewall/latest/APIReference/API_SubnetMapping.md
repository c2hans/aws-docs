---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_SubnetMapping.html
---

# SubnetMapping
<a name="API_SubnetMapping"></a>

The ID for a subnet that's used in an association with a firewall. This is used in [CreateFirewall](API_CreateFirewall.md), [AssociateSubnets](API_AssociateSubnets.md), and [CreateVpcEndpointAssociation](API_CreateVpcEndpointAssociation.md). AWS Network Firewall creates an instance of the associated firewall in each subnet that you specify, to filter traffic in the subnet's Availability Zone.

## Contents
<a name="API_SubnetMapping_Contents"></a>

 ** SubnetId **   <a name="networkfirewall-Type-SubnetMapping-SubnetId"></a>
The unique identifier for the subnet.
Type: String
Required: Yes

 ** IPAddressType **   <a name="networkfirewall-Type-SubnetMapping-IPAddressType"></a>
The subnet's IP address type. You can't change the IP address type after you create the subnet.
Type: String
Valid Values: `DUALSTACK | IPV4 | IPV6`
Required: No

## See Also
<a name="API_SubnetMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/SubnetMapping)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/SubnetMapping)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/SubnetMapping)
