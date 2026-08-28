---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_MouseClickResult.html
---

# MouseClickResult
<a name="API_MouseClickResult"></a>

The result of a mouse click action.

## Contents
<a name="API_MouseClickResult_Contents"></a>

 ** status **   <a name="BedrockAgentCore-Type-MouseClickResult-status"></a>
The status of the action execution.
Type: String
Valid Values: `SUCCESS | FAILED`
Required: Yes

 ** error **   <a name="BedrockAgentCore-Type-MouseClickResult-error"></a>
The error message. Present only when the action failed.
Type: String
Required: No

## See Also
<a name="API_MouseClickResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/MouseClickResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/MouseClickResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/MouseClickResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore Data Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
