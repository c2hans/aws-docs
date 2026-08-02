---
source_url: https://docs.aws.amazon.com/notifications/latest/APIReference/API_NotificationHubOverview.html
---

# NotificationHubOverview
<a name="API_NotificationHubOverview"></a>

Describes an overview of a `NotificationHub`.

A `NotificationConfiguration` is an account-level setting used to select the Regions where you want to store, process and replicate your notifications.

## Contents
<a name="API_NotificationHubOverview_Contents"></a>

 ** creationTime **   <a name="Notifications-Type-NotificationHubOverview-creationTime"></a>
The date and time the `NotificationHubOverview` was created.
Type: Timestamp
Required: Yes

 ** notificationHubRegion **   <a name="Notifications-Type-NotificationHubOverview-notificationHubRegion"></a>
The Region of the resource.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 25.
Pattern: `([a-z]{1,4})-([a-z]{1,15}-)+([0-9])`
Required: Yes

 ** statusSummary **   <a name="Notifications-Type-NotificationHubOverview-statusSummary"></a>
The status summary of the resource.
Type: [NotificationHubStatusSummary](API_NotificationHubStatusSummary.md) object
Required: Yes

 ** lastActivationTime **   <a name="Notifications-Type-NotificationHubOverview-lastActivationTime"></a>
The most recent time this `NotificationHub` had an `ACTIVE` status.
Type: Timestamp
Required: No

## See Also
<a name="API_NotificationHubOverview_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/notifications-2018-05-10/NotificationHubOverview)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/notifications-2018-05-10/NotificationHubOverview)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/notifications-2018-05-10/NotificationHubOverview)
