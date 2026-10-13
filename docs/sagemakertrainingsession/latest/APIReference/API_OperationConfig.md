---
source_url: https://docs.aws.amazon.com/sagemakertrainingsession/latest/APIReference/API_OperationConfig.html
---

# OperationConfig
<a name="API_OperationConfig"></a>

The configuration for a training operation. Exactly one member must be set to specify the operation type and its parameters.

## Contents
<a name="API_OperationConfig_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** forward **   <a name="sagemakertrainingsession-Type-OperationConfig-forward"></a>
The configuration for a forward-only pass through the model without gradient computation.
Type: [ForwardConfig](API_ForwardConfig.md) object
Required: No

 ** forwardBackward **   <a name="sagemakertrainingsession-Type-OperationConfig-forwardBackward"></a>
The configuration for a forward and backward pass that computes gradients.
Type: [ForwardBackwardConfig](API_ForwardBackwardConfig.md) object
Required: No

 ** loadState **   <a name="sagemakertrainingsession-Type-OperationConfig-loadState"></a>
The configuration for loading training state from a previously saved checkpoint.
Type: [LoadStateConfig](API_LoadStateConfig.md) object
Required: No

 ** optimizerStep **   <a name="sagemakertrainingsession-Type-OperationConfig-optimizerStep"></a>
The configuration for an optimizer step that updates model weights using accumulated gradients.
Type: [OptimizerStepConfig](API_OptimizerStepConfig.md) object
Required: No

 ** saveState **   <a name="sagemakertrainingsession-Type-OperationConfig-saveState"></a>
The configuration for saving full training state, including model weights and optimizer state.
Type: [SaveStateConfig](API_SaveStateConfig.md) object
Required: No

 ** saveWeights **   <a name="sagemakertrainingsession-Type-OperationConfig-saveWeights"></a>
The configuration for saving model weights as a checkpoint.
Type: [SaveWeightsConfig](API_SaveWeightsConfig.md) object
Required: No

## See Also
<a name="API_OperationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemakertrainingsessionruntime-2025-02-10/OperationConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemakertrainingsessionruntime-2025-02-10/OperationConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemakertrainingsessionruntime-2025-02-10/OperationConfig)
