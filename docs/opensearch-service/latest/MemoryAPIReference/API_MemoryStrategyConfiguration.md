---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_MemoryStrategyConfiguration.html
---

# MemoryStrategyConfiguration

Settings for a memory strategy. The defaults described here apply when you create a strategy. In `UpdateSpace`, a member you omit for a kept strategy keeps its current value.

## Contents
<a name="API_MemoryStrategyConfiguration_Contents"></a>

 ** consolidationEnabled **   <a name="opensearchmemory-Type-MemoryStrategyConfiguration-consolidationEnabled"></a>
Specifies whether the strategy consolidates memories. With consolidation, each new memory is compared with similar stored memories, and the service adds it, updates a stored memory, or skips it, so duplicate or contradicting facts don't accumulate. Without it, every extracted memory is stored as a new memory, which costs less and keeps a full history.
The default is on for every strategy type.
Type: Boolean
Required: No

 ** extractEveryNMessages **   <a name="opensearchmemory-Type-MemoryStrategyConfiguration-extractEveryNMessages"></a>
Extract once this many messages have accumulated, from 1 to 1000. Lower values extract more often, in smaller batches. The default is 12.
Messages accumulate until the first of `extractEveryNMessages`, `extractEveryNTokens`, and `idleTimeoutSeconds` is reached. The service then extracts them together in one pass.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** extractEveryNTokens **   <a name="opensearchmemory-Type-MemoryStrategyConfiguration-extractEveryNTokens"></a>
Extract once this many tokens of conversation have accumulated, from 1 to 80,000, however few messages that takes. Use it to bound how much text one extraction call carries when message sizes vary widely. Omit it to bound a batch only by `extractEveryNMessages`, `idleTimeoutSeconds`, and the service's maximum batch size.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 80000.
Required: No

 ** extractionPrompt **   <a name="opensearchmemory-Type-MemoryStrategyConfiguration-extractionPrompt"></a>
Instructions that define what a `CUSTOM` strategy extracts, up to 30,720 characters. Required for a `CUSTOM` strategy: `CreateSpace` and `UpdateSpace` fail with `ValidationException` if a `CUSTOM` strategy has none.
Only `CUSTOM` strategies use it. `SEMANTIC` and `SUMMARY` strategies use built-in instructions and don't take an extraction prompt.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 30720.
Required: No

 ** extractionSeedRecentN **   <a name="opensearchmemory-Type-MemoryStrategyConfiguration-extractionSeedRecentN"></a>
How many of the strategy's most recent stored memories to include in the extraction prompt, from 0 to 20. If you omit this or set it to 0, the service uses its default: no seeding for most strategy types, and the 10 most recent memories for a `SUMMARY` strategy when neither seed setting is given. When this and `extractionSeedTopK` are both set, the two sets of memories are combined without duplicates.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 20.
Required: No

 ** extractionSeedTopK **   <a name="opensearchmemory-Type-MemoryStrategyConfiguration-extractionSeedTopK"></a>
How many of the strategy's stored memories that are most relevant to the conversation to include in the extraction prompt, from 0 to 20, to improve extraction and reduce duplicates. If you omit this or set it to 0, the service uses its default (see `extractionSeedRecentN`). When this and `extractionSeedRecentN` are both set, the two sets of memories are combined without duplicates.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 20.
Required: No

 ** idleTimeoutSeconds **   <a name="opensearchmemory-Type-MemoryStrategyConfiguration-idleTimeoutSeconds"></a>
Extract what has accumulated once the conversation has been idle for this many seconds, from 1 to 86,400. The default is 60. This is what extracts the end of a conversation that stops. Raise it when the pauses in your conversations are longer than that, so that one exchange isn't split across several extraction passes.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 86400.
Required: No

## See Also
<a name="API_MemoryStrategyConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchmemory-2026-08-24/MemoryStrategyConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchmemory-2026-08-24/MemoryStrategyConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchmemory-2026-08-24/MemoryStrategyConfiguration)
