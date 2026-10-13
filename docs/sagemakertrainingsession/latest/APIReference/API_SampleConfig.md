---
source_url: https://docs.aws.amazon.com/sagemakertrainingsession/latest/APIReference/API_SampleConfig.html
---

# SampleConfig
<a name="API_SampleConfig"></a>

The configuration for generating text samples from the model.

## Contents
<a name="API_SampleConfig_Contents"></a>

 ** numSamples **   <a name="sagemakertrainingsession-Type-SampleConfig-numSamples"></a>
The number of independent samples to generate for the prompt.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: Yes

 ** prompt **   <a name="sagemakertrainingsession-Type-SampleConfig-prompt"></a>
The input prompt to send to the model for text generation.
Type: [ModelInput](API_ModelInput.md) object
Required: Yes

 ** samplingParams **   <a name="sagemakertrainingsession-Type-SampleConfig-samplingParams"></a>
The parameters controlling the sampling strategy.
Type: [SamplingParams](API_SamplingParams.md) object
Required: Yes

 ** includePromptLogprobs **   <a name="sagemakertrainingsession-Type-SampleConfig-includePromptLogprobs"></a>
Specifies whether to include per-token log-probabilities for the input prompt in the response.
Type: Boolean
Required: No

 ** modelPackageArn **   <a name="sagemakertrainingsession-Type-SampleConfig-modelPackageArn"></a>
The ARN of the model package whose checkpoint this sample should run against. Must be a valid SageMaker model package ARN in the format `arn:aws:sagemaker:REGION:ACCOUNT:model-package/PACKAGE_NAME/VERSION`. When absent, the sample runs against the session's latest checkpoint.
Type: String
Required: No

 ** topkPromptLogprobs **   <a name="sagemakertrainingsession-Type-SampleConfig-topkPromptLogprobs"></a>
The number of top-k log-probabilities to return per prompt token.
Type: Integer
Required: No

## See Also
<a name="API_SampleConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemakertrainingsessionruntime-2025-02-10/SampleConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemakertrainingsessionruntime-2025-02-10/SampleConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemakertrainingsessionruntime-2025-02-10/SampleConfig)
