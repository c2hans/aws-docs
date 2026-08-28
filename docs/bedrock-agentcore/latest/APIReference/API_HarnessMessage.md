---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_HarnessMessage.html
---

# HarnessMessage
<a name="API_HarnessMessage"></a>

A message in the conversation.

## Contents
<a name="API_HarnessMessage_Contents"></a>

 ** content **   <a name="BedrockAgentCore-Type-HarnessMessage-content"></a>
The content blocks of the message.
Type: Array of [HarnessContentBlock](API_HarnessContentBlock.md) objects
Required: Yes

 ** role **   <a name="BedrockAgentCore-Type-HarnessMessage-role"></a>
The role of the message sender.
Type: String
Valid Values: `user | assistant`
Required: Yes

## See Also
<a name="API_HarnessMessage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/HarnessMessage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/HarnessMessage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/HarnessMessage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore Data Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
