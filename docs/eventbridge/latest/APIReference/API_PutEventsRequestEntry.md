---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutEventsRequestEntry.html
---

# PutEventsRequestEntry
<a name="API_PutEventsRequestEntry"></a>

Represents an event to be submitted.

## Contents
<a name="API_PutEventsRequestEntry_Contents"></a>

 ** Detail **   <a name="eventbridge-Type-PutEventsRequestEntry-Detail"></a>
A valid JSON object. There is no other schema imposed. The JSON object may contain fields and nested sub-objects.
 `Detail`, `DetailType`, and `Source` are required for EventBridge to successfully send an event to an event bus. If you include event entries in a request that do not include each of those properties, EventBridge fails that entry. If you submit a request in which *none* of the entries have each of these properties, EventBridge fails the entire request.
Type: String
Required: No

 ** DetailType **   <a name="eventbridge-Type-PutEventsRequestEntry-DetailType"></a>
Free-form string, with a maximum of 128 characters, used to decide what fields to expect in the event detail.
 `Detail`, `DetailType`, and `Source` are required for EventBridge to successfully send an event to an event bus. If you include event entries in a request that do not include each of those properties, EventBridge fails that entry. If you submit a request in which *none* of the entries have each of these properties, EventBridge fails the entire request.
Type: String
Required: No

 ** EventBusName **   <a name="eventbridge-Type-PutEventsRequestEntry-EventBusName"></a>
The name or ARN of the event bus to receive the event. Only the rules that are associated with this event bus are used to match the event. If you omit this, the default event bus is used.
If you're using a global endpoint with a custom bus, you can enter either the name or Amazon Resource Name (ARN) of the event bus in either the primary or secondary Region here. EventBridge then determines the corresponding event bus in the other Region based on the endpoint referenced by the `EndpointId`. Specifying the event bus ARN is preferred.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `(arn:aws[\w-]*:events:[a-z]+-[a-z]+-[\w-]+:[0-9]{12}:event-bus\/)?[\.\-_A-Za-z0-9]+`
Required: No

 ** Resources **   <a name="eventbridge-Type-PutEventsRequestEntry-Resources"></a>
 AWS resources, identified by Amazon Resource Name (ARN), which the event primarily concerns. Any number, including zero, may be present.
Type: Array of strings
Length Constraints: Maximum length of 2048.
Required: No

 ** Source **   <a name="eventbridge-Type-PutEventsRequestEntry-Source"></a>
The source of the event.
 `Detail`, `DetailType`, and `Source` are required for EventBridge to successfully send an event to an event bus. If you include event entries in a request that do not include each of those properties, EventBridge fails that entry. If you submit a request in which *none* of the entries have each of these properties, EventBridge fails the entire request.
Type: String
Required: No

 ** Time **   <a name="eventbridge-Type-PutEventsRequestEntry-Time"></a>
The time stamp of the event, per [RFC3339](https://www.rfc-editor.org/rfc/rfc3339.txt). If no time stamp is provided, the time stamp of the [PutEvents](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutEvents.html) call is used.
Type: Timestamp
Required: No

 ** TraceHeader **   <a name="eventbridge-Type-PutEventsRequestEntry-TraceHeader"></a>
An AWS X-Ray trace header, which is an http header (X-Amzn-Trace-Id) that contains the trace-id associated with the event.
To learn more about X-Ray trace headers, see [Tracing header](https://docs.aws.amazon.com/xray/latest/devguide/xray-concepts.html#xray-concepts-tracingheader) in the AWS X-Ray Developer Guide.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

## See Also
<a name="API_PutEventsRequestEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/PutEventsRequestEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/PutEventsRequestEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/PutEventsRequestEntry)
