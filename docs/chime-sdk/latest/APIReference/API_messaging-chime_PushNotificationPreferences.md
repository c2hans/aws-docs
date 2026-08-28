---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_PushNotificationPreferences.html
---

# PushNotificationPreferences
<a name="API_messaging-chime_PushNotificationPreferences"></a>

The channel membership preferences for push notification.

## Contents
<a name="API_messaging-chime_PushNotificationPreferences_Contents"></a>

 ** AllowNotifications **   <a name="chimesdk-Type-messaging-chime_PushNotificationPreferences-AllowNotifications"></a>
Enum value that indicates which push notifications to send to the requested member of a channel. `ALL` sends all push notifications, `NONE` sends no push notifications, `FILTERED` sends only filtered push notifications.
Type: String
Valid Values: `ALL | NONE | FILTERED`
Required: Yes

 ** FilterRule **   <a name="chimesdk-Type-messaging-chime_PushNotificationPreferences-FilterRule"></a>
The simple JSON object used to send a subset of a push notification to the requested member.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `[\s\S]*`
Required: No

## See Also
<a name="API_messaging-chime_PushNotificationPreferences_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-messaging-2021-05-15/PushNotificationPreferences)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-messaging-2021-05-15/PushNotificationPreferences)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-messaging-2021-05-15/PushNotificationPreferences)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
