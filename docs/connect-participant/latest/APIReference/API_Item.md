---
source_url: https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_Item.html
---

# Item
<a name="API_connect-participant_Item"></a>

An item - message or event - that has been sent.

## Contents
<a name="API_connect-participant_Item_Contents"></a>

 ** AbsoluteTime **   <a name="connect-Type-connect-participant_Item-AbsoluteTime"></a>
The time when the message or event was sent.
It's specified in ISO 8601 format: yyyy-MM-ddThh:mm:ss.SSSZ. For example, 2019-11-08T02:41:28.172Z.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** Attachments **   <a name="connect-Type-connect-participant_Item-Attachments"></a>
Provides information about the attachments.
Type: Array of [AttachmentItem](API_connect-participant_AttachmentItem.md) objects
Required: No

 ** ContactId **   <a name="connect-Type-connect-participant_Item-ContactId"></a>
The contactId on which the transcript item was originally sent. This field is populated only when the transcript item is from the current chat session.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** Content **   <a name="connect-Type-connect-participant_Item-Content"></a>
The content of the message or event.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16384.
Required: No

 ** ContentType **   <a name="connect-Type-connect-participant_Item-ContentType"></a>
The type of content of the item.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** DisplayName **   <a name="connect-Type-connect-participant_Item-DisplayName"></a>
The chat display name of the sender.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** Id **   <a name="connect-Type-connect-participant_Item-Id"></a>
The ID of the item.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** MessageMetadata **   <a name="connect-Type-connect-participant_Item-MessageMetadata"></a>
The metadata related to the message. Currently this supports only information related to message receipts.
Type: [MessageMetadata](API_connect-participant_MessageMetadata.md) object
Required: No

 ** ParticipantId **   <a name="connect-Type-connect-participant_Item-ParticipantId"></a>
The ID of the sender in the session.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** ParticipantRole **   <a name="connect-Type-connect-participant_Item-ParticipantRole"></a>
The role of the sender. For example, is it a customer, agent, or system.
Type: String
Valid Values: `AGENT | CUSTOMER | SYSTEM | CUSTOM_BOT | SUPERVISOR`
Required: No

 ** RelatedContactId **   <a name="connect-Type-connect-participant_Item-RelatedContactId"></a>
The contactId on which the transcript item was originally sent. This field is only populated for persistent chats when the transcript item is from the past chat session. For more information, see [Enable persistent chat](https://docs.aws.amazon.com/connect/latest/adminguide/chat-persistence.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** Type **   <a name="connect-Type-connect-participant_Item-Type"></a>
Type of the item: message or event.
Type: String
Valid Values: `TYPING | PARTICIPANT_JOINED | PARTICIPANT_LEFT | CHAT_ENDED | TRANSFER_SUCCEEDED | TRANSFER_FAILED | MESSAGE | EVENT | ATTACHMENT | CONNECTION_ACK | MESSAGE_DELIVERED | MESSAGE_READ`
Required: No

## See Also
<a name="API_connect-participant_Item_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectparticipant-2018-09-07/Item)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectparticipant-2018-09-07/Item)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectparticipant-2018-09-07/Item)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
