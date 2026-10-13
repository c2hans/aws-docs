---
source_url: https://docs.aws.amazon.com/sagemakertrainingsession/latest/APIReference/API_ForwardBackwardResult.html
---

# ForwardBackwardResult
<a name="API_ForwardBackwardResult"></a>

The result of a forward and backward pass through the model, including computed gradients.

## Contents
<a name="API_ForwardBackwardResult_Contents"></a>

 ** lossFnOutputs **   <a name="sagemakertrainingsession-Type-ForwardBackwardResult-lossFnOutputs"></a>
The loss function output tensors, keyed by name.
Type: Array of string to [TensorData](API_TensorData.md) object maps
Required: No

 ** lossFnOutputType **   <a name="sagemakertrainingsession-Type-ForwardBackwardResult-lossFnOutputType"></a>
The data type of the loss function output tensors.
Type: String
Required: No

 ** metrics **   <a name="sagemakertrainingsession-Type-ForwardBackwardResult-metrics"></a>
The training metrics emitted by the engine, such as loss values.
Type: String to double map
Required: No

 ** tokenUsage **   <a name="sagemakertrainingsession-Type-ForwardBackwardResult-tokenUsage"></a>
The token usage statistics for metering.
Type: [TrainingTokenUsage](API_TrainingTokenUsage.md) object
Required: No

## See Also
<a name="API_ForwardBackwardResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemakertrainingsessionruntime-2025-02-10/ForwardBackwardResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemakertrainingsessionruntime-2025-02-10/ForwardBackwardResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemakertrainingsessionruntime-2025-02-10/ForwardBackwardResult)
