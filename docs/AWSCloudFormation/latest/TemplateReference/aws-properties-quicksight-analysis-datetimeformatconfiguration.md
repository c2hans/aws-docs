---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-datetimeformatconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis DateTimeFormatConfiguration
<a name="aws-properties-quicksight-analysis-datetimeformatconfiguration"></a>

Formatting configuration for `DateTime` fields.

## Syntax
<a name="aws-properties-quicksight-analysis-datetimeformatconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-datetimeformatconfiguration-syntax.json"></a>

```
{
  "[DateTimeFormat](#cfn-quicksight-analysis-datetimeformatconfiguration-datetimeformat)" : {{String}},
  "[NullValueFormatConfiguration](#cfn-quicksight-analysis-datetimeformatconfiguration-nullvalueformatconfiguration)" : {{NullValueFormatConfiguration}},
  "[NumericFormatConfiguration](#cfn-quicksight-analysis-datetimeformatconfiguration-numericformatconfiguration)" : {{NumericFormatConfiguration}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-datetimeformatconfiguration-syntax.yaml"></a>

```
  [DateTimeFormat](#cfn-quicksight-analysis-datetimeformatconfiguration-datetimeformat): {{String}}
  [NullValueFormatConfiguration](#cfn-quicksight-analysis-datetimeformatconfiguration-nullvalueformatconfiguration): {{
    NullValueFormatConfiguration}}
  [NumericFormatConfiguration](#cfn-quicksight-analysis-datetimeformatconfiguration-numericformatconfiguration): {{
    NumericFormatConfiguration}}
```

## Properties
<a name="aws-properties-quicksight-analysis-datetimeformatconfiguration-properties"></a>

`DateTimeFormat`  <a name="cfn-quicksight-analysis-datetimeformatconfiguration-datetimeformat"></a>
Determines the `DateTime` format.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NullValueFormatConfiguration`  <a name="cfn-quicksight-analysis-datetimeformatconfiguration-nullvalueformatconfiguration"></a>
The options that determine the null value format configuration.
*Required*: No
*Type*: [NullValueFormatConfiguration](aws-properties-quicksight-analysis-nullvalueformatconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NumericFormatConfiguration`  <a name="cfn-quicksight-analysis-datetimeformatconfiguration-numericformatconfiguration"></a>
The formatting configuration for numeric `DateTime` fields.
*Required*: No
*Type*: [NumericFormatConfiguration](aws-properties-quicksight-analysis-numericformatconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
