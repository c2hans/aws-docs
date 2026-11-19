---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_StrategySelector.html
---

# StrategySelector

A memory type and, optionally, specific strategy names of that type. A space can hold several strategies of the same type, so the type and its names are given together.

## Contents
<a name="API_StrategySelector_Contents"></a>

 ** memoryType **   <a name="opensearchmemory-Type-StrategySelector-memoryType"></a>
The memory type to search or list.
Type: String
Valid Values: `SEMANTIC | SUMMARY | CUSTOM`
Required: Yes

 ** memoryStrategyNames **   <a name="opensearchmemory-Type-StrategySelector-memoryStrategyNames"></a>
Specific strategy names of `memoryType`. Omit it to include every strategy of that type.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## See Also
<a name="API_StrategySelector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchmemory-2026-08-24/StrategySelector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchmemory-2026-08-24/StrategySelector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchmemory-2026-08-24/StrategySelector)
