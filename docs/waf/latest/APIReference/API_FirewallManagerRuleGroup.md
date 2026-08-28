---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_FirewallManagerRuleGroup.html
---

# FirewallManagerRuleGroup
<a name="API_FirewallManagerRuleGroup"></a>

A rule group that's defined for an AWS Firewall Manager AWS WAF policy.

## Contents
<a name="API_FirewallManagerRuleGroup_Contents"></a>

 ** FirewallManagerStatement **   <a name="WAF-Type-FirewallManagerRuleGroup-FirewallManagerStatement"></a>
The processing guidance for an AWS Firewall Manager rule. This is like a regular rule [Statement](API_Statement.md), but it can only contain a rule group reference.
Type: [FirewallManagerStatement](API_FirewallManagerStatement.md) object
Required: Yes

 ** Name **   <a name="WAF-Type-FirewallManagerRuleGroup-Name"></a>
The name of the rule group. You cannot change the name of a rule group after you create it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[\w\-]+$`
Required: Yes

 ** OverrideAction **   <a name="WAF-Type-FirewallManagerRuleGroup-OverrideAction"></a>
The action to use in the place of the action that results from the rule group evaluation. Set the override action to none to leave the result of the rule group alone. Set it to count to override the result to count only.
You can only use this for rule statements that reference a rule group, like `RuleGroupReferenceStatement` and `ManagedRuleGroupStatement`.
This option is usually set to none. It does not affect how the rules in the rule group are evaluated. If you want the rules in the rule group to only count matches, do not use this and instead use the rule action override option, with `Count` action, in your rule group reference statement settings.
Type: [OverrideAction](API_OverrideAction.md) object
Required: Yes

 ** Priority **   <a name="WAF-Type-FirewallManagerRuleGroup-Priority"></a>
If you define more than one rule group in the first or last Firewall Manager rule groups, AWS WAF evaluates each request against the rule groups in order, starting from the lowest priority setting. The priorities don't need to be consecutive, but they must all be different.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** VisibilityConfig **   <a name="WAF-Type-FirewallManagerRuleGroup-VisibilityConfig"></a>
Defines and enables Amazon CloudWatch metrics and web request sample collection.
Type: [VisibilityConfig](API_VisibilityConfig.md) object
Required: Yes

## See Also
<a name="API_FirewallManagerRuleGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/FirewallManagerRuleGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/FirewallManagerRuleGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/FirewallManagerRuleGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
