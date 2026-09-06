---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-harness-harnessbedrockmodelconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Harness HarnessBedrockModelConfig
<a name="aws-properties-bedrockagentcore-harness-harnessbedrockmodelconfig"></a>

Configuration for an Amazon Bedrock model provider.

## Syntax
<a name="aws-properties-bedrockagentcore-harness-harnessbedrockmodelconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-harness-harnessbedrockmodelconfig-syntax.json"></a>

```
{
  "[AdditionalParams](#cfn-bedrockagentcore-harness-harnessbedrockmodelconfig-additionalparams)" : {{{{{Key}}: {{Value}}, ...}}},
  "[ApiFormat](#cfn-bedrockagentcore-harness-harnessbedrockmodelconfig-apiformat)" : {{String}},
  "[MaxTokens](#cfn-bedrockagentcore-harness-harnessbedrockmodelconfig-maxtokens)" : {{Integer}},
  "[ModelId](#cfn-bedrockagentcore-harness-harnessbedrockmodelconfig-modelid)" : {{String}},
  "[Temperature](#cfn-bedrockagentcore-harness-harnessbedrockmodelconfig-temperature)" : {{Number}},
  "[TopP](#cfn-bedrockagentcore-harness-harnessbedrockmodelconfig-topp)" : {{Number}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-harness-harnessbedrockmodelconfig-syntax.yaml"></a>

```
  [AdditionalParams](#cfn-bedrockagentcore-harness-harnessbedrockmodelconfig-additionalparams): {{
    {{Key}}: {{Value}}}}
  [ApiFormat](#cfn-bedrockagentcore-harness-harnessbedrockmodelconfig-apiformat): {{String}}
  [MaxTokens](#cfn-bedrockagentcore-harness-harnessbedrockmodelconfig-maxtokens): {{Integer}}
  [ModelId](#cfn-bedrockagentcore-harness-harnessbedrockmodelconfig-modelid): {{String}}
  [Temperature](#cfn-bedrockagentcore-harness-harnessbedrockmodelconfig-temperature): {{Number}}
  [TopP](#cfn-bedrockagentcore-harness-harnessbedrockmodelconfig-topp): {{Number}}
```

## Properties
<a name="aws-properties-bedrockagentcore-harness-harnessbedrockmodelconfig-properties"></a>

`AdditionalParams`  <a name="cfn-bedrockagentcore-harness-harnessbedrockmodelconfig-additionalparams"></a>
Provider-specific parameters passed through to the model provider unchanged.
*Required*: No
*Type*: Object
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApiFormat`  <a name="cfn-bedrockagentcore-harness-harnessbedrockmodelconfig-apiformat"></a>
The API format to use when calling the Bedrock provider.
*Required*: No
*Type*: String
*Allowed values*: `converse_stream | responses | chat_completions`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxTokens`  <a name="cfn-bedrockagentcore-harness-harnessbedrockmodelconfig-maxtokens"></a>
The maximum number of tokens to allow in the generated response per model call.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ModelId`  <a name="cfn-bedrockagentcore-harness-harnessbedrockmodelconfig-modelid"></a>
The Bedrock model ID.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Temperature`  <a name="cfn-bedrockagentcore-harness-harnessbedrockmodelconfig-temperature"></a>
The temperature to set when calling the model.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TopP`  <a name="cfn-bedrockagentcore-harness-harnessbedrockmodelconfig-topp"></a>
The topP set when calling the model.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
