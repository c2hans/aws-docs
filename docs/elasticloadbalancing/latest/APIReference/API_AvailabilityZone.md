---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_AvailabilityZone.html
---

# AvailabilityZone
<a name="API_AvailabilityZone"></a>

Information about an Availability Zone.

## Contents
<a name="API_AvailabilityZone_Contents"></a>

 ** LoadBalancerAddresses.member.N **
[Network Load Balancers] If you need static IP addresses for your load balancer, you can specify one Elastic IP address per Availability Zone when you create an internal-facing load balancer. For internal load balancers, you can specify a private IP address from the IPv4 range of the subnet.
Type: Array of [LoadBalancerAddress](API_LoadBalancerAddress.md) objects
Required: No

 ** OutpostId **
[Application Load Balancers on Outposts] The ID of the Outpost.
Type: String
Required: No

 ** SourceNatIpv6Prefixes.member.N **
[Network Load Balancers with UDP listeners] The IPv6 prefixes to use for source NAT. For each subnet, specify an IPv6 prefix (/80 netmask) from the subnet CIDR block or `auto_assigned` to use an IPv6 prefix selected at random from the subnet CIDR block.
Type: Array of strings
Required: No

 ** SubnetId **
The ID of the subnet. You can specify one subnet per Availability Zone.
Type: String
Required: No

 ** ZoneName **
The name of the Availability Zone.
Type: String
Required: No

## See Also
<a name="API_AvailabilityZone_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/AvailabilityZone)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/AvailabilityZone)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/AvailabilityZone)
