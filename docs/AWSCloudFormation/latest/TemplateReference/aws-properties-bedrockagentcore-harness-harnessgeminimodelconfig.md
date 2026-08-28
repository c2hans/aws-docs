---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-harness-harnessgeminimodelconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Harness HarnessGeminiModelConfig
<a name="aws-properties-bedrockagentcore-harness-harnessgeminimodelconfig"></a>

Configuration for a Google Gemini model provider. Requires an API key stored in AgentCore Identity.

## Syntax
<a name="aws-properties-bedrockagentcore-harness-harnessgeminimodelconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-harness-harnessgeminimodelconfig-syntax.json"></a>

```
{
  "[ApiKeyArn](#cfn-bedrockagentcore-harness-harnessgeminimodelconfig-apikeyarn)" : {{String}},
  "[MaxTokens](#cfn-bedrockagentcore-harness-harnessgeminimodelconfig-maxtokens)" : {{Integer}},
  "[ModelId](#cfn-bedrockagentcore-harness-harnessgeminimodelconfig-modelid)" : {{String}},
  "[Temperature](#cfn-bedrockagentcore-harness-harnessgeminimodelconfig-temperature)" : {{Number}},
  "[TopK](#cfn-bedrockagentcore-harness-harnessgeminimodelconfig-topk)" : {{Integer}},
  "[TopP](#cfn-bedrockagentcore-harness-harnessgeminimodelconfig-topp)" : {{Number}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-harness-harnessgeminimodelconfig-syntax.yaml"></a>

```
  [ApiKeyArn](#cfn-bedrockagentcore-harness-harnessgeminimodelconfig-apikeyarn): {{String}}
  [MaxTokens](#cfn-bedrockagentcore-harness-harnessgeminimodelconfig-maxtokens): {{Integer}}
  [ModelId](#cfn-bedrockagentcore-harness-harnessgeminimodelconfig-modelid): {{String}}
  [Temperature](#cfn-bedrockagentcore-harness-harnessgeminimodelconfig-temperature): {{Number}}
  [TopK](#cfn-bedrockagentcore-harness-harnessgeminimodelconfig-topk): {{Integer}}
  [TopP](#cfn-bedrockagentcore-harness-harnessgeminimodelconfig-topp): {{Number}}
```

## Properties
<a name="aws-properties-bedrockagentcore-harness-harnessgeminimodelconfig-properties"></a>

`ApiKeyArn`  <a name="cfn-bedrockagentcore-harness-harnessgeminimodelconfig-apikeyarn"></a>
The ARN of your Gemini API key on AgentCore Identity.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:token-vault/[a-zA-Z0-9-.]+/apikeycredentialprovider/[a-zA-Z0-9-.]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxTokens`  <a name="cfn-bedrockagentcore-harness-harnessgeminimodelconfig-maxtokens"></a>
The maximum number of tokens to allow in the generated response per model call.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ModelId`  <a name="cfn-bedrockagentcore-harness-harnessgeminimodelconfig-modelid"></a>
The Gemini model ID.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Temperature`  <a name="cfn-bedrockagentcore-harness-harnessgeminimodelconfig-temperature"></a>
The temperature to set when calling the model.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TopK`  <a name="cfn-bedrockagentcore-harness-harnessgeminimodelconfig-topk"></a>
The topK set when calling the model.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TopP`  <a name="cfn-bedrockagentcore-harness-harnessgeminimodelconfig-topp"></a>
The topP set when calling the model.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
