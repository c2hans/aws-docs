---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-harness-harnessmodelconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Harness HarnessModelConfiguration
<a name="aws-properties-bedrockagentcore-harness-harnessmodelconfiguration"></a>

Specification of which model to use.

## Syntax
<a name="aws-properties-bedrockagentcore-harness-harnessmodelconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-harness-harnessmodelconfiguration-syntax.json"></a>

```
{
  "[BedrockModelConfig](#cfn-bedrockagentcore-harness-harnessmodelconfiguration-bedrockmodelconfig)" : {{HarnessBedrockModelConfig}},
  "[GeminiModelConfig](#cfn-bedrockagentcore-harness-harnessmodelconfiguration-geminimodelconfig)" : {{HarnessGeminiModelConfig}},
  "[LiteLlmModelConfig](#cfn-bedrockagentcore-harness-harnessmodelconfiguration-litellmmodelconfig)" : {{HarnessLiteLlmModelConfig}},
  "[OpenAiModelConfig](#cfn-bedrockagentcore-harness-harnessmodelconfiguration-openaimodelconfig)" : {{HarnessOpenAiModelConfig}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-harness-harnessmodelconfiguration-syntax.yaml"></a>

```
  [BedrockModelConfig](#cfn-bedrockagentcore-harness-harnessmodelconfiguration-bedrockmodelconfig): {{
    HarnessBedrockModelConfig}}
  [GeminiModelConfig](#cfn-bedrockagentcore-harness-harnessmodelconfiguration-geminimodelconfig): {{
    HarnessGeminiModelConfig}}
  [LiteLlmModelConfig](#cfn-bedrockagentcore-harness-harnessmodelconfiguration-litellmmodelconfig): {{
    HarnessLiteLlmModelConfig}}
  [OpenAiModelConfig](#cfn-bedrockagentcore-harness-harnessmodelconfiguration-openaimodelconfig): {{
    HarnessOpenAiModelConfig}}
```

## Properties
<a name="aws-properties-bedrockagentcore-harness-harnessmodelconfiguration-properties"></a>

`BedrockModelConfig`  <a name="cfn-bedrockagentcore-harness-harnessmodelconfiguration-bedrockmodelconfig"></a>
Configuration for an Amazon Bedrock model.
*Required*: No
*Type*: [HarnessBedrockModelConfig](aws-properties-bedrockagentcore-harness-harnessbedrockmodelconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GeminiModelConfig`  <a name="cfn-bedrockagentcore-harness-harnessmodelconfiguration-geminimodelconfig"></a>
Configuration for a Google Gemini model.
*Required*: No
*Type*: [HarnessGeminiModelConfig](aws-properties-bedrockagentcore-harness-harnessgeminimodelconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LiteLlmModelConfig`  <a name="cfn-bedrockagentcore-harness-harnessmodelconfiguration-litellmmodelconfig"></a>
The LiteLLM model configuration for connecting to third-party model providers.
*Required*: No
*Type*: [HarnessLiteLlmModelConfig](aws-properties-bedrockagentcore-harness-harnesslitellmmodelconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OpenAiModelConfig`  <a name="cfn-bedrockagentcore-harness-harnessmodelconfiguration-openaimodelconfig"></a>
Configuration for an OpenAI model.
*Required*: No
*Type*: [HarnessOpenAiModelConfig](aws-properties-bedrockagentcore-harness-harnessopenaimodelconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
