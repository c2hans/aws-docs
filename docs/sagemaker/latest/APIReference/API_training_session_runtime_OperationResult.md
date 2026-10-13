---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_training_session_runtime_OperationResult.html
---

# OperationResult
<a name="API_training_session_runtime_OperationResult"></a>

The result of a completed training operation. Exactly one member is populated, corresponding to the operation type that was submitted.

## Contents
<a name="API_training_session_runtime_OperationResult_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** forward **   <a name="sagemaker-Type-training_session_runtime_OperationResult-forward"></a>
The result from a forward-only pass.
Type: [ForwardResult](API_training_session_runtime_ForwardResult.md) object
Required: No

 ** forwardBackward **   <a name="sagemaker-Type-training_session_runtime_OperationResult-forwardBackward"></a>
The result from a forward and backward pass.
Type: [ForwardBackwardResult](API_training_session_runtime_ForwardBackwardResult.md) object
Required: No

 ** loadState **   <a name="sagemaker-Type-training_session_runtime_OperationResult-loadState"></a>
The result from loading training state.
Type: [LoadStateResult](API_training_session_runtime_LoadStateResult.md) object
Required: No

 ** optimizerStep **   <a name="sagemaker-Type-training_session_runtime_OperationResult-optimizerStep"></a>
The result from an optimizer step.
Type: [OptimizerStepResult](API_training_session_runtime_OptimizerStepResult.md) object
Required: No

 ** saveState **   <a name="sagemaker-Type-training_session_runtime_OperationResult-saveState"></a>
The result from saving full training state.
Type: [SaveStateResult](API_training_session_runtime_SaveStateResult.md) object
Required: No

 ** saveWeights **   <a name="sagemaker-Type-training_session_runtime_OperationResult-saveWeights"></a>
The result from saving model weights.
Type: [SaveWeightsResult](API_training_session_runtime_SaveWeightsResult.md) object
Required: No

## See Also
<a name="API_training_session_runtime_OperationResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemakertrainingsessionruntime-2025-02-10/OperationResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemakertrainingsessionruntime-2025-02-10/OperationResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemakertrainingsessionruntime-2025-02-10/OperationResult)
