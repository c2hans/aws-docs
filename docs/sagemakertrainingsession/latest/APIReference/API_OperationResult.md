---
source_url: https://docs.aws.amazon.com/sagemakertrainingsession/latest/APIReference/API_OperationResult.html
---

# OperationResult
<a name="API_OperationResult"></a>

The result of a completed training operation. Exactly one member is populated, corresponding to the operation type that was submitted.

## Contents
<a name="API_OperationResult_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** forward **   <a name="sagemakertrainingsession-Type-OperationResult-forward"></a>
The result from a forward-only pass.
Type: [ForwardResult](API_ForwardResult.md) object
Required: No

 ** forwardBackward **   <a name="sagemakertrainingsession-Type-OperationResult-forwardBackward"></a>
The result from a forward and backward pass.
Type: [ForwardBackwardResult](API_ForwardBackwardResult.md) object
Required: No

 ** loadState **   <a name="sagemakertrainingsession-Type-OperationResult-loadState"></a>
The result from loading training state.
Type: [LoadStateResult](API_LoadStateResult.md) object
Required: No

 ** optimizerStep **   <a name="sagemakertrainingsession-Type-OperationResult-optimizerStep"></a>
The result from an optimizer step.
Type: [OptimizerStepResult](API_OptimizerStepResult.md) object
Required: No

 ** saveState **   <a name="sagemakertrainingsession-Type-OperationResult-saveState"></a>
The result from saving full training state.
Type: [SaveStateResult](API_SaveStateResult.md) object
Required: No

 ** saveWeights **   <a name="sagemakertrainingsession-Type-OperationResult-saveWeights"></a>
The result from saving model weights.
Type: [SaveWeightsResult](API_SaveWeightsResult.md) object
Required: No

## See Also
<a name="API_OperationResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemakertrainingsessionruntime-2025-02-10/OperationResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemakertrainingsessionruntime-2025-02-10/OperationResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemakertrainingsessionruntime-2025-02-10/OperationResult)
