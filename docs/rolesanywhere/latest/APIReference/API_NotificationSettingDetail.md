---
source_url: https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_NotificationSettingDetail.html
---

# NotificationSettingDetail
<a name="API_NotificationSettingDetail"></a>

The state of a notification setting.

A notification setting includes information such as event name, threshold, status of the notification setting, and the channel to notify.

## Contents
<a name="API_NotificationSettingDetail_Contents"></a>

 ** enabled **   <a name="rolesanywhere-Type-NotificationSettingDetail-enabled"></a>
Indicates whether the notification setting is enabled.
Type: Boolean
Required: Yes

 ** event **   <a name="rolesanywhere-Type-NotificationSettingDetail-event"></a>
The event to which this notification setting is applied.
Type: String
Valid Values: `CA_CERTIFICATE_EXPIRY | END_ENTITY_CERTIFICATE_EXPIRY`
Required: Yes

 ** channel **   <a name="rolesanywhere-Type-NotificationSettingDetail-channel"></a>
The specified channel of notification. IAM Roles Anywhere uses CloudWatch metrics, EventBridge, and Health Dashboard to notify for an event.
In the absence of a specific channel, IAM Roles Anywhere applies this setting to 'ALL' channels.
Type: String
Valid Values: `ALL`
Required: No

 ** configuredBy **   <a name="rolesanywhere-Type-NotificationSettingDetail-configuredBy"></a>
The principal that configured the notification setting. For default settings configured by IAM Roles Anywhere, the value is `rolesanywhere.amazonaws.com`, and for customized notifications settings, it is the respective account ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: No

 ** threshold **   <a name="rolesanywhere-Type-NotificationSettingDetail-threshold"></a>
The number of days before a notification event.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 360.
Required: No

## See Also
<a name="API_NotificationSettingDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rolesanywhere-2018-05-10/NotificationSettingDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rolesanywhere-2018-05-10/NotificationSettingDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rolesanywhere-2018-05-10/NotificationSettingDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IAM Roles Anywhere. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rolesanywhere` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
