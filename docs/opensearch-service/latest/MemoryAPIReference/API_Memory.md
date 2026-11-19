---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_Memory.html
---

# Memory

A memory, as returned by `GetMemory` and `UpdateMemory`. Unlike `MemoryListSummary` it includes `content`, and unlike `MemorySearchSummary` it has no relevance score.

## Contents
<a name="API_Memory_Contents"></a>

 ** content **   <a name="opensearchmemory-Type-Memory-content"></a>
The memory text.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 40000.
Required: Yes

 ** memoryId **   <a name="opensearchmemory-Type-Memory-memoryId"></a>
The memory's ID, assigned by the service.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** memoryType **   <a name="opensearchmemory-Type-Memory-memoryType"></a>
The memory type.
Type: String
Valid Values: `SEMANTIC | SUMMARY | CUSTOM`
Required: Yes

 ** systemMetadata **   <a name="opensearchmemory-Type-Memory-systemMetadata"></a>
Provenance for the memory: the owning actor and session, and when it was created and last updated. Always present. `updatedAt` equals `createdAt` for a memory that has never been updated.
Type: [SystemMetadata](API_SystemMetadata.md) object
Required: Yes

 ** metadata **   <a name="opensearchmemory-Type-Memory-metadata"></a>
The memory's metadata tags. All values are strings. May be empty.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 15 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[a-zA-Z0-9_-]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[a-zA-Z0-9\s._:\/=+@-]*`
Required: No

 ** strategyName **   <a name="opensearchmemory-Type-Memory-strategyName"></a>
The name of the strategy the memory belongs to, for example `user-facts`. A space can hold several strategies of the same type, so this tells them apart. Absent when the memory's strategy is no longer declared on the space, for example right after the strategy is deleted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## See Also
<a name="API_Memory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchmemory-2026-08-24/Memory)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchmemory-2026-08-24/Memory)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchmemory-2026-08-24/Memory)
