---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_EventSearchSummary.html
---

# EventSearchSummary
<a name="API_EventSearchSummary"></a>

A `SearchEvents` result: the matching chunk of an event and its provenance. Unlike `EventSummary` from `ListEvents`, it has a relevance score and the matched content, but not the full payload.

## Contents
<a name="API_EventSearchSummary_Contents"></a>

 ** eventId **   <a name="opensearchmemory-Type-EventSearchSummary-eventId"></a>
The ID of the event that the chunk belongs to. Use it with `GetEvent` or `DeleteEvent`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** matchedContent **   <a name="opensearchmemory-Type-EventSearchSummary-matchedContent"></a>
The text of the matching chunk.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 40000.
Required: No

 ** metadata **   <a name="opensearchmemory-Type-EventSearchSummary-metadata"></a>
The event's metadata tags. All values are strings. In a query, filter on a tag as `metadata.<key>`.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 15 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[a-zA-Z0-9_-]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[a-zA-Z0-9\s._:\/=+@-]*`
Required: No

 ** score **   <a name="opensearchmemory-Type-EventSearchSummary-score"></a>
The relevance score of the result. A higher score is more relevant. Scores aren't normalized to a fixed range and can be greater than 1, so use them only to order results.
Type: Double
Required: No

 ** systemMetadata **   <a name="opensearchmemory-Type-EventSearchSummary-systemMetadata"></a>
Provenance for the chunk: the owning actor and session, and when it was created and last updated. It is the same block that `ListMemories` and `SearchMemories` return. Event chunks are never modified, so `updatedAt` always equals `createdAt`.
Absent when the service has no provenance for the chunk.
Type: [SystemMetadata](API_SystemMetadata.md) object
Required: No

## See Also
<a name="API_EventSearchSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchmemory-2026-08-24/EventSearchSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchmemory-2026-08-24/EventSearchSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchmemory-2026-08-24/EventSearchSummary)
