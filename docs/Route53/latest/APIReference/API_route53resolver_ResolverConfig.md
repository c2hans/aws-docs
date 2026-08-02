---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ResolverConfig.html
---

# ResolverConfig
<a name="API_route53resolver_ResolverConfig"></a>

A complex type that contains information about a Resolver configuration for a VPC.

## Contents
<a name="API_route53resolver_ResolverConfig_Contents"></a>

 ** AutodefinedReverse **   <a name="Route53Resolver-Type-route53resolver_ResolverConfig-AutodefinedReverse"></a>
 The status of whether or not the Resolver will create autodefined rules for reverse DNS lookups. This is enabled by default. The status can be one of following:
+  **ENABLING:** Autodefined rules for reverse DNS lookups are being enabled but are not complete.
+  **ENABLED:** Autodefined rules for reverse DNS lookups are enabled.
+  **DISABLING:** Autodefined rules for reverse DNS lookups are being disabled but are not complete.
+  **DISABLED:** Autodefined rules for reverse DNS lookups are disabled.
Type: String
Valid Values: `ENABLING | ENABLED | DISABLING | DISABLED | UPDATING_TO_USE_LOCAL_RESOURCE_SETTING | USE_LOCAL_RESOURCE_SETTING`
Required: No

 ** Id **   <a name="Route53Resolver-Type-route53resolver_ResolverConfig-Id"></a>
ID for the Resolver configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** OwnerId **   <a name="Route53Resolver-Type-route53resolver_ResolverConfig-OwnerId"></a>
The owner account ID of the Amazon Virtual Private Cloud VPC.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 32.
Required: No

 ** ResourceId **   <a name="Route53Resolver-Type-route53resolver_ResolverConfig-ResourceId"></a>
The ID of the Amazon Virtual Private Cloud VPC or a Route 53 Profile that you're configuring Resolver for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

## See Also
<a name="API_route53resolver_ResolverConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/ResolverConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/ResolverConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/ResolverConfig)
