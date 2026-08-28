---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ShadowModelVariantConfig.html
---

# ShadowModelVariantConfig
<a name="API_ShadowModelVariantConfig"></a>

The name and sampling percentage of a shadow variant.

## Contents
<a name="API_ShadowModelVariantConfig_Contents"></a>

 ** SamplingPercentage **   <a name="sagemaker-Type-ShadowModelVariantConfig-SamplingPercentage"></a>
 The percentage of inference requests that Amazon SageMaker replicates from the production variant to the shadow variant.
Type: Integer
Valid Range: Maximum value of 100.
Required: Yes

 ** ShadowModelVariantName **   <a name="sagemaker-Type-ShadowModelVariantConfig-ShadowModelVariantName"></a>
The name of the shadow variant.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `[a-zA-Z0-9]([\-a-zA-Z0-9]*[a-zA-Z0-9])?`
Required: Yes

## See Also
<a name="API_ShadowModelVariantConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ShadowModelVariantConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ShadowModelVariantConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ShadowModelVariantConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
