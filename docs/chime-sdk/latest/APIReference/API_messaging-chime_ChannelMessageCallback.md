---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ChannelMessageCallback.html
---

# ChannelMessageCallback
<a name="API_messaging-chime_ChannelMessageCallback"></a>

Stores information about a callback.

## Contents
<a name="API_messaging-chime_ChannelMessageCallback_Contents"></a>

 ** MessageId **   <a name="chimesdk-Type-messaging-chime_ChannelMessageCallback-MessageId"></a>
The message ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[-_a-zA-Z0-9]*`
Required: Yes

 ** Content **   <a name="chimesdk-Type-messaging-chime_ChannelMessageCallback-Content"></a>
The message content. For Amazon Lex V2 bot responses, this field holds a list of messages originating from the bot. For more information, refer to [Processing responses from an AppInstanceBot](https://docs.aws.amazon.com/chime-sdk/latest/dg/appinstance-bots#process-response.html) in the *Amazon Chime SDK Messaging Developer Guide*.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `[\s\S]*`
Required: No

 ** ContentType **   <a name="chimesdk-Type-messaging-chime_ChannelMessageCallback-ContentType"></a>
The content type of the call-back message. For Amazon Lex V2 bot responses, the content type is `application/amz-chime-lex-msgs` for success responses and `application/amz-chime-lex-error` for failure responses. For more information, refer to [Processing responses from an AppInstanceBot](https://docs.aws.amazon.com/chime-sdk/latest/dg/appinstance-bots#process-response.html) in the *Amazon Chime SDK Messaging Developer Guide*.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 45.
Pattern: `[\s\S]*`
Required: No

 ** MessageAttributes **   <a name="chimesdk-Type-messaging-chime_ChannelMessageCallback-MessageAttributes"></a>
The attributes for the channel message. For Amazon Lex V2 bot responses, the attributes are mapped to specific fields from the bot. For more information, refer to [Processing responses from an AppInstanceBot](https://docs.aws.amazon.com/chime-sdk/latest/dg/appinstance-bots#process-response.html) in the *Amazon Chime SDK Messaging Developer Guide*.
Type: String to [MessageAttributeValue](API_messaging-chime_MessageAttributeValue.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Key Pattern: `[\s\S]*`
Required: No

 ** Metadata **   <a name="chimesdk-Type-messaging-chime_ChannelMessageCallback-Metadata"></a>
The message metadata.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** PushNotification **   <a name="chimesdk-Type-messaging-chime_ChannelMessageCallback-PushNotification"></a>
The push notification configuration of the message.
Type: [PushNotificationConfiguration](API_messaging-chime_PushNotificationConfiguration.md) object
Required: No

 ** SubChannelId **   <a name="chimesdk-Type-messaging-chime_ChannelMessageCallback-SubChannelId"></a>
The ID of the SubChannel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[-_a-zA-Z0-9]*`
Required: No

## See Also
<a name="API_messaging-chime_ChannelMessageCallback_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-messaging-2021-05-15/ChannelMessageCallback)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-messaging-2021-05-15/ChannelMessageCallback)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-messaging-2021-05-15/ChannelMessageCallback)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
