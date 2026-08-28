---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-geospatiallayercolorfield.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard GeospatialLayerColorField
<a name="aws-properties-quicksight-dashboard-geospatiallayercolorfield"></a>

The color field that defines a gradient or categorical style.

## Syntax
<a name="aws-properties-quicksight-dashboard-geospatiallayercolorfield-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-geospatiallayercolorfield-syntax.json"></a>

```
{
  "[ColorDimensionsFields](#cfn-quicksight-dashboard-geospatiallayercolorfield-colordimensionsfields)" : {{[ DimensionField, ... ]}},
  "[ColorValuesFields](#cfn-quicksight-dashboard-geospatiallayercolorfield-colorvaluesfields)" : {{[ MeasureField, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-geospatiallayercolorfield-syntax.yaml"></a>

```
  [ColorDimensionsFields](#cfn-quicksight-dashboard-geospatiallayercolorfield-colordimensionsfields): {{
    - DimensionField}}
  [ColorValuesFields](#cfn-quicksight-dashboard-geospatiallayercolorfield-colorvaluesfields): {{
    - MeasureField}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-geospatiallayercolorfield-properties"></a>

`ColorDimensionsFields`  <a name="cfn-quicksight-dashboard-geospatiallayercolorfield-colordimensionsfields"></a>
A list of color dimension fields.
*Required*: No
*Type*: Array of [DimensionField](aws-properties-quicksight-dashboard-dimensionfield.md)
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ColorValuesFields`  <a name="cfn-quicksight-dashboard-geospatiallayercolorfield-colorvaluesfields"></a>
A list of color measure fields.
*Required*: No
*Type*: Array of [MeasureField](aws-properties-quicksight-dashboard-measurefield.md)
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
