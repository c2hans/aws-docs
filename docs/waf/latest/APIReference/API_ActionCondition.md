---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_ActionCondition.html
---

# ActionCondition
<a name="API_ActionCondition"></a>

A single action condition for a [Condition](API_Condition.md) in a logging filter.

## Contents
<a name="API_ActionCondition_Contents"></a>

 ** Action **   <a name="WAF-Type-ActionCondition-Action"></a>
The action setting that a log record must contain in order to meet the condition. This is the action that AWS WAF applied to the web request.
For rule groups, this is either the configured rule action setting, or if you've applied a rule action override to the rule, it's the override action. The value `EXCLUDED_AS_COUNT` matches on excluded rules and also on rules that have a rule action override of Count.
Type: String
Valid Values: `ALLOW | BLOCK | COUNT | CAPTCHA | CHALLENGE | MONETIZE | EXCLUDED_AS_COUNT`
Required: Yes

## See Also
<a name="API_ActionCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/ActionCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/ActionCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/ActionCondition)
