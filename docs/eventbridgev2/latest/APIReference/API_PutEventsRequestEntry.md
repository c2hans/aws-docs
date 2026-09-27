---
source_url: https://docs.aws.amazon.com/eventbridgev2/latest/APIReference/API_PutEventsRequestEntry.html
---

# PutEventsRequestEntry
<a name="API_PutEventsRequestEntry"></a>

A single event entry in a PutEvents request.

## Contents
<a name="API_PutEventsRequestEntry_Contents"></a>

 ** DetailType **   <a name="eventbridgev2-Type-PutEventsRequestEntry-DetailType"></a>
Free-form detail-type classifying an event within its source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** Source **   <a name="eventbridgev2-Type-PutEventsRequestEntry-Source"></a>
The source of the event. The `aws.` value prefix is service-reserved and cannot be used as a value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** Detail **   <a name="eventbridgev2-Type-PutEventsRequestEntry-Detail"></a>
The event payload, as a valid JSON string.
Type: String
Required: No

 ** Resources **   <a name="eventbridgev2-Type-PutEventsRequestEntry-Resources"></a>
ARNs of resources the event concerns. Included in the event delivered to subscribers.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** SystemMetadata **   <a name="eventbridgev2-Type-PutEventsRequestEntry-SystemMetadata"></a>
System metadata for PutEvents entries. ContentType is not applicable (always application/eventbridge\+json, set server-side).
Type: [PutEventsSystemMetadata](API_PutEventsSystemMetadata.md) object
Required: No

 ** Time **   <a name="eventbridgev2-Type-PutEventsRequestEntry-Time"></a>
The time the event occurred. Defaults to the time the service receives the event when omitted.
Type: Timestamp
Required: No

## See Also
<a name="API_PutEventsRequestEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridgev2-2025-05-15/PutEventsRequestEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridgev2-2025-05-15/PutEventsRequestEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridgev2-2025-05-15/PutEventsRequestEntry)
