---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-colorsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard ColorsConfiguration
<a name="aws-properties-quicksight-dashboard-colorsconfiguration"></a>

The color configurations for a column.

## Syntax
<a name="aws-properties-quicksight-dashboard-colorsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-colorsconfiguration-syntax.json"></a>

```
{
  "[CustomColors](#cfn-quicksight-dashboard-colorsconfiguration-customcolors)" : {{[ CustomColor, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-colorsconfiguration-syntax.yaml"></a>

```
  [CustomColors](#cfn-quicksight-dashboard-colorsconfiguration-customcolors): {{
    - CustomColor}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-colorsconfiguration-properties"></a>

`CustomColors`  <a name="cfn-quicksight-dashboard-colorsconfiguration-customcolors"></a>
A list of up to 50 custom colors.
*Required*: No
*Type*: Array of [CustomColor](aws-properties-quicksight-dashboard-customcolor.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
