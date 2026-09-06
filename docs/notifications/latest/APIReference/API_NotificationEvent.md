---
source_url: https://docs.aws.amazon.com/notifications/latest/APIReference/API_NotificationEvent.html
---

# NotificationEvent
<a name="API_NotificationEvent"></a>

A `NotificationEvent` is a notification-focused representation of an event. They contain semantic information used by Channels to create end-user notifications.

## Contents
<a name="API_NotificationEvent_Contents"></a>

 ** id **   <a name="Notifications-Type-NotificationEvent-id"></a>
The unique identifier for a `NotificationEvent`.
Type: String
Pattern: `[a-z0-9]{27}`
Required: Yes

 ** media **   <a name="Notifications-Type-NotificationEvent-media"></a>
A list of media elements.
Type: Array of [MediaElement](API_MediaElement.md) objects
Required: Yes

 ** messageComponents **   <a name="Notifications-Type-NotificationEvent-messageComponents"></a>
Describes the components of a notification message.
Type: [MessageComponents](API_MessageComponents.md) object
Required: Yes

 ** notificationType **   <a name="Notifications-Type-NotificationEvent-notificationType"></a>
The type of event causing the notification.
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

 ** schemaVersion **   <a name="Notifications-Type-NotificationEvent-schemaVersion"></a>
The schema version of the Notification Event.
Type: String
Valid Values: `v1.0`
Required: Yes

 ** sourceEventMetadata **   <a name="Notifications-Type-NotificationEvent-sourceEventMetadata"></a>
The source event metadata.
Type: [SourceEventMetadata](API_SourceEventMetadata.md) object
Required: Yes

 ** textParts **   <a name="Notifications-Type-NotificationEvent-textParts"></a>
A list of text values.
Type: String to [TextPartValue](API_TextPartValue.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `[A-Za-z0-9_]+`
Required: Yes

 ** aggregateNotificationEventArn **   <a name="Notifications-Type-NotificationEvent-aggregateNotificationEventArn"></a>
If the value of `aggregationEventType` is not `NONE`, this is the Amazon Resource Event (ARN) of the parent aggregate notification.
This is omitted if notification isn't aggregated.
Type: String
Pattern: `arn:[a-z-]{3,10}:notifications:[-.a-z0-9]{1,63}:[0-9]{12}:configuration/[a-z0-9]{27}/event/[a-z0-9]{27}`
Required: No

 ** aggregationEventType **   <a name="Notifications-Type-NotificationEvent-aggregationEventType"></a>
The aggregation type of the `NotificationConfiguration`.
+ Values:
  +  `AGGREGATE`
    + The notification event is an aggregate notification. Aggregate notifications summarize grouped events over a specified time period.
  +  `CHILD`
    + Some `EventRules` are `ACTIVE` and some are `INACTIVE`. Any call can be run.
  +  `NONE`
    + The notification isn't aggregated.
Type: String
Valid Values: `AGGREGATE | CHILD | NONE`
Required: No

 ** aggregationSummary **   <a name="Notifications-Type-NotificationEvent-aggregationSummary"></a>
Provides additional information about how multiple notifications are grouped.
Type: [AggregationSummary](API_AggregationSummary.md) object
Required: No

 ** endTime **   <a name="Notifications-Type-NotificationEvent-endTime"></a>
The end time of the event.
Type: Timestamp
Required: No

 ** eventStatus **   <a name="Notifications-Type-NotificationEvent-eventStatus"></a>
The assessed nature of the event.
+ Values:
  +  `HEALTHY`
    + All `EventRules` are `ACTIVE` and any call can be run.
  +  `UNHEALTHY`
    + Some `EventRules` are `ACTIVE` and some are `INACTIVE`. Any call can be run.
Type: String
Valid Values: `HEALTHY | UNHEALTHY`
Required: No

 ** organizationalUnitId **   <a name="Notifications-Type-NotificationEvent-organizationalUnitId"></a>
The unique identifier of the organizational unit associated with the notification event.
Type: String
Pattern: `(Root|r-[0-9a-z]{4,32}|ou-[0-9a-z]{4,32}-[a-z0-9]{8,32})`
Required: No

 ** sourceEventDetailUrl **   <a name="Notifications-Type-NotificationEvent-sourceEventDetailUrl"></a>
The source event URL.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.
Pattern: `(https?)://.*`
Required: No

 ** sourceEventDetailUrlDisplayText **   <a name="Notifications-Type-NotificationEvent-sourceEventDetailUrlDisplayText"></a>
The detailed URL for the source event.
Type: String
Required: No

 ** startTime **   <a name="Notifications-Type-NotificationEvent-startTime"></a>
The notification event start time.
Type: Timestamp
Required: No

## See Also
<a name="API_NotificationEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/notifications-2018-05-10/NotificationEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/notifications-2018-05-10/NotificationEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/notifications-2018-05-10/NotificationEvent)
