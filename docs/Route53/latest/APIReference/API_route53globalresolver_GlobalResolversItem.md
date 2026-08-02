---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_GlobalResolversItem.html
---

# GlobalResolversItem
<a name="API_route53globalresolver_GlobalResolversItem"></a>

Summary information about a global resolver.

## Contents
<a name="API_route53globalresolver_GlobalResolversItem_Contents"></a>

 ** arn **   <a name="Route53GlobalResolver-Type-route53globalresolver_GlobalResolversItem-arn"></a>
The Amazon Resource Name (ARN) of the global resolver.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[-.a-z0-9]{1,63}:[-.a-z0-9]{1,63}:[-.a-z0-9]{0,63}:[-.a-z0-9]{0,63}:[^/].{0,1023}`
Required: Yes

 ** clientToken **   <a name="Route53GlobalResolver-Type-route53globalresolver_GlobalResolversItem-clientToken"></a>
The unique string that identifies the request and ensures idempotency.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** createdAt **   <a name="Route53GlobalResolver-Type-route53globalresolver_GlobalResolversItem-createdAt"></a>
The date and time when the global resolver was created.
Type: Timestamp
Required: Yes

 ** dnsName **   <a name="Route53GlobalResolver-Type-route53globalresolver_GlobalResolversItem-dnsName"></a>
The DNS name of the global resolver.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** id **   <a name="Route53GlobalResolver-Type-route53globalresolver_GlobalResolversItem-id"></a>
The unique identifier of the global resolver.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`
Required: Yes

 ** ipv4Addresses **   <a name="Route53GlobalResolver-Type-route53globalresolver_GlobalResolversItem-ipv4Addresses"></a>
The IPv4 addresses assigned to the global resolver.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 15.
Pattern: `((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}`
Required: Yes

 ** name **   <a name="Route53GlobalResolver-Type-route53globalresolver_GlobalResolversItem-name"></a>
The name of the global resolver.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9-_/' ']+)`
Required: Yes

 ** regions **   <a name="Route53GlobalResolver-Type-route53globalresolver_GlobalResolversItem-regions"></a>
The AWS Regions where the global resolver is deployed.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 32.
Required: Yes

 ** status **   <a name="Route53GlobalResolver-Type-route53globalresolver_GlobalResolversItem-status"></a>
The current status of the global resolver.
Type: String
Valid Values: `CREATING | OPERATIONAL | UPDATING | DELETING`
Required: Yes

 ** updatedAt **   <a name="Route53GlobalResolver-Type-route53globalresolver_GlobalResolversItem-updatedAt"></a>
The date and time when the global resolver was last updated.
Type: Timestamp
Required: Yes

 ** description **   <a name="Route53GlobalResolver-Type-route53globalresolver_GlobalResolversItem-description"></a>
A description of the global resolver.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** ipAddressType **   <a name="Route53GlobalResolver-Type-route53globalresolver_GlobalResolversItem-ipAddressType"></a>
The IP address type configured for the global resolver.
Type: String
Valid Values: `IPV4 | DUAL_STACK`
Required: No

 ** ipv6Addresses **   <a name="Route53GlobalResolver-Type-route53globalresolver_GlobalResolversItem-ipv6Addresses"></a>
The IPv6 addresses assigned to the global resolver. This field is only populated when ipAddressType is DUAL\_STACK.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 39.
Pattern: `(?:[A-Fa-f0-9]{0,4}:){2,7}[A-Fa-f0-9]{1,4}`
Required: No

 ** observabilityRegion **   <a name="Route53GlobalResolver-Type-route53globalresolver_GlobalResolversItem-observabilityRegion"></a>
The AWS Region where observability data is collected for the global resolver.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32.
Required: No

## See Also
<a name="API_route53globalresolver_GlobalResolversItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53globalresolver-2022-09-27/GlobalResolversItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53globalresolver-2022-09-27/GlobalResolversItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53globalresolver-2022-09-27/GlobalResolversItem)
