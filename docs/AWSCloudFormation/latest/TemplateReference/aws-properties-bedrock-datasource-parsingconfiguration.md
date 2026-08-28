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
The parsing strategy for the data source. Only `SMART_PARSING` can be selected for managed knowledge bases. For more information, see [Customize ingestion for managed knowledge bases](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-managed-customize-ingestion.html).
*Required*: Yes
*Type*: String
*Allowed values*: `BEDROCK_FOUNDATION_MODEL | BEDROCK_DATA_AUTOMATION | SMART_PARSING`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
