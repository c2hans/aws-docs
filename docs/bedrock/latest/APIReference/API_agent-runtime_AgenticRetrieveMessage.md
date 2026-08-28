---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_AgenticRetrieveMessage.html
---

# AgenticRetrieveMessage
<a name="API_agent-runtime_AgenticRetrieveMessage"></a>

A message in the agentic retrieval conversation.

## Contents
<a name="API_agent-runtime_AgenticRetrieveMessage_Contents"></a>

 ** content **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveMessage-content"></a>
The content of the message.
Type: [AgenticRetrieveMessageContent](API_agent-runtime_AgenticRetrieveMessageContent.md) object
Required: Yes

 ** role **   <a name="bedrock-Type-agent-runtime_AgenticRetrieveMessage-role"></a>
The role of the message sender (e.g., user or assistant).
Type: String
Valid Values: `user | assistant`
Required: Yes

## See Also
<a name="API_agent-runtime_AgenticRetrieveMessage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/AgenticRetrieveMessage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/AgenticRetrieveMessage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/AgenticRetrieveMessage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
