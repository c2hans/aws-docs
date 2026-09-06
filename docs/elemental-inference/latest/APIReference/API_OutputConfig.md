---
source_url: https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_OutputConfig.html
---

# OutputConfig
<a name="API_OutputConfig"></a>

Contains one typed output. It is used in the CreateOutput, GetOutput, and Update Output structures.

## Contents
<a name="API_OutputConfig_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** clipping **   <a name="elementalinference-Type-OutputConfig-clipping"></a>
The output config type that applies to the clipping feature.
Type: [ClippingConfig](API_ClippingConfig.md) object
Required: No

 ** cropping **   <a name="elementalinference-Type-OutputConfig-cropping"></a>
The output config type that applies to the cropping feature.
Type: [CroppingConfig](API_CroppingConfig.md) object
Required: No

 ** subtitling **   <a name="elementalinference-Type-OutputConfig-subtitling"></a>
The output config type that applies to the smart subtitling feature.
Type: [SubtitlingConfig](API_SubtitlingConfig.md) object
Required: No

## See Also
<a name="API_OutputConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elementalinference-2018-11-14/OutputConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elementalinference-2018-11-14/OutputConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elementalinference-2018-11-14/OutputConfig)
