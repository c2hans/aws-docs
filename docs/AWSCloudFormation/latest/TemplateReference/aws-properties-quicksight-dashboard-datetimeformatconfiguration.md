---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-datetimeformatconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard DateTimeFormatConfiguration
<a name="aws-properties-quicksight-dashboard-datetimeformatconfiguration"></a>

Formatting configuration for `DateTime` fields.

## Syntax
<a name="aws-properties-quicksight-dashboard-datetimeformatconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-datetimeformatconfiguration-syntax.json"></a>

```
{
  "[DateTimeFormat](#cfn-quicksight-dashboard-datetimeformatconfiguration-datetimeformat)" : {{String}},
  "[NullValueFormatConfiguration](#cfn-quicksight-dashboard-datetimeformatconfiguration-nullvalueformatconfiguration)" : {{NullValueFormatConfiguration}},
  "[NumericFormatConfiguration](#cfn-quicksight-dashboard-datetimeformatconfiguration-numericformatconfiguration)" : {{NumericFormatConfiguration}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-datetimeformatconfiguration-syntax.yaml"></a>

```
  [DateTimeFormat](#cfn-quicksight-dashboard-datetimeformatconfiguration-datetimeformat): {{String}}
  [NullValueFormatConfiguration](#cfn-quicksight-dashboard-datetimeformatconfiguration-nullvalueformatconfiguration): {{
    NullValueFormatConfiguration}}
  [NumericFormatConfiguration](#cfn-quicksight-dashboard-datetimeformatconfiguration-numericformatconfiguration): {{
    NumericFormatConfiguration}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-datetimeformatconfiguration-properties"></a>

`DateTimeFormat`  <a name="cfn-quicksight-dashboard-datetimeformatconfiguration-datetimeformat"></a>
Determines the `DateTime` format.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NullValueFormatConfiguration`  <a name="cfn-quicksight-dashboard-datetimeformatconfiguration-nullvalueformatconfiguration"></a>
The options that determine the null value format configuration.
*Required*: No
*Type*: [NullValueFormatConfiguration](aws-properties-quicksight-dashboard-nullvalueformatconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NumericFormatConfiguration`  <a name="cfn-quicksight-dashboard-datetimeformatconfiguration-numericformatconfiguration"></a>
The formatting configuration for numeric `DateTime` fields.
*Required*: No
*Type*: [NumericFormatConfiguration](aws-properties-quicksight-dashboard-numericformatconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
