---
source_url: https://docs.aws.amazon.com/notifications/latest/APIReference/API_ManagedNotificationEvent.html
---

# ManagedNotificationEvent
<a name="API_ManagedNotificationEvent"></a>

A notification-focused representation of an event. They contain semantic information used by AccountContacts or Additional Channels to create end-user notifications.

## Contents
<a name="API_ManagedNotificationEvent_Contents"></a>

 ** id **   <a name="Notifications-Type-ManagedNotificationEvent-id"></a>
Unique identifier for a `ManagedNotificationEvent`.
Type: String
Pattern: `[a-z0-9]{27}`
Required: Yes

 ** messageComponents **   <a name="Notifications-Type-ManagedNotificationEvent-messageComponents"></a>
Describes the components of a notification message.
Type: [MessageComponents](API_MessageComponents.md) object
Required: Yes

 ** notificationType **   <a name="Notifications-Type-ManagedNotificationEvent-notificationType"></a>
The nature of the event causing this notification.
+ Values:
  +  `ALERT`
    + A notification about an event where something was triggered, initiated, reopened, deployed, or a threshold was breached.
  +  `WARNING`
    + A notification about an event where an issue is about to arise. For example, something is approaching a threshold.
  +  `ANNOUNCEMENT`
    + A notification about an important event. For example, a step in a workflow or escalation path or that a workflow was updated.
  +  `INFORMATIONAL`
    + A notification about informational messages. For example, recommendations, service announcements, or reminders.
Type: String
Valid Values: `ALERT | WARNING | ANNOUNCEMENT | INFORMATIONAL`
Required: Yes

 ** schemaVersion **   <a name="Notifications-Type-ManagedNotificationEvent-schemaVersion"></a>
Version of the `ManagedNotificationEvent` schema.
Type: String
Valid Values: `v1.0`
Required: Yes

 ** textParts **   <a name="Notifications-Type-ManagedNotificationEvent-textParts"></a>
A list of text values.
Type: String to [TextPartValue](API_TextPartValue.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `[A-Za-z0-9_]+`
Required: Yes

 ** aggregationEventType **   <a name="Notifications-Type-ManagedNotificationEvent-aggregationEventType"></a>
The notifications aggregation type.
Type: String
Valid Values: `AGGREGATE | CHILD | NONE`
Required: No

 ** aggregationSummary **   <a name="Notifications-Type-ManagedNotificationEvent-aggregationSummary"></a>
Provides additional information about the aggregation key.
Type: [AggregationSummary](API_AggregationSummary.md) object
Required: No

 ** endTime **   <a name="Notifications-Type-ManagedNotificationEvent-endTime"></a>
The end time of the notification event.
Type: Timestamp
Required: No

 ** eventStatus **   <a name="Notifications-Type-ManagedNotificationEvent-eventStatus"></a>
The status of an event.
+ Values:
  +  `HEALTHY`
    + All EventRules are `ACTIVE` and any call can be run.
  +  `UNHEALTHY`
    + Some EventRules are `ACTIVE` and some are `INACTIVE`. Any call can be run.
Type: String
Valid Values: `HEALTHY | UNHEALTHY`
Required: No

 ** organizationalUnitId **   <a name="Notifications-Type-ManagedNotificationEvent-organizationalUnitId"></a>
The Organizational Unit Id that an AWS account belongs to.
Type: String
Pattern: `(Root|r-[0-9a-z]{4,32}|ou-[0-9a-z]{4,32}-[a-z0-9]{8,32})`
Required: No

 ** sourceEventDetailUrl **   <a name="Notifications-Type-ManagedNotificationEvent-sourceEventDetailUrl"></a>
URL defined by Source Service to be used by notification consumers to get additional information about event.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.
Pattern: `(https?)://.*`
Required: No

 ** sourceEventDetailUrlDisplayText **   <a name="Notifications-Type-ManagedNotificationEvent-sourceEventDetailUrlDisplayText"></a>
Text that needs to be hyperlinked with the sourceEventDetailUrl. For example, the description of the sourceEventDetailUrl.
Type: String
Required: No

 ** startTime **   <a name="Notifications-Type-ManagedNotificationEvent-startTime"></a>
The earliest time of events to return from this call.
Type: Timestamp
Required: No

## See Also
<a name="API_ManagedNotificationEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/notifications-2018-05-10/ManagedNotificationEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/notifications-2018-05-10/ManagedNotificationEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/notifications-2018-05-10/ManagedNotificationEvent)
