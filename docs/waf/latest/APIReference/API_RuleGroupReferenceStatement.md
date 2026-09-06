---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_RuleGroupReferenceStatement.html
---

# RuleGroupReferenceStatement
<a name="API_RuleGroupReferenceStatement"></a>

A rule statement used to run the rules that are defined in a [RuleGroup](API_RuleGroup.md). To use this, create a rule group with your rules, then provide the ARN of the rule group in this statement.

You cannot nest a `RuleGroupReferenceStatement`, for example for use inside a `NotStatement` or `OrStatement`. You cannot use a rule group reference statement inside another rule group. You can only reference a rule group as a top-level statement within a rule that you define in a web ACL.

## Contents
<a name="API_RuleGroupReferenceStatement_Contents"></a>

 ** ARN **   <a name="WAF-Type-RuleGroupReferenceStatement-ARN"></a>
The Amazon Resource Name (ARN) of the entity.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `.*\S.*`
Required: Yes

 ** ExcludedRules **   <a name="WAF-Type-RuleGroupReferenceStatement-ExcludedRules"></a>
Rules in the referenced rule group whose actions are set to `Count`.
Instead of this option, use `RuleActionOverrides`. It accepts any valid action setting, including `Count`.
Type: Array of [ExcludedRule](API_ExcludedRule.md) objects
Array Members: Maximum number of 100 items.
Required: No

 ** RuleActionOverrides **   <a name="WAF-Type-RuleGroupReferenceStatement-RuleActionOverrides"></a>
Action settings to use in the place of the rule actions that are configured inside the rule group. You specify one override for each rule whose action you want to change.
Verify the rule names in your overrides carefully. With managed rule groups, AWS WAF silently ignores any override that uses an invalid rule name. With customer-owned rule groups, invalid rule names in your overrides will cause web ACL updates to fail. An invalid rule name is any name that doesn't exactly match the case-sensitive name of an existing rule in the rule group.
You can use overrides for testing, for example you can override all of rule actions to `Count` and then monitor the resulting count metrics to understand how the rule group would handle your web traffic. You can also permanently override some or all actions, to modify how the rule group manages your web traffic.
Type: Array of [RuleActionOverride](API_RuleActionOverride.md) objects
Array Members: Maximum number of 100 items.
Required: No

## See Also
<a name="API_RuleGroupReferenceStatement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/RuleGroupReferenceStatement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/RuleGroupReferenceStatement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/RuleGroupReferenceStatement)
