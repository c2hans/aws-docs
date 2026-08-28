---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_SystemPromptRecommendationConfig.html
---

# SystemPromptRecommendationConfig
<a name="API_SystemPromptRecommendationConfig"></a>

Configuration for generating system prompt optimization recommendations.

## Contents
<a name="API_SystemPromptRecommendationConfig_Contents"></a>

 ** agentTraces **   <a name="BedrockAgentCore-Type-SystemPromptRecommendationConfig-agentTraces"></a>
The agent traces to analyze for generating recommendations.
Type: [AgentTracesConfig](API_AgentTracesConfig.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** systemPrompt **   <a name="BedrockAgentCore-Type-SystemPromptRecommendationConfig-systemPrompt"></a>
The current system prompt to optimize.
Type: [SystemPromptConfig](API_SystemPromptConfig.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** evaluationConfig **   <a name="BedrockAgentCore-Type-SystemPromptRecommendationConfig-evaluationConfig"></a>
The evaluation configuration specifying which evaluator to use for assessing recommendation quality.
Type: [RecommendationEvaluationConfig](API_RecommendationEvaluationConfig.md) object
Required: No

## See Also
<a name="API_SystemPromptRecommendationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/SystemPromptRecommendationConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/SystemPromptRecommendationConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/SystemPromptRecommendationConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore Data Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
