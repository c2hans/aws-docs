---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_FirewallRuleTypeDefinition.html
---

# FirewallRuleTypeDefinition
<a name="API_route53resolver_FirewallRuleTypeDefinition"></a>

The definition of an available rule type that can be used in DNS Firewall rules. This is returned by [ListFirewallRuleTypes](API_route53resolver_ListFirewallRuleTypes.md).

## Contents
<a name="API_route53resolver_FirewallRuleTypeDefinition_Contents"></a>

 ** Description **   <a name="Route53Resolver-Type-route53resolver_FirewallRuleTypeDefinition-Description"></a>
A description of the rule type.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

 ** DisplayName **   <a name="Route53Resolver-Type-route53resolver_FirewallRuleTypeDefinition-DisplayName"></a>
The display name of the rule type.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** RuleType **   <a name="Route53Resolver-Type-route53resolver_FirewallRuleTypeDefinition-RuleType"></a>
The category or class of the rule type, such as `FirewallAdvancedContentCategory` or `FirewallAdvancedThreatCategory`.
Type: String
Length Constraints: Maximum length of 128.
Required: No

 ** SubscriptionInfo **   <a name="Route53Resolver-Type-route53resolver_FirewallRuleTypeDefinition-SubscriptionInfo"></a>
For rule types that require an external subscription (today, only the `PartnerThreatProtection` variant), describes the AWS Marketplace product that backs the rule type. Absent for rule types that are managed by AWS and do not require a separate subscription. See [SubscriptionInfo](API_route53resolver_SubscriptionInfo.md).
Type: [SubscriptionInfo](API_route53resolver_SubscriptionInfo.md) object
Required: No

 ** Value **   <a name="Route53Resolver-Type-route53resolver_FirewallRuleTypeDefinition-Value"></a>
The specific identifier within the rule type category, such as `VIOLENCE_AND_HATE_SPEECH` or `PHISHING`.
Type: String
Length Constraints: Maximum length of 128.
Required: No

## See Also
<a name="API_route53resolver_FirewallRuleTypeDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/FirewallRuleTypeDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/FirewallRuleTypeDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/FirewallRuleTypeDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
