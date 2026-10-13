---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_training_session_runtime_TensorData.html
---

# TensorData
<a name="API_training_session_runtime_TensorData"></a>

A tensor with data, data type, and shape metadata.

## Contents
<a name="API_training_session_runtime_TensorData_Contents"></a>

 ** data **   <a name="sagemaker-Type-training_session_runtime_TensorData-data"></a>
The raw tensor data as JSON. The format is determined by the `dtype` field: integer arrays for `int64`, floating-point arrays for `float32`.
Type: JSON value
Required: Yes

 ** dtype **   <a name="sagemaker-Type-training_session_runtime_TensorData-dtype"></a>
The data type of the tensor elements, such as `int64` or `float32`.
Type: String
Required: Yes

 ** shape **   <a name="sagemaker-Type-training_session_runtime_TensorData-shape"></a>
The dimensions of the tensor, such as [batch\_size, seq\_length].
Type: Array of integers
Required: No

## See Also
<a name="API_training_session_runtime_TensorData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemakertrainingsessionruntime-2025-02-10/TensorData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemakertrainingsessionruntime-2025-02-10/TensorData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemakertrainingsessionruntime-2025-02-10/TensorData)
