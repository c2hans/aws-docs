---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-qnaintentconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot QnAIntentConfiguration
<a name="aws-properties-lex-bot-qnaintentconfiguration"></a>

Details about the the configuration of the built-in `Amazon.QnAIntent`.

## Syntax
<a name="aws-properties-lex-bot-qnaintentconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-qnaintentconfiguration-syntax.json"></a>

```
{
  "[BedrockModelConfiguration](#cfn-lex-bot-qnaintentconfiguration-bedrockmodelconfiguration)" : {{BedrockModelSpecification}},
  "[DataSourceConfiguration](#cfn-lex-bot-qnaintentconfiguration-datasourceconfiguration)" : {{DataSourceConfiguration}}
}
```

### YAML
<a name="aws-properties-lex-bot-qnaintentconfiguration-syntax.yaml"></a>

```
  [BedrockModelConfiguration](#cfn-lex-bot-qnaintentconfiguration-bedrockmodelconfiguration): {{
    BedrockModelSpecification}}
  [DataSourceConfiguration](#cfn-lex-bot-qnaintentconfiguration-datasourceconfiguration): {{
    DataSourceConfiguration}}
```

## Properties
<a name="aws-properties-lex-bot-qnaintentconfiguration-properties"></a>

`BedrockModelConfiguration`  <a name="cfn-lex-bot-qnaintentconfiguration-bedrockmodelconfiguration"></a>
Property description not available.
*Required*: Yes
*Type*: [BedrockModelSpecification](aws-properties-lex-bot-bedrockmodelspecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataSourceConfiguration`  <a name="cfn-lex-bot-qnaintentconfiguration-datasourceconfiguration"></a>
Contains details about the configuration of the data source used for the `AMAZON.QnAIntent`.
*Required*: Yes
*Type*: [DataSourceConfiguration](aws-properties-lex-bot-datasourceconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
