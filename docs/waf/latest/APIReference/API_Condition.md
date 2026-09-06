---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_Condition.html
---

# Condition
<a name="API_Condition"></a>

A single match condition for a [Filter](API_Filter.md).

## Contents
<a name="API_Condition_Contents"></a>

 ** ActionCondition **   <a name="WAF-Type-Condition-ActionCondition"></a>
A single action condition. This is the action setting that a log record must contain in order to meet the condition.
Type: [ActionCondition](API_ActionCondition.md) object
Required: No

 ** LabelNameCondition **   <a name="WAF-Type-Condition-LabelNameCondition"></a>
A single label name condition. This is the fully qualified label name that a log record must contain in order to meet the condition. Fully qualified labels have a prefix, optional namespaces, and label name. The prefix identifies the rule group or web ACL context of the rule that added the label.
Type: [LabelNameCondition](API_LabelNameCondition.md) object
Required: No

## See Also
<a name="API_Condition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/Condition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/Condition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/Condition)
