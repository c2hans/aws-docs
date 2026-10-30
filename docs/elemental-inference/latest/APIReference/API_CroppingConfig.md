---
source_url: https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_CroppingConfig.html
---

# CroppingConfig
<a name="API_CroppingConfig"></a>

A type of OutputConfig, used when the output in a feed is for the crop feature.

## Contents
<a name="API_CroppingConfig_Contents"></a>

 ** templateGroups **   <a name="elementalinference-Type-CroppingConfig-templateGroups"></a>
An array of template groups for the crop output. Each template group provides the graphics-compositing templates that Elemental Inference applies to the cropped video. You can specify from 1 to 4 template groups.
Type: Array of [TemplateGroup](API_TemplateGroup.md) objects
Array Members: Minimum number of 1 item. Maximum number of 4 items.
Required: No

## See Also
<a name="API_CroppingConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elementalinference-2018-11-14/CroppingConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elementalinference-2018-11-14/CroppingConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elementalinference-2018-11-14/CroppingConfig)
