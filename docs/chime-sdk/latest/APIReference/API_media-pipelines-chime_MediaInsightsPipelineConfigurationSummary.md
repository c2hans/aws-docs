---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_MediaInsightsPipelineConfigurationSummary.html
---

# MediaInsightsPipelineConfigurationSummary
<a name="API_media-pipelines-chime_MediaInsightsPipelineConfigurationSummary"></a>

A summary of the media insights pipeline configuration.

## Contents
<a name="API_media-pipelines-chime_MediaInsightsPipelineConfigurationSummary_Contents"></a>

 ** MediaInsightsPipelineConfigurationArn **   <a name="chimesdk-Type-media-pipelines-chime_MediaInsightsPipelineConfigurationSummary-MediaInsightsPipelineConfigurationArn"></a>
The ARN of the media insights pipeline configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^arn[\/\:\-\_\.a-zA-Z0-9]+$`
Required: No

 ** MediaInsightsPipelineConfigurationId **   <a name="chimesdk-Type-media-pipelines-chime_MediaInsightsPipelineConfigurationSummary-MediaInsightsPipelineConfigurationId"></a>
The ID of the media insights pipeline configuration.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-fA-F0-9]{8}(?:-[a-fA-F0-9]{4}){3}-[a-fA-F0-9]{12}`
Required: No

 ** MediaInsightsPipelineConfigurationName **   <a name="chimesdk-Type-media-pipelines-chime_MediaInsightsPipelineConfigurationSummary-MediaInsightsPipelineConfigurationName"></a>
The name of the media insights pipeline configuration.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 64.
Pattern: `^[0-9a-zA-Z._-]+`
Required: No

## See Also
<a name="API_media-pipelines-chime_MediaInsightsPipelineConfigurationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-media-pipelines-2021-07-15/MediaInsightsPipelineConfigurationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-media-pipelines-2021-07-15/MediaInsightsPipelineConfigurationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-media-pipelines-2021-07-15/MediaInsightsPipelineConfigurationSummary)
