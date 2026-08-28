---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_FirewallRuleType.html
---

# FirewallRuleType
<a name="API_route53resolver_FirewallRuleType"></a>

The rule-type configuration for a DNS Firewall rule. `FirewallRuleType` is a tagged union — exactly one member must be set per rule, and the member determines what the rule matches against. This shape is mutually exclusive with the top-level `FirewallDomainListId` and `DnsThreatProtection` fields on [CreateFirewallRule](API_route53resolver_CreateFirewallRule.md) and [UpdateFirewallRule](API_route53resolver_UpdateFirewallRule.md).

Call [ListFirewallRuleTypes](API_route53resolver_ListFirewallRuleTypes.md) to discover which rule-type variants and which values within each variant are available in your account and Region.

## Contents
<a name="API_route53resolver_FirewallRuleType_Contents"></a>

 ** DnsThreatProtection **   <a name="Route53Resolver-Type-route53resolver_FirewallRuleType-DnsThreatProtection"></a>
Configures the rule to match a built-in DNS Firewall Advanced threat detector — `DGA`, `DNS_TUNNELING`, or `DICTIONARY_DGA`. See [DnsThreatProtectionRuleTypeConfig](API_route53resolver_DnsThreatProtectionRuleTypeConfig.md).
Type: [DnsThreatProtectionRuleTypeConfig](API_route53resolver_DnsThreatProtectionRuleTypeConfig.md) object
Required: No

 ** FirewallAdvancedContentCategory **   <a name="Route53Resolver-Type-route53resolver_FirewallRuleType-FirewallAdvancedContentCategory"></a>
Configures the rule to match an AWS-managed content category (for example, `VIOLENCE_AND_HATE_SPEECH`). See [FirewallAdvancedContentCategoryConfig](API_route53resolver_FirewallAdvancedContentCategoryConfig.md).
Type: [FirewallAdvancedContentCategoryConfig](API_route53resolver_FirewallAdvancedContentCategoryConfig.md) object
Required: No

 ** FirewallAdvancedThreatCategory **   <a name="Route53Resolver-Type-route53resolver_FirewallRuleType-FirewallAdvancedThreatCategory"></a>
Configures the rule to match an AWS-managed advanced threat category (for example, `PHISHING`). See [FirewallAdvancedThreatCategoryConfig](API_route53resolver_FirewallAdvancedThreatCategoryConfig.md).
Type: [FirewallAdvancedThreatCategoryConfig](API_route53resolver_FirewallAdvancedThreatCategoryConfig.md) object
Required: No

 ** PartnerThreatProtection **   <a name="Route53Resolver-Type-route53resolver_FirewallRuleType-PartnerThreatProtection"></a>
Configures the rule to match a third-party threat feed delivered through AWS Marketplace. The calling account must hold an active subscription to the partner product named in `Partner`; if the subscription is missing or revoked, the rule is created with `Status` `CREATION_FAILED` and cannot be modified — only deleted. See [PartnerThreatProtectionConfig](API_route53resolver_PartnerThreatProtectionConfig.md).
Type: [PartnerThreatProtectionConfig](API_route53resolver_PartnerThreatProtectionConfig.md) object
Required: No

## See Also
<a name="API_route53resolver_FirewallRuleType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/FirewallRuleType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/FirewallRuleType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/FirewallRuleType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
