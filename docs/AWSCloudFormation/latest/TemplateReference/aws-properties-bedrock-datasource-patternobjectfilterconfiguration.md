---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-datasource-patternobjectfilterconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataSource PatternObjectFilterConfiguration
<a name="aws-properties-bedrock-datasource-patternobjectfilterconfiguration"></a>

The configuration of filtering certain objects or content types of the data source.

## Syntax
<a name="aws-properties-bedrock-datasource-patternobjectfilterconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-datasource-patternobjectfilterconfiguration-syntax.json"></a>

```
{
  "[Filters](#cfn-bedrock-datasource-patternobjectfilterconfiguration-filters)" : {{[ PatternObjectFilter, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrock-datasource-patternobjectfilterconfiguration-syntax.yaml"></a>

```
  [Filters](#cfn-bedrock-datasource-patternobjectfilterconfiguration-filters): {{
    - PatternObjectFilter}}
```

## Properties
<a name="aws-properties-bedrock-datasource-patternobjectfilterconfiguration-properties"></a>

`Filters`  <a name="cfn-bedrock-datasource-patternobjectfilterconfiguration-filters"></a>
The configuration of specific filters applied to your data source content. You can filter out or include certain content.
*Required*: Yes
*Type*: Array of [PatternObjectFilter](aws-properties-bedrock-datasource-patternobjectfilter.md)
*Minimum*: `1`
*Maximum*: `25`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
