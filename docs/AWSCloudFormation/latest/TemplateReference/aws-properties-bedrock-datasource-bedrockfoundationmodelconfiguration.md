---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-datasource-bedrockfoundationmodelconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataSource BedrockFoundationModelConfiguration
<a name="aws-properties-bedrock-datasource-bedrockfoundationmodelconfiguration"></a>

Configuration for a Bedrock foundation model.

## Syntax
<a name="aws-properties-bedrock-datasource-bedrockfoundationmodelconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-datasource-bedrockfoundationmodelconfiguration-syntax.json"></a>

```
{
  "[ModelArn](#cfn-bedrock-datasource-bedrockfoundationmodelconfiguration-modelarn)" : {{String}},
  "[ParsingModality](#cfn-bedrock-datasource-bedrockfoundationmodelconfiguration-parsingmodality)" : {{String}},
  "[ParsingPrompt](#cfn-bedrock-datasource-bedrockfoundationmodelconfiguration-parsingprompt)" : {{ParsingPrompt}}
}
```

### YAML
<a name="aws-properties-bedrock-datasource-bedrockfoundationmodelconfiguration-syntax.yaml"></a>

```
  [ModelArn](#cfn-bedrock-datasource-bedrockfoundationmodelconfiguration-modelarn): {{String}}
  [ParsingModality](#cfn-bedrock-datasource-bedrockfoundationmodelconfiguration-parsingmodality): {{String}}
  [ParsingPrompt](#cfn-bedrock-datasource-bedrockfoundationmodelconfiguration-parsingprompt): {{
    ParsingPrompt}}
```

## Properties
<a name="aws-properties-bedrock-datasource-bedrockfoundationmodelconfiguration-properties"></a>

`ModelArn`  <a name="cfn-bedrock-datasource-bedrockfoundationmodelconfiguration-modelarn"></a>
The ARN of the foundation model to use for parsing.
*Required*: Yes
*Type*: String
*Pattern*: `^(arn:aws(-cn|-us-gov|-eusc|-iso(-[b-f])?)?:(bedrock):[a-z0-9-]{1,20}:([0-9]{12})?:([a-z-]+/)?)?([a-zA-Z0-9.-]{1,63}){0,2}(([:][a-z0-9-]{1,63}){0,2})?(/[a-z0-9]{1,12})?$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ParsingModality`  <a name="cfn-bedrock-datasource-bedrockfoundationmodelconfiguration-parsingmodality"></a>
Specifies whether to enable parsing of multimodal data, including both text and/or images.
*Required*: No
*Type*: String
*Allowed values*: `MULTIMODAL`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ParsingPrompt`  <a name="cfn-bedrock-datasource-bedrockfoundationmodelconfiguration-parsingprompt"></a>
Instructions for interpreting the contents of a document.
*Required*: No
*Type*: [ParsingPrompt](aws-properties-bedrock-datasource-parsingprompt.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
