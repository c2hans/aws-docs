---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_IpAddressRequest.html
---

# IpAddressRequest
<a name="API_route53resolver_IpAddressRequest"></a>

In a [CreateResolverEndpoint](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_CreateResolverEndpoint.html) request, the IP address that DNS queries originate from (for outbound endpoints) or that you forward DNS queries to (for inbound endpoints). `IpAddressRequest` also includes the ID of the subnet that contains the IP address.

## Contents
<a name="API_route53resolver_IpAddressRequest_Contents"></a>

 ** SubnetId **   <a name="Route53Resolver-Type-route53resolver_IpAddressRequest-SubnetId"></a>
The ID of the subnet that contains the IP address.
We recommend using [VPC Resolver on AWS Outposts](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/outpost-resolver-getting-started.html) to create endpoints on AWS Outposts Racks.
Outposts subnets with [Local Network Interface (LNI)](https://docs.aws.amazon.com/outposts/latest/server-userguide/local-network-interface.html) enabled are not compatible with Route 53 Resolver endpoints. If you enable LNI on a subnet that contains Route 53 Resolver endpoint elastic network interfaces (ENIs), those ENIs will stop functioning. For more information, see [Subnet compatibility for Resolver endpoints](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/best-practices-resolver.html#best-practices-resolver-subnet-compatibility) in the *Amazon Route 53 Developer Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: Yes

 ** Ip **   <a name="Route53Resolver-Type-route53resolver_IpAddressRequest-Ip"></a>
The IPv4 address that you want to use for DNS queries.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 36.
Required: No

 ** Ipv6 **   <a name="Route53Resolver-Type-route53resolver_IpAddressRequest-Ipv6"></a>
 The IPv6 address that you want to use for DNS queries.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 39.
Required: No

## See Also
<a name="API_route53resolver_IpAddressRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/IpAddressRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/IpAddressRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/IpAddressRequest)
