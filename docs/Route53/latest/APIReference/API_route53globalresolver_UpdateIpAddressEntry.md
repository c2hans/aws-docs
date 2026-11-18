---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_UpdateIpAddressEntry.html
---

# UpdateIpAddressEntry
<a name="API_route53globalresolver_UpdateIpAddressEntry"></a>

A single change to apply to the DNS IP addresses of a core network endpoint when you update it. Each entry specifies the operation to perform and the IP address details that the operation acts on.

## Contents
<a name="API_route53globalresolver_UpdateIpAddressEntry_Contents"></a>

 ** operation **   <a name="Route53GlobalResolver-Type-route53globalresolver_UpdateIpAddressEntry-operation"></a>
The operation to perform on the IP address. Valid values are `ADD`, `REMOVE`, and `UPDATE`.
Type: String
Valid Values: `ADD | REMOVE | UPDATE`
Required: Yes

 ** dnsLabel **   <a name="Route53GlobalResolver-Type-route53globalresolver_UpdateIpAddressEntry-dnsLabel"></a>
The DNS label associated with the IP address.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: No

 ** ipv4Address **   <a name="Route53GlobalResolver-Type-route53globalresolver_UpdateIpAddressEntry-ipv4Address"></a>
The IPv4 address that the operation acts on.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 15.
Pattern: `((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}`
Required: No

 ** ipv6Address **   <a name="Route53GlobalResolver-Type-route53globalresolver_UpdateIpAddressEntry-ipv6Address"></a>
The IPv6 address that the operation acts on.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 39.
Pattern: `(?:[A-Fa-f0-9]{0,4}:){2,7}[A-Fa-f0-9]{1,4}`
Required: No

 ** regions **   <a name="Route53GlobalResolver-Type-route53globalresolver_UpdateIpAddressEntry-regions"></a>
The AWS Regions in which the IP address applies when the region scope is `REGIONAL`.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 32.
Required: No

 ** regionScope **   <a name="Route53GlobalResolver-Type-route53globalresolver_UpdateIpAddressEntry-regionScope"></a>
Indicates whether the IP address applies to all AWS Regions or only to the specific Regions that you identify. When the value is `REGIONAL`, the Regions are listed in the `regions` field.
Type: String
Valid Values: `ALL | REGIONAL`
Required: No

## See Also
<a name="API_route53globalresolver_UpdateIpAddressEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53globalresolver-2022-09-27/UpdateIpAddressEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53globalresolver-2022-09-27/UpdateIpAddressEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53globalresolver-2022-09-27/UpdateIpAddressEntry)
