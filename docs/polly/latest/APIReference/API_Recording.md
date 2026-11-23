---
source_url: https://docs.aws.amazon.com/polly/latest/APIReference/API_Recording.html
---

# Recording

A recording of the speaker whose voice you want to create. The recording specifies its audio format and its audio source.

## Contents
<a name="API_Recording_Contents"></a>

 ** Data **   <a name="polly-Type-Recording-Data"></a>
The audio source of the recording. Specify either an Amazon S3 object or the audio data.
Type: [RecordingData](API_RecordingData.md) object
Required: Yes

 ** Format **   <a name="polly-Type-Recording-Format"></a>
The audio format of the recording: `wav`, `flac`, `ogg_vorbis`, or `mp3`. The format must match the audio data.
Type: String
Valid Values: `wav | flac | ogg_vorbis | mp3`
Required: Yes

## See Also
<a name="API_Recording_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/polly-2016-06-10/Recording)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/polly-2016-06-10/Recording)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/polly-2016-06-10/Recording)
