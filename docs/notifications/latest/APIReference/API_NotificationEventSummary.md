---
source_url: https://docs.aws.amazon.com/notifications/latest/APIReference/API_NotificationEventSummary.html
---

# NotificationEventSummary
<a name="API_NotificationEventSummary"></a>

Describes a short summary and metadata for a `NotificationEvent`.

## Contents
<a name="API_NotificationEventSummary_Contents"></a>

 ** eventStatus **   <a name="Notifications-Type-NotificationEventSummary-eventStatus"></a>
Provides additional information about the current status of the `NotificationEvent`.
+ Values:
  +  `HEALTHY`
    + All `EventRules` are `ACTIVE`.
  +  `UNHEALTHY`
    + Some `EventRules` are `ACTIVE` and some are `INACTIVE`.
Type: String
Valid Values: `HEALTHY | UNHEALTHY`
Required: Yes

 ** messageComponents **   <a name="Notifications-Type-NotificationEventSummary-messageComponents"></a>
The message components of a notification event.
Type: [MessageComponentsSummary](API_MessageComponentsSummary.md) object
Required: Yes

 ** notificationType **   <a name="Notifications-Type-NotificationEventSummary-notificationType"></a>
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

 ** schemaVersion **   <a name="Notifications-Type-NotificationEventSummary-schemaVersion"></a>
The schema version of the Notification Event.
Type: String
Valid Values: `v1.0`
Required: Yes

 ** sourceEventMetadata **   <a name="Notifications-Type-NotificationEventSummary-sourceEventMetadata"></a>
The source event metadata.
Type: [SourceEventMetadataSummary](API_SourceEventMetadataSummary.md) object
Required: Yes

## See Also
<a name="API_NotificationEventSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/notifications-2018-05-10/NotificationEventSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/notifications-2018-05-10/NotificationEventSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/notifications-2018-05-10/NotificationEventSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS User Notifications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query notifications` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
