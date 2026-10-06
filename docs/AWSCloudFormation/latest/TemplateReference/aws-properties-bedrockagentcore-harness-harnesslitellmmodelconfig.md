---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-harness-harnesslitellmmodelconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Harness HarnessLiteLlmModelConfig
<a name="aws-properties-bedrockagentcore-harness-harnesslitellmmodelconfig"></a>

Configuration for a LiteLLM model provider, enabling connection to third-party model providers.

## Syntax
<a name="aws-properties-bedrockagentcore-harness-harnesslitellmmodelconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-harness-harnesslitellmmodelconfig-syntax.json"></a>

```
{
  "[AdditionalParams](#cfn-bedrockagentcore-harness-harnesslitellmmodelconfig-additionalparams)" : {{Json}},
  "[ApiBase](#cfn-bedrockagentcore-harness-harnesslitellmmodelconfig-apibase)" : {{String}},
  "[ApiKeyArn](#cfn-bedrockagentcore-harness-harnesslitellmmodelconfig-apikeyarn)" : {{String}},
  "[MaxTokens](#cfn-bedrockagentcore-harness-harnesslitellmmodelconfig-maxtokens)" : {{Integer}},
  "[ModelId](#cfn-bedrockagentcore-harness-harnesslitellmmodelconfig-modelid)" : {{String}},
  "[Temperature](#cfn-bedrockagentcore-harness-harnesslitellmmodelconfig-temperature)" : {{Number}},
  "[TopP](#cfn-bedrockagentcore-harness-harnesslitellmmodelconfig-topp)" : {{Number}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-harness-harnesslitellmmodelconfig-syntax.yaml"></a>

```
  [AdditionalParams](#cfn-bedrockagentcore-harness-harnesslitellmmodelconfig-additionalparams): {{Json}}
  [ApiBase](#cfn-bedrockagentcore-harness-harnesslitellmmodelconfig-apibase): {{String}}
  [ApiKeyArn](#cfn-bedrockagentcore-harness-harnesslitellmmodelconfig-apikeyarn): {{String}}
  [MaxTokens](#cfn-bedrockagentcore-harness-harnesslitellmmodelconfig-maxtokens): {{Integer}}
  [ModelId](#cfn-bedrockagentcore-harness-harnesslitellmmodelconfig-modelid): {{String}}
  [Temperature](#cfn-bedrockagentcore-harness-harnesslitellmmodelconfig-temperature): {{Number}}
  [TopP](#cfn-bedrockagentcore-harness-harnesslitellmmodelconfig-topp): {{Number}}
```

## Properties
<a name="aws-properties-bedrockagentcore-harness-harnesslitellmmodelconfig-properties"></a>

`AdditionalParams`  <a name="cfn-bedrockagentcore-harness-harnesslitellmmodelconfig-additionalparams"></a>
Provider-specific parameters passed through to the model provider unchanged.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApiBase`  <a name="cfn-bedrockagentcore-harness-harnesslitellmmodelconfig-apibase"></a>
The base URL for the model provider's API endpoint.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `16383`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApiKeyArn`  <a name="cfn-bedrockagentcore-harness-harnesslitellmmodelconfig-apikeyarn"></a>
The ARN of the API key in AgentCore Identity for authenticating with the model provider.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:token-vault/[a-zA-Z0-9-.]+/apikeycredentialprovider/[a-zA-Z0-9-.]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxTokens`  <a name="cfn-bedrockagentcore-harness-harnesslitellmmodelconfig-maxtokens"></a>
The maximum number of tokens to allow in the generated response per iteration.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ModelId`  <a name="cfn-bedrockagentcore-harness-harnesslitellmmodelconfig-modelid"></a>
The LiteLLM model identifier (e.g., "anthropic/claude-3-sonnet").
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Temperature`  <a name="cfn-bedrockagentcore-harness-harnesslitellmmodelconfig-temperature"></a>
The temperature to set when calling the model.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TopP`  <a name="cfn-bedrockagentcore-harness-harnesslitellmmodelconfig-topp"></a>
The topP set when calling the model.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
