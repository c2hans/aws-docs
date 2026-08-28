---
source_url: https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_NotificationSettingKey.html
---

# NotificationSettingKey
<a name="API_NotificationSettingKey"></a>

A notification setting key to reset. A notification setting key includes the event and the channel.

## Contents
<a name="API_NotificationSettingKey_Contents"></a>

 ** event **   <a name="rolesanywhere-Type-NotificationSettingKey-event"></a>
The notification setting event to reset.
Type: String
Valid Values: `CA_CERTIFICATE_EXPIRY | END_ENTITY_CERTIFICATE_EXPIRY`
Required: Yes

 ** channel **   <a name="rolesanywhere-Type-NotificationSettingKey-channel"></a>
The specified channel of notification.
Type: String
Valid Values: `ALL`
Required: No

## See Also
<a name="API_NotificationSettingKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rolesanywhere-2018-05-10/NotificationSettingKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rolesanywhere-2018-05-10/NotificationSettingKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rolesanywhere-2018-05-10/NotificationSettingKey)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IAM Roles Anywhere. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rolesanywhere` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
