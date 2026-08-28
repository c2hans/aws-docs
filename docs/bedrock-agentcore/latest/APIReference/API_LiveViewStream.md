---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_LiveViewStream.html
---

# LiveViewStream
<a name="API_LiveViewStream"></a>

The configuration for a stream that provides a visual representation of a browser session in Amazon Bedrock AgentCore. This stream enables agents to observe the current state of the browser, including rendered web pages, visual elements, and the results of interactions.

## Contents
<a name="API_LiveViewStream_Contents"></a>

 ** streamEndpoint **   <a name="BedrockAgentCore-Type-LiveViewStream-streamEndpoint"></a>
The endpoint URL for the live view stream. This URL is used to establish a connection to receive visual updates from the browser session.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 512.
Required: No

## See Also
<a name="API_LiveViewStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/LiveViewStream)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/LiveViewStream)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/LiveViewStream)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore Data Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
