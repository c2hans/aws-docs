---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-stringformatconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis StringFormatConfiguration
<a name="aws-properties-quicksight-analysis-stringformatconfiguration"></a>

Formatting configuration for string fields.

## Syntax
<a name="aws-properties-quicksight-analysis-stringformatconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-stringformatconfiguration-syntax.json"></a>

```
{
  "[NullValueFormatConfiguration](#cfn-quicksight-analysis-stringformatconfiguration-nullvalueformatconfiguration)" : {{NullValueFormatConfiguration}},
  "[NumericFormatConfiguration](#cfn-quicksight-analysis-stringformatconfiguration-numericformatconfiguration)" : {{NumericFormatConfiguration}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-stringformatconfiguration-syntax.yaml"></a>

```
  [NullValueFormatConfiguration](#cfn-quicksight-analysis-stringformatconfiguration-nullvalueformatconfiguration): {{
    NullValueFormatConfiguration}}
  [NumericFormatConfiguration](#cfn-quicksight-analysis-stringformatconfiguration-numericformatconfiguration): {{
    NumericFormatConfiguration}}
```

## Properties
<a name="aws-properties-quicksight-analysis-stringformatconfiguration-properties"></a>

`NullValueFormatConfiguration`  <a name="cfn-quicksight-analysis-stringformatconfiguration-nullvalueformatconfiguration"></a>
The options that determine the null value format configuration.
*Required*: No
*Type*: [NullValueFormatConfiguration](aws-properties-quicksight-analysis-nullvalueformatconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NumericFormatConfiguration`  <a name="cfn-quicksight-analysis-stringformatconfiguration-numericformatconfiguration"></a>
The formatting configuration for numeric strings.
*Required*: No
*Type*: [NumericFormatConfiguration](aws-properties-quicksight-analysis-numericformatconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
