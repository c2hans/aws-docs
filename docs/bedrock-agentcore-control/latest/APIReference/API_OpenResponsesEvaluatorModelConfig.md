---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_OpenResponsesEvaluatorModelConfig.html
---

# OpenResponsesEvaluatorModelConfig
<a name="API_OpenResponsesEvaluatorModelConfig"></a>

 The configuration for using models served through the OpenResponses API in evaluator assessments, including model selection and inference parameters.

## Contents
<a name="API_OpenResponsesEvaluatorModelConfig_Contents"></a>

 ** modelId **   <a name="bedrockagentcorecontrol-Type-OpenResponsesEvaluatorModelConfig-modelId"></a>
 The identifier of the model to use for evaluation.
Type: String
Required: Yes

 ** maxOutputTokens **   <a name="bedrockagentcorecontrol-Type-OpenResponsesEvaluatorModelConfig-maxOutputTokens"></a>
 The maximum number of tokens to generate in the model response, including visible output and reasoning tokens.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** reasoning **   <a name="bedrockagentcorecontrol-Type-OpenResponsesEvaluatorModelConfig-reasoning"></a>
 The reasoning configuration for reasoning models. Non-reasoning models ignore this configuration.
Type: [ReasoningConfiguration](API_ReasoningConfiguration.md) object
Required: No

 ** temperature **   <a name="bedrockagentcorecontrol-Type-OpenResponsesEvaluatorModelConfig-temperature"></a>
 The temperature value that controls randomness in the model's responses. Lower values produce more deterministic outputs.
Type: Float
Valid Range: Minimum value of 0. Maximum value of 2.
Required: No

 ** topP **   <a name="bedrockagentcorecontrol-Type-OpenResponsesEvaluatorModelConfig-topP"></a>
 The top-p sampling parameter that controls the diversity of the model's responses by limiting the cumulative probability of token choices.
Type: Float
Valid Range: Minimum value of 0. Maximum value of 1.
Required: No

## See Also
<a name="API_OpenResponsesEvaluatorModelConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/OpenResponsesEvaluatorModelConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/OpenResponsesEvaluatorModelConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/OpenResponsesEvaluatorModelConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore Control Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore-control` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
