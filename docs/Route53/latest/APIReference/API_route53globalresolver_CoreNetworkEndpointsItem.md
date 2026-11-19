---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_CoreNetworkEndpointsItem.html
---

# CoreNetworkEndpointsItem

Summary information about a core network endpoint. Route 53 Global Resolver returns one of these items for each endpoint in the response to a `ListCoreNetworkEndpoints` request. Each item describes the endpoint's identifiers, the Global Resolver and Cloud WAN core network that it connects, its DNS IP addresses, and its current status.

## Contents
<a name="API_route53globalresolver_CoreNetworkEndpointsItem_Contents"></a>

 ** arn **   <a name="Route53GlobalResolver-Type-route53globalresolver_CoreNetworkEndpointsItem-arn"></a>
The Amazon Resource Name (ARN) of the core network endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[-.a-z0-9]{1,63}:[-.a-z0-9]{1,63}:[-.a-z0-9]{0,63}:[-.a-z0-9]{0,63}:[^/].{0,1023}`
Required: Yes

 ** availableRegions **   <a name="Route53GlobalResolver-Type-route53globalresolver_CoreNetworkEndpointsItem-availableRegions"></a>
The AWS Regions in which the core network endpoint is available.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 32.
Required: Yes

 ** coreNetworkArn **   <a name="Route53GlobalResolver-Type-route53globalresolver_CoreNetworkEndpointsItem-coreNetworkArn"></a>
The Amazon Resource Name (ARN) of the Cloud WAN core network that the endpoint connects to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[-.a-z0-9]{1,63}:[-.a-z0-9]{1,63}:[-.a-z0-9]{0,63}:[-.a-z0-9]{0,63}:[^/].{0,1023}`
Required: Yes

 ** createdAt **   <a name="Route53GlobalResolver-Type-route53globalresolver_CoreNetworkEndpointsItem-createdAt"></a>
The date and time when the core network endpoint was created.
Type: Timestamp
Required: Yes

 ** globalResolverId **   <a name="Route53GlobalResolver-Type-route53globalresolver_CoreNetworkEndpointsItem-globalResolverId"></a>
The identifier of the Route 53 Global Resolver that the core network endpoint is associated with.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`
Required: Yes

 ** id **   <a name="Route53GlobalResolver-Type-route53globalresolver_CoreNetworkEndpointsItem-id"></a>
The unique identifier of the core network endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`
Required: Yes

 ** ipAddresses **   <a name="Route53GlobalResolver-Type-route53globalresolver_CoreNetworkEndpointsItem-ipAddresses"></a>
The DNS IP addresses that the core network endpoint uses to receive DNS queries.
Type: Array of [CoreNetworkEndpointDnsIpItem](API_route53globalresolver_CoreNetworkEndpointDnsIpItem.md) objects
Required: Yes

 ** status **   <a name="Route53GlobalResolver-Type-route53globalresolver_CoreNetworkEndpointsItem-status"></a>
The current status of the core network endpoint.
Type: String
Valid Values: `CREATING | OPERATIONAL | UPDATING | DELETING`
Required: Yes

 ** updatedAt **   <a name="Route53GlobalResolver-Type-route53globalresolver_CoreNetworkEndpointsItem-updatedAt"></a>
The date and time when the core network endpoint was last updated.
Type: Timestamp
Required: Yes

 ** name **   <a name="Route53GlobalResolver-Type-route53globalresolver_CoreNetworkEndpointsItem-name"></a>
The name of the core network endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9-_/' ']+)`
Required: No

## See Also
<a name="API_route53globalresolver_CoreNetworkEndpointsItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53globalresolver-2022-09-27/CoreNetworkEndpointsItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53globalresolver-2022-09-27/CoreNetworkEndpointsItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53globalresolver-2022-09-27/CoreNetworkEndpointsItem)
