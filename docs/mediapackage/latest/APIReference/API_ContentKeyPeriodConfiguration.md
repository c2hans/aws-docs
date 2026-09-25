---
source_url: https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_ContentKeyPeriodConfiguration.html
---

# ContentKeyPeriodConfiguration
<a name="API_ContentKeyPeriodConfiguration"></a>

The configuration that controls the content key period timing information that MediaPackage signals to your DRM key provider.

## Contents
<a name="API_ContentKeyPeriodConfiguration_Contents"></a>

 ** ContentKeyPeriodTiming **   <a name="mediapackage-Type-ContentKeyPeriodConfiguration-ContentKeyPeriodTiming"></a>
Specifies what timing information MediaPackage signals in the `ContentKeyPeriod` to your DRM key provider. If you don't specify a value, the default is `INDEX_ONLY`. Signaling start and end times (`START_END_ONLY` or `INDEX_WITH_START_END`) also requires key rotation to be enabled.
The allowed values are:
+  `INDEX_ONLY` - Signals only the content key index. This is the default and matches the current behavior. It's supported for both SPEKE Version 2.0 and 2.1.
+  `START_END_ONLY` - Signals only the start and end times the key is used for. Requires `SpekeVersion` `V2_1`.
+  `INDEX_WITH_START_END` - Signals both the content key index and the start and end times the key is used for. Requires `SpekeVersion` `V2_1`.
Type: String
Valid Values: `INDEX_ONLY | START_END_ONLY | INDEX_WITH_START_END`
Required: No

## See Also
<a name="API_ContentKeyPeriodConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediapackagev2-2022-12-25/ContentKeyPeriodConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediapackagev2-2022-12-25/ContentKeyPeriodConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediapackagev2-2022-12-25/ContentKeyPeriodConfiguration)
