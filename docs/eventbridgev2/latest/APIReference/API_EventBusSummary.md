---
source_url: https://docs.aws.amazon.com/eventbridgev2/latest/APIReference/API_EventBusSummary.html
---

# EventBusSummary
<a name="API_EventBusSummary"></a>

Summary of an event bus, as returned by ListEventBuses.

## Contents
<a name="API_EventBusSummary_Contents"></a>

 ** CreationTime **   <a name="eventbridgev2-Type-EventBusSummary-CreationTime"></a>
The time the event bus was created.
Type: Timestamp
Required: No

 ** Description **   <a name="eventbridgev2-Type-EventBusSummary-Description"></a>
Free-text description. Used by every resource type that has one: event buses, subscribers, and event sources.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Pattern: `[^\u0000-\u001F\u007F-\u009F\u2028\u2029]*(?![\s\S]).*`
Required: No

 ** EventBusAccountId **   <a name="eventbridgev2-Type-EventBusSummary-EventBusAccountId"></a>
AWS Account Id.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** EventBusArn **   <a name="eventbridgev2-Type-EventBusSummary-EventBusArn"></a>
The Amazon Resource Name (ARN) that uniquely identifies an event bus.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws(-[a-z0-9]+)*:events:[a-z][a-z0-9]*(-[a-z0-9]+)*:([0-9]{12}):event-busv2\/[A-Za-z0-9][\.\-_A-Za-z0-9]{0,255}\/[a-z0-9]{25}`
Required: No

 ** LastModifiedTime **   <a name="eventbridgev2-Type-EventBusSummary-LastModifiedTime"></a>
The time the event bus was last modified.
Type: Timestamp
Required: No

 ** Name **   <a name="eventbridgev2-Type-EventBusSummary-Name"></a>
Name of an event bus. The first character must be alphanumeric; the remaining characters may also include '.', '-', and '\_'. The grammar matches the name segment of EventBusArn (event-busv2/<name>/<id>), so every valid name can be represented in the bus's ARN. The same type is used everywhere a bus name appears.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9][\.\-_A-Za-z0-9]*`
Required: No

 ** State **   <a name="eventbridgev2-Type-EventBusSummary-State"></a>
Lifecycle state of an event bus.
+ CREATING: Bus creation is in progress.
+ CREATE\_FAILED: Bus creation failed; see StateReason. The bus cannot be recovered or recreated in place: delete it with DeleteEventBus, then create a new bus.
+ ACTIVE: Bus is fully operational and can accept events.
+ UPDATING: Bus update is in progress.
+ UPDATE\_FAILED: Bus update failed; the bus remains operational with its previous configuration.
+ DELETING: Bus deletion is actively in progress.
+ DELETE\_FAILED: Bus deletion failed; see StateReason. Retry DeleteEventBus after removing subscribers and event sources.
Type: String
Valid Values: `CREATING | CREATE_FAILED | UPDATING | UPDATE_FAILED | DELETING | ACTIVE | DELETE_FAILED`
Required: No

 ** StateReason **   <a name="eventbridgev2-Type-EventBusSummary-StateReason"></a>
Human-readable explanation of why an event bus is in its current State. Omitted when the bus is in a normal operational state (ACTIVE). It stands in for the error response an asynchronous failure cannot return, so it applies only to resources with an asynchronous lifecycle: event buses. EventSources and subscribers are provisioned synchronously and report failures directly on the request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

## See Also
<a name="API_EventBusSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridgev2-2025-05-15/EventBusSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridgev2-2025-05-15/EventBusSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridgev2-2025-05-15/EventBusSummary)
