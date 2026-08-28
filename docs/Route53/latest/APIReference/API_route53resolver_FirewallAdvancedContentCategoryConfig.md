---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_FirewallAdvancedContentCategoryConfig.html
---

# FirewallAdvancedContentCategoryConfig
<a name="API_route53resolver_FirewallAdvancedContentCategoryConfig"></a>

The configuration for a content category-based filtering rule. This specifies which content category to use for DNS query evaluation.

## Contents
<a name="API_route53resolver_FirewallAdvancedContentCategoryConfig_Contents"></a>

 ** Category **   <a name="Route53Resolver-Type-route53resolver_FirewallAdvancedContentCategoryConfig-Category"></a>
The content category identifier. To retrieve the list of available content categories, call [ListFirewallRuleTypes](API_route53resolver_ListFirewallRuleTypes.md) with `RuleType` set to `FirewallAdvancedContentCategory`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

## See Also
<a name="API_route53resolver_FirewallAdvancedContentCategoryConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53resolver-2018-04-01/FirewallAdvancedContentCategoryConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53resolver-2018-04-01/FirewallAdvancedContentCategoryConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53resolver-2018-04-01/FirewallAdvancedContentCategoryConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
