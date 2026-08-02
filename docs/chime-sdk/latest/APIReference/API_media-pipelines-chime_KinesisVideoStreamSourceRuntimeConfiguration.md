---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_KinesisVideoStreamSourceRuntimeConfiguration.html
---

# KinesisVideoStreamSourceRuntimeConfiguration
<a name="API_media-pipelines-chime_KinesisVideoStreamSourceRuntimeConfiguration"></a>

The runtime configuration settings for the Kinesis video stream source.

## Contents
<a name="API_media-pipelines-chime_KinesisVideoStreamSourceRuntimeConfiguration_Contents"></a>

 ** MediaEncoding **   <a name="chimesdk-Type-media-pipelines-chime_KinesisVideoStreamSourceRuntimeConfiguration-MediaEncoding"></a>
Specifies the encoding of your input audio. Supported format: PCM (only signed 16-bit little-endian audio formats, which does not include WAV)
For more information, see [Media formats](https://docs.aws.amazon.com/transcribe/latest/dg/how-input.html#how-input-audio) in the *Amazon Transcribe Developer Guide*.
Type: String
Valid Values: `pcm`
Required: Yes

 ** MediaSampleRate **   <a name="chimesdk-Type-media-pipelines-chime_KinesisVideoStreamSourceRuntimeConfiguration-MediaSampleRate"></a>
The sample rate of the input audio (in hertz). Low-quality audio, such as telephone audio, is typically around 8,000 Hz. High-quality audio typically ranges from 16,000 Hz to 48,000 Hz. Note that the sample rate you specify must match that of your audio.
Valid Range: Minimum value of 8000. Maximum value of 48000.
Type: Integer
Valid Range: Minimum value of 8000. Maximum value of 48000.
Required: Yes

 ** Streams **   <a name="chimesdk-Type-media-pipelines-chime_KinesisVideoStreamSourceRuntimeConfiguration-Streams"></a>
The streams in the source runtime configuration of a Kinesis video stream.
Type: Array of [StreamConfiguration](API_media-pipelines-chime_StreamConfiguration.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Required: Yes

## See Also
<a name="API_media-pipelines-chime_KinesisVideoStreamSourceRuntimeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-media-pipelines-2021-07-15/KinesisVideoStreamSourceRuntimeConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-media-pipelines-2021-07-15/KinesisVideoStreamSourceRuntimeConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-media-pipelines-2021-07-15/KinesisVideoStreamSourceRuntimeConfiguration)
