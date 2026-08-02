---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-sankeydiagramaggregatedfieldwells.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard SankeyDiagramAggregatedFieldWells
<a name="aws-properties-quicksight-dashboard-sankeydiagramaggregatedfieldwells"></a>

The field well configuration of a sankey diagram.

## Syntax
<a name="aws-properties-quicksight-dashboard-sankeydiagramaggregatedfieldwells-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-sankeydiagramaggregatedfieldwells-syntax.json"></a>

```
{
  "[Destination](#cfn-quicksight-dashboard-sankeydiagramaggregatedfieldwells-destination)" : {{[ DimensionField, ... ]}},
  "[Source](#cfn-quicksight-dashboard-sankeydiagramaggregatedfieldwells-source)" : {{[ DimensionField, ... ]}},
  "[Weight](#cfn-quicksight-dashboard-sankeydiagramaggregatedfieldwells-weight)" : {{[ MeasureField, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-sankeydiagramaggregatedfieldwells-syntax.yaml"></a>

```
  [Destination](#cfn-quicksight-dashboard-sankeydiagramaggregatedfieldwells-destination): {{
    - DimensionField}}
  [Source](#cfn-quicksight-dashboard-sankeydiagramaggregatedfieldwells-source): {{
    - DimensionField}}
  [Weight](#cfn-quicksight-dashboard-sankeydiagramaggregatedfieldwells-weight): {{
    - MeasureField}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-sankeydiagramaggregatedfieldwells-properties"></a>

`Destination`  <a name="cfn-quicksight-dashboard-sankeydiagramaggregatedfieldwells-destination"></a>
The destination field wells of a sankey diagram.
*Required*: No
*Type*: Array of [DimensionField](aws-properties-quicksight-dashboard-dimensionfield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Source`  <a name="cfn-quicksight-dashboard-sankeydiagramaggregatedfieldwells-source"></a>
The source field wells of a sankey diagram.
*Required*: No
*Type*: Array of [DimensionField](aws-properties-quicksight-dashboard-dimensionfield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Weight`  <a name="cfn-quicksight-dashboard-sankeydiagramaggregatedfieldwells-weight"></a>
The weight field wells of a sankey diagram.
*Required*: No
*Type*: Array of [MeasureField](aws-properties-quicksight-dashboard-measurefield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
