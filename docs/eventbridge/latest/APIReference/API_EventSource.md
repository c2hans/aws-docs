---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_EventSource.html
---

# EventSource
<a name="API_EventSource"></a>

A partner event source is created by an SaaS partner. If a customer creates a partner event bus that matches this event source, that AWS account can receive events from the partner's applications or services.

## Contents
<a name="API_EventSource_Contents"></a>

 ** Arn **   <a name="eventbridge-Type-EventSource-Arn"></a>
The ARN of the event source.
Type: String
Required: No

 ** CreatedBy **   <a name="eventbridge-Type-EventSource-CreatedBy"></a>
The name of the partner that created the event source.
Type: String
Required: No

 ** CreationTime **   <a name="eventbridge-Type-EventSource-CreationTime"></a>
The date and time the event source was created.
Type: Timestamp
Required: No

 ** ExpirationTime **   <a name="eventbridge-Type-EventSource-ExpirationTime"></a>
The date and time that the event source will expire, if the AWS account doesn't create a matching event bus for it.
Type: Timestamp
Required: No

 ** Name **   <a name="eventbridge-Type-EventSource-Name"></a>
The name of the event source.
Type: String
Required: No

 ** State **   <a name="eventbridge-Type-EventSource-State"></a>
The state of the event source. If it is ACTIVE, you have already created a matching event bus for this event source, and that event bus is active. If it is PENDING, either you haven't yet created a matching event bus, or that event bus is deactivated. If it is DELETED, you have created a matching event bus, but the event source has since been deleted.
Type: String
Valid Values: `PENDING | ACTIVE | DELETED`
Required: No

## See Also
<a name="API_EventSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/EventSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/EventSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/EventSource)
