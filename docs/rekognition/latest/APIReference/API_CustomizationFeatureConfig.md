---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CustomizationFeatureConfig.html
---

# CustomizationFeatureConfig
<a name="API_CustomizationFeatureConfig"></a>

Feature specific configuration for the training job. Configuration provided for the job must match the feature type parameter associated with project. If configuration and feature type do not match an InvalidParameterException is returned.

## Contents
<a name="API_CustomizationFeatureConfig_Contents"></a>

 ** ContentModeration **   <a name="rekognition-Type-CustomizationFeatureConfig-ContentModeration"></a>
Configuration options for Custom Moderation training.
Type: [CustomizationFeatureContentModerationConfig](API_CustomizationFeatureContentModerationConfig.md) object
Required: No

## See Also
<a name="API_CustomizationFeatureConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/CustomizationFeatureConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/CustomizationFeatureConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/CustomizationFeatureConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
