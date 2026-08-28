---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_MediaStreamPipeline.html
---

# MediaStreamPipeline
<a name="API_media-pipelines-chime_MediaStreamPipeline"></a>

Structure that contains the settings for a media stream pipeline.

## Contents
<a name="API_media-pipelines-chime_MediaStreamPipeline_Contents"></a>

 ** CreatedTimestamp **   <a name="chimesdk-Type-media-pipelines-chime_MediaStreamPipeline-CreatedTimestamp"></a>
The time at which the media stream pipeline was created.
Type: Timestamp
Required: No

 ** MediaPipelineArn **   <a name="chimesdk-Type-media-pipelines-chime_MediaStreamPipeline-MediaPipelineArn"></a>
The ARN of the media stream pipeline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `^arn[\/\:\-\_\.a-zA-Z0-9]+$`
Required: No

 ** MediaPipelineId **   <a name="chimesdk-Type-media-pipelines-chime_MediaStreamPipeline-MediaPipelineId"></a>
The ID of the media stream pipeline
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-fA-F0-9]{8}(?:-[a-fA-F0-9]{4}){3}-[a-fA-F0-9]{12}`
Required: No

 ** Sinks **   <a name="chimesdk-Type-media-pipelines-chime_MediaStreamPipeline-Sinks"></a>
The media stream pipeline's data sinks.
Type: Array of [MediaStreamSink](API_media-pipelines-chime_MediaStreamSink.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Required: No

 ** Sources **   <a name="chimesdk-Type-media-pipelines-chime_MediaStreamPipeline-Sources"></a>
The media stream pipeline's data sources.
Type: Array of [MediaStreamSource](API_media-pipelines-chime_MediaStreamSource.md) objects
Array Members: Minimum number of 1 item.
Required: No

 ** Status **   <a name="chimesdk-Type-media-pipelines-chime_MediaStreamPipeline-Status"></a>
The status of the media stream pipeline.
Type: String
Valid Values: `Initializing | InProgress | Failed | Stopping | Stopped | Paused | NotStarted`
Required: No

 ** UpdatedTimestamp **   <a name="chimesdk-Type-media-pipelines-chime_MediaStreamPipeline-UpdatedTimestamp"></a>
The time at which the media stream pipeline was updated.
Type: Timestamp
Required: No

## See Also
<a name="API_media-pipelines-chime_MediaStreamPipeline_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-media-pipelines-2021-07-15/MediaStreamPipeline)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-media-pipelines-2021-07-15/MediaStreamPipeline)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-media-pipelines-2021-07-15/MediaStreamPipeline)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
