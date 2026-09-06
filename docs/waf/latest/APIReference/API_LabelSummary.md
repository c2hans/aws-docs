---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_LabelSummary.html
---

# LabelSummary
<a name="API_LabelSummary"></a>

List of labels used by one or more of the rules of a [RuleGroup](API_RuleGroup.md). This summary object is used for the following rule group lists:
+  `AvailableLabels` - Labels that rules add to matching requests. These labels are defined in the `RuleLabels` for a [Rule](API_Rule.md).
+  `ConsumedLabels` - Labels that rules match against. These labels are defined in a `LabelMatchStatement` specification, in the [Statement](API_Statement.md) definition of a rule.

## Contents
<a name="API_LabelSummary_Contents"></a>

 ** Name **   <a name="WAF-Type-LabelSummary-Name"></a>
An individual label specification.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^[0-9A-Za-z_\-:]+$`
Required: No

## See Also
<a name="API_LabelSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/LabelSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/LabelSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/LabelSummary)
