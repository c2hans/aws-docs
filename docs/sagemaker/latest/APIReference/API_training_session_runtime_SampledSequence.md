---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_training_session_runtime_SampledSequence.html
---

# SampledSequence
<a name="API_training_session_runtime_SampledSequence"></a>

A single generated sequence from the model.

## Contents
<a name="API_training_session_runtime_SampledSequence_Contents"></a>

 ** stopReason **   <a name="sagemaker-Type-training_session_runtime_SampledSequence-stopReason"></a>
The reason why generation stopped. A value of `stop` indicates a stop sequence was encountered. A value of `length` indicates the maximum token limit was reached.
Type: String
Valid Values: `stop | length`
Required: Yes

 ** tokens **   <a name="sagemaker-Type-training_session_runtime_SampledSequence-tokens"></a>
The token IDs of the generated sequence.
Type: Array of integers
Required: Yes

 ** logprobs **   <a name="sagemaker-Type-training_session_runtime_SampledSequence-logprobs"></a>
The per-token log-probabilities for the generated tokens.
Type: Array of doubles
Required: No

 ** tokenUsage **   <a name="sagemaker-Type-training_session_runtime_SampledSequence-tokenUsage"></a>
The token usage statistics for this individual sample.
Type: [SampleTokenUsage](API_training_session_runtime_SampleTokenUsage.md) object
Required: No

## See Also
<a name="API_training_session_runtime_SampledSequence_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemakertrainingsessionruntime-2025-02-10/SampledSequence)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemakertrainingsessionruntime-2025-02-10/SampledSequence)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemakertrainingsessionruntime-2025-02-10/SampledSequence)
