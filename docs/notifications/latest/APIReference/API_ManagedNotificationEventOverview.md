---
source_url: https://docs.aws.amazon.com/notifications/latest/APIReference/API_ManagedNotificationEventOverview.html
---

# ManagedNotificationEventOverview
<a name="API_ManagedNotificationEventOverview"></a>

Describes an overview and metadata for a ManagedNotificationEvent.

## Contents
<a name="API_ManagedNotificationEventOverview_Contents"></a>

 ** arn **   <a name="Notifications-Type-ManagedNotificationEventOverview-arn"></a>
The Amazon Resource Name (ARN) of the ManagedNotificationEvent.
Type: String
Pattern: `arn:[a-z-]{3,10}:notifications::[0-9]{12}:managed-notification-configuration/category/[a-zA-Z0-9\-]{3,64}/sub-category/[a-zA-Z0-9\-]{3,64}/event/[a-z0-9]{27}`
Required: Yes

 ** creationTime **   <a name="Notifications-Type-ManagedNotificationEventOverview-creationTime"></a>
The creation time of the `ManagedNotificationEvent`.
Type: Timestamp
Required: Yes

 ** managedNotificationConfigurationArn **   <a name="Notifications-Type-ManagedNotificationEventOverview-managedNotificationConfigurationArn"></a>
The Amazon Resource Name (ARN) of the `ManagedNotificationConfiguration`.
Type: String
Pattern: `arn:[a-z-]{3,10}:notifications::[0-9]{12}:managed-notification-configuration/category/[a-zA-Z0-9\-]{3,64}/sub-category/[a-zA-Z0-9\-]{3,64}`
Required: Yes

 ** notificationEvent **   <a name="Notifications-Type-ManagedNotificationEventOverview-notificationEvent"></a>

Type: [ManagedNotificationEventSummary](API_ManagedNotificationEventSummary.md) object
Required: Yes

 ** relatedAccount **   <a name="Notifications-Type-ManagedNotificationEventOverview-relatedAccount"></a>
The account that related to the `ManagedNotificationEvent`.
Type: String
Pattern: `\d{12}`
Required: Yes

 ** aggregatedNotificationRegions **   <a name="Notifications-Type-ManagedNotificationEventOverview-aggregatedNotificationRegions"></a>
The list of the regions where the aggregated notifications in this `NotificationEvent` originated.
Type: Array of strings
Length Constraints: Minimum length of 2. Maximum length of 25.
Pattern: `([a-z]{1,4})-([a-z]{1,15}-)+([0-9])`
Required: No

 ** aggregationEventType **   <a name="Notifications-Type-ManagedNotificationEventOverview-aggregationEventType"></a>
The notifications aggregation type.
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

 ** aggregationSummary **   <a name="Notifications-Type-ManagedNotificationEventOverview-aggregationSummary"></a>
Provides additional information about the aggregation key.
Type: [AggregationSummary](API_AggregationSummary.md) object
Required: No

 ** organizationalUnitId **   <a name="Notifications-Type-ManagedNotificationEventOverview-organizationalUnitId"></a>
The Organizational Unit Id that an AWS account belongs to.
Type: String
Pattern: `(Root|r-[0-9a-z]{4,32}|ou-[0-9a-z]{4,32}-[a-z0-9]{8,32})`
Required: No

## See Also
<a name="API_ManagedNotificationEventOverview_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/notifications-2018-05-10/ManagedNotificationEventOverview)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/notifications-2018-05-10/ManagedNotificationEventOverview)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/notifications-2018-05-10/ManagedNotificationEventOverview)
