---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_IpAddressUpdate.html
---

# IpAddressUpdate
<a name="API_route53resolver_IpAddressUpdate"></a>

In an [UpdateResolverEndpoint](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_UpdateResolverEndpoint.html) request, information about an IP address to update.

## Contents
<a name="API_route53resolver_IpAddressUpdate_Contents"></a>

 ** Ip **   <a name="Route53Resolver-Type-route53resolver_IpAddressUpdate-Ip"></a>
The new IPv4 address.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 36.
Required: No

 ** IpId **   <a name="Route53Resolver-Type-route53resolver_IpAddressUpdate-IpId"></a>
 *Only when removing an IP address from a Resolver endpoint*: The ID of the IP address that you want to remove. To get this ID, use [GetResolverEndpoint](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetResolverEndpoint.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** Ipv6 **   <a name="Route53Resolver-Type-route53resolver_IpAddressUpdate-Ipv6"></a>
 The new IPv6 address.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 39.
Required: No

 ** SubnetId **   <a name="Route53Resolver-Type-route53resolver_IpAddressUpdate-SubnetId"></a>
The ID of the subnet that includes the IP address that you want to update. To get this ID, use [GetResolverEndpoint](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetResolverEndpoint.html).
We recommend using [VPC Resolver on AWS Outposts](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/outpost-resolver-getting-started.html) to create endpoints on AWS Outposts Racks.
Outposts subnets with [Local Network Interface (LNI)](https://docs.aws.amazon.com/outposts/latest/server-userguide/local-network-interface.html) enabled are not compatible with Route 53 Resolver endpoints. If you enable LNI on a subnet that contains Route 53 Resolver endpoint elastic network interfaces (ENIs), those ENIs will stop functioning. For more information, see [Subnet compatibility for Resolver endpoints](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/best-practices-resolver.html#best-practices-resolver-subnet-compatibility) in the *Amazon Route 53 Developer Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: No

## See Also
<a name="API_route53resolver_IpAddressUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/IpAddressUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/IpAddressUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/IpAddressUpdate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
