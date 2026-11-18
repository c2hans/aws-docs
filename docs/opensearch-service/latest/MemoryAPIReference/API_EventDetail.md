---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_EventDetail.html
---

# EventDetail
<a name="API_EventDetail"></a>

The stored event's identifiers. Call `GetEvent` for the payload.

## Contents
<a name="API_EventDetail_Contents"></a>

 ** actorId **   <a name="opensearchmemory-Type-EventDetail-actorId"></a>
The ID of the actor the event belongs to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`
Required: Yes

 ** eventId **   <a name="opensearchmemory-Type-EventDetail-eventId"></a>
The event's ID, assigned by the service. Use it with `GetEvent` and `DeleteEvent`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** eventTimestamp **   <a name="opensearchmemory-Type-EventDetail-eventTimestamp"></a>
When the event occurred: the value supplied, or the time the request was received.
Type: Timestamp
Required: Yes

 ** sessionId **   <a name="opensearchmemory-Type-EventDetail-sessionId"></a>
The ID of the session the event belongs to, including one the service generated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`
Required: Yes

 ** spaceId **   <a name="opensearchmemory-Type-EventDetail-spaceId"></a>
The ID of the space.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `sp-[a-f0-9]{12}`
Required: Yes

## See Also
<a name="API_EventDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchmemory-2026-08-24/EventDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchmemory-2026-08-24/EventDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchmemory-2026-08-24/EventDetail)
