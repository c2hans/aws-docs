---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_training_session_runtime_LoadWeightsForSamplingConfig.html
---

# LoadWeightsForSamplingConfig
<a name="API_training_session_runtime_LoadWeightsForSamplingConfig"></a>

The configuration for loading model weights for inference and sampling without restoring optimizer state.

## Contents
<a name="API_training_session_runtime_LoadWeightsForSamplingConfig_Contents"></a>

 ** modelPackageArn **   <a name="sagemaker-Type-training_session_runtime_LoadWeightsForSamplingConfig-modelPackageArn"></a>
The ARN of the model package containing the weights to load for sampling. Must be a valid SageMaker model package ARN in the format `arn:aws:sagemaker:REGION:ACCOUNT:model-package/PACKAGE_NAME/VERSION`. The model package must belong to the same AWS account as the training session.
Type: String
Required: Yes

## See Also
<a name="API_training_session_runtime_LoadWeightsForSamplingConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemakertrainingsessionruntime-2025-02-10/LoadWeightsForSamplingConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemakertrainingsessionruntime-2025-02-10/LoadWeightsForSamplingConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemakertrainingsessionruntime-2025-02-10/LoadWeightsForSamplingConfig)
