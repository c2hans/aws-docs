---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-pluginvisualfieldwell.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis PluginVisualFieldWell
<a name="aws-properties-quicksight-analysis-pluginvisualfieldwell"></a>

A collection of field wells for a plugin visual.

## Syntax
<a name="aws-properties-quicksight-analysis-pluginvisualfieldwell-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-pluginvisualfieldwell-syntax.json"></a>

```
{
  "[AxisName](#cfn-quicksight-analysis-pluginvisualfieldwell-axisname)" : {{String}},
  "[Dimensions](#cfn-quicksight-analysis-pluginvisualfieldwell-dimensions)" : {{[ DimensionField, ... ]}},
  "[Measures](#cfn-quicksight-analysis-pluginvisualfieldwell-measures)" : {{[ MeasureField, ... ]}},
  "[Unaggregated](#cfn-quicksight-analysis-pluginvisualfieldwell-unaggregated)" : {{[ UnaggregatedField, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-pluginvisualfieldwell-syntax.yaml"></a>

```
  [AxisName](#cfn-quicksight-analysis-pluginvisualfieldwell-axisname): {{String}}
  [Dimensions](#cfn-quicksight-analysis-pluginvisualfieldwell-dimensions): {{
    - DimensionField}}
  [Measures](#cfn-quicksight-analysis-pluginvisualfieldwell-measures): {{
    - MeasureField}}
  [Unaggregated](#cfn-quicksight-analysis-pluginvisualfieldwell-unaggregated): {{
    - UnaggregatedField}}
```

## Properties
<a name="aws-properties-quicksight-analysis-pluginvisualfieldwell-properties"></a>

`AxisName`  <a name="cfn-quicksight-analysis-pluginvisualfieldwell-axisname"></a>
The semantic axis name for the field well.
*Required*: No
*Type*: String
*Allowed values*: `GROUP_BY | VALUE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Dimensions`  <a name="cfn-quicksight-analysis-pluginvisualfieldwell-dimensions"></a>
A list of dimensions for the field well.
*Required*: No
*Type*: Array of [DimensionField](aws-properties-quicksight-analysis-dimensionfield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Measures`  <a name="cfn-quicksight-analysis-pluginvisualfieldwell-measures"></a>
A list of measures that exist in the field well.
*Required*: No
*Type*: Array of [MeasureField](aws-properties-quicksight-analysis-measurefield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Unaggregated`  <a name="cfn-quicksight-analysis-pluginvisualfieldwell-unaggregated"></a>
A list of unaggregated fields that exist in the field well.
*Required*: No
*Type*: Array of [UnaggregatedField](aws-properties-quicksight-analysis-unaggregatedfield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
