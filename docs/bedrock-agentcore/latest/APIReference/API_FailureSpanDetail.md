---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_FailureSpanDetail.html
---

# FailureSpanDetail
<a name="API_FailureSpanDetail"></a>

Details about a specific span where a failure was detected.

## Contents
<a name="API_FailureSpanDetail_Contents"></a>

 ** signals **   <a name="BedrockAgentCore-Type-FailureSpanDetail-signals"></a>
The failure signals detected in this span.
Type: Array of [InsightsFailureSignal](API_InsightsFailureSignal.md) objects
Required: Yes

 ** spanId **   <a name="BedrockAgentCore-Type-FailureSpanDetail-spanId"></a>
The unique identifier of the span where the failure occurred.
Type: String
Required: Yes

 ** traceId **   <a name="BedrockAgentCore-Type-FailureSpanDetail-traceId"></a>
The trace identifier associated with the failure span.
Type: String
Required: Yes

## See Also
<a name="API_FailureSpanDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/FailureSpanDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/FailureSpanDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/FailureSpanDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore Data Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
