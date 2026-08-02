---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-visualpalette.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template VisualPalette
<a name="aws-properties-quicksight-template-visualpalette"></a>

The visual display options for the visual palette.

## Syntax
<a name="aws-properties-quicksight-template-visualpalette-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-visualpalette-syntax.json"></a>

```
{
  "[ChartColor](#cfn-quicksight-template-visualpalette-chartcolor)" : {{String}},
  "[ColorMap](#cfn-quicksight-template-visualpalette-colormap)" : {{[ DataPathColor, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-template-visualpalette-syntax.yaml"></a>

```
  [ChartColor](#cfn-quicksight-template-visualpalette-chartcolor): {{String}}
  [ColorMap](#cfn-quicksight-template-visualpalette-colormap): {{
    - DataPathColor}}
```

## Properties
<a name="aws-properties-quicksight-template-visualpalette-properties"></a>

`ChartColor`  <a name="cfn-quicksight-template-visualpalette-chartcolor"></a>
The chart color options for the visual palette.
*Required*: No
*Type*: String
*Pattern*: `^#[A-F0-9]{6}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ColorMap`  <a name="cfn-quicksight-template-visualpalette-colormap"></a>
The color map options for the visual palette.
*Required*: No
*Type*: Array of [DataPathColor](aws-properties-quicksight-template-datapathcolor.md)
*Minimum*: `0`
*Maximum*: `5000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
