---
source_url: https://docs.aws.amazon.com/eventbridgev2/latest/APIReference/API_EventBusV2SystemMetadata.html
---

# EventBusV2SystemMetadata
<a name="API_EventBusV2SystemMetadata"></a>

Customer-controllable system metadata attached to events forwarded to the downstream event bus.

## Contents
<a name="API_EventBusV2SystemMetadata_Contents"></a>

 ** DeduplicationId **   <a name="eventbridgev2-Type-EventBusV2SystemMetadata-DeduplicationId"></a>
Deduplication ID for FIFO deduplication on the downstream bus. Accepts a literal or a JSONata expression.
Type: String
Required: No

 ** EventGroupId **   <a name="eventbridgev2-Type-EventBusV2SystemMetadata-EventGroupId"></a>
Event group ID for FIFO ordering on the downstream bus. Accepts a literal or a JSONata expression.
Type: String
Required: No

## See Also
<a name="API_EventBusV2SystemMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridgev2-2025-05-15/EventBusV2SystemMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridgev2-2025-05-15/EventBusV2SystemMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridgev2-2025-05-15/EventBusV2SystemMetadata)
