---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-waterfallchartaggregatedfieldwells.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard WaterfallChartAggregatedFieldWells
<a name="aws-properties-quicksight-dashboard-waterfallchartaggregatedfieldwells"></a>

The field well configuration of a waterfall visual.

## Syntax
<a name="aws-properties-quicksight-dashboard-waterfallchartaggregatedfieldwells-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-waterfallchartaggregatedfieldwells-syntax.json"></a>

```
{
  "[Breakdowns](#cfn-quicksight-dashboard-waterfallchartaggregatedfieldwells-breakdowns)" : {{[ DimensionField, ... ]}},
  "[Categories](#cfn-quicksight-dashboard-waterfallchartaggregatedfieldwells-categories)" : {{[ DimensionField, ... ]}},
  "[Values](#cfn-quicksight-dashboard-waterfallchartaggregatedfieldwells-values)" : {{[ MeasureField, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-waterfallchartaggregatedfieldwells-syntax.yaml"></a>

```
  [Breakdowns](#cfn-quicksight-dashboard-waterfallchartaggregatedfieldwells-breakdowns): {{
    - DimensionField}}
  [Categories](#cfn-quicksight-dashboard-waterfallchartaggregatedfieldwells-categories): {{
    - DimensionField}}
  [Values](#cfn-quicksight-dashboard-waterfallchartaggregatedfieldwells-values): {{
    - MeasureField}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-waterfallchartaggregatedfieldwells-properties"></a>

`Breakdowns`  <a name="cfn-quicksight-dashboard-waterfallchartaggregatedfieldwells-breakdowns"></a>
The breakdown field wells of a waterfall visual.
*Required*: No
*Type*: Array of [DimensionField](aws-properties-quicksight-dashboard-dimensionfield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Categories`  <a name="cfn-quicksight-dashboard-waterfallchartaggregatedfieldwells-categories"></a>
The category field wells of a waterfall visual.
*Required*: No
*Type*: Array of [DimensionField](aws-properties-quicksight-dashboard-dimensionfield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-quicksight-dashboard-waterfallchartaggregatedfieldwells-values"></a>
The value field wells of a waterfall visual.
*Required*: No
*Type*: Array of [MeasureField](aws-properties-quicksight-dashboard-measurefield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
