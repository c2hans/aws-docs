---
source_url: https://docs.aws.amazon.com/eventbridgev2/latest/APIReference/API_EventBusV2Parameters.html
---

# EventBusV2Parameters
<a name="API_EventBusV2Parameters"></a>

Parameters for forwarding events to another EventBridge event bus.

## Contents
<a name="API_EventBusV2Parameters_Contents"></a>

 ** DeduplicationConfiguration **   <a name="eventbridgev2-Type-EventBusV2Parameters-DeduplicationConfiguration"></a>
Deduplication settings applied to the forwarded events on the downstream bus.
Type: [DeduplicationConfiguration](API_DeduplicationConfiguration.md) object
Required: No

 ** Metadata **   <a name="eventbridgev2-Type-EventBusV2Parameters-Metadata"></a>
Customer-defined metadata forwarded with each event.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** SystemMetadata **   <a name="eventbridgev2-Type-EventBusV2Parameters-SystemMetadata"></a>
Customer-controllable system metadata attached to each forwarded event.
Type: [EventBusV2SystemMetadata](API_EventBusV2SystemMetadata.md) object
Required: No

## See Also
<a name="API_EventBusV2Parameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridgev2-2025-05-15/EventBusV2Parameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridgev2-2025-05-15/EventBusV2Parameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridgev2-2025-05-15/EventBusV2Parameters)
