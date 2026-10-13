---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_training_session_runtime_ComputeLogprobsConfig.html
---

# ComputeLogprobsConfig
<a name="API_training_session_runtime_ComputeLogprobsConfig"></a>

The configuration for computing log-probabilities of prompt tokens without generating new text.

## Contents
<a name="API_training_session_runtime_ComputeLogprobsConfig_Contents"></a>

 ** prompt **   <a name="sagemaker-Type-training_session_runtime_ComputeLogprobsConfig-prompt"></a>
The input prompt whose token log-probabilities will be computed.
Type: [ModelInput](API_training_session_runtime_ModelInput.md) object
Required: Yes

 ** modelPackageArn **   <a name="sagemaker-Type-training_session_runtime_ComputeLogprobsConfig-modelPackageArn"></a>
The ARN of the model package whose checkpoint this operation should run against. Must be a valid SageMaker model package ARN in the format `arn:aws:sagemaker:REGION:ACCOUNT:model-package/PACKAGE_NAME/VERSION`. When absent, the operation runs against the session's latest checkpoint.
Type: String
Required: No

## See Also
<a name="API_training_session_runtime_ComputeLogprobsConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemakertrainingsessionruntime-2025-02-10/ComputeLogprobsConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemakertrainingsessionruntime-2025-02-10/ComputeLogprobsConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemakertrainingsessionruntime-2025-02-10/ComputeLogprobsConfig)
