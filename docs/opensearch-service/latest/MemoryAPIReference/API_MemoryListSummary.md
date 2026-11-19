---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_MemoryListSummary.html
---

# MemoryListSummary

A summary of a memory, as returned by `ListMemories`: its ID, type, provenance, and tags. It doesn't include `content`. Call `GetMemory` for the full memory.

## Contents
<a name="API_MemoryListSummary_Contents"></a>

 ** memoryId **   <a name="opensearchmemory-Type-MemoryListSummary-memoryId"></a>
The memory's ID, assigned by the service. IDs are opaque, can contain hyphens and underscores, and can be up to 512 characters long.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** memoryType **   <a name="opensearchmemory-Type-MemoryListSummary-memoryType"></a>
The memory type.
Type: String
Valid Values: `SEMANTIC | SUMMARY | CUSTOM`
Required: Yes

 ** systemMetadata **   <a name="opensearchmemory-Type-MemoryListSummary-systemMetadata"></a>
Provenance for the memory: the owning actor and session, and when it was created and last updated. Always present, with both timestamps.
Type: [SystemMetadata](API_SystemMetadata.md) object
Required: Yes

 ** metadata **   <a name="opensearchmemory-Type-MemoryListSummary-metadata"></a>
The memory's metadata tags. All values are strings.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 15 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[a-zA-Z0-9_-]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[a-zA-Z0-9\s._:\/=+@-]*`
Required: No

 ** strategyName **   <a name="opensearchmemory-Type-MemoryListSummary-strategyName"></a>
The name of the strategy the memory belongs to, for example `user-facts`: the strategy `memoryStrategies` selects on in `ListMemories`. Absent when the memory's strategy is no longer declared on the space, for example right after the strategy is deleted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## See Also
<a name="API_MemoryListSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchmemory-2026-08-24/MemoryListSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchmemory-2026-08-24/MemoryListSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchmemory-2026-08-24/MemoryListSummary)
