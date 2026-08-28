---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_InvokeHarnessStreamOutput.html
---

# InvokeHarnessStreamOutput
<a name="API_InvokeHarnessStreamOutput"></a>

The streaming events returned by a harness invocation.

## Contents
<a name="API_InvokeHarnessStreamOutput_Contents"></a>

 ** contentBlockDelta **   <a name="BedrockAgentCore-Type-InvokeHarnessStreamOutput-contentBlockDelta"></a>
A delta update to the current content block.
Type: [HarnessContentBlockDeltaEvent](API_HarnessContentBlockDeltaEvent.md) object
Required: No

 ** contentBlockStart **   <a name="BedrockAgentCore-Type-InvokeHarnessStreamOutput-contentBlockStart"></a>
Indicates the start of a new content block.
Type: [HarnessContentBlockStartEvent](API_HarnessContentBlockStartEvent.md) object
Required: No

 ** contentBlockStop **   <a name="BedrockAgentCore-Type-InvokeHarnessStreamOutput-contentBlockStop"></a>
Indicates the end of the current content block.
Type: [HarnessContentBlockStopEvent](API_HarnessContentBlockStopEvent.md) object
Required: No

 ** internalServerException **   <a name="BedrockAgentCore-Type-InvokeHarnessStreamOutput-internalServerException"></a>
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.
Type: Exception
HTTP Status Code: 500
Required: No

 ** messageStart **   <a name="BedrockAgentCore-Type-InvokeHarnessStreamOutput-messageStart"></a>
Indicates the start of a new message from the agent.
Type: [HarnessMessageStartEvent](API_HarnessMessageStartEvent.md) object
Required: No

 ** messageStop **   <a name="BedrockAgentCore-Type-InvokeHarnessStreamOutput-messageStop"></a>
Indicates the end of the current message.
Type: [HarnessMessageStopEvent](API_HarnessMessageStopEvent.md) object
Required: No

 ** metadata **   <a name="BedrockAgentCore-Type-InvokeHarnessStreamOutput-metadata"></a>
Token usage and latency metrics for the invocation.
Type: [HarnessMetadataEvent](API_HarnessMetadataEvent.md) object
Required: No

 ** runtimeClientError **   <a name="BedrockAgentCore-Type-InvokeHarnessStreamOutput-runtimeClientError"></a>
An error returned by the runtime container during agent execution.
Type: Exception
HTTP Status Code: 424
Required: No

 ** validationException **   <a name="BedrockAgentCore-Type-InvokeHarnessStreamOutput-validationException"></a>
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.
Type: Exception
HTTP Status Code: 400
Required: No

## See Also
<a name="API_InvokeHarnessStreamOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/InvokeHarnessStreamOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/InvokeHarnessStreamOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/InvokeHarnessStreamOutput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore Data Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
