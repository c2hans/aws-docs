---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_MediaInsightsPipelineConfiguration.html
---

# MediaInsightsPipelineConfiguration
<a name="API_media-pipelines-chime_MediaInsightsPipelineConfiguration"></a>

A structure that contains the configuration settings for a media insights pipeline.

## Contents
<a name="API_media-pipelines-chime_MediaInsightsPipelineConfiguration_Contents"></a>

 ** CreatedTimestamp **   <a name="chimesdk-Type-media-pipelines-chime_MediaInsightsPipelineConfiguration-CreatedTimestamp"></a>
The time at which the configuration was created.
Type: Timestamp
Required: No

 ** Elements **   <a name="chimesdk-Type-media-pipelines-chime_MediaInsightsPipelineConfiguration-Elements"></a>
The elements in the configuration.
Type: Array of [MediaInsightsPipelineConfigurationElement](API_media-pipelines-chime_MediaInsightsPipelineConfigurationElement.md) objects
Required: No

 ** MediaInsightsPipelineConfigurationArn **   <a name="chimesdk-Type-media-pipelines-chime_MediaInsightsPipelineConfiguration-MediaInsightsPipelineConfigurationArn"></a>
The ARN of the configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^arn[\/\:\-\_\.a-zA-Z0-9]+$`
Required: No

 ** MediaInsightsPipelineConfigurationId **   <a name="chimesdk-Type-media-pipelines-chime_MediaInsightsPipelineConfiguration-MediaInsightsPipelineConfigurationId"></a>
The ID of the configuration.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-fA-F0-9]{8}(?:-[a-fA-F0-9]{4}){3}-[a-fA-F0-9]{12}`
Required: No

 ** MediaInsightsPipelineConfigurationName **   <a name="chimesdk-Type-media-pipelines-chime_MediaInsightsPipelineConfiguration-MediaInsightsPipelineConfigurationName"></a>
The name of the configuration.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 64.
Pattern: `^[0-9a-zA-Z._-]+`
Required: No

 ** RealTimeAlertConfiguration **   <a name="chimesdk-Type-media-pipelines-chime_MediaInsightsPipelineConfiguration-RealTimeAlertConfiguration"></a>
Lists the rules that trigger a real-time alert.
Type: [RealTimeAlertConfiguration](API_media-pipelines-chime_RealTimeAlertConfiguration.md) object
Required: No

 ** ResourceAccessRoleArn **   <a name="chimesdk-Type-media-pipelines-chime_MediaInsightsPipelineConfiguration-ResourceAccessRoleArn"></a>
The ARN of the role used by the service to access AWS resources.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^arn[\/\:\-\_\.a-zA-Z0-9]+$`
Required: No

 ** UpdatedTimestamp **   <a name="chimesdk-Type-media-pipelines-chime_MediaInsightsPipelineConfiguration-UpdatedTimestamp"></a>
The time at which the configuration was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_media-pipelines-chime_MediaInsightsPipelineConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-media-pipelines-2021-07-15/MediaInsightsPipelineConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-media-pipelines-2021-07-15/MediaInsightsPipelineConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-media-pipelines-2021-07-15/MediaInsightsPipelineConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
