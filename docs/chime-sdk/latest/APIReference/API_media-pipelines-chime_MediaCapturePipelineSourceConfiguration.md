---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_MediaCapturePipelineSourceConfiguration.html
---

# MediaCapturePipelineSourceConfiguration
<a name="API_media-pipelines-chime_MediaCapturePipelineSourceConfiguration"></a>

The source configuration object of a media capture pipeline.

## Contents
<a name="API_media-pipelines-chime_MediaCapturePipelineSourceConfiguration_Contents"></a>

 ** ChimeSdkMeetingConfiguration **   <a name="chimesdk-Type-media-pipelines-chime_MediaCapturePipelineSourceConfiguration-ChimeSdkMeetingConfiguration"></a>
The meeting configuration settings in a media capture pipeline configuration object.
Type: [ChimeSdkMeetingConcatenationConfiguration](API_media-pipelines-chime_ChimeSdkMeetingConcatenationConfiguration.md) object
Required: Yes

 ** MediaPipelineArn **   <a name="chimesdk-Type-media-pipelines-chime_MediaCapturePipelineSourceConfiguration-MediaPipelineArn"></a>
The media pipeline ARN in the configuration object of a media capture pipeline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^arn[\/\:\-\_\.a-zA-Z0-9]+$`
Required: Yes

## See Also
<a name="API_media-pipelines-chime_MediaCapturePipelineSourceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-media-pipelines-2021-07-15/MediaCapturePipelineSourceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-media-pipelines-2021-07-15/MediaCapturePipelineSourceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-media-pipelines-2021-07-15/MediaCapturePipelineSourceConfiguration)
