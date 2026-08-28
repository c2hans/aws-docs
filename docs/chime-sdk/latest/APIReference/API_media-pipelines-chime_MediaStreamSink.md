---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_MediaStreamSink.html
---

# MediaStreamSink
<a name="API_media-pipelines-chime_MediaStreamSink"></a>

Structure that contains the settings for a media stream sink.

## Contents
<a name="API_media-pipelines-chime_MediaStreamSink_Contents"></a>

 ** MediaStreamType **   <a name="chimesdk-Type-media-pipelines-chime_MediaStreamSink-MediaStreamType"></a>
The media stream sink's media stream type.
Type: String
Valid Values: `MixedAudio | IndividualAudio`
Required: Yes

 ** ReservedStreamCapacity **   <a name="chimesdk-Type-media-pipelines-chime_MediaStreamSink-ReservedStreamCapacity"></a>
Specifies the number of streams that the sink can accept.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10.
Required: Yes

 ** SinkArn **   <a name="chimesdk-Type-media-pipelines-chime_MediaStreamSink-SinkArn"></a>
The ARN of the Kinesis Video Stream pool returned by the [CreateMediaPipelineKinesisVideoStreamPool](API_media-pipelines-chime_CreateMediaPipelineKinesisVideoStreamPool.md) API.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^arn[\/\:\-\_\.a-zA-Z0-9]+$`
Required: Yes

 ** SinkType **   <a name="chimesdk-Type-media-pipelines-chime_MediaStreamSink-SinkType"></a>
The media stream sink's type.
Type: String
Valid Values: `KinesisVideoStreamPool`
Required: Yes

## See Also
<a name="API_media-pipelines-chime_MediaStreamSink_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-media-pipelines-2021-07-15/MediaStreamSink)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-media-pipelines-2021-07-15/MediaStreamSink)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-media-pipelines-2021-07-15/MediaStreamSink)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
