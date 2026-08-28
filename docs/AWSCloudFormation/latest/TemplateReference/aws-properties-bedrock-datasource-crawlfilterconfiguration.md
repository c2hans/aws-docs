---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-datasource-crawlfilterconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataSource CrawlFilterConfiguration
<a name="aws-properties-bedrock-datasource-crawlfilterconfiguration"></a>

The configuration of filtering the data source content. For example, configuring regular expression patterns to include or exclude certain content.

## Syntax
<a name="aws-properties-bedrock-datasource-crawlfilterconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-datasource-crawlfilterconfiguration-syntax.json"></a>

```
{
  "[PatternObjectFilter](#cfn-bedrock-datasource-crawlfilterconfiguration-patternobjectfilter)" : {{PatternObjectFilterConfiguration}},
  "[Type](#cfn-bedrock-datasource-crawlfilterconfiguration-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-datasource-crawlfilterconfiguration-syntax.yaml"></a>

```
  [PatternObjectFilter](#cfn-bedrock-datasource-crawlfilterconfiguration-patternobjectfilter): {{
    PatternObjectFilterConfiguration}}
  [Type](#cfn-bedrock-datasource-crawlfilterconfiguration-type): {{String}}
```

## Properties
<a name="aws-properties-bedrock-datasource-crawlfilterconfiguration-properties"></a>

`PatternObjectFilter`  <a name="cfn-bedrock-datasource-crawlfilterconfiguration-patternobjectfilter"></a>
The configuration of filtering certain objects or content types of the data source.
*Required*: No
*Type*: [PatternObjectFilterConfiguration](aws-properties-bedrock-datasource-patternobjectfilterconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-bedrock-datasource-crawlfilterconfiguration-type"></a>
The type of filtering that you want to apply to certain objects or content of the data source. For example, the `PATTERN` type is regular expression patterns you can apply to filter your content.
*Required*: Yes
*Type*: String
*Allowed values*: `PATTERN`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
