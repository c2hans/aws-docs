---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-visualpalette.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard VisualPalette
<a name="aws-properties-quicksight-dashboard-visualpalette"></a>

The visual display options for the visual palette.

## Syntax
<a name="aws-properties-quicksight-dashboard-visualpalette-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-visualpalette-syntax.json"></a>

```
{
  "[ChartColor](#cfn-quicksight-dashboard-visualpalette-chartcolor)" : {{String}},
  "[ColorMap](#cfn-quicksight-dashboard-visualpalette-colormap)" : {{[ DataPathColor, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-visualpalette-syntax.yaml"></a>

```
  [ChartColor](#cfn-quicksight-dashboard-visualpalette-chartcolor): {{String}}
  [ColorMap](#cfn-quicksight-dashboard-visualpalette-colormap): {{
    - DataPathColor}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-visualpalette-properties"></a>

`ChartColor`  <a name="cfn-quicksight-dashboard-visualpalette-chartcolor"></a>
The chart color options for the visual palette.
*Required*: No
*Type*: String
*Pattern*: `^#[A-F0-9]{6}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ColorMap`  <a name="cfn-quicksight-dashboard-visualpalette-colormap"></a>
The color map options for the visual palette.
*Required*: No
*Type*: Array of [DataPathColor](aws-properties-quicksight-dashboard-datapathcolor.md)
*Minimum*: `0`
*Maximum*: `5000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
