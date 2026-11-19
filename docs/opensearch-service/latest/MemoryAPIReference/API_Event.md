---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_Event.html
---

# Event

An event, including its payload.

## Contents
<a name="API_Event_Contents"></a>

 ** actorId **   <a name="opensearchmemory-Type-Event-actorId"></a>
The ID of the actor the event belongs to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`
Required: Yes

 ** eventId **   <a name="opensearchmemory-Type-Event-eventId"></a>
The event's ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** eventTimestamp **   <a name="opensearchmemory-Type-Event-eventTimestamp"></a>
The time the event occurred.
Type: Timestamp
Required: Yes

 ** payload **   <a name="opensearchmemory-Type-Event-payload"></a>
The event's content, as submitted to `CreateEvent`.
Type: [EventPayload](API_EventPayload.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** sessionId **   <a name="opensearchmemory-Type-Event-sessionId"></a>
The ID of the session the event belongs to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`
Required: Yes

 ** spaceId **   <a name="opensearchmemory-Type-Event-spaceId"></a>
The ID of the space.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `sp-[a-f0-9]{12}`
Required: Yes

 ** metadata **   <a name="opensearchmemory-Type-Event-metadata"></a>
The event's metadata tags, as supplied to `CreateEvent`. May be empty.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 15 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[a-zA-Z0-9_-]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[a-zA-Z0-9\s._:\/=+@-]*`
Required: No

## See Also
<a name="API_Event_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchmemory-2026-08-24/Event)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchmemory-2026-08-24/Event)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchmemory-2026-08-24/Event)
