---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_MemorySearchSummary.html
---

# MemorySearchSummary

A `SearchMemories` result: a matching memory and its relevance score.

## Contents
<a name="API_MemorySearchSummary_Contents"></a>

 ** memoryId **   <a name="opensearchmemory-Type-MemorySearchSummary-memoryId"></a>
The memory's ID, assigned by the service. Always present.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** content **   <a name="opensearchmemory-Type-MemorySearchSummary-content"></a>
The memory text.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 40000.
Required: No

 ** memoryType **   <a name="opensearchmemory-Type-MemorySearchSummary-memoryType"></a>
The memory type of the result.
Type: String
Valid Values: `SEMANTIC | SUMMARY | CUSTOM`
Required: No

 ** metadata **   <a name="opensearchmemory-Type-MemorySearchSummary-metadata"></a>
The memory's metadata tags. All values are strings. In a query, filter on a tag as `metadata.<key>`.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 15 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[a-zA-Z0-9_-]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[a-zA-Z0-9\s._:\/=+@-]*`
Required: No

 ** score **   <a name="opensearchmemory-Type-MemorySearchSummary-score"></a>
The relevance score of the result. A higher score is more relevant. Scores aren't normalized to a fixed range and can be greater than 1, so use them only to order results.
Type: Double
Required: No

 ** sourceEventIds **   <a name="opensearchmemory-Type-MemorySearchSummary-sourceEventIds"></a>
The IDs of the events the memory was derived from, without duplicates. Use them with `GetEvent` or `BatchGetEvent`, or to search those events' content with `SearchEvents` by filtering on `event_ids` in the query. Absent for a memory created directly with `CreateMemory`. A memory can be derived from several events. The service sets this value.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** strategyName **   <a name="opensearchmemory-Type-MemorySearchSummary-strategyName"></a>
The name of the strategy the memory belongs to, for example `user-facts`: the strategy `memoryStrategies` selects on in `SearchMemories`. Absent when the memory's strategy is no longer declared on the space, for example right after the strategy is deleted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** systemMetadata **   <a name="opensearchmemory-Type-MemorySearchSummary-systemMetadata"></a>
Provenance for the memory: the actor and session that own it, and when it was created and last updated. It is the same block that `ListMemories`, `GetMemory`, and `SearchEvents` return.
In a query, filter or sort on the timestamps as `system_metadata.created_at` and `system_metadata.updated_at`. Scope by owner with the top-level `actorId`, not in the query. Searching memories doesn't filter by session.
Absent when the service has no provenance for the memory.
Type: [SystemMetadata](API_SystemMetadata.md) object
Required: No

## See Also
<a name="API_MemorySearchSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchmemory-2026-08-24/MemorySearchSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchmemory-2026-08-24/MemorySearchSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchmemory-2026-08-24/MemorySearchSummary)
