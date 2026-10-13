---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_training_session_runtime_LoadStateConfig.html
---

# LoadStateConfig
<a name="API_training_session_runtime_LoadStateConfig"></a>

The configuration for loading training state from a previously saved checkpoint. This restores model weights and optionally optimizer state.

## Contents
<a name="API_training_session_runtime_LoadStateConfig_Contents"></a>

 ** loadOptimizer **   <a name="sagemaker-Type-training_session_runtime_LoadStateConfig-loadOptimizer"></a>
Specifies whether to also restore the optimizer state alongside model weights. When true, optimizer state is restored to resume training from where it left off.
Type: Boolean
Required: Yes

 ** modelPackageArn **   <a name="sagemaker-Type-training_session_runtime_LoadStateConfig-modelPackageArn"></a>
The ARN of the model package containing the checkpoint to load. Must be a valid SageMaker model package ARN in the format `arn:aws:sagemaker:REGION:ACCOUNT:model-package/PACKAGE_NAME/VERSION`. Model package group ARNs are not accepted.
Type: String
Required: Yes

## See Also
<a name="API_training_session_runtime_LoadStateConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemakertrainingsessionruntime-2025-02-10/LoadStateConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemakertrainingsessionruntime-2025-02-10/LoadStateConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemakertrainingsessionruntime-2025-02-10/LoadStateConfig)
