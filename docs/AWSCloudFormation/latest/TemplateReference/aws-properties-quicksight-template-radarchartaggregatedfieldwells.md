---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-radarchartaggregatedfieldwells.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template RadarChartAggregatedFieldWells
<a name="aws-properties-quicksight-template-radarchartaggregatedfieldwells"></a>

The aggregated field well configuration of a `RadarChartVisual`.

## Syntax
<a name="aws-properties-quicksight-template-radarchartaggregatedfieldwells-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-radarchartaggregatedfieldwells-syntax.json"></a>

```
{
  "[Category](#cfn-quicksight-template-radarchartaggregatedfieldwells-category)" : {{[ DimensionField, ... ]}},
  "[Color](#cfn-quicksight-template-radarchartaggregatedfieldwells-color)" : {{[ DimensionField, ... ]}},
  "[Values](#cfn-quicksight-template-radarchartaggregatedfieldwells-values)" : {{[ MeasureField, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-template-radarchartaggregatedfieldwells-syntax.yaml"></a>

```
  [Category](#cfn-quicksight-template-radarchartaggregatedfieldwells-category): {{
    - DimensionField}}
  [Color](#cfn-quicksight-template-radarchartaggregatedfieldwells-color): {{
    - DimensionField}}
  [Values](#cfn-quicksight-template-radarchartaggregatedfieldwells-values): {{
    - MeasureField}}
```

## Properties
<a name="aws-properties-quicksight-template-radarchartaggregatedfieldwells-properties"></a>

`Category`  <a name="cfn-quicksight-template-radarchartaggregatedfieldwells-category"></a>
The aggregated field well categories of a radar chart.
*Required*: No
*Type*: Array of [DimensionField](aws-properties-quicksight-template-dimensionfield.md)
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Color`  <a name="cfn-quicksight-template-radarchartaggregatedfieldwells-color"></a>
The color that are assigned to the aggregated field wells of a radar chart.
*Required*: No
*Type*: Array of [DimensionField](aws-properties-quicksight-template-dimensionfield.md)
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-quicksight-template-radarchartaggregatedfieldwells-values"></a>
The values that are assigned to the aggregated field wells of a radar chart.
*Required*: No
*Type*: Array of [MeasureField](aws-properties-quicksight-template-measurefield.md)
*Minimum*: `0`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
