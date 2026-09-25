---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-geospatialgradientcolor.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template GeospatialGradientColor
<a name="aws-properties-quicksight-template-geospatialgradientcolor"></a>

The definition for a gradient color.

## Syntax
<a name="aws-properties-quicksight-template-geospatialgradientcolor-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-geospatialgradientcolor-syntax.json"></a>

```
{
  "[DefaultOpacity](#cfn-quicksight-template-geospatialgradientcolor-defaultopacity)" : {{Number}},
  "[NullDataSettings](#cfn-quicksight-template-geospatialgradientcolor-nulldatasettings)" : {{GeospatialNullDataSettings}},
  "[NullDataVisibility](#cfn-quicksight-template-geospatialgradientcolor-nulldatavisibility)" : {{String}},
  "[StepColors](#cfn-quicksight-template-geospatialgradientcolor-stepcolors)" : {{[ GeospatialGradientStepColor, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-template-geospatialgradientcolor-syntax.yaml"></a>

```
  [DefaultOpacity](#cfn-quicksight-template-geospatialgradientcolor-defaultopacity): {{Number}}
  [NullDataSettings](#cfn-quicksight-template-geospatialgradientcolor-nulldatasettings): {{
    GeospatialNullDataSettings}}
  [NullDataVisibility](#cfn-quicksight-template-geospatialgradientcolor-nulldatavisibility): {{String}}
  [StepColors](#cfn-quicksight-template-geospatialgradientcolor-stepcolors): {{
    - GeospatialGradientStepColor}}
```

## Properties
<a name="aws-properties-quicksight-template-geospatialgradientcolor-properties"></a>

`DefaultOpacity`  <a name="cfn-quicksight-template-geospatialgradientcolor-defaultopacity"></a>
The default opacity for the gradient color.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NullDataSettings`  <a name="cfn-quicksight-template-geospatialgradientcolor-nulldatasettings"></a>
The null data visualization settings.
*Required*: No
*Type*: [GeospatialNullDataSettings](aws-properties-quicksight-template-geospatialnulldatasettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NullDataVisibility`  <a name="cfn-quicksight-template-geospatialgradientcolor-nulldatavisibility"></a>
The state of visibility for null data.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StepColors`  <a name="cfn-quicksight-template-geospatialgradientcolor-stepcolors"></a>
A list of gradient step colors for the gradient.
*Required*: Yes
*Type*: Array of [GeospatialGradientStepColor](aws-properties-quicksight-template-geospatialgradientstepcolor.md)
*Minimum*: `2`
*Maximum*: `3`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
