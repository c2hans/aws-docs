---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_SessionFilterConfig.html
---

# SessionFilterConfig
<a name="API_SessionFilterConfig"></a>

A time range filter for selecting sessions. Specifies the start and end times to narrow down which sessions are included.

## Contents
<a name="API_SessionFilterConfig_Contents"></a>

 ** endTime **   <a name="BedrockAgentCore-Type-SessionFilterConfig-endTime"></a>
The end time of the time range. Only sessions with activity before this timestamp are included.
Type: Timestamp
Required: No

 ** startTime **   <a name="BedrockAgentCore-Type-SessionFilterConfig-startTime"></a>
The start time of the time range. Only sessions with activity at or after this timestamp are included.
Type: Timestamp
Required: No

## See Also
<a name="API_SessionFilterConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/SessionFilterConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/SessionFilterConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/SessionFilterConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore Data Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
