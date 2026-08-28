---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-geospatialcategoricalcolor.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard GeospatialCategoricalColor
<a name="aws-properties-quicksight-dashboard-geospatialcategoricalcolor"></a>

The definition for a categorical color.

## Syntax
<a name="aws-properties-quicksight-dashboard-geospatialcategoricalcolor-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-geospatialcategoricalcolor-syntax.json"></a>

```
{
  "[CategoryDataColors](#cfn-quicksight-dashboard-geospatialcategoricalcolor-categorydatacolors)" : {{[ GeospatialCategoricalDataColor, ... ]}},
  "[DefaultOpacity](#cfn-quicksight-dashboard-geospatialcategoricalcolor-defaultopacity)" : {{Number}},
  "[NullDataSettings](#cfn-quicksight-dashboard-geospatialcategoricalcolor-nulldatasettings)" : {{GeospatialNullDataSettings}},
  "[NullDataVisibility](#cfn-quicksight-dashboard-geospatialcategoricalcolor-nulldatavisibility)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-geospatialcategoricalcolor-syntax.yaml"></a>

```
  [CategoryDataColors](#cfn-quicksight-dashboard-geospatialcategoricalcolor-categorydatacolors): {{
    - GeospatialCategoricalDataColor}}
  [DefaultOpacity](#cfn-quicksight-dashboard-geospatialcategoricalcolor-defaultopacity): {{Number}}
  [NullDataSettings](#cfn-quicksight-dashboard-geospatialcategoricalcolor-nulldatasettings): {{
    GeospatialNullDataSettings}}
  [NullDataVisibility](#cfn-quicksight-dashboard-geospatialcategoricalcolor-nulldatavisibility): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-geospatialcategoricalcolor-properties"></a>

`CategoryDataColors`  <a name="cfn-quicksight-dashboard-geospatialcategoricalcolor-categorydatacolors"></a>
A list of categorical data colors for each category.
*Required*: Yes
*Type*: Array of [GeospatialCategoricalDataColor](aws-properties-quicksight-dashboard-geospatialcategoricaldatacolor.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultOpacity`  <a name="cfn-quicksight-dashboard-geospatialcategoricalcolor-defaultopacity"></a>
The default opacity of a categorical color.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NullDataSettings`  <a name="cfn-quicksight-dashboard-geospatialcategoricalcolor-nulldatasettings"></a>
The null data visualization settings.
*Required*: No
*Type*: [GeospatialNullDataSettings](aws-properties-quicksight-dashboard-geospatialnulldatasettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NullDataVisibility`  <a name="cfn-quicksight-dashboard-geospatialcategoricalcolor-nulldatavisibility"></a>
The state of visibility for null data.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | VISIBLE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
