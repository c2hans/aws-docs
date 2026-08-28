---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-stringformatconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template StringFormatConfiguration
<a name="aws-properties-quicksight-template-stringformatconfiguration"></a>

Formatting configuration for string fields.

## Syntax
<a name="aws-properties-quicksight-template-stringformatconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-stringformatconfiguration-syntax.json"></a>

```
{
  "[NullValueFormatConfiguration](#cfn-quicksight-template-stringformatconfiguration-nullvalueformatconfiguration)" : {{NullValueFormatConfiguration}},
  "[NumericFormatConfiguration](#cfn-quicksight-template-stringformatconfiguration-numericformatconfiguration)" : {{NumericFormatConfiguration}}
}
```

### YAML
<a name="aws-properties-quicksight-template-stringformatconfiguration-syntax.yaml"></a>

```
  [NullValueFormatConfiguration](#cfn-quicksight-template-stringformatconfiguration-nullvalueformatconfiguration): {{
    NullValueFormatConfiguration}}
  [NumericFormatConfiguration](#cfn-quicksight-template-stringformatconfiguration-numericformatconfiguration): {{
    NumericFormatConfiguration}}
```

## Properties
<a name="aws-properties-quicksight-template-stringformatconfiguration-properties"></a>

`NullValueFormatConfiguration`  <a name="cfn-quicksight-template-stringformatconfiguration-nullvalueformatconfiguration"></a>
The options that determine the null value format configuration.
*Required*: No
*Type*: [NullValueFormatConfiguration](aws-properties-quicksight-template-nullvalueformatconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NumericFormatConfiguration`  <a name="cfn-quicksight-template-stringformatconfiguration-numericformatconfiguration"></a>
The formatting configuration for numeric strings.
*Required*: No
*Type*: [NumericFormatConfiguration](aws-properties-quicksight-template-numericformatconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
