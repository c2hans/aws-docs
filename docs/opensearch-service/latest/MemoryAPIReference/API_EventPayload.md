---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_EventPayload.html
---

# EventPayload

The event content. Exactly one member must be set.

## Contents
<a name="API_EventPayload_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** blob **   <a name="opensearchmemory-Type-EventPayload-blob"></a>
A document stored in Amazon S3, such as a PDF, PNG, or JPEG file.
Type: [BlobPayload](API_BlobPayload.md) object
Required: No

 ** conversational **   <a name="opensearchmemory-Type-EventPayload-conversational"></a>
Conversation turns.
Type: [ConversationalPayload](API_ConversationalPayload.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** structuredData **   <a name="opensearchmemory-Type-EventPayload-structuredData"></a>
Structured (non-conversational) content, for example a deployment result that an agent should remember.
Type: [StructuredDataPayload](API_StructuredDataPayload.md) object
Required: No

## See Also
<a name="API_EventPayload_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchmemory-2026-08-24/EventPayload)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchmemory-2026-08-24/EventPayload)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchmemory-2026-08-24/EventPayload)
