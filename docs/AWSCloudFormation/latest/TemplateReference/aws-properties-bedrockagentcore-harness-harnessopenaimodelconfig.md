---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-harness-harnessopenaimodelconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Harness HarnessOpenAiModelConfig
<a name="aws-properties-bedrockagentcore-harness-harnessopenaimodelconfig"></a>

Configuration for an OpenAI model provider. Requires an API key stored in AgentCore Identity.

## Syntax
<a name="aws-properties-bedrockagentcore-harness-harnessopenaimodelconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-harness-harnessopenaimodelconfig-syntax.json"></a>

```
{
  "[AdditionalParams](#cfn-bedrockagentcore-harness-harnessopenaimodelconfig-additionalparams)" : {{Json}},
  "[ApiFormat](#cfn-bedrockagentcore-harness-harnessopenaimodelconfig-apiformat)" : {{String}},
  "[ApiKeyArn](#cfn-bedrockagentcore-harness-harnessopenaimodelconfig-apikeyarn)" : {{String}},
  "[MaxTokens](#cfn-bedrockagentcore-harness-harnessopenaimodelconfig-maxtokens)" : {{Integer}},
  "[ModelId](#cfn-bedrockagentcore-harness-harnessopenaimodelconfig-modelid)" : {{String}},
  "[Temperature](#cfn-bedrockagentcore-harness-harnessopenaimodelconfig-temperature)" : {{Number}},
  "[TopP](#cfn-bedrockagentcore-harness-harnessopenaimodelconfig-topp)" : {{Number}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-harness-harnessopenaimodelconfig-syntax.yaml"></a>

```
  [AdditionalParams](#cfn-bedrockagentcore-harness-harnessopenaimodelconfig-additionalparams): {{Json}}
  [ApiFormat](#cfn-bedrockagentcore-harness-harnessopenaimodelconfig-apiformat): {{String}}
  [ApiKeyArn](#cfn-bedrockagentcore-harness-harnessopenaimodelconfig-apikeyarn): {{String}}
  [MaxTokens](#cfn-bedrockagentcore-harness-harnessopenaimodelconfig-maxtokens): {{Integer}}
  [ModelId](#cfn-bedrockagentcore-harness-harnessopenaimodelconfig-modelid): {{String}}
  [Temperature](#cfn-bedrockagentcore-harness-harnessopenaimodelconfig-temperature): {{Number}}
  [TopP](#cfn-bedrockagentcore-harness-harnessopenaimodelconfig-topp): {{Number}}
```

## Properties
<a name="aws-properties-bedrockagentcore-harness-harnessopenaimodelconfig-properties"></a>

`AdditionalParams`  <a name="cfn-bedrockagentcore-harness-harnessopenaimodelconfig-additionalparams"></a>
Provider-specific parameters passed through to the model provider unchanged.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApiFormat`  <a name="cfn-bedrockagentcore-harness-harnessopenaimodelconfig-apiformat"></a>
The API format to use when calling the OpenAI provider.
*Required*: No
*Type*: String
*Allowed values*: `chat_completions | responses`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApiKeyArn`  <a name="cfn-bedrockagentcore-harness-harnessopenaimodelconfig-apikeyarn"></a>
The ARN of your OpenAI API key on AgentCore Identity.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:token-vault/[a-zA-Z0-9-.]+/apikeycredentialprovider/[a-zA-Z0-9-.]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxTokens`  <a name="cfn-bedrockagentcore-harness-harnessopenaimodelconfig-maxtokens"></a>
The maximum number of tokens to allow in the generated response per model call.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ModelId`  <a name="cfn-bedrockagentcore-harness-harnessopenaimodelconfig-modelid"></a>
The OpenAI model ID.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Temperature`  <a name="cfn-bedrockagentcore-harness-harnessopenaimodelconfig-temperature"></a>
The temperature to set when calling the model.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TopP`  <a name="cfn-bedrockagentcore-harness-harnessopenaimodelconfig-topp"></a>
The topP set when calling the model.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
