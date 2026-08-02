---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_KinesisVideoStreamRecordingSourceRuntimeConfiguration.html
---

# KinesisVideoStreamRecordingSourceRuntimeConfiguration
<a name="API_media-pipelines-chime_KinesisVideoStreamRecordingSourceRuntimeConfiguration"></a>

A structure that contains the runtime settings for recording a Kinesis video stream.

## Contents
<a name="API_media-pipelines-chime_KinesisVideoStreamRecordingSourceRuntimeConfiguration_Contents"></a>

 ** FragmentSelector **   <a name="chimesdk-Type-media-pipelines-chime_KinesisVideoStreamRecordingSourceRuntimeConfiguration-FragmentSelector"></a>
Describes the timestamp range and timestamp origin of a range of fragments in the Kinesis video stream.
Type: [FragmentSelector](API_media-pipelines-chime_FragmentSelector.md) object
Required: Yes

 ** Streams **   <a name="chimesdk-Type-media-pipelines-chime_KinesisVideoStreamRecordingSourceRuntimeConfiguration-Streams"></a>
The stream or streams to be recorded.
Type: Array of [RecordingStreamConfiguration](API_media-pipelines-chime_RecordingStreamConfiguration.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Required: Yes

## See Also
<a name="API_media-pipelines-chime_KinesisVideoStreamRecordingSourceRuntimeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-media-pipelines-2021-07-15/KinesisVideoStreamRecordingSourceRuntimeConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-media-pipelines-2021-07-15/KinesisVideoStreamRecordingSourceRuntimeConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-media-pipelines-2021-07-15/KinesisVideoStreamRecordingSourceRuntimeConfiguration)
