---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-bedrockagentintentknowledgebaseconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot BedrockAgentIntentKnowledgeBaseConfiguration
<a name="aws-properties-lex-bot-bedrockagentintentknowledgebaseconfiguration"></a>

<a name="aws-properties-lex-bot-bedrockagentintentknowledgebaseconfiguration-description"></a>The `BedrockAgentIntentKnowledgeBaseConfiguration` property type specifies Property description not available. for an [AWS::Lex::Bot](aws-resource-lex-bot.md).

## Syntax
<a name="aws-properties-lex-bot-bedrockagentintentknowledgebaseconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-bedrockagentintentknowledgebaseconfiguration-syntax.json"></a>

```
{
  "[BedrockKnowledgeBaseArn](#cfn-lex-bot-bedrockagentintentknowledgebaseconfiguration-bedrockknowledgebasearn)" : {{String}},
  "[BedrockModelConfiguration](#cfn-lex-bot-bedrockagentintentknowledgebaseconfiguration-bedrockmodelconfiguration)" : {{BedrockModelSpecification}}
}
```

### YAML
<a name="aws-properties-lex-bot-bedrockagentintentknowledgebaseconfiguration-syntax.yaml"></a>

```
  [BedrockKnowledgeBaseArn](#cfn-lex-bot-bedrockagentintentknowledgebaseconfiguration-bedrockknowledgebasearn): {{String}}
  [BedrockModelConfiguration](#cfn-lex-bot-bedrockagentintentknowledgebaseconfiguration-bedrockmodelconfiguration): {{
    BedrockModelSpecification}}
```

## Properties
<a name="aws-properties-lex-bot-bedrockagentintentknowledgebaseconfiguration-properties"></a>

`BedrockKnowledgeBaseArn`  <a name="cfn-lex-bot-bedrockagentintentknowledgebaseconfiguration-bedrockknowledgebasearn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `5000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BedrockModelConfiguration`  <a name="cfn-lex-bot-bedrockagentintentknowledgebaseconfiguration-bedrockmodelconfiguration"></a>
Property description not available.
*Required*: Yes
*Type*: [BedrockModelSpecification](aws-properties-lex-bot-bedrockmodelspecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
