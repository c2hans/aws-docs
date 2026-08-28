---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_RecommendationResult.html
---

# RecommendationResult
<a name="API_RecommendationResult"></a>

The result of a recommendation, containing the optimized output.

## Contents
<a name="API_RecommendationResult_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** systemPromptRecommendationResult **   <a name="BedrockAgentCore-Type-RecommendationResult-systemPromptRecommendationResult"></a>
The result of a system prompt recommendation.
Type: [SystemPromptRecommendationResult](API_SystemPromptRecommendationResult.md) object
Required: No

 ** toolDescriptionRecommendationResult **   <a name="BedrockAgentCore-Type-RecommendationResult-toolDescriptionRecommendationResult"></a>
The result of a tool description recommendation.
Type: [ToolDescriptionRecommendationResult](API_ToolDescriptionRecommendationResult.md) object
Required: No

## See Also
<a name="API_RecommendationResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/RecommendationResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/RecommendationResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/RecommendationResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore Data Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
