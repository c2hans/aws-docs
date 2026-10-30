---
source_url: https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_ClippingConfig.html
---

# ClippingConfig
<a name="API_ClippingConfig"></a>

A type of OutputConfig, used when the output in a feed is for the clip feature.

## Contents
<a name="API_ClippingConfig_Contents"></a>

 ** callbackMetadata **   <a name="elementalinference-Type-ClippingConfig-callbackMetadata"></a>
A string that you want Elemental Inference to always include in the event clipping metadata for this output. The string might identify the sports event in the source media, for example.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\w \-\.',@:;]*`
Required: No

 ** dataSourceConfiguration **   <a name="elementalinference-Type-ClippingConfig-dataSourceConfiguration"></a>
The data source to map onto this clipping output. This parameter is optional. When you include this parameter, Elemental Inference reads the event data for the fixture that you specify, and includes that data in the event clipping metadata for this output.
If you omit this parameter, Elemental Inference doesn't map a data source onto this output.
Type: [DataSourceConfiguration](API_DataSourceConfiguration.md) object
Required: No

## See Also
<a name="API_ClippingConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elementalinference-2018-11-14/ClippingConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elementalinference-2018-11-14/ClippingConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elementalinference-2018-11-14/ClippingConfig)
