---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_ControlStats.html
---

# ControlStats
<a name="API_ControlStats"></a>

Statistics for the control variant in an A/B test.

## Contents
<a name="API_ControlStats_Contents"></a>

 ** mean **   <a name="BedrockAgentCore-Type-ControlStats-mean"></a>
The mean evaluation score for the control variant.
Type: Double
Required: Yes

 ** sampleSize **   <a name="BedrockAgentCore-Type-ControlStats-sampleSize"></a>
The number of sessions evaluated for the control variant.
Type: Integer
Required: Yes

 ** variantName **   <a name="BedrockAgentCore-Type-ControlStats-variantName"></a>
The name of the control variant.
Type: String
Required: Yes

## See Also
<a name="API_ControlStats_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ControlStats)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ControlStats)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ControlStats)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore Data Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
