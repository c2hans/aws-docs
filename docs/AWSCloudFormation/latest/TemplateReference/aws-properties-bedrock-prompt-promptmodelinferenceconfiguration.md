---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-prompt-promptmodelinferenceconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Prompt PromptModelInferenceConfiguration
<a name="aws-properties-bedrock-prompt-promptmodelinferenceconfiguration"></a>

Contains inference configurations related to model inference for a prompt. For more information, see [Inference parameters](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-parameters.html).

## Syntax
<a name="aws-properties-bedrock-prompt-promptmodelinferenceconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-prompt-promptmodelinferenceconfiguration-syntax.json"></a>

```
{
  "[MaxTokens](#cfn-bedrock-prompt-promptmodelinferenceconfiguration-maxtokens)" : {{Number}},
  "[StopSequences](#cfn-bedrock-prompt-promptmodelinferenceconfiguration-stopsequences)" : {{[ String, ... ]}},
  "[Temperature](#cfn-bedrock-prompt-promptmodelinferenceconfiguration-temperature)" : {{Number}},
  "[TopP](#cfn-bedrock-prompt-promptmodelinferenceconfiguration-topp)" : {{Number}}
}
```

### YAML
<a name="aws-properties-bedrock-prompt-promptmodelinferenceconfiguration-syntax.yaml"></a>

```
  [MaxTokens](#cfn-bedrock-prompt-promptmodelinferenceconfiguration-maxtokens): {{Number}}
  [StopSequences](#cfn-bedrock-prompt-promptmodelinferenceconfiguration-stopsequences): {{
    - String}}
  [Temperature](#cfn-bedrock-prompt-promptmodelinferenceconfiguration-temperature): {{Number}}
  [TopP](#cfn-bedrock-prompt-promptmodelinferenceconfiguration-topp): {{Number}}
```

## Properties
<a name="aws-properties-bedrock-prompt-promptmodelinferenceconfiguration-properties"></a>

`MaxTokens`  <a name="cfn-bedrock-prompt-promptmodelinferenceconfiguration-maxtokens"></a>
The maximum number of tokens to return in the response.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `512000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StopSequences`  <a name="cfn-bedrock-prompt-promptmodelinferenceconfiguration-stopsequences"></a>
A list of strings that define sequences after which the model will stop generating.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `4`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Temperature`  <a name="cfn-bedrock-prompt-promptmodelinferenceconfiguration-temperature"></a>
Controls the randomness of the response. Choose a lower value for more predictable outputs and a higher value for more surprising outputs.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TopP`  <a name="cfn-bedrock-prompt-promptmodelinferenceconfiguration-topp"></a>
The percentage of most-likely candidates that the model considers for the next token.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
