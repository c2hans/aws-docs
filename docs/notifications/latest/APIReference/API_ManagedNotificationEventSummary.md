---
source_url: https://docs.aws.amazon.com/notifications/latest/APIReference/API_ManagedNotificationEventSummary.html
---

# ManagedNotificationEventSummary
<a name="API_ManagedNotificationEventSummary"></a>

A short summary of a `ManagedNotificationEvent`. This is only used when listing managed notification events.

## Contents
<a name="API_ManagedNotificationEventSummary_Contents"></a>

 ** eventStatus **   <a name="Notifications-Type-ManagedNotificationEventSummary-eventStatus"></a>
The managed notification event status.
+ Values:
  +  `HEALTHY`
    + All `EventRules` are `ACTIVE`.
  +  `UNHEALTHY`
    + Some `EventRules` are `ACTIVE` and some are `INACTIVE`.
Type: String
Valid Values: `HEALTHY | UNHEALTHY`
Required: Yes

 ** messageComponents **   <a name="Notifications-Type-ManagedNotificationEventSummary-messageComponents"></a>
Contains the headline message component.
Type: [MessageComponentsSummary](API_MessageComponentsSummary.md) object
Required: Yes

 ** notificationType **   <a name="Notifications-Type-ManagedNotificationEventSummary-notificationType"></a>
The Type of event causing the notification.
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

 ** schemaVersion **   <a name="Notifications-Type-ManagedNotificationEventSummary-schemaVersion"></a>
The schema version of the `ManagedNotificationEvent`.
Type: String
Valid Values: `v1.0`
Required: Yes

 ** sourceEventMetadata **   <a name="Notifications-Type-ManagedNotificationEventSummary-sourceEventMetadata"></a>
Contains metadata about the event that caused the `ManagedNotificationEvent`.
Type: [ManagedSourceEventMetadataSummary](API_ManagedSourceEventMetadataSummary.md) object
Required: Yes

## See Also
<a name="API_ManagedNotificationEventSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/notifications-2018-05-10/ManagedNotificationEventSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/notifications-2018-05-10/ManagedNotificationEventSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/notifications-2018-05-10/ManagedNotificationEventSummary)
