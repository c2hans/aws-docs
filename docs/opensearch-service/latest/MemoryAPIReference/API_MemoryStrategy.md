---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_MemoryStrategy.html
---

# MemoryStrategy

A memory strategy: how a space extracts one kind of memory from its events.

## Contents
<a name="API_MemoryStrategy_Contents"></a>

 ** type **   <a name="opensearchmemory-Type-MemoryStrategy-type"></a>
The type of memory the strategy extracts.
Type: String
Valid Values: `SEMANTIC | SUMMARY | CUSTOM`
Required: Yes

 ** configuration **   <a name="opensearchmemory-Type-MemoryStrategy-configuration"></a>
Settings for the strategy. When you create a strategy, omit it to use the defaults for the strategy's type.
A `CUSTOM` strategy must set `extractionPrompt`.
Type: [MemoryStrategyConfiguration](API_MemoryStrategyConfiguration.md) object
Required: No

 ** description **   <a name="opensearchmemory-Type-MemoryStrategy-description"></a>
A description of the strategy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** name **   <a name="opensearchmemory-Type-MemoryStrategy-name"></a>
A name for the strategy, unique within the space. Omit it to have the service generate one from the type, for example `semantic_1`. The name must be 1 to 64 characters: letters, digits, periods, hyphens, and underscores, starting with a letter or digit. A strategy's name can't be changed, and the strategy's memories are stored under it: a strategy added under a new name starts with no memories.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9][A-Za-z0-9_.-]*`
Required: No

## See Also
<a name="API_MemoryStrategy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchmemory-2026-08-24/MemoryStrategy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchmemory-2026-08-24/MemoryStrategy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchmemory-2026-08-24/MemoryStrategy)
