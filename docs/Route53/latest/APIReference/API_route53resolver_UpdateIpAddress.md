---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_UpdateIpAddress.html
---

# UpdateIpAddress
<a name="API_route53resolver_UpdateIpAddress"></a>

 Provides information about the IP address type in response to [UpdateResolverEndpoint](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_UpdateResolverEndpoint.html).

## Contents
<a name="API_route53resolver_UpdateIpAddress_Contents"></a>

 ** IpId **   <a name="Route53Resolver-Type-route53resolver_UpdateIpAddress-IpId"></a>
 The ID of the IP address, specified by the `ResolverEndpointId`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** Ipv6 **   <a name="Route53Resolver-Type-route53resolver_UpdateIpAddress-Ipv6"></a>
 The IPv6 address that you want to use for DNS queries.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 39.
Required: Yes

## See Also
<a name="API_route53resolver_UpdateIpAddress_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/UpdateIpAddress)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/UpdateIpAddress)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/UpdateIpAddress)
