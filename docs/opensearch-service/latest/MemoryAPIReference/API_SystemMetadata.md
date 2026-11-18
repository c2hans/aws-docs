---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_SystemMetadata.html
---

# SystemMetadata
<a name="API_SystemMetadata"></a>

System-generated provenance for a memory or event: the owning actor and session, and the creation and last-update timestamps. `SearchMemories`, `SearchEvents`, `ListMemories`, and `GetMemory` return the same block.

 `ListMemories` and `GetMemory` always return `createdAt` and `updatedAt`. The search operations return what is recorded and omit the block when nothing is.

In a query, the timestamps are `system_metadata.created_at` and `system_metadata.updated_at`. Scope by owner with the top-level parameters (`actorId` on the search operations, `actorIds` on `ListMemories`) and `sessionIds` (`SearchEvents` and `ListMemories`). The search operations reject actor and session fields inside the query or sort.

## Contents
<a name="API_SystemMetadata_Contents"></a>

 ** actorId **   <a name="opensearchmemory-Type-SystemMetadata-actorId"></a>
The owning actor. Absent when none was recorded.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`
Required: No

 ** createdAt **   <a name="opensearchmemory-Type-SystemMetadata-createdAt"></a>
When the record was created. Always present on `ListMemories` and `GetMemory`. It can be absent from search results.
Type: Timestamp
Required: No

 ** sessionId **   <a name="opensearchmemory-Type-SystemMetadata-sessionId"></a>
The owning session. Absent when none was recorded.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`
Required: No

 ** updatedAt **   <a name="opensearchmemory-Type-SystemMetadata-updatedAt"></a>
When the record was last updated. Equals `createdAt` for a record that has never been updated, and always for a `SearchEvents` result.
Type: Timestamp
Required: No

## See Also
<a name="API_SystemMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchmemory-2026-08-24/SystemMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchmemory-2026-08-24/SystemMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchmemory-2026-08-24/SystemMetadata)
