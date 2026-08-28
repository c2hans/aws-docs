---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-formatconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template FormatConfiguration
<a name="aws-properties-quicksight-template-formatconfiguration"></a>

The formatting configuration for all types of field.

## Syntax
<a name="aws-properties-quicksight-template-formatconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-formatconfiguration-syntax.json"></a>

```
{
  "[DateTimeFormatConfiguration](#cfn-quicksight-template-formatconfiguration-datetimeformatconfiguration)" : {{DateTimeFormatConfiguration}},
  "[NumberFormatConfiguration](#cfn-quicksight-template-formatconfiguration-numberformatconfiguration)" : {{NumberFormatConfiguration}},
  "[StringFormatConfiguration](#cfn-quicksight-template-formatconfiguration-stringformatconfiguration)" : {{StringFormatConfiguration}}
}
```

### YAML
<a name="aws-properties-quicksight-template-formatconfiguration-syntax.yaml"></a>

```
  [DateTimeFormatConfiguration](#cfn-quicksight-template-formatconfiguration-datetimeformatconfiguration): {{
    DateTimeFormatConfiguration}}
  [NumberFormatConfiguration](#cfn-quicksight-template-formatconfiguration-numberformatconfiguration): {{
    NumberFormatConfiguration}}
  [StringFormatConfiguration](#cfn-quicksight-template-formatconfiguration-stringformatconfiguration): {{
    StringFormatConfiguration}}
```

## Properties
<a name="aws-properties-quicksight-template-formatconfiguration-properties"></a>

`DateTimeFormatConfiguration`  <a name="cfn-quicksight-template-formatconfiguration-datetimeformatconfiguration"></a>
Formatting configuration for `DateTime` fields.
*Required*: No
*Type*: [DateTimeFormatConfiguration](aws-properties-quicksight-template-datetimeformatconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NumberFormatConfiguration`  <a name="cfn-quicksight-template-formatconfiguration-numberformatconfiguration"></a>
Formatting configuration for number fields.
*Required*: No
*Type*: [NumberFormatConfiguration](aws-properties-quicksight-template-numberformatconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StringFormatConfiguration`  <a name="cfn-quicksight-template-formatconfiguration-stringformatconfiguration"></a>
Formatting configuration for string fields.
*Required*: No
*Type*: [StringFormatConfiguration](aws-properties-quicksight-template-stringformatconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
