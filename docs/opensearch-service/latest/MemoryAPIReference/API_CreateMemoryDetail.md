---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_CreateMemoryDetail.html
---

# CreateMemoryDetail
<a name="API_CreateMemoryDetail"></a>

The memory as `CreateMemory` acknowledges it: its identifiers. The memory isn't searchable yet when the call returns.

## Contents
<a name="API_CreateMemoryDetail_Contents"></a>

 ** actorId **   <a name="opensearchmemory-Type-CreateMemoryDetail-actorId"></a>
The ID of the actor the memory belongs to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`
Required: Yes

 ** memoryId **   <a name="opensearchmemory-Type-CreateMemoryDetail-memoryId"></a>
The final ID of the memory. Until the memory is indexed, `GetMemory`, `UpdateMemory`, and `DeleteMemory` return `ResourceNotFoundException` for it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** name **   <a name="opensearchmemory-Type-CreateMemoryDetail-name"></a>
The name of the strategy the memory belongs to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** sessionId **   <a name="opensearchmemory-Type-CreateMemoryDetail-sessionId"></a>
The ID of the session the memory belongs to, including one the service generated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`
Required: Yes

 ** spaceId **   <a name="opensearchmemory-Type-CreateMemoryDetail-spaceId"></a>
The ID of the space.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `sp-[a-f0-9]{12}`
Required: Yes

## See Also
<a name="API_CreateMemoryDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchmemory-2026-08-24/CreateMemoryDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchmemory-2026-08-24/CreateMemoryDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchmemory-2026-08-24/CreateMemoryDetail)
