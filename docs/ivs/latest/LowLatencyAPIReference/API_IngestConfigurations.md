---
source_url: https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_IngestConfigurations.html
---

# IngestConfigurations
<a name="API_IngestConfigurations"></a>

Object specifying the ingest configuration set up by the broadcaster, usually in an encoder.

 **Note:** Use IngestConfigurations instead of [IngestConfiguration](API_IngestConfiguration.md) (which is deprecated). If multitrack is not enabled, IngestConfiguration and IngestConfigurations contain the same data, namely information about Track0 (the sole track). If multitrack is enabled, IngestConfiguration contains data for only the first track (Track0) and IngestConfigurations contains data for all tracks.

## Contents
<a name="API_IngestConfigurations_Contents"></a>

 ** audioConfigurations **   <a name="ivs-Type-IngestConfigurations-audioConfigurations"></a>
Encoder settings for audio.
Type: Array of [AudioConfiguration](API_AudioConfiguration.md) objects
Required: Yes

 ** videoConfigurations **   <a name="ivs-Type-IngestConfigurations-videoConfigurations"></a>
Encoder settings for video
Type: Array of [VideoConfiguration](API_VideoConfiguration.md) objects
Required: Yes

## See Also
<a name="API_IngestConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-2020-07-14/IngestConfigurations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-2020-07-14/IngestConfigurations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-2020-07-14/IngestConfigurations)
