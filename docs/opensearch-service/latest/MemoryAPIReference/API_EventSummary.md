---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_EventSummary.html
---

# EventSummary

A summary of an event, as returned by `ListEvents`. It doesn't include the payload.

## Contents
<a name="API_EventSummary_Contents"></a>

 ** eventId **   <a name="opensearchmemory-Type-EventSummary-eventId"></a>
The event's ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** eventTimestamp **   <a name="opensearchmemory-Type-EventSummary-eventTimestamp"></a>
The time the event occurred.
Type: Timestamp
Required: Yes

 ** metadata **   <a name="opensearchmemory-Type-EventSummary-metadata"></a>
The event's metadata tags, as supplied to `CreateEvent`. May be empty.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 15 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[a-zA-Z0-9_-]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[a-zA-Z0-9\s._:\/=+@-]*`
Required: No

## See Also
<a name="API_EventSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchmemory-2026-08-24/EventSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchmemory-2026-08-24/EventSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchmemory-2026-08-24/EventSummary)
