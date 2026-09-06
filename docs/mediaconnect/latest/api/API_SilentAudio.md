---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_SilentAudio.html
---

# SilentAudio
<a name="API_SilentAudio"></a>

Configures settings for the `SilentAudio` metric.

## Contents
<a name="API_SilentAudio_Contents"></a>

 ** state **   <a name="mediaconnect-Type-SilentAudio-state"></a>
Indicates whether the `SilentAudio` metric is enabled or disabled.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** thresholdSeconds **   <a name="mediaconnect-Type-SilentAudio-thresholdSeconds"></a>
Specifies the number of consecutive seconds of silence that triggers an event or alert.
Type: Integer
Required: No

## See Also
<a name="API_SilentAudio_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/SilentAudio)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/SilentAudio)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/SilentAudio)
