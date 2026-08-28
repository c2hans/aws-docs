---
source_url: https://docs.aws.amazon.com/notifications/latest/APIReference/API_NotificationEventOverview.html
---

# NotificationEventOverview
<a name="API_NotificationEventOverview"></a>

Describes a short summary of a `NotificationEvent`. This is only used when listing notification events.

## Contents
<a name="API_NotificationEventOverview_Contents"></a>

 ** arn **   <a name="Notifications-Type-NotificationEventOverview-arn"></a>
The Amazon Resource Name (ARN) of the resource.
Type: String
Pattern: `arn:[a-z-]{3,10}:notifications:[-.a-z0-9]{1,63}:[0-9]{12}:configuration/[a-z0-9]{27}/event/[a-z0-9]{27}`
Required: Yes

 ** creationTime **   <a name="Notifications-Type-NotificationEventOverview-creationTime"></a>
The creation time of the `NotificationEvent`.
Type: Timestamp
Required: Yes

 ** notificationConfigurationArn **   <a name="Notifications-Type-NotificationEventOverview-notificationConfigurationArn"></a>
The ARN of the `NotificationConfiguration`.
Type: String
Pattern: `arn:[a-z-]{3,10}:notifications::[0-9]{12}:configuration/[a-z0-9]{27}`
Required: Yes

 ** notificationEvent **   <a name="Notifications-Type-NotificationEventOverview-notificationEvent"></a>
Refers to a `NotificationEventSummary` object.
Similar in structure to `content` in the `GetNotificationEvent` response.
Type: [NotificationEventSummary](API_NotificationEventSummary.md) object
Required: Yes

 ** relatedAccount **   <a name="Notifications-Type-NotificationEventOverview-relatedAccount"></a>
The account name containing the `NotificationHub`.
Type: String
Pattern: `\d{12}`
Required: Yes

 ** aggregateNotificationEventArn **   <a name="Notifications-Type-NotificationEventOverview-aggregateNotificationEventArn"></a>
The ARN of the `aggregatedNotificationEventArn` to match.
Type: String
Pattern: `arn:[a-z-]{3,10}:notifications:[-.a-z0-9]{1,63}:[0-9]{12}:configuration/[a-z0-9]{27}/event/[a-z0-9]{27}`
Required: No

 ** aggregationEventType **   <a name="Notifications-Type-NotificationEventOverview-aggregationEventType"></a>
The `NotificationConfiguration`'s aggregation type.
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

 ** aggregationSummary **   <a name="Notifications-Type-NotificationEventOverview-aggregationSummary"></a>
Provides an aggregated summary data for notification events.
Type: [AggregationSummary](API_AggregationSummary.md) object
Required: No

 ** organizationalUnitId **   <a name="Notifications-Type-NotificationEventOverview-organizationalUnitId"></a>
The unique identifier of the organizational unit in the notification event overview.
Type: String
Pattern: `(Root|r-[0-9a-z]{4,32}|ou-[0-9a-z]{4,32}-[a-z0-9]{8,32})`
Required: No

## See Also
<a name="API_NotificationEventOverview_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/notifications-2018-05-10/NotificationEventOverview)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/notifications-2018-05-10/NotificationEventOverview)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/notifications-2018-05-10/NotificationEventOverview)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS User Notifications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query notifications` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
