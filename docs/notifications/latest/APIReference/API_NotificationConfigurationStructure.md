---
source_url: https://docs.aws.amazon.com/notifications/latest/APIReference/API_NotificationConfigurationStructure.html
---

# NotificationConfigurationStructure
<a name="API_NotificationConfigurationStructure"></a>

Contains the complete list of fields for a NotificationConfiguration.

## Contents
<a name="API_NotificationConfigurationStructure_Contents"></a>

 ** arn **   <a name="Notifications-Type-NotificationConfigurationStructure-arn"></a>
The Amazon Resource Name (ARN) of the `NotificationConfiguration` resource.
Type: String
Pattern: `arn:[a-z-]{3,10}:notifications::[0-9]{12}:configuration/[a-z0-9]{27}`
Required: Yes

 ** creationTime **   <a name="Notifications-Type-NotificationConfigurationStructure-creationTime"></a>
The creation time of the `NotificationConfiguration`.
Type: Timestamp
Required: Yes

 ** description **   <a name="Notifications-Type-NotificationConfigurationStructure-description"></a>
The description of the `NotificationConfiguration`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[^\u0001-\u001F\u007F-\u009F]*`
Required: Yes

 ** name **   <a name="Notifications-Type-NotificationConfigurationStructure-name"></a>
The name of the `NotificationConfiguration`. Supports RFC 3986's unreserved characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_\-]+`
Required: Yes

 ** status **   <a name="Notifications-Type-NotificationConfigurationStructure-status"></a>
The current status of the `NotificationConfiguration`.
Type: String
Valid Values: `ACTIVE | PARTIALLY_ACTIVE | INACTIVE | DELETING`
Required: Yes

 ** aggregationDuration **   <a name="Notifications-Type-NotificationConfigurationStructure-aggregationDuration"></a>
The aggregation preference of the `NotificationConfiguration`.
+ Values:
  +  `LONG`
    + Aggregate notifications for long periods of time (12 hours).
  +  `SHORT`
    + Aggregate notifications for short periods of time (5 minutes).
  +  `NONE`
    + Don't aggregate notifications.
Type: String
Valid Values: `LONG | SHORT | NONE`
Required: No

 ** subtype **   <a name="Notifications-Type-NotificationConfigurationStructure-subtype"></a>
The subtype of the notification configuration.
Type: String
Valid Values: `ACCOUNT | ADMIN_MANAGED`
Required: No

## See Also
<a name="API_NotificationConfigurationStructure_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/notifications-2018-05-10/NotificationConfigurationStructure)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/notifications-2018-05-10/NotificationConfigurationStructure)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/notifications-2018-05-10/NotificationConfigurationStructure)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS User Notifications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query notifications` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
