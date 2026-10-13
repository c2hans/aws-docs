---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_training_session_runtime_SamplingParams.html
---

# SamplingParams
<a name="API_training_session_runtime_SamplingParams"></a>

The parameters controlling the text generation sampling strategy.

## Contents
<a name="API_training_session_runtime_SamplingParams_Contents"></a>

 ** maxTokens **   <a name="sagemaker-Type-training_session_runtime_SamplingParams-maxTokens"></a>
The maximum number of tokens to generate per sample.
Type: Integer
Valid Range: Minimum value of 512. Maximum value of 131072.
Required: Yes

 ** seed **   <a name="sagemaker-Type-training_session_runtime_SamplingParams-seed"></a>
The random seed for reproducible sampling. When set, the same seed with the same input produces deterministic outputs.
Type: Integer
Required: No

 ** stop **   <a name="sagemaker-Type-training_session_runtime_SamplingParams-stop"></a>
The list of stop sequences that terminate generation when encountered in the output.
Type: Array of strings
Required: No

 ** temperature **   <a name="sagemaker-Type-training_session_runtime_SamplingParams-temperature"></a>
The sampling temperature controlling randomness. Higher values produce more diverse outputs.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 2.
Required: No

 ** topK **   <a name="sagemaker-Type-training_session_runtime_SamplingParams-topK"></a>
The number of highest-probability vocabulary tokens to keep for top-k filtering. Set to -1 to disable.
Type: Integer
Required: No

 ** topP **   <a name="sagemaker-Type-training_session_runtime_SamplingParams-topP"></a>
The cumulative probability threshold for nucleus (top-p) sampling. Only tokens with cumulative probability below this threshold are considered.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 1.
Required: No

## See Also
<a name="API_training_session_runtime_SamplingParams_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemakertrainingsessionruntime-2025-02-10/SamplingParams)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemakertrainingsessionruntime-2025-02-10/SamplingParams)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemakertrainingsessionruntime-2025-02-10/SamplingParams)
