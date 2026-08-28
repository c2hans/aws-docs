---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_ConversationMessage.html
---

# ConversationMessage
<a name="API_qapps_ConversationMessage"></a>

A message in a conversation, used as input for generating an Amazon Q App definition.

## Contents
<a name="API_qapps_ConversationMessage_Contents"></a>

 ** body **   <a name="qbusiness-Type-qapps_ConversationMessage-body"></a>
The text content of the conversation message.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 7000.
Required: Yes

 ** type **   <a name="qbusiness-Type-qapps_ConversationMessage-type"></a>
The type of the conversation message.
Type: String
Valid Values: `USER | SYSTEM`
Required: Yes

## See Also
<a name="API_qapps_ConversationMessage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qapps-2023-11-27/ConversationMessage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qapps-2023-11-27/ConversationMessage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qapps-2023-11-27/ConversationMessage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
