---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_MediaLiveConnectorPipeline.html
---

# MediaLiveConnectorPipeline
<a name="API_media-pipelines-chime_MediaLiveConnectorPipeline"></a>

The connector pipeline.

## Contents
<a name="API_media-pipelines-chime_MediaLiveConnectorPipeline_Contents"></a>

 ** CreatedTimestamp **   <a name="chimesdk-Type-media-pipelines-chime_MediaLiveConnectorPipeline-CreatedTimestamp"></a>
The time at which the connector pipeline was created.
Type: Timestamp
Required: No

 ** MediaPipelineArn **   <a name="chimesdk-Type-media-pipelines-chime_MediaLiveConnectorPipeline-MediaPipelineArn"></a>
The connector pipeline's ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `^arn[\/\:\-\_\.a-zA-Z0-9]+$`
Required: No

 ** MediaPipelineId **   <a name="chimesdk-Type-media-pipelines-chime_MediaLiveConnectorPipeline-MediaPipelineId"></a>
The connector pipeline's ID.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-fA-F0-9]{8}(?:-[a-fA-F0-9]{4}){3}-[a-fA-F0-9]{12}`
Required: No

 ** Sinks **   <a name="chimesdk-Type-media-pipelines-chime_MediaLiveConnectorPipeline-Sinks"></a>
The connector pipeline's data sinks.
Type: Array of [LiveConnectorSinkConfiguration](API_media-pipelines-chime_LiveConnectorSinkConfiguration.md) objects
Array Members: Fixed number of 1 item.
Required: No

 ** Sources **   <a name="chimesdk-Type-media-pipelines-chime_MediaLiveConnectorPipeline-Sources"></a>
The connector pipeline's data sources.
Type: Array of [LiveConnectorSourceConfiguration](API_media-pipelines-chime_LiveConnectorSourceConfiguration.md) objects
Array Members: Fixed number of 1 item.
Required: No

 ** Status **   <a name="chimesdk-Type-media-pipelines-chime_MediaLiveConnectorPipeline-Status"></a>
The connector pipeline's status.
Type: String
Valid Values: `Initializing | InProgress | Failed | Stopping | Stopped | Paused | NotStarted`
Required: No

 ** UpdatedTimestamp **   <a name="chimesdk-Type-media-pipelines-chime_MediaLiveConnectorPipeline-UpdatedTimestamp"></a>
The time at which the connector pipeline was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_media-pipelines-chime_MediaLiveConnectorPipeline_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-media-pipelines-2021-07-15/MediaLiveConnectorPipeline)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-media-pipelines-2021-07-15/MediaLiveConnectorPipeline)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-media-pipelines-2021-07-15/MediaLiveConnectorPipeline)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
