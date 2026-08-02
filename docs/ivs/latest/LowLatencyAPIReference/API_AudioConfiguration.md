---
source_url: https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_AudioConfiguration.html
---

# AudioConfiguration
<a name="API_AudioConfiguration"></a>

Object specifying a stream’s audio configuration, as set up by the broadcaster (usually in an encoder). This is part of the [IngestConfigurations](API_IngestConfigurations.md) object and the deprecated [IngestConfiguration](API_IngestConfiguration.md) object. It is used for monitoring stream health.

## Contents
<a name="API_AudioConfiguration_Contents"></a>

 ** channels **   <a name="ivs-Type-AudioConfiguration-channels"></a>
Number of audio channels.
Type: Long
Required: No

 ** codec **   <a name="ivs-Type-AudioConfiguration-codec"></a>
Codec used for the audio encoding.
Type: String
Required: No

 ** sampleRate **   <a name="ivs-Type-AudioConfiguration-sampleRate"></a>
Number of audio samples recorded per second.
Type: Long
Required: No

 ** targetBitrate **   <a name="ivs-Type-AudioConfiguration-targetBitrate"></a>
The expected ingest bitrate (bits per second). This is configured in the encoder.
Type: Long
Required: No

 ** track **   <a name="ivs-Type-AudioConfiguration-track"></a>
Name of the audio track (if the stream has an audio track). If multitrack is not enabled, this is Track0 (the sole track).
Type: String
Required: No

## See Also
<a name="API_AudioConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-2020-07-14/AudioConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-2020-07-14/AudioConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-2020-07-14/AudioConfiguration)
