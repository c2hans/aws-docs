---
source_url: https://docs.aws.amazon.com/eventbridgev2/latest/APIReference/API_EventSourceConfiguration.html
---

# EventSourceConfiguration
<a name="API_EventSourceConfiguration"></a>

Discriminated EventSource configuration. Exactly one variant must be set.

## Contents
<a name="API_EventSourceConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** AwsServiceEventsConfiguration **   <a name="eventbridgev2-Type-EventSourceConfiguration-AwsServiceEventsConfiguration"></a>
Configuration for forwarding a single AWS service's events from the account's default event bus.
Type: [AwsServiceEventsSourceConfiguration](API_AwsServiceEventsSourceConfiguration.md) object
Required: No

 ** PartnerEventsConfiguration **   <a name="eventbridgev2-Type-EventSourceConfiguration-PartnerEventsConfiguration"></a>
Configuration for forwarding a partner event source's events through a managed partner event bus.
Type: [PartnerEventsSourceConfiguration](API_PartnerEventsSourceConfiguration.md) object
Required: No

## See Also
<a name="API_EventSourceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridgev2-2025-05-15/EventSourceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridgev2-2025-05-15/EventSourceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridgev2-2025-05-15/EventSourceConfiguration)
