---
source_url: https://docs.aws.amazon.com/notifications/latest/APIReference/API_ManagedNotificationChildEvent.html
---

# ManagedNotificationChildEvent
<a name="API_ManagedNotificationChildEvent"></a>

A notification-focused representation of an event. They contain semantic information used to create aggregated or non-aggregated end-user notifications.

## Contents
<a name="API_ManagedNotificationChildEvent_Contents"></a>

 ** aggregateManagedNotificationEventArn **   <a name="Notifications-Type-ManagedNotificationChildEvent-aggregateManagedNotificationEventArn"></a>
The Amazon Resource Name (ARN) of the ManagedNotificationEvent that is associated with this Managed Notification Child Event.
Type: String
Pattern: `arn:[a-z-]{3,10}:notifications::[0-9]{12}:managed-notification-configuration/category/[a-zA-Z0-9\-]{3,64}/sub-category/[a-zA-Z0-9\-]{3,64}/event/[a-z0-9]{27}`
Required: Yes

 ** id **   <a name="Notifications-Type-ManagedNotificationChildEvent-id"></a>
The unique identifier for a Managed Notification Child Event.
Type: String
Pattern: `[a-z0-9]{27}`
Required: Yes

 ** messageComponents **   <a name="Notifications-Type-ManagedNotificationChildEvent-messageComponents"></a>
Describes the components of a notification message.
Type: [MessageComponents](API_MessageComponents.md) object
Required: Yes

 ** notificationType **   <a name="Notifications-Type-ManagedNotificationChildEvent-notificationType"></a>
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

 ** schemaVersion **   <a name="Notifications-Type-ManagedNotificationChildEvent-schemaVersion"></a>
The schema version of the Managed Notification Child Event.
Type: String
Valid Values: `v1.0`
Required: Yes

 ** textParts **   <a name="Notifications-Type-ManagedNotificationChildEvent-textParts"></a>
A list of text values.
Type: String to [TextPartValue](API_TextPartValue.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `[A-Za-z0-9_]+`
Required: Yes

 ** aggregationDetail **   <a name="Notifications-Type-ManagedNotificationChildEvent-aggregationDetail"></a>
Provides detailed information about the dimensions used for event summarization and aggregation.
Type: [AggregationDetail](API_AggregationDetail.md) object
Required: No

 ** endTime **   <a name="Notifications-Type-ManagedNotificationChildEvent-endTime"></a>
The end time of the event.
Type: Timestamp
Required: No

 ** eventStatus **   <a name="Notifications-Type-ManagedNotificationChildEvent-eventStatus"></a>
The assesed nature of the event.
+ Values:
  +  `HEALTHY`
    + All `EventRules` are `ACTIVE`.
  +  `UNHEALTHY`
    + Some `EventRules` are `ACTIVE` and some are `INACTIVE`.
Type: String
Valid Values: `HEALTHY | UNHEALTHY`
Required: No

 ** organizationalUnitId **   <a name="Notifications-Type-ManagedNotificationChildEvent-organizationalUnitId"></a>
The Organizational Unit Id that an AWS account belongs to.
Type: String
Pattern: `(Root|r-[0-9a-z]{4,32}|ou-[0-9a-z]{4,32}-[a-z0-9]{8,32})`
Required: No

 ** sourceEventDetailUrl **   <a name="Notifications-Type-ManagedNotificationChildEvent-sourceEventDetailUrl"></a>
The source event URL.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.
Required: No

 ** sourceEventDetailUrlDisplayText **   <a name="Notifications-Type-ManagedNotificationChildEvent-sourceEventDetailUrlDisplayText"></a>
The detailed URL for the source event.
Type: String
Required: No

 ** startTime **   <a name="Notifications-Type-ManagedNotificationChildEvent-startTime"></a>
The notification event start time.
Type: Timestamp
Required: No

## See Also
<a name="API_ManagedNotificationChildEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/notifications-2018-05-10/ManagedNotificationChildEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/notifications-2018-05-10/ManagedNotificationChildEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/notifications-2018-05-10/ManagedNotificationChildEvent)
