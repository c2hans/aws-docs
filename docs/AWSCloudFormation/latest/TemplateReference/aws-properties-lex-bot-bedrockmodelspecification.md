---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-bedrockmodelspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot BedrockModelSpecification
<a name="aws-properties-lex-bot-bedrockmodelspecification"></a>

Contains information about the Amazon Bedrock model used to interpret the prompt used in descriptive bot building.

## Syntax
<a name="aws-properties-lex-bot-bedrockmodelspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-bedrockmodelspecification-syntax.json"></a>

```
{
  "[BedrockGuardrailConfiguration](#cfn-lex-bot-bedrockmodelspecification-bedrockguardrailconfiguration)" : {{BedrockGuardrailConfiguration}},
  "[BedrockModelCustomPrompt](#cfn-lex-bot-bedrockmodelspecification-bedrockmodelcustomprompt)" : {{String}},
  "[BedrockTraceStatus](#cfn-lex-bot-bedrockmodelspecification-bedrocktracestatus)" : {{String}},
  "[ModelArn](#cfn-lex-bot-bedrockmodelspecification-modelarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-lex-bot-bedrockmodelspecification-syntax.yaml"></a>

```
  [BedrockGuardrailConfiguration](#cfn-lex-bot-bedrockmodelspecification-bedrockguardrailconfiguration): {{
    BedrockGuardrailConfiguration}}
  [BedrockModelCustomPrompt](#cfn-lex-bot-bedrockmodelspecification-bedrockmodelcustomprompt): {{String}}
  [BedrockTraceStatus](#cfn-lex-bot-bedrockmodelspecification-bedrocktracestatus): {{String}}
  [ModelArn](#cfn-lex-bot-bedrockmodelspecification-modelarn): {{String}}
```

## Properties
<a name="aws-properties-lex-bot-bedrockmodelspecification-properties"></a>

`BedrockGuardrailConfiguration`  <a name="cfn-lex-bot-bedrockmodelspecification-bedrockguardrailconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [BedrockGuardrailConfiguration](aws-properties-lex-bot-bedrockguardrailconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BedrockModelCustomPrompt`  <a name="cfn-lex-bot-bedrockmodelspecification-bedrockmodelcustomprompt"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `5000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BedrockTraceStatus`  <a name="cfn-lex-bot-bedrockmodelspecification-bedrocktracestatus"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ModelArn`  <a name="cfn-lex-bot-bedrockmodelspecification-modelarn"></a>
The ARN of the foundation model used in descriptive bot building.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `5000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
