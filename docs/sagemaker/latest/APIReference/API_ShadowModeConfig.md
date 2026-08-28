---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ShadowModeConfig.html
---

# ShadowModeConfig
<a name="API_ShadowModeConfig"></a>

 The configuration of `ShadowMode` inference experiment type, which specifies a production variant to take all the inference requests, and a shadow variant to which Amazon SageMaker replicates a percentage of the inference requests. For the shadow variant it also specifies the percentage of requests that Amazon SageMaker replicates.

## Contents
<a name="API_ShadowModeConfig_Contents"></a>

 ** ShadowModelVariants **   <a name="sagemaker-Type-ShadowModeConfig-ShadowModelVariants"></a>
List of shadow variant configurations.
Type: Array of [ShadowModelVariantConfig](API_ShadowModelVariantConfig.md) objects
Array Members: Fixed number of 1 item.
Required: Yes

 ** SourceModelVariantName **   <a name="sagemaker-Type-ShadowModeConfig-SourceModelVariantName"></a>
 The name of the production variant, which takes all the inference requests.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9]([\-a-zA-Z0-9]*[a-zA-Z0-9])?`
Required: Yes

## See Also
<a name="API_ShadowModeConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ShadowModeConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ShadowModeConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ShadowModeConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
