---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_training_session_runtime_SampleOperationConfig.html
---

# SampleOperationConfig
<a name="API_training_session_runtime_SampleOperationConfig"></a>

The configuration for a sampling operation. Exactly one member must be set to specify the operation type.

## Contents
<a name="API_training_session_runtime_SampleOperationConfig_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** computeLogprobs **   <a name="sagemaker-Type-training_session_runtime_SampleOperationConfig-computeLogprobs"></a>
The configuration for computing log-probabilities of prompt tokens without generating new text.
Type: [ComputeLogprobsConfig](API_training_session_runtime_ComputeLogprobsConfig.md) object
Required: No

 ** loadWeightsForSampling **   <a name="sagemaker-Type-training_session_runtime_SampleOperationConfig-loadWeightsForSampling"></a>
The configuration for loading model weights for inference and sampling without restoring optimizer state.
Type: [LoadWeightsForSamplingConfig](API_training_session_runtime_LoadWeightsForSamplingConfig.md) object
Required: No

 ** sample **   <a name="sagemaker-Type-training_session_runtime_SampleOperationConfig-sample"></a>
The configuration for generating text samples from the model.
Type: [SampleConfig](API_training_session_runtime_SampleConfig.md) object
Required: No

## See Also
<a name="API_training_session_runtime_SampleOperationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemakertrainingsessionruntime-2025-02-10/SampleOperationConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemakertrainingsessionruntime-2025-02-10/SampleOperationConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemakertrainingsessionruntime-2025-02-10/SampleOperationConfig)
