---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-geospatiallayercolorfield.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template GeospatialLayerColorField
<a name="aws-properties-quicksight-template-geospatiallayercolorfield"></a>

The color field that defines a gradient or categorical style.

## Syntax
<a name="aws-properties-quicksight-template-geospatiallayercolorfield-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-geospatiallayercolorfield-syntax.json"></a>

```
{
  "[ColorDimensionsFields](#cfn-quicksight-template-geospatiallayercolorfield-colordimensionsfields)" : {{[ DimensionField, ... ]}},
  "[ColorValuesFields](#cfn-quicksight-template-geospatiallayercolorfield-colorvaluesfields)" : {{[ MeasureField, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-template-geospatiallayercolorfield-syntax.yaml"></a>

```
  [ColorDimensionsFields](#cfn-quicksight-template-geospatiallayercolorfield-colordimensionsfields): {{
    - DimensionField}}
  [ColorValuesFields](#cfn-quicksight-template-geospatiallayercolorfield-colorvaluesfields): {{
    - MeasureField}}
```

## Properties
<a name="aws-properties-quicksight-template-geospatiallayercolorfield-properties"></a>

`ColorDimensionsFields`  <a name="cfn-quicksight-template-geospatiallayercolorfield-colordimensionsfields"></a>
A list of color dimension fields.
*Required*: No
*Type*: Array of [DimensionField](aws-properties-quicksight-template-dimensionfield.md)
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ColorValuesFields`  <a name="cfn-quicksight-template-geospatiallayercolorfield-colorvaluesfields"></a>
A list of color measure fields.
*Required*: No
*Type*: Array of [MeasureField](aws-properties-quicksight-template-measurefield.md)
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
