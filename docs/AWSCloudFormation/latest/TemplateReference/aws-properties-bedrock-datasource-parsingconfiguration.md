---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-datasource-parsingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataSource ParsingConfiguration
<a name="aws-properties-bedrock-datasource-parsingconfiguration"></a>

Settings for parsing document contents. If you exclude this field, the default parser converts the contents of each document into text before splitting it into chunks. Specify the parsing strategy to use in the `parsingStrategy` field and include the relevant configuration, or omit it to use the Amazon Bedrock default parser. For more information, see [Parsing options for your data source](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-advanced-parsing.html).

**Note**
If you specify `BEDROCK_DATA_AUTOMATION` or `BEDROCK_FOUNDATION_MODEL` and it fails to parse a file, the Amazon Bedrock default parser will be used instead.

## Syntax
<a name="aws-properties-bedrock-datasource-parsingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-datasource-parsingconfiguration-syntax.json"></a>

```
{
  "[BedrockDataAutomationConfiguration](#cfn-bedrock-datasource-parsingconfiguration-bedrockdataautomationconfiguration)" : {{BedrockDataAutomationConfiguration}},
  "[BedrockFoundationModelConfiguration](#cfn-bedrock-datasource-parsingconfiguration-bedrockfoundationmodelconfiguration)" : {{BedrockFoundationModelConfiguration}},
  "[ParsingStrategy](#cfn-bedrock-datasource-parsingconfiguration-parsingstrategy)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-datasource-parsingconfiguration-syntax.yaml"></a>

```
  [BedrockDataAutomationConfiguration](#cfn-bedrock-datasource-parsingconfiguration-bedrockdataautomationconfiguration): {{
    BedrockDataAutomationConfiguration}}
  [BedrockFoundationModelConfiguration](#cfn-bedrock-datasource-parsingconfiguration-bedrockfoundationmodelconfiguration): {{
    BedrockFoundationModelConfiguration}}
  [ParsingStrategy](#cfn-bedrock-datasource-parsingconfiguration-parsingstrategy): {{String}}
```

## Properties
<a name="aws-properties-bedrock-datasource-parsingconfiguration-properties"></a>

`BedrockDataAutomationConfiguration`  <a name="cfn-bedrock-datasource-parsingconfiguration-bedrockdataautomationconfiguration"></a>
If you specify `BEDROCK_DATA_AUTOMATION` as the parsing strategy for ingesting your data source, use this object to modify configurations for using the Amazon Bedrock Data Automation parser.
*Required*: No
*Type*: [BedrockDataAutomationConfiguration](aws-properties-bedrock-datasource-bedrockdataautomationconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`BedrockFoundationModelConfiguration`  <a name="cfn-bedrock-datasource-parsingconfiguration-bedrockfoundationmodelconfiguration"></a>
If you specify `BEDROCK_FOUNDATION_MODEL` as the parsing strategy for ingesting your data source, use this object to modify configurations for using a foundation model to parse documents.
*Required*: No
*Type*: [BedrockFoundationModelConfiguration](aws-properties-bedrock-datasource-bedrockfoundationmodelconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ParsingStrategy`  <a name="cfn-bedrock-datasource-parsingconfiguration-parsingstrategy"></a>
The parsing strategy for the data source.
For managed knowledge bases, the strategy that you can select depends on the embedding model that your knowledge base uses:
+ If your knowledge base uses a native multimodal embedding model, specify `MULTI_MODAL_EMBEDDINGS`. With this strategy, files are sent directly to the embedding model instead of being parsed into text. This is the only strategy that is supported for these knowledge bases.
+ Otherwise, specify `SMART_PARSING`.
For more information, see [Customize ingestion for managed knowledge bases](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-managed-customize-ingestion.html).
*Required*: Yes
*Type*: String
*Allowed values*: `BEDROCK_FOUNDATION_MODEL | BEDROCK_DATA_AUTOMATION | SMART_PARSING | MULTI_MODAL_EMBEDDINGS`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
