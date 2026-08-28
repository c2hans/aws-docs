---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_NewSessionDetails.html
---

# NewSessionDetails
<a name="API_NewSessionDetails"></a>

Payload of chat properties to apply when starting a new contact.

## Contents
<a name="API_NewSessionDetails_Contents"></a>

 ** Attributes **   <a name="connect-Type-NewSessionDetails-Attributes"></a>
 A custom key-value pair using an attribute map. The attributes are standard Connect Customer attributes. They can be accessed in flows just like any other contact attributes.
 There can be up to 32,768 UTF-8 bytes across all key-value pairs per contact. Attribute keys can include only alphanumeric, dash, and underscore characters.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 32767.
Value Length Constraints: Minimum length of 0. Maximum length of 32767.
Required: No

 ** ParticipantDetails **   <a name="connect-Type-NewSessionDetails-ParticipantDetails"></a>
The details of the participant, including their display name.
Type: [ParticipantDetails](API_ParticipantDetails.md) object
Required: No

 ** StreamingConfiguration **   <a name="connect-Type-NewSessionDetails-StreamingConfiguration"></a>
The streaming configuration, such as the Amazon SNS streaming endpoint.
Type: [ChatStreamingConfiguration](API_ChatStreamingConfiguration.md) object
Required: No

 ** SupportedMessagingContentTypes **   <a name="connect-Type-NewSessionDetails-SupportedMessagingContentTypes"></a>
 The supported chat message content types. Supported types are `text/plain`, `text/markdown`, `application/json`, `application/vnd.amazonaws.connect.message.interactive`, and `application/vnd.amazonaws.connect.message.interactive.response`.
Content types must always contain ` text/plain`. You can then put any other supported type in the list. For example, all the following lists are valid because they contain `text/plain`: `[text/plain, text/markdown, application/json]`, ` [text/markdown, text/plain]`, `[text/plain, application/json, application/vnd.amazonaws.connect.message.interactive.response]`.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

## See Also
<a name="API_NewSessionDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/NewSessionDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/NewSessionDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/NewSessionDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
