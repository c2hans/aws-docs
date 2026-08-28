---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-numberformatconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard NumberFormatConfiguration
<a name="aws-properties-quicksight-dashboard-numberformatconfiguration"></a>

Formatting configuration for number fields.

## Syntax
<a name="aws-properties-quicksight-dashboard-numberformatconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-numberformatconfiguration-syntax.json"></a>

```
{
  "[FormatConfiguration](#cfn-quicksight-dashboard-numberformatconfiguration-formatconfiguration)" : {{NumericFormatConfiguration}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-numberformatconfiguration-syntax.yaml"></a>

```
  [FormatConfiguration](#cfn-quicksight-dashboard-numberformatconfiguration-formatconfiguration): {{
    NumericFormatConfiguration}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-numberformatconfiguration-properties"></a>

`FormatConfiguration`  <a name="cfn-quicksight-dashboard-numberformatconfiguration-formatconfiguration"></a>
The options that determine the numeric format configuration.
*Required*: No
*Type*: [NumericFormatConfiguration](aws-properties-quicksight-dashboard-numericformatconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
