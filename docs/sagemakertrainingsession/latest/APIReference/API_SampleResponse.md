---
source_url: https://docs.aws.amazon.com/sagemakertrainingsession/latest/APIReference/API_SampleResponse.html
---

# SampleResponse
<a name="API_SampleResponse"></a>

The response containing generated samples and optional log-probabilities.

## Contents
<a name="API_SampleResponse_Contents"></a>

 ** sequences **   <a name="sagemakertrainingsession-Type-SampleResponse-sequences"></a>
The list of generated sequences.
Type: Array of [SampledSequence](API_SampledSequence.md) objects
Required: Yes

 ** promptLogprobs **   <a name="sagemakertrainingsession-Type-SampleResponse-promptLogprobs"></a>
The per-token log-probabilities for the input prompt. Populated only when `includePromptLogprobs` is true.
Type: Array of doubles
Required: No

 ** topkPromptLogprobs **   <a name="sagemakertrainingsession-Type-SampleResponse-topkPromptLogprobs"></a>
The top-k log-probabilities per prompt token, as a list of lists. Populated only when `topkPromptLogprobs` is greater than 0.
Type: Array of arrays of [TokenLogprob](API_TokenLogprob.md) objects
Required: No

## See Also
<a name="API_SampleResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemakertrainingsessionruntime-2025-02-10/SampleResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemakertrainingsessionruntime-2025-02-10/SampleResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemakertrainingsessionruntime-2025-02-10/SampleResponse)
