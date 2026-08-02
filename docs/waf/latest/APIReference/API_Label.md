---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_Label.html
---

# Label
<a name="API_Label"></a>

A single label container. This is used as an element of a label array in multiple contexts, for example, in `RuleLabels` inside a [Rule](API_Rule.md) and in `Labels` inside a [SampledHTTPRequest](API_SampledHTTPRequest.md).

## Contents
<a name="API_Label_Contents"></a>

 ** Name **   <a name="WAF-Type-Label-Name"></a>
The label string.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^[0-9A-Za-z_\-:]+$`
Required: Yes

## See Also
<a name="API_Label_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/Label)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/Label)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/Label)
