---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_ChimeSdkMeetingLiveConnectorConfiguration.html
---

# ChimeSdkMeetingLiveConnectorConfiguration
<a name="API_media-pipelines-chime_ChimeSdkMeetingLiveConnectorConfiguration"></a>

The media pipeline's configuration object.

## Contents
<a name="API_media-pipelines-chime_ChimeSdkMeetingLiveConnectorConfiguration_Contents"></a>

 ** Arn **   <a name="chimesdk-Type-media-pipelines-chime_ChimeSdkMeetingLiveConnectorConfiguration-Arn"></a>
The configuration object's Chime SDK meeting ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^arn[\/\:\-\_\.a-zA-Z0-9]+$`
Required: Yes

 ** MuxType **   <a name="chimesdk-Type-media-pipelines-chime_ChimeSdkMeetingLiveConnectorConfiguration-MuxType"></a>
The configuration object's multiplex type.
Type: String
Valid Values: `AudioWithCompositedVideo | AudioWithActiveSpeakerVideo`
Required: Yes

 ** CompositedVideo **   <a name="chimesdk-Type-media-pipelines-chime_ChimeSdkMeetingLiveConnectorConfiguration-CompositedVideo"></a>
The media pipeline's composited video.
Type: [CompositedVideoArtifactsConfiguration](API_media-pipelines-chime_CompositedVideoArtifactsConfiguration.md) object
Required: No

 ** SourceConfiguration **   <a name="chimesdk-Type-media-pipelines-chime_ChimeSdkMeetingLiveConnectorConfiguration-SourceConfiguration"></a>
The source configuration settings of the media pipeline's configuration object.
Type: [SourceConfiguration](API_media-pipelines-chime_SourceConfiguration.md) object
Required: No

## See Also
<a name="API_media-pipelines-chime_ChimeSdkMeetingLiveConnectorConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-media-pipelines-2021-07-15/ChimeSdkMeetingLiveConnectorConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-media-pipelines-2021-07-15/ChimeSdkMeetingLiveConnectorConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-media-pipelines-2021-07-15/ChimeSdkMeetingLiveConnectorConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
