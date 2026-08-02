---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_RuleSummary.html
---

# RuleSummary
<a name="API_RuleSummary"></a>

High-level information about a [Rule](API_Rule.md), returned by operations like [DescribeManagedRuleGroup](API_DescribeManagedRuleGroup.md). This provides information like the ID, that you can use to retrieve and manage a `RuleGroup`, and the ARN, that you provide to the [RuleGroupReferenceStatement](API_RuleGroupReferenceStatement.md) to use the rule group in a [Rule](API_Rule.md).

## Contents
<a name="API_RuleSummary_Contents"></a>

 ** Action **   <a name="WAF-Type-RuleSummary-Action"></a>
The action that AWS WAF should take on a web request when it matches a rule's statement. Settings at the web ACL level can override the rule action setting.
Type: [RuleAction](API_RuleAction.md) object
Required: No

 ** Name **   <a name="WAF-Type-RuleSummary-Name"></a>
The name of the rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[\w\-]+$`
Required: No

## See Also
<a name="API_RuleSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/RuleSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/RuleSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/RuleSummary)
