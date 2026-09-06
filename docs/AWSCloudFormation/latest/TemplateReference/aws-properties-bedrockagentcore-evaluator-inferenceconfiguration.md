---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-evaluator-inferenceconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Evaluator InferenceConfiguration
<a name="aws-properties-bedrockagentcore-evaluator-inferenceconfiguration"></a>

 The inference configuration parameters that control model behavior during evaluation, including temperature, token limits, and sampling settings.

## Syntax
<a name="aws-properties-bedrockagentcore-evaluator-inferenceconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-evaluator-inferenceconfiguration-syntax.json"></a>

```
{
  "[MaxTokens](#cfn-bedrockagentcore-evaluator-inferenceconfiguration-maxtokens)" : {{Integer}},
  "[Temperature](#cfn-bedrockagentcore-evaluator-inferenceconfiguration-temperature)" : {{Number}},
  "[TopP](#cfn-bedrockagentcore-evaluator-inferenceconfiguration-topp)" : {{Number}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-evaluator-inferenceconfiguration-syntax.yaml"></a>

```
  [MaxTokens](#cfn-bedrockagentcore-evaluator-inferenceconfiguration-maxtokens): {{Integer}}
  [Temperature](#cfn-bedrockagentcore-evaluator-inferenceconfiguration-temperature): {{Number}}
  [TopP](#cfn-bedrockagentcore-evaluator-inferenceconfiguration-topp): {{Number}}
```

## Properties
<a name="aws-properties-bedrockagentcore-evaluator-inferenceconfiguration-properties"></a>

`MaxTokens`  <a name="cfn-bedrockagentcore-evaluator-inferenceconfiguration-maxtokens"></a>
 The maximum number of tokens to generate in the model response during evaluation.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Temperature`  <a name="cfn-bedrockagentcore-evaluator-inferenceconfiguration-temperature"></a>
 The temperature value that controls randomness in the model's responses. Lower values produce more deterministic outputs.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TopP`  <a name="cfn-bedrockagentcore-evaluator-inferenceconfiguration-topp"></a>
 The top-p sampling parameter that controls the diversity of the model's responses by limiting the cumulative probability of token choices.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
