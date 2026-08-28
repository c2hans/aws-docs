---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_MessageMetadata.html
---

# MessageMetadata
<a name="API_MessageMetadata"></a>

Metadata information associated with this message.

## Contents
<a name="API_MessageMetadata_Contents"></a>

 ** eventId **   <a name="BedrockAgentCore-Type-MessageMetadata-eventId"></a>
The identifier of the event associated with this message.
Type: String
Required: Yes

 ** messageIndex **   <a name="BedrockAgentCore-Type-MessageMetadata-messageIndex"></a>
The position of this message within that event’s ordered list of messages.
Type: Integer
Required: Yes

## See Also
<a name="API_MessageMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/MessageMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/MessageMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/MessageMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore Data Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
