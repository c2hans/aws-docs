---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-sankeydiagramaggregatedfieldwells.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis SankeyDiagramAggregatedFieldWells
<a name="aws-properties-quicksight-analysis-sankeydiagramaggregatedfieldwells"></a>

The field well configuration of a sankey diagram.

## Syntax
<a name="aws-properties-quicksight-analysis-sankeydiagramaggregatedfieldwells-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-sankeydiagramaggregatedfieldwells-syntax.json"></a>

```
{
  "[Destination](#cfn-quicksight-analysis-sankeydiagramaggregatedfieldwells-destination)" : {{[ DimensionField, ... ]}},
  "[Source](#cfn-quicksight-analysis-sankeydiagramaggregatedfieldwells-source)" : {{[ DimensionField, ... ]}},
  "[Weight](#cfn-quicksight-analysis-sankeydiagramaggregatedfieldwells-weight)" : {{[ MeasureField, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-sankeydiagramaggregatedfieldwells-syntax.yaml"></a>

```
  [Destination](#cfn-quicksight-analysis-sankeydiagramaggregatedfieldwells-destination): {{
    - DimensionField}}
  [Source](#cfn-quicksight-analysis-sankeydiagramaggregatedfieldwells-source): {{
    - DimensionField}}
  [Weight](#cfn-quicksight-analysis-sankeydiagramaggregatedfieldwells-weight): {{
    - MeasureField}}
```

## Properties
<a name="aws-properties-quicksight-analysis-sankeydiagramaggregatedfieldwells-properties"></a>

`Destination`  <a name="cfn-quicksight-analysis-sankeydiagramaggregatedfieldwells-destination"></a>
The destination field wells of a sankey diagram.
*Required*: No
*Type*: Array of [DimensionField](aws-properties-quicksight-analysis-dimensionfield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Source`  <a name="cfn-quicksight-analysis-sankeydiagramaggregatedfieldwells-source"></a>
The source field wells of a sankey diagram.
*Required*: No
*Type*: Array of [DimensionField](aws-properties-quicksight-analysis-dimensionfield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Weight`  <a name="cfn-quicksight-analysis-sankeydiagramaggregatedfieldwells-weight"></a>
The weight field wells of a sankey diagram.
*Required*: No
*Type*: Array of [MeasureField](aws-properties-quicksight-analysis-measurefield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
