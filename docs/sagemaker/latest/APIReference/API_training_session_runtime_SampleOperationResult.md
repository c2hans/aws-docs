---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_training_session_runtime_SampleOperationResult.html
---

# SampleOperationResult
<a name="API_training_session_runtime_SampleOperationResult"></a>

The result of a completed sampling operation. Exactly one member is populated, corresponding to the operation type that was submitted.

## Contents
<a name="API_training_session_runtime_SampleOperationResult_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** computeLogprobs **   <a name="sagemaker-Type-training_session_runtime_SampleOperationResult-computeLogprobs"></a>
The computed log-probabilities for the prompt tokens.
Type: [ComputeLogprobsResult](API_training_session_runtime_ComputeLogprobsResult.md) object
Required: No

 ** loadWeightsForSampling **   <a name="sagemaker-Type-training_session_runtime_SampleOperationResult-loadWeightsForSampling"></a>
The result from loading weights for sampling.
Type: [LoadWeightsForSamplingResult](API_training_session_runtime_LoadWeightsForSamplingResult.md) object
Required: No

 ** sample **   <a name="sagemaker-Type-training_session_runtime_SampleOperationResult-sample"></a>
The generated text samples from the model.
Type: [SampleResponse](API_training_session_runtime_SampleResponse.md) object
Required: No

## See Also
<a name="API_training_session_runtime_SampleOperationResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemakertrainingsessionruntime-2025-02-10/SampleOperationResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemakertrainingsessionruntime-2025-02-10/SampleOperationResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemakertrainingsessionruntime-2025-02-10/SampleOperationResult)
