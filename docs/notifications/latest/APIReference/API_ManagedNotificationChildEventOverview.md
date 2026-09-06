---
source_url: https://docs.aws.amazon.com/notifications/latest/APIReference/API_ManagedNotificationChildEventOverview.html
---

# ManagedNotificationChildEventOverview
<a name="API_ManagedNotificationChildEventOverview"></a>

Describes an overview and metadata for a `ManagedNotificationChildEvent`.

## Contents
<a name="API_ManagedNotificationChildEventOverview_Contents"></a>

 ** aggregateManagedNotificationEventArn **   <a name="Notifications-Type-ManagedNotificationChildEventOverview-aggregateManagedNotificationEventArn"></a>
The Amazon Resource Name (ARN) of the ManagedNotificationEvent that is associated with this `ManagedNotificationChildEvent`.
Type: String
Pattern: `arn:[a-z-]{3,10}:notifications::[0-9]{12}:managed-notification-configuration/category/[a-zA-Z0-9\-]{3,64}/sub-category/[a-zA-Z0-9\-]{3,64}/event/[a-z0-9]{27}`
Required: Yes

 ** arn **   <a name="Notifications-Type-ManagedNotificationChildEventOverview-arn"></a>
The Amazon Resource Name (ARN) of the `ManagedNotificationChildEvent`.
Type: String
Pattern: `arn:[a-z-]{3,10}:notifications::[0-9]{12}:managed-notification-configuration/category/[a-zA-Z0-9\-]{3,64}/sub-category/[a-zA-Z0-9\-]{3,64}/event/[a-z0-9]{27}`
Required: Yes

 ** childEvent **   <a name="Notifications-Type-ManagedNotificationChildEventOverview-childEvent"></a>
The content of the `ManagedNotificationChildEvent`.
Type: [ManagedNotificationChildEventSummary](API_ManagedNotificationChildEventSummary.md) object
Required: Yes

 ** creationTime **   <a name="Notifications-Type-ManagedNotificationChildEventOverview-creationTime"></a>
The creation time of the `ManagedNotificationChildEvent`.
Type: Timestamp
Required: Yes

 ** managedNotificationConfigurationArn **   <a name="Notifications-Type-ManagedNotificationChildEventOverview-managedNotificationConfigurationArn"></a>
The Amazon Resource Name (ARN) of the `ManagedNotificationConfiguration`.
Type: String
Pattern: `arn:[-.a-z0-9]{1,63}:notifications::[0-9]{12}:managed-notification-configuration/category/[a-zA-Z0-9\-]{3,64}/sub-category/[a-zA-Z0-9\-]{3,64}`
Required: Yes

 ** relatedAccount **   <a name="Notifications-Type-ManagedNotificationChildEventOverview-relatedAccount"></a>
The account that related to the `ManagedNotificationChildEvent`.
Type: String
Pattern: `\d{12}`
Required: Yes

 ** organizationalUnitId **   <a name="Notifications-Type-ManagedNotificationChildEventOverview-organizationalUnitId"></a>
The Organizational Unit Id that an AWS account belongs to.
Type: String
Pattern: `(Root|r-[0-9a-z]{4,32}|ou-[0-9a-z]{4,32}-[a-z0-9]{8,32})`
Required: No

## See Also
<a name="API_ManagedNotificationChildEventOverview_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/notifications-2018-05-10/ManagedNotificationChildEventOverview)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/notifications-2018-05-10/ManagedNotificationChildEventOverview)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/notifications-2018-05-10/ManagedNotificationChildEventOverview)
