---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_HarnessToolResultBlockStart.html
---

# HarnessToolResultBlockStart
<a name="API_HarnessToolResultBlockStart"></a>

Start payload for a tool result content block.

## Contents
<a name="API_HarnessToolResultBlockStart_Contents"></a>

 ** toolUseId **   <a name="BedrockAgentCore-Type-HarnessToolResultBlockStart-toolUseId"></a>
The tool use ID that this result corresponds to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

 ** status **   <a name="BedrockAgentCore-Type-HarnessToolResultBlockStart-status"></a>
The status of the tool execution.
Type: String
Valid Values: `success | error`
Required: No

## See Also
<a name="API_HarnessToolResultBlockStart_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/HarnessToolResultBlockStart)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/HarnessToolResultBlockStart)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/HarnessToolResultBlockStart)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore Data Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
