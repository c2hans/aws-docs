---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_PushNotificationConfiguration.html
---

# PushNotificationConfiguration
<a name="API_messaging-chime_PushNotificationConfiguration"></a>

The push notification configuration of the message.

## Contents
<a name="API_messaging-chime_PushNotificationConfiguration_Contents"></a>

 ** Body **   <a name="chimesdk-Type-messaging-chime_PushNotificationConfiguration-Body"></a>
The body of the push notification.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 150.
Pattern: `[\s\S]*`
Required: No

 ** Title **   <a name="chimesdk-Type-messaging-chime_PushNotificationConfiguration-Title"></a>
The title of the push notification.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `.*`
Required: No

 ** Type **   <a name="chimesdk-Type-messaging-chime_PushNotificationConfiguration-Type"></a>
Enum value that indicates the type of the push notification for a message. `DEFAULT`: Normal mobile push notification. `VOIP`: VOIP mobile push notification.
Type: String
Valid Values: `DEFAULT | VOIP`
Required: No

## See Also
<a name="API_messaging-chime_PushNotificationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-messaging-2021-05-15/PushNotificationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-messaging-2021-05-15/PushNotificationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-messaging-2021-05-15/PushNotificationConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
