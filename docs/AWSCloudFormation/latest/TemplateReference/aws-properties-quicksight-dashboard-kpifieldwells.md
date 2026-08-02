---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-kpifieldwells.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard KPIFieldWells
<a name="aws-properties-quicksight-dashboard-kpifieldwells"></a>

The field well configuration of a KPI visual.

## Syntax
<a name="aws-properties-quicksight-dashboard-kpifieldwells-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-kpifieldwells-syntax.json"></a>

```
{
  "[TargetValues](#cfn-quicksight-dashboard-kpifieldwells-targetvalues)" : {{[ MeasureField, ... ]}},
  "[TrendGroups](#cfn-quicksight-dashboard-kpifieldwells-trendgroups)" : {{[ DimensionField, ... ]}},
  "[Values](#cfn-quicksight-dashboard-kpifieldwells-values)" : {{[ MeasureField, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-kpifieldwells-syntax.yaml"></a>

```
  [TargetValues](#cfn-quicksight-dashboard-kpifieldwells-targetvalues): {{
    - MeasureField}}
  [TrendGroups](#cfn-quicksight-dashboard-kpifieldwells-trendgroups): {{
    - DimensionField}}
  [Values](#cfn-quicksight-dashboard-kpifieldwells-values): {{
    - MeasureField}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-kpifieldwells-properties"></a>

`TargetValues`  <a name="cfn-quicksight-dashboard-kpifieldwells-targetvalues"></a>
The target value field wells of a KPI visual.
*Required*: No
*Type*: Array of [MeasureField](aws-properties-quicksight-dashboard-measurefield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TrendGroups`  <a name="cfn-quicksight-dashboard-kpifieldwells-trendgroups"></a>
The trend group field wells of a KPI visual.
*Required*: No
*Type*: Array of [DimensionField](aws-properties-quicksight-dashboard-dimensionfield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-quicksight-dashboard-kpifieldwells-values"></a>
The value field wells of a KPI visual.
*Required*: No
*Type*: Array of [MeasureField](aws-properties-quicksight-dashboard-measurefield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
