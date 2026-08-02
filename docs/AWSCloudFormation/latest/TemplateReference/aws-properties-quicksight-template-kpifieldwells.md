---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-kpifieldwells.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template KPIFieldWells
<a name="aws-properties-quicksight-template-kpifieldwells"></a>

The field well configuration of a KPI visual.

## Syntax
<a name="aws-properties-quicksight-template-kpifieldwells-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-kpifieldwells-syntax.json"></a>

```
{
  "[TargetValues](#cfn-quicksight-template-kpifieldwells-targetvalues)" : {{[ MeasureField, ... ]}},
  "[TrendGroups](#cfn-quicksight-template-kpifieldwells-trendgroups)" : {{[ DimensionField, ... ]}},
  "[Values](#cfn-quicksight-template-kpifieldwells-values)" : {{[ MeasureField, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-template-kpifieldwells-syntax.yaml"></a>

```
  [TargetValues](#cfn-quicksight-template-kpifieldwells-targetvalues): {{
    - MeasureField}}
  [TrendGroups](#cfn-quicksight-template-kpifieldwells-trendgroups): {{
    - DimensionField}}
  [Values](#cfn-quicksight-template-kpifieldwells-values): {{
    - MeasureField}}
```

## Properties
<a name="aws-properties-quicksight-template-kpifieldwells-properties"></a>

`TargetValues`  <a name="cfn-quicksight-template-kpifieldwells-targetvalues"></a>
The target value field wells of a KPI visual.
*Required*: No
*Type*: Array of [MeasureField](aws-properties-quicksight-template-measurefield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TrendGroups`  <a name="cfn-quicksight-template-kpifieldwells-trendgroups"></a>
The trend group field wells of a KPI visual.
*Required*: No
*Type*: Array of [DimensionField](aws-properties-quicksight-template-dimensionfield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-quicksight-template-kpifieldwells-values"></a>
The value field wells of a KPI visual.
*Required*: No
*Type*: Array of [MeasureField](aws-properties-quicksight-template-measurefield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
