---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ChatMessage.html
---

# ChatMessage
<a name="API_ChatMessage"></a>

A chat message.

## Contents
<a name="API_ChatMessage_Contents"></a>

 ** Content **   <a name="connect-Type-ChatMessage-Content"></a>
The content of the chat message. Maximum of 16,384 bytes for all content types (`text/plain`, `text/markdown`, `application/json`, and `application/vnd.amazonaws.connect.message.interactive.response`).
Some messaging channels enforce lower limits. For channel-specific message size limits, see [Chat message size limits by channel](https://docs.aws.amazon.com/connect/latest/adminguide/feature-limits.html#chat-message-size-limits) in the *Amazon Connect Customer Administrator Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16384.
Required: Yes

 ** ContentType **   <a name="connect-Type-ChatMessage-ContentType"></a>
The type of the content. Supported types are `text/plain`, `text/markdown`, `application/json`, and `application/vnd.amazonaws.connect.message.interactive.response`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## See Also
<a name="API_ChatMessage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ChatMessage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ChatMessage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ChatMessage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
