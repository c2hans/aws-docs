---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_MediaCapturePipelineSummary.html
---

# MediaCapturePipelineSummary
<a name="API_media-pipelines-chime_MediaCapturePipelineSummary"></a>

The summary data of a media capture pipeline.

## Contents
<a name="API_media-pipelines-chime_MediaCapturePipelineSummary_Contents"></a>

 ** MediaPipelineArn **   <a name="chimesdk-Type-media-pipelines-chime_MediaCapturePipelineSummary-MediaPipelineArn"></a>
The ARN of the media pipeline in the summary.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `^arn[\/\:\-\_\.a-zA-Z0-9]+$`
Required: No

 ** MediaPipelineId **   <a name="chimesdk-Type-media-pipelines-chime_MediaCapturePipelineSummary-MediaPipelineId"></a>
The ID of the media pipeline in the summary.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-fA-F0-9]{8}(?:-[a-fA-F0-9]{4}){3}-[a-fA-F0-9]{12}`
Required: No

## See Also
<a name="API_media-pipelines-chime_MediaCapturePipelineSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-media-pipelines-2021-07-15/MediaCapturePipelineSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-media-pipelines-2021-07-15/MediaCapturePipelineSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-media-pipelines-2021-07-15/MediaCapturePipelineSummary)
