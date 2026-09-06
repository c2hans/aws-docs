---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-agent-inferenceconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Agent InferenceConfiguration
<a name="aws-properties-bedrock-agent-inferenceconfiguration"></a>

Base inference parameters to pass to a model in a call to [Converse](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html) or [ConverseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html). For more information, see [Inference parameters for foundation models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html).

If you need to pass additional parameters that the model supports, use the `additionalModelRequestFields` request field in the call to `Converse` or `ConverseStream`. For more information, see [Model parameters](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html).

## Syntax
<a name="aws-properties-bedrock-agent-inferenceconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-agent-inferenceconfiguration-syntax.json"></a>

```
{
  "[MaximumLength](#cfn-bedrock-agent-inferenceconfiguration-maximumlength)" : {{Number}},
  "[StopSequences](#cfn-bedrock-agent-inferenceconfiguration-stopsequences)" : {{[ String, ... ]}},
  "[Temperature](#cfn-bedrock-agent-inferenceconfiguration-temperature)" : {{Number}},
  "[TopK](#cfn-bedrock-agent-inferenceconfiguration-topk)" : {{Number}},
  "[TopP](#cfn-bedrock-agent-inferenceconfiguration-topp)" : {{Number}}
}
```

### YAML
<a name="aws-properties-bedrock-agent-inferenceconfiguration-syntax.yaml"></a>

```
  [MaximumLength](#cfn-bedrock-agent-inferenceconfiguration-maximumlength): {{Number}}
  [StopSequences](#cfn-bedrock-agent-inferenceconfiguration-stopsequences): {{
    - String}}
  [Temperature](#cfn-bedrock-agent-inferenceconfiguration-temperature): {{Number}}
  [TopK](#cfn-bedrock-agent-inferenceconfiguration-topk): {{Number}}
  [TopP](#cfn-bedrock-agent-inferenceconfiguration-topp): {{Number}}
```

## Properties
<a name="aws-properties-bedrock-agent-inferenceconfiguration-properties"></a>

`MaximumLength`  <a name="cfn-bedrock-agent-inferenceconfiguration-maximumlength"></a>
The maximum number of tokens allowed in the generated response.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `131072`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StopSequences`  <a name="cfn-bedrock-agent-inferenceconfiguration-stopsequences"></a>
A list of stop sequences. A stop sequence is a sequence of characters that causes the model to stop generating the response.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `4`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Temperature`  <a name="cfn-bedrock-agent-inferenceconfiguration-temperature"></a>
The likelihood of the model selecting higher-probability options while generating a response. A lower value makes the model more likely to choose higher-probability options, while a higher value makes the model more likely to choose lower-probability options.
The default value is the default value for the model that you are using. For more information, see [Inference parameters for foundation models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html).
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TopK`  <a name="cfn-bedrock-agent-inferenceconfiguration-topk"></a>
While generating a response, the model determines the probability of the following token at each point of generation. The value that you set for `topK` is the number of most-likely candidates from which the model chooses the next token in the sequence. For example, if you set `topK` to 50, the model selects the next token from among the top 50 most likely choices.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TopP`  <a name="cfn-bedrock-agent-inferenceconfiguration-topp"></a>
The percentage of most-likely candidates that the model considers for the next token. For example, if you choose a value of 0.8 for `topP`, the model selects from the top 80% of the probability distribution of tokens that could be next in the sequence.
The default value is the default value for the model that you are using. For more information, see [Inference parameters for foundation models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html).
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
