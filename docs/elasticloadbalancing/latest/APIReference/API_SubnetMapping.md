---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_SubnetMapping.html
---

# SubnetMapping
<a name="API_SubnetMapping"></a>

Information about a subnet mapping.

## Contents
<a name="API_SubnetMapping_Contents"></a>

 ** AllocationId **
[Network Load Balancers] The allocation ID of the Elastic IP address for an internet-facing load balancer.
Type: String
Required: No

 ** IPv6Address **
[Network Load Balancers] The IPv6 address.
Type: String
Required: No

 ** PrivateIPv4Address **
[Network Load Balancers] The private IPv4 address for an internal load balancer.
Type: String
Required: No

 ** SourceNatIpv6Prefix **
[Network Load Balancers with UDP listeners] The IPv6 prefix to use for source NAT. Specify an IPv6 prefix (/80 netmask) from the subnet CIDR block or `auto_assigned` to use an IPv6 prefix selected at random from the subnet CIDR block.
Type: String
Required: No

 ** SubnetId **
The ID of the subnet.
Type: String
Required: No

## See Also
<a name="API_SubnetMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/SubnetMapping)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/SubnetMapping)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/SubnetMapping)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Elastic Load Balancing. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticloadbalancing` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
