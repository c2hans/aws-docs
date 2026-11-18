---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_CoreNetworkEndpointDnsIpItem.html
---

# CoreNetworkEndpointDnsIpItem
<a name="API_route53globalresolver_CoreNetworkEndpointDnsIpItem"></a>

A DNS IP address configuration returned for a core network endpoint. Each item describes an IP address that the endpoint uses to receive DNS queries, along with its DNS label and name, and the scope and AWS Regions in which the address applies.

## Contents
<a name="API_route53globalresolver_CoreNetworkEndpointDnsIpItem_Contents"></a>

 ** dnsLabel **   <a name="Route53GlobalResolver-Type-route53globalresolver_CoreNetworkEndpointDnsIpItem-dnsLabel"></a>
The DNS label associated with the IP address.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: Yes

 ** regionScope **   <a name="Route53GlobalResolver-Type-route53globalresolver_CoreNetworkEndpointDnsIpItem-regionScope"></a>
Indicates whether the IP address applies to all AWS Regions or only to the specific Regions that you identify. When the value is `REGIONAL`, the Regions are listed in the `regions` field.
Type: String
Valid Values: `ALL | REGIONAL`
Required: Yes

 ** dnsName **   <a name="Route53GlobalResolver-Type-route53globalresolver_CoreNetworkEndpointDnsIpItem-dnsName"></a>
The fully qualified DNS name associated with the IP address.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** ipv4Address **   <a name="Route53GlobalResolver-Type-route53globalresolver_CoreNetworkEndpointDnsIpItem-ipv4Address"></a>
The IPv4 address that the core network endpoint uses to receive DNS queries.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 15.
Pattern: `((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}`
Required: No

 ** ipv6Address **   <a name="Route53GlobalResolver-Type-route53globalresolver_CoreNetworkEndpointDnsIpItem-ipv6Address"></a>
The IPv6 address that the core network endpoint uses to receive DNS queries.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 39.
Pattern: `(?:[A-Fa-f0-9]{0,4}:){2,7}[A-Fa-f0-9]{1,4}`
Required: No

 ** regions **   <a name="Route53GlobalResolver-Type-route53globalresolver_CoreNetworkEndpointDnsIpItem-regions"></a>
The AWS Regions in which the IP address applies when the region scope is `REGIONAL`.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 32.
Required: No

## See Also
<a name="API_route53globalresolver_CoreNetworkEndpointDnsIpItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53globalresolver-2022-09-27/CoreNetworkEndpointDnsIpItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53globalresolver-2022-09-27/CoreNetworkEndpointDnsIpItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53globalresolver-2022-09-27/CoreNetworkEndpointDnsIpItem)
