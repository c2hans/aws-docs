---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_StatelessRule.html
---

# StatelessRule
<a name="API_StatelessRule"></a>

A single stateless rule. This is used in [StatelessRulesAndCustomActions](API_StatelessRulesAndCustomActions.md).

## Contents
<a name="API_StatelessRule_Contents"></a>

 ** Priority **   <a name="networkfirewall-Type-StatelessRule-Priority"></a>
Indicates the order in which to run this rule relative to all of the rules that are defined for a stateless rule group. Network Firewall evaluates the rules in a rule group starting with the lowest priority setting. You must ensure that the priority settings are unique for the rule group.
Each stateless rule group uses exactly one `StatelessRulesAndCustomActions` object, and each `StatelessRulesAndCustomActions` contains exactly one `StatelessRules` object. To ensure unique priority settings for your rule groups, set unique priorities for the stateless rules that you define inside any single `StatelessRules` object.
You can change the priority settings of your rules at any time. To make it easier to insert rules later, number them so there's a wide range in between, for example use 100, 200, and so on.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65535.
Required: Yes

 ** RuleDefinition **   <a name="networkfirewall-Type-StatelessRule-RuleDefinition"></a>
Defines the stateless 5-tuple packet inspection criteria and the action to take on a packet that matches the criteria.
Type: [RuleDefinition](API_RuleDefinition.md) object
Required: Yes

## See Also
<a name="API_StatelessRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/StatelessRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/StatelessRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/StatelessRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Firewall. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-firewall` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
