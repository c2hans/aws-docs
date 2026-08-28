---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ChatEvent.html
---

# ChatEvent
<a name="API_ChatEvent"></a>

Chat integration event containing payload to perform different chat actions such as:
+ Sending a chat message
+ Sending a chat event, such as typing
+ Disconnecting from a chat

## Contents
<a name="API_ChatEvent_Contents"></a>

 ** Type **   <a name="connect-Type-ChatEvent-Type"></a>
Type of chat integration event.
Type: String
Valid Values: `DISCONNECT | MESSAGE | EVENT`
Required: Yes

 ** Content **   <a name="connect-Type-ChatEvent-Content"></a>
Content of the message or event. This is required when `Type` is `MESSAGE` and for certain `ContentTypes` when `Type` is `EVENT`.
+ For allowed message content, see the `Content` parameter in the [SendMessage](https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_SendMessage.html) topic in the *Connect Customer Participant Service API Reference*.
+ For allowed event content, see the `Content` parameter in the [SendEvent](https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_SendEvent.html) topic in the *Connect Customer Participant Service API Reference*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16384.
Required: No

 ** ContentType **   <a name="connect-Type-ChatEvent-ContentType"></a>
Type of content. This is required when `Type` is `MESSAGE` or `EVENT`.
+ For allowed message content types, see the `ContentType` parameter in the [SendMessage](https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_SendMessage.html) topic in the *Connect Customer Participant Service API Reference*.
+ For allowed event content types, see the `ContentType` parameter in the [SendEvent](https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_SendEvent.html) topic in the *Connect Customer Participant Service API Reference*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

## See Also
<a name="API_ChatEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ChatEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ChatEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ChatEvent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
