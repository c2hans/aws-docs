---
source_url: https://docs.aws.amazon.com/sagemakertrainingsession/latest/APIReference/API_ForwardResult.html
---

# ForwardResult
<a name="API_ForwardResult"></a>

The result of a forward-only pass through the model.

## Contents
<a name="API_ForwardResult_Contents"></a>

 ** lossFnOutputs **   <a name="sagemakertrainingsession-Type-ForwardResult-lossFnOutputs"></a>
The loss function output tensors, keyed by name.
Type: Array of string to [TensorData](API_TensorData.md) object maps
Required: No

 ** lossFnOutputType **   <a name="sagemakertrainingsession-Type-ForwardResult-lossFnOutputType"></a>
The data type of the loss function output tensors.
Type: String
Required: No

 ** metrics **   <a name="sagemakertrainingsession-Type-ForwardResult-metrics"></a>
The training metrics emitted by the engine, such as loss values.
Type: String to double map
Required: No

 ** tokenUsage **   <a name="sagemakertrainingsession-Type-ForwardResult-tokenUsage"></a>
The token usage statistics for metering.
Type: [TrainingTokenUsage](API_TrainingTokenUsage.md) object
Required: No

## See Also
<a name="API_ForwardResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemakertrainingsessionruntime-2025-02-10/ForwardResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemakertrainingsessionruntime-2025-02-10/ForwardResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemakertrainingsessionruntime-2025-02-10/ForwardResult)
