---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-knowledgebase-parsingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::KnowledgeBase ParsingConfiguration
<a name="aws-properties-wisdom-knowledgebase-parsingconfiguration"></a>

Settings for parsing document contents. By default, the service converts the contents of each document into text before splitting it into chunks. To improve processing of PDF files with tables and images, you can configure the data source to convert the pages of text into images and use a model to describe the contents of each page.

## Syntax
<a name="aws-properties-wisdom-knowledgebase-parsingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-knowledgebase-parsingconfiguration-syntax.json"></a>

```
{
  "[BedrockFoundationModelConfiguration](#cfn-wisdom-knowledgebase-parsingconfiguration-bedrockfoundationmodelconfiguration)" : {{BedrockFoundationModelConfiguration}},
  "[ParsingStrategy](#cfn-wisdom-knowledgebase-parsingconfiguration-parsingstrategy)" : {{String}}
}
```

### YAML
<a name="aws-properties-wisdom-knowledgebase-parsingconfiguration-syntax.yaml"></a>

```
  [BedrockFoundationModelConfiguration](#cfn-wisdom-knowledgebase-parsingconfiguration-bedrockfoundationmodelconfiguration): {{
    BedrockFoundationModelConfiguration}}
  [ParsingStrategy](#cfn-wisdom-knowledgebase-parsingconfiguration-parsingstrategy): {{String}}
```

## Properties
<a name="aws-properties-wisdom-knowledgebase-parsingconfiguration-properties"></a>

`BedrockFoundationModelConfiguration`  <a name="cfn-wisdom-knowledgebase-parsingconfiguration-bedrockfoundationmodelconfiguration"></a>
Settings for a foundation model used to parse documents for a data source.
*Required*: No
*Type*: [BedrockFoundationModelConfiguration](aws-properties-wisdom-knowledgebase-bedrockfoundationmodelconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParsingStrategy`  <a name="cfn-wisdom-knowledgebase-parsingconfiguration-parsingstrategy"></a>
The parsing strategy for the data source.
*Required*: Yes
*Type*: String
*Allowed values*: `BEDROCK_FOUNDATION_MODEL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
