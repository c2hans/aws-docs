---
source_url: https://docs.aws.amazon.com/notifications/latest/APIReference/API_ManagedNotificationChildEventSummary.html
---

# ManagedNotificationChildEventSummary
<a name="API_ManagedNotificationChildEventSummary"></a>

Describes a short summary and metadata for a `ManagedNotificationChildEvent`.

## Contents
<a name="API_ManagedNotificationChildEventSummary_Contents"></a>

 ** aggregationDetail **   <a name="Notifications-Type-ManagedNotificationChildEventSummary-aggregationDetail"></a>
Provides detailed information about the dimensions used for event summarization and aggregation.
Type: [AggregationDetail](API_AggregationDetail.md) object
Required: Yes

 ** eventStatus **   <a name="Notifications-Type-ManagedNotificationChildEventSummary-eventStatus"></a>
The perceived nature of the event.
+ Values:
  +  `HEALTHY`
    + All EventRules are `ACTIVE` and any call can be run.
  +  `UNHEALTHY`
    + Some EventRules are `ACTIVE` and some are `INACTIVE`. Any call can be run.
Type: String
Valid Values: `HEALTHY | UNHEALTHY`
Required: Yes

 ** messageComponents **   <a name="Notifications-Type-ManagedNotificationChildEventSummary-messageComponents"></a>
Contains the headline message component.
Type: [MessageComponentsSummary](API_MessageComponentsSummary.md) object
Required: Yes

 ** notificationType **   <a name="Notifications-Type-ManagedNotificationChildEventSummary-notificationType"></a>
The Type of the event causing this notification.
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

 ** schemaVersion **   <a name="Notifications-Type-ManagedNotificationChildEventSummary-schemaVersion"></a>
The schema version of the `ManagedNotificationChildEvent`.
Type: String
Valid Values: `v1.0`
Required: Yes

 ** sourceEventMetadata **   <a name="Notifications-Type-ManagedNotificationChildEventSummary-sourceEventMetadata"></a>
Contains all event metadata present identically across all `NotificationEvents`. All fields are present in Source Events via Eventbridge.
Type: [ManagedSourceEventMetadataSummary](API_ManagedSourceEventMetadataSummary.md) object
Required: Yes

## See Also
<a name="API_ManagedNotificationChildEventSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/notifications-2018-05-10/ManagedNotificationChildEventSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/notifications-2018-05-10/ManagedNotificationChildEventSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/notifications-2018-05-10/ManagedNotificationChildEventSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS User Notifications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query notifications` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
