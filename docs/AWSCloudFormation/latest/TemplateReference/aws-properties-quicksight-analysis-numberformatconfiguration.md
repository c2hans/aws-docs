---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-numberformatconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis NumberFormatConfiguration
<a name="aws-properties-quicksight-analysis-numberformatconfiguration"></a>

Formatting configuration for number fields.

## Syntax
<a name="aws-properties-quicksight-analysis-numberformatconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-numberformatconfiguration-syntax.json"></a>

```
{
  "[FormatConfiguration](#cfn-quicksight-analysis-numberformatconfiguration-formatconfiguration)" : {{NumericFormatConfiguration}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-numberformatconfiguration-syntax.yaml"></a>

```
  [FormatConfiguration](#cfn-quicksight-analysis-numberformatconfiguration-formatconfiguration): {{
    NumericFormatConfiguration}}
```

## Properties
<a name="aws-properties-quicksight-analysis-numberformatconfiguration-properties"></a>

`FormatConfiguration`  <a name="cfn-quicksight-analysis-numberformatconfiguration-formatconfiguration"></a>
The options that determine the numeric format configuration.
*Required*: No
*Type*: [NumericFormatConfiguration](aws-properties-quicksight-analysis-numericformatconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
