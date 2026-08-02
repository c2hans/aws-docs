---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_FirewallAdvancedThreatCategoryConfig.html
---

# FirewallAdvancedThreatCategoryConfig
<a name="API_route53resolver_FirewallAdvancedThreatCategoryConfig"></a>

The configuration for a threat category-based filtering rule. This specifies which threat category to use for DNS query evaluation.

## Contents
<a name="API_route53resolver_FirewallAdvancedThreatCategoryConfig_Contents"></a>

 ** Category **   <a name="Route53Resolver-Type-route53resolver_FirewallAdvancedThreatCategoryConfig-Category"></a>
The threat category identifier. To retrieve the list of available threat categories, call [ListFirewallRuleTypes](API_route53resolver_ListFirewallRuleTypes.md) with `RuleType` set to `FirewallAdvancedThreatCategory`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

## See Also
<a name="API_route53resolver_FirewallAdvancedThreatCategoryConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/FirewallAdvancedThreatCategoryConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/FirewallAdvancedThreatCategoryConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/FirewallAdvancedThreatCategoryConfig)
