---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_Conversation.html
---

# Conversation
<a name="API_Conversation"></a>

A conversation in an Amazon Q Business application.

## Contents
<a name="API_Conversation_Contents"></a>

 ** conversationId **   <a name="qbusiness-Type-Conversation-conversationId"></a>
The identifier of the Amazon Q Business conversation.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: No

 ** startTime **   <a name="qbusiness-Type-Conversation-startTime"></a>
The start time of the conversation.
Type: Timestamp
Required: No

 ** title **   <a name="qbusiness-Type-Conversation-title"></a>
The title of the conversation.
Type: String
Required: No

## See Also
<a name="API_Conversation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/Conversation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/Conversation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/Conversation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
