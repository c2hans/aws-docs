---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-datasource-bedrockdataautomationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataSource BedrockDataAutomationConfiguration
<a name="aws-properties-bedrock-datasource-bedrockdataautomationconfiguration"></a>

Contains configurations for using Amazon Bedrock Data Automation as the parser for ingesting your data sources.

## Syntax
<a name="aws-properties-bedrock-datasource-bedrockdataautomationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-datasource-bedrockdataautomationconfiguration-syntax.json"></a>

```
{
  "[ParsingModality](#cfn-bedrock-datasource-bedrockdataautomationconfiguration-parsingmodality)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-datasource-bedrockdataautomationconfiguration-syntax.yaml"></a>

```
  [ParsingModality](#cfn-bedrock-datasource-bedrockdataautomationconfiguration-parsingmodality): {{String}}
```

## Properties
<a name="aws-properties-bedrock-datasource-bedrockdataautomationconfiguration-properties"></a>

`ParsingModality`  <a name="cfn-bedrock-datasource-bedrockdataautomationconfiguration-parsingmodality"></a>
Specifies whether to enable parsing of multimodal data, including both text and/or images.
*Required*: No
*Type*: String
*Allowed values*: `MULTIMODAL`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
