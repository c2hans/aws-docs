---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_MediaCapturePipeline.html
---

# MediaCapturePipeline
<a name="API_media-pipelines-chime_MediaCapturePipeline"></a>

A media pipeline object consisting of an ID, source type, source ARN, a sink type, a sink ARN, and a configuration object.

## Contents
<a name="API_media-pipelines-chime_MediaCapturePipeline_Contents"></a>

 ** ChimeSdkMeetingConfiguration **   <a name="chimesdk-Type-media-pipelines-chime_MediaCapturePipeline-ChimeSdkMeetingConfiguration"></a>
The configuration for a specified media pipeline. `SourceType` must be `ChimeSdkMeeting`.
Type: [ChimeSdkMeetingConfiguration](API_media-pipelines-chime_ChimeSdkMeetingConfiguration.md) object
Required: No

 ** CreatedTimestamp **   <a name="chimesdk-Type-media-pipelines-chime_MediaCapturePipeline-CreatedTimestamp"></a>
The time at which the pipeline was created, in ISO 8601 format.
Type: Timestamp
Required: No

 ** MediaPipelineArn **   <a name="chimesdk-Type-media-pipelines-chime_MediaCapturePipeline-MediaPipelineArn"></a>
The ARN of the media capture pipeline
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `^arn[\/\:\-\_\.a-zA-Z0-9]+$`
Required: No

 ** MediaPipelineId **   <a name="chimesdk-Type-media-pipelines-chime_MediaCapturePipeline-MediaPipelineId"></a>
The ID of a media pipeline.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-fA-F0-9]{8}(?:-[a-fA-F0-9]{4}){3}-[a-fA-F0-9]{12}`
Required: No

 ** SinkArn **   <a name="chimesdk-Type-media-pipelines-chime_MediaCapturePipeline-SinkArn"></a>
ARN of the destination to which the media artifacts are saved.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^arn[\/\:\-\_\.a-zA-Z0-9]+$`
Required: No

 ** SinkIamRoleArn **   <a name="chimesdk-Type-media-pipelines-chime_MediaCapturePipeline-SinkIamRoleArn"></a>
The Amazon Resource Name (ARN) of the sink role to be used with `AwsKmsKeyId` in `SseAwsKeyManagementParams`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^arn[\/\:\-\_\.a-zA-Z0-9]+$`
Required: No

 ** SinkType **   <a name="chimesdk-Type-media-pipelines-chime_MediaCapturePipeline-SinkType"></a>
Destination type to which the media artifacts are saved. You must use an S3 Bucket.
Type: String
Valid Values: `S3Bucket`
Required: No

 ** SourceArn **   <a name="chimesdk-Type-media-pipelines-chime_MediaCapturePipeline-SourceArn"></a>
ARN of the source from which the media artifacts are saved.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^arn[\/\:\-\_\.a-zA-Z0-9]+$`
Required: No

 ** SourceType **   <a name="chimesdk-Type-media-pipelines-chime_MediaCapturePipeline-SourceType"></a>
Source type from which media artifacts are saved. You must use `ChimeMeeting`.
Type: String
Valid Values: `ChimeSdkMeeting`
Required: No

 ** SseAwsKeyManagementParams **   <a name="chimesdk-Type-media-pipelines-chime_MediaCapturePipeline-SseAwsKeyManagementParams"></a>
An object that contains server side encryption parameters to be used by media capture pipeline. The parameters can also be used by media concatenation pipeline taking media capture pipeline as a media source.
Type: [SseAwsKeyManagementParams](API_media-pipelines-chime_SseAwsKeyManagementParams.md) object
Required: No

 ** Status **   <a name="chimesdk-Type-media-pipelines-chime_MediaCapturePipeline-Status"></a>
The status of the media pipeline.
Type: String
Valid Values: `Initializing | InProgress | Failed | Stopping | Stopped | Paused | NotStarted`
Required: No

 ** UpdatedTimestamp **   <a name="chimesdk-Type-media-pipelines-chime_MediaCapturePipeline-UpdatedTimestamp"></a>
The time at which the pipeline was updated, in ISO 8601 format.
Type: Timestamp
Required: No

## See Also
<a name="API_media-pipelines-chime_MediaCapturePipeline_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-media-pipelines-2021-07-15/MediaCapturePipeline)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-media-pipelines-2021-07-15/MediaCapturePipeline)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-media-pipelines-2021-07-15/MediaCapturePipeline)
