---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_PartnerThreatProtectionConfig.html
---

# PartnerThreatProtectionConfig
<a name="API_route53resolver_PartnerThreatProtectionConfig"></a>

The configuration for a partner threat-protection rule. To enumerate the partners available in your account, call [ListFirewallRuleTypes](API_route53resolver_ListFirewallRuleTypes.md) with `RuleType` set to `PartnerThreatProtection` — each returned [FirewallRuleTypeDefinition](API_route53resolver_FirewallRuleTypeDefinition.md) includes a [SubscriptionInfo](API_route53resolver_SubscriptionInfo.md) identifying the AWS Marketplace product that backs it.

## Contents
<a name="API_route53resolver_PartnerThreatProtectionConfig_Contents"></a>

 ** Partner **   <a name="Route53Resolver-Type-route53resolver_PartnerThreatProtectionConfig-Partner"></a>
The identifier of the partner threat-protection product, exactly as returned in the `Value` field of a [FirewallRuleTypeDefinition](API_route53resolver_FirewallRuleTypeDefinition.md) with `RuleType` set to `PartnerThreatProtection`. The calling account must hold an active AWS Marketplace subscription to this product.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

## See Also
<a name="API_route53resolver_PartnerThreatProtectionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/PartnerThreatProtectionConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/PartnerThreatProtectionConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/PartnerThreatProtectionConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
