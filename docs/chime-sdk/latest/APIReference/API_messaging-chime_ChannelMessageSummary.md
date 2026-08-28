---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ChannelMessageSummary.html
---

# ChannelMessageSummary
<a name="API_messaging-chime_ChannelMessageSummary"></a>

Summary of the messages in a `Channel`.

## Contents
<a name="API_messaging-chime_ChannelMessageSummary_Contents"></a>

 ** Content **   <a name="chimesdk-Type-messaging-chime_ChannelMessageSummary-Content"></a>
The content of the channel message. For Amazon Lex V2 bot responses, this field holds a list of messages originating from the bot. For more information, refer to [Processing responses from an AppInstanceBot](https://docs.aws.amazon.com/chime-sdk/latest/dg/appinstance-bots#process-response.html) in the *Amazon Chime SDK Messaging Developer Guide*.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Pattern: `[\s\S]*`
Required: No

 ** ContentType **   <a name="chimesdk-Type-messaging-chime_ChannelMessageSummary-ContentType"></a>
The content type of the channel message listed in the summary. For Amazon Lex V2 bot responses, the content type is `application/amz-chime-lex-msgs` for success responses and `application/amz-chime-lex-error` for failure responses. For more information, refer to [Processing responses from an AppInstanceBot](https://docs.aws.amazon.com/chime-sdk/latest/dg/appinstance-bots#process-response.html) in the *Amazon Chime SDK Messaging Developer Guide*.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 45.
Pattern: `[\s\S]*`
Required: No

 ** CreatedTimestamp **   <a name="chimesdk-Type-messaging-chime_ChannelMessageSummary-CreatedTimestamp"></a>
The time at which the message summary was created.
Type: Timestamp
Required: No

 ** LastEditedTimestamp **   <a name="chimesdk-Type-messaging-chime_ChannelMessageSummary-LastEditedTimestamp"></a>
The time at which a message was last edited.
Type: Timestamp
Required: No

 ** LastUpdatedTimestamp **   <a name="chimesdk-Type-messaging-chime_ChannelMessageSummary-LastUpdatedTimestamp"></a>
The time at which a message was last updated.
Type: Timestamp
Required: No

 ** MessageAttributes **   <a name="chimesdk-Type-messaging-chime_ChannelMessageSummary-MessageAttributes"></a>
The attributes for the channel message. For Amazon Lex V2 bot responses, the attributes are mapped to specific fields from the bot. For more information, refer to [Processing responses from an AppInstanceBot](https://docs.aws.amazon.com/chime-sdk/latest/dg/appinstance-bots#process-response.html) in the *Amazon Chime SDK Messaging Developer Guide*.
Type: String to [MessageAttributeValue](API_messaging-chime_MessageAttributeValue.md) object map
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Key Pattern: `[\s\S]*`
Required: No

 ** MessageId **   <a name="chimesdk-Type-messaging-chime_ChannelMessageSummary-MessageId"></a>
The ID of the message.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[-_a-zA-Z0-9]*`
Required: No

 ** Metadata **   <a name="chimesdk-Type-messaging-chime_ChannelMessageSummary-Metadata"></a>
The metadata of the message.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** Redacted **   <a name="chimesdk-Type-messaging-chime_ChannelMessageSummary-Redacted"></a>
Indicates whether a message was redacted.
Type: Boolean
Required: No

 ** Sender **   <a name="chimesdk-Type-messaging-chime_ChannelMessageSummary-Sender"></a>
The message sender.
Type: [Identity](API_messaging-chime_Identity.md) object
Required: No

 ** Status **   <a name="chimesdk-Type-messaging-chime_ChannelMessageSummary-Status"></a>
The message status. The status value is `SENT` for messages sent to a channel without a channel flow. For channels associated with channel flow, the value determines the processing stage.
Type: [ChannelMessageStatusStructure](API_messaging-chime_ChannelMessageStatusStructure.md) object
Required: No

 ** Target **   <a name="chimesdk-Type-messaging-chime_ChannelMessageSummary-Target"></a>
The target of a message, a sender, a user, or a bot. Only the target and the sender can view targeted messages. Only users who can see targeted messages can take actions on them. However, administrators can delete targeted messages that they can’t see.
Type: Array of [Target](API_messaging-chime_Target.md) objects
Array Members: Fixed number of 1 item.
Required: No

 ** Type **   <a name="chimesdk-Type-messaging-chime_ChannelMessageSummary-Type"></a>
The type of message.
Type: String
Valid Values: `STANDARD | CONTROL`
Required: No

## See Also
<a name="API_messaging-chime_ChannelMessageSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-messaging-2021-05-15/ChannelMessageSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-messaging-2021-05-15/ChannelMessageSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-messaging-2021-05-15/ChannelMessageSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
