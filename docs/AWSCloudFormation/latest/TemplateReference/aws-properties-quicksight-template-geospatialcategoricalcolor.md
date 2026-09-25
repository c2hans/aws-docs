---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-geospatialcategoricalcolor.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template GeospatialCategoricalColor
<a name="aws-properties-quicksight-template-geospatialcategoricalcolor"></a>

The definition for a categorical color.

## Syntax
<a name="aws-properties-quicksight-template-geospatialcategoricalcolor-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-geospatialcategoricalcolor-syntax.json"></a>

```
{
  "[CategoryDataColors](#cfn-quicksight-template-geospatialcategoricalcolor-categorydatacolors)" : {{[ GeospatialCategoricalDataColor, ... ]}},
  "[DefaultOpacity](#cfn-quicksight-template-geospatialcategoricalcolor-defaultopacity)" : {{Number}},
  "[NullDataSettings](#cfn-quicksight-template-geospatialcategoricalcolor-nulldatasettings)" : {{GeospatialNullDataSettings}},
  "[NullDataVisibility](#cfn-quicksight-template-geospatialcategoricalcolor-nulldatavisibility)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-geospatialcategoricalcolor-syntax.yaml"></a>

```
  [CategoryDataColors](#cfn-quicksight-template-geospatialcategoricalcolor-categorydatacolors): {{
    - GeospatialCategoricalDataColor}}
  [DefaultOpacity](#cfn-quicksight-template-geospatialcategoricalcolor-defaultopacity): {{Number}}
  [NullDataSettings](#cfn-quicksight-template-geospatialcategoricalcolor-nulldatasettings): {{
    GeospatialNullDataSettings}}
  [NullDataVisibility](#cfn-quicksight-template-geospatialcategoricalcolor-nulldatavisibility): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-geospatialcategoricalcolor-properties"></a>

`CategoryDataColors`  <a name="cfn-quicksight-template-geospatialcategoricalcolor-categorydatacolors"></a>
A list of categorical data colors for each category.
*Required*: Yes
*Type*: Array of [GeospatialCategoricalDataColor](aws-properties-quicksight-template-geospatialcategoricaldatacolor.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultOpacity`  <a name="cfn-quicksight-template-geospatialcategoricalcolor-defaultopacity"></a>
The default opacity of a categorical color.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NullDataSettings`  <a name="cfn-quicksight-template-geospatialcategoricalcolor-nulldatasettings"></a>
The null data visualization settings.
*Required*: No
*Type*: [GeospatialNullDataSettings](aws-properties-quicksight-template-geospatialnulldatasettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NullDataVisibility`  <a name="cfn-quicksight-template-geospatialcategoricalcolor-nulldatavisibility"></a>
The state of visibility for null data.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
