---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ResolverRuleConfig.html
---

# ResolverRuleConfig
<a name="API_route53resolver_ResolverRuleConfig"></a>

In an [UpdateResolverRule](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_UpdateResolverRule.html) request, information about the changes that you want to make.

## Contents
<a name="API_route53resolver_ResolverRuleConfig_Contents"></a>

 ** Name **   <a name="Route53Resolver-Type-route53resolver_ResolverRuleConfig-Name"></a>
The new name for the Resolver rule. The name that you specify appears in the Resolver dashboard in the Route 53 console.
The name can be up to 64 characters long and can contain letters (a-z, A-Z), numbers (0-9), hyphens (-), underscores (\_), and spaces. The name cannot consist of only numbers.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9\-_' ']+)`
Required: No

 ** ResolverEndpointId **   <a name="Route53Resolver-Type-route53resolver_ResolverRuleConfig-ResolverEndpointId"></a>
The ID of the new outbound Resolver endpoint that you want to use to route DNS queries to the IP addresses that you specify in `TargetIps`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** TargetIps **   <a name="Route53Resolver-Type-route53resolver_ResolverRuleConfig-TargetIps"></a>
For DNS queries that originate in your VPC, the new IP addresses that you want to route outbound DNS queries to.
Type: Array of [TargetAddress](API_route53resolver_TargetAddress.md) objects
Array Members: Minimum number of 1 item.
Required: No

## See Also
<a name="API_route53resolver_ResolverRuleConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/ResolverRuleConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/ResolverRuleConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/ResolverRuleConfig)
