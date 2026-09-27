---
source_url: https://docs.aws.amazon.com/eventbridgev2/latest/APIReference/API_PutRawEventsRequestEntry.html
---

# PutRawEventsRequestEntry
<a name="API_PutRawEventsRequestEntry"></a>

A single event entry in a raw publish request.

## Contents
<a name="API_PutRawEventsRequestEntry_Contents"></a>

 ** Data **   <a name="eventbridgev2-Type-PutRawEventsRequestEntry-Data"></a>
The event data as a base64-encoded blob. Supports binary formats.
Type: Base64-encoded binary data object
Required: Yes

 ** SystemMetadata **   <a name="eventbridgev2-Type-PutRawEventsRequestEntry-SystemMetadata"></a>
Structured system metadata with defined properties.
Type: [PutRawEventsSystemMetadata](API_PutRawEventsSystemMetadata.md) object
Required: Yes

 ** Metadata **   <a name="eventbridgev2-Type-PutRawEventsRequestEntry-Metadata"></a>
Metadata key-value pairs you define. Keys must be 1-128 characters and must not contain "/".
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 100 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[^/]+`
Value Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_PutRawEventsRequestEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridgev2-2025-05-15/PutRawEventsRequestEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridgev2-2025-05-15/PutRawEventsRequestEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridgev2-2025-05-15/PutRawEventsRequestEntry)
