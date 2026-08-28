---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_MouseClickArguments.html
---

# MouseClickArguments
<a name="API_MouseClickArguments"></a>

Arguments for a mouse click action.

## Contents
<a name="API_MouseClickArguments_Contents"></a>

 ** x **   <a name="BedrockAgentCore-Type-MouseClickArguments-x"></a>
The X coordinate on screen where the click occurs.
Type: Integer
Required: Yes

 ** y **   <a name="BedrockAgentCore-Type-MouseClickArguments-y"></a>
The Y coordinate on screen where the click occurs.
Type: Integer
Required: Yes

 ** button **   <a name="BedrockAgentCore-Type-MouseClickArguments-button"></a>
The mouse button to use. Defaults to `LEFT`.
Type: String
Valid Values: `LEFT | RIGHT | MIDDLE`
Required: No

 ** clickCount **   <a name="BedrockAgentCore-Type-MouseClickArguments-clickCount"></a>
The number of clicks to perform. Valid range: 1–10. Defaults to 1.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10.
Required: No

## See Also
<a name="API_MouseClickArguments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/MouseClickArguments)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/MouseClickArguments)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/MouseClickArguments)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore Data Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
