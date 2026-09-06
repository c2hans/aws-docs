---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ChannelMessage.html
---

# ChannelMessage
<a name="API_messaging-chime_ChannelMessage"></a>

The details of a message in a channel.

## Contents
<a name="API_messaging-chime_ChannelMessage_Contents"></a>

 ** ChannelArn **   <a name="chimesdk-Type-messaging-chime_ChannelMessage-ChannelArn"></a>
The ARN of the channel.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 1600.
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
Required: No

 ** Content **   <a name="chimesdk-Type-messaging-chime_ChannelMessage-Content"></a>
The content of the channel message. For Amazon Lex V2 bot responses, this field holds a list of messages originating from the bot. For more information, refer to [Processing responses from an AppInstanceBot](https://docs.aws.amazon.com/chime-sdk/latest/dg/appinstance-bots#process-response.html) in the *Amazon Chime SDK Messaging Developer Guide*.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Pattern: `[\s\S]*`
Required: No

 ** ContentType **   <a name="chimesdk-Type-messaging-chime_ChannelMessage-ContentType"></a>
The content type of the channel message. For Amazon Lex V2 bot responses, the content type is `application/amz-chime-lex-msgs` for success responses and `application/amz-chime-lex-error` for failure responses. For more information, refer to [Processing responses from an AppInstanceBot](https://docs.aws.amazon.com/chime-sdk/latest/dg/appinstance-bots#process-response.html) in the *Amazon Chime SDK Messaging Developer Guide*.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 45.
Pattern: `[\s\S]*`
Required: No

 ** CreatedTimestamp **   <a name="chimesdk-Type-messaging-chime_ChannelMessage-CreatedTimestamp"></a>
The time at which the message was created.
Type: Timestamp
Required: No

 ** LastEditedTimestamp **   <a name="chimesdk-Type-messaging-chime_ChannelMessage-LastEditedTimestamp"></a>
The time at which a message was edited.
Type: Timestamp
Required: No

 ** LastUpdatedTimestamp **   <a name="chimesdk-Type-messaging-chime_ChannelMessage-LastUpdatedTimestamp"></a>
The time at which a message was updated.
Type: Timestamp
Required: No

 ** MessageAttributes **   <a name="chimesdk-Type-messaging-chime_ChannelMessage-MessageAttributes"></a>
The attributes for the channel message. For Amazon Lex V2 bot responses, the attributes are mapped to specific fields from the bot. For more information, refer to [Processing responses from an AppInstanceBot](https://docs.aws.amazon.com/chime-sdk/latest/dg/appinstance-bots#process-response.html) in the *Amazon Chime SDK Messaging Developer Guide*.
Type: String to [MessageAttributeValue](API_messaging-chime_MessageAttributeValue.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Key Pattern: `[\s\S]*`
Required: No

 ** MessageId **   <a name="chimesdk-Type-messaging-chime_ChannelMessage-MessageId"></a>
The ID of a message.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[-_a-zA-Z0-9]*`
Required: No

 ** Metadata **   <a name="chimesdk-Type-messaging-chime_ChannelMessage-Metadata"></a>
The message metadata.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** Persistence **   <a name="chimesdk-Type-messaging-chime_ChannelMessage-Persistence"></a>
The persistence setting for a channel message.
Type: String
Valid Values: `PERSISTENT | NON_PERSISTENT`
Required: No

 ** Redacted **   <a name="chimesdk-Type-messaging-chime_ChannelMessage-Redacted"></a>
Hides the content of a message.
Type: Boolean
Required: No

 ** Sender **   <a name="chimesdk-Type-messaging-chime_ChannelMessage-Sender"></a>
The message sender.
Type: [Identity](API_messaging-chime_Identity.md) object
Required: No

 ** Status **   <a name="chimesdk-Type-messaging-chime_ChannelMessage-Status"></a>
The status of the channel message.
Type: [ChannelMessageStatusStructure](API_messaging-chime_ChannelMessageStatusStructure.md) object
Required: No

 ** SubChannelId **   <a name="chimesdk-Type-messaging-chime_ChannelMessage-SubChannelId"></a>
The ID of the SubChannel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[-_a-zA-Z0-9]*`
Required: No

 ** Target **   <a name="chimesdk-Type-messaging-chime_ChannelMessage-Target"></a>
The target of a message, a sender, a user, or a bot. Only the target and the sender can view targeted messages. Only users who can see targeted messages can take actions on them. However, administrators can delete targeted messages that they can’t see.
Type: Array of [Target](API_messaging-chime_Target.md) objects
Array Members: Fixed number of 1 item.
Required: No

 ** Type **   <a name="chimesdk-Type-messaging-chime_ChannelMessage-Type"></a>
The message type.
Type: String
Valid Values: `STANDARD | CONTROL`
Required: No

## See Also
<a name="API_messaging-chime_ChannelMessage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-messaging-2021-05-15/ChannelMessage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-messaging-2021-05-15/ChannelMessage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-messaging-2021-05-15/ChannelMessage)
