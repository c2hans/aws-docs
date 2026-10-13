---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_training_session_runtime_AdamParamsConfig.html
---

# AdamParamsConfig
<a name="API_training_session_runtime_AdamParamsConfig"></a>

The Adam optimizer hyperparameters used during an optimizer step.

## Contents
<a name="API_training_session_runtime_AdamParamsConfig_Contents"></a>

 ** learningRate **   <a name="sagemaker-Type-training_session_runtime_AdamParamsConfig-learningRate"></a>
The learning rate for the optimizer. Must be greater than 0.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 0.01.
Required: Yes

 ** beta1 **   <a name="sagemaker-Type-training_session_runtime_AdamParamsConfig-beta1"></a>
The exponential decay rate for the first moment estimates.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 0.999999.
Required: No

 ** beta2 **   <a name="sagemaker-Type-training_session_runtime_AdamParamsConfig-beta2"></a>
The exponential decay rate for the second moment estimates.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 0.999999.
Required: No

 ** eps **   <a name="sagemaker-Type-training_session_runtime_AdamParamsConfig-eps"></a>
A small constant added to the denominator for numerical stability.
Type: Double
Valid Range: Minimum value of 1.0e-16. Maximum value of 0.01.
Required: No

 ** gradClipNorm **   <a name="sagemaker-Type-training_session_runtime_AdamParamsConfig-gradClipNorm"></a>
The maximum gradient norm for gradient clipping. Gradients are scaled down if their norm exceeds this value.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** loraPlusLrRatio **   <a name="sagemaker-Type-training_session_runtime_AdamParamsConfig-loraPlusLrRatio"></a>
The learning rate multiplier for LoRA\+ B matrices relative to A matrices. When set, B matrices use `learningRate * loraPlusLrRatio` while A matrices use the base learning rate.
Type: Double
Valid Range: Minimum value of 1.0. Maximum value of 100.0.
Required: No

 ** weightDecay **   <a name="sagemaker-Type-training_session_runtime_AdamParamsConfig-weightDecay"></a>
The weight decay (L2 regularization) coefficient.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 1.
Required: No

## See Also
<a name="API_training_session_runtime_AdamParamsConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemakertrainingsessionruntime-2025-02-10/AdamParamsConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemakertrainingsessionruntime-2025-02-10/AdamParamsConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemakertrainingsessionruntime-2025-02-10/AdamParamsConfig)
