---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-flow-promptmodelinferenceconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Flow PromptModelInferenceConfiguration
<a name="aws-properties-bedrock-flow-promptmodelinferenceconfiguration"></a>

Contains inference configurations related to model inference for a prompt. For more information, see [Inference parameters](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-parameters.html).

## Syntax
<a name="aws-properties-bedrock-flow-promptmodelinferenceconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-flow-promptmodelinferenceconfiguration-syntax.json"></a>

```
{
  "[MaxTokens](#cfn-bedrock-flow-promptmodelinferenceconfiguration-maxtokens)" : {{Number}},
  "[StopSequences](#cfn-bedrock-flow-promptmodelinferenceconfiguration-stopsequences)" : {{[ String, ... ]}},
  "[Temperature](#cfn-bedrock-flow-promptmodelinferenceconfiguration-temperature)" : {{Number}},
  "[TopP](#cfn-bedrock-flow-promptmodelinferenceconfiguration-topp)" : {{Number}}
}
```

### YAML
<a name="aws-properties-bedrock-flow-promptmodelinferenceconfiguration-syntax.yaml"></a>

```
  [MaxTokens](#cfn-bedrock-flow-promptmodelinferenceconfiguration-maxtokens): {{Number}}
  [StopSequences](#cfn-bedrock-flow-promptmodelinferenceconfiguration-stopsequences): {{
    - String}}
  [Temperature](#cfn-bedrock-flow-promptmodelinferenceconfiguration-temperature): {{Number}}
  [TopP](#cfn-bedrock-flow-promptmodelinferenceconfiguration-topp): {{Number}}
```

## Properties
<a name="aws-properties-bedrock-flow-promptmodelinferenceconfiguration-properties"></a>

`MaxTokens`  <a name="cfn-bedrock-flow-promptmodelinferenceconfiguration-maxtokens"></a>
The maximum number of tokens to return in the response.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StopSequences`  <a name="cfn-bedrock-flow-promptmodelinferenceconfiguration-stopsequences"></a>
A list of strings that define sequences after which the model will stop generating.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `4`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Temperature`  <a name="cfn-bedrock-flow-promptmodelinferenceconfiguration-temperature"></a>
Controls the randomness of the response. Choose a lower value for more predictable outputs and a higher value for more surprising outputs.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TopP`  <a name="cfn-bedrock-flow-promptmodelinferenceconfiguration-topp"></a>
The percentage of most-likely candidates that the model considers for the next token.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
