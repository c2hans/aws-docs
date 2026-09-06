---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_MediaInsightsPipeline.html
---

# MediaInsightsPipeline
<a name="API_media-pipelines-chime_MediaInsightsPipeline"></a>

A media pipeline that streams call analytics data.

## Contents
<a name="API_media-pipelines-chime_MediaInsightsPipeline_Contents"></a>

 ** CreatedTimestamp **   <a name="chimesdk-Type-media-pipelines-chime_MediaInsightsPipeline-CreatedTimestamp"></a>
The time at which the media insights pipeline was created.
Type: Timestamp
Required: No

 ** ElementStatuses **   <a name="chimesdk-Type-media-pipelines-chime_MediaInsightsPipeline-ElementStatuses"></a>
The statuses that the elements in a media insights pipeline can have during data processing.
Type: Array of [MediaInsightsPipelineElementStatus](API_media-pipelines-chime_MediaInsightsPipelineElementStatus.md) objects
Required: No

 ** KinesisVideoStreamRecordingSourceRuntimeConfiguration **   <a name="chimesdk-Type-media-pipelines-chime_MediaInsightsPipeline-KinesisVideoStreamRecordingSourceRuntimeConfiguration"></a>
The runtime configuration settings for a Kinesis recording video stream in a media insights pipeline.
Type: [KinesisVideoStreamRecordingSourceRuntimeConfiguration](API_media-pipelines-chime_KinesisVideoStreamRecordingSourceRuntimeConfiguration.md) object
Required: No

 ** KinesisVideoStreamSourceRuntimeConfiguration **   <a name="chimesdk-Type-media-pipelines-chime_MediaInsightsPipeline-KinesisVideoStreamSourceRuntimeConfiguration"></a>
The configuration settings for a Kinesis runtime video stream in a media insights pipeline.
Type: [KinesisVideoStreamSourceRuntimeConfiguration](API_media-pipelines-chime_KinesisVideoStreamSourceRuntimeConfiguration.md) object
Required: No

 ** MediaInsightsPipelineConfigurationArn **   <a name="chimesdk-Type-media-pipelines-chime_MediaInsightsPipeline-MediaInsightsPipelineConfigurationArn"></a>
The ARN of a media insight pipeline's configuration settings.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^arn[\/\:\-\_\.a-zA-Z0-9]+$`
Required: No

 ** MediaInsightsRuntimeMetadata **   <a name="chimesdk-Type-media-pipelines-chime_MediaInsightsPipeline-MediaInsightsRuntimeMetadata"></a>
The runtime metadata of a media insights pipeline.
Type: String to string map
Key Length Constraints: Maximum length of 1024.
Key Pattern: `.*\S.*`
Value Length Constraints: Maximum length of 4096.
Value Pattern: `.*`
Required: No

 ** MediaPipelineArn **   <a name="chimesdk-Type-media-pipelines-chime_MediaInsightsPipeline-MediaPipelineArn"></a>
The ARN of a media insights pipeline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^arn[\/\:\-\_\.a-zA-Z0-9]+$`
Required: No

 ** MediaPipelineId **   <a name="chimesdk-Type-media-pipelines-chime_MediaInsightsPipeline-MediaPipelineId"></a>
The ID of a media insights pipeline.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-fA-F0-9]{8}(?:-[a-fA-F0-9]{4}){3}-[a-fA-F0-9]{12}`
Required: No

 ** S3RecordingSinkRuntimeConfiguration **   <a name="chimesdk-Type-media-pipelines-chime_MediaInsightsPipeline-S3RecordingSinkRuntimeConfiguration"></a>
The runtime configuration of the Amazon S3 bucket that stores recordings in a media insights pipeline.
Type: [S3RecordingSinkRuntimeConfiguration](API_media-pipelines-chime_S3RecordingSinkRuntimeConfiguration.md) object
Required: No

 ** Status **   <a name="chimesdk-Type-media-pipelines-chime_MediaInsightsPipeline-Status"></a>
The status of a media insights pipeline.
Type: String
Valid Values: `Initializing | InProgress | Failed | Stopping | Stopped | Paused | NotStarted`
Required: No

## See Also
<a name="API_media-pipelines-chime_MediaInsightsPipeline_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-media-pipelines-2021-07-15/MediaInsightsPipeline)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-media-pipelines-2021-07-15/MediaInsightsPipeline)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-media-pipelines-2021-07-15/MediaInsightsPipeline)
