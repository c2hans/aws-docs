---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-sankeydiagramaggregatedfieldwells.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template SankeyDiagramAggregatedFieldWells
<a name="aws-properties-quicksight-template-sankeydiagramaggregatedfieldwells"></a>

The field well configuration of a sankey diagram.

## Syntax
<a name="aws-properties-quicksight-template-sankeydiagramaggregatedfieldwells-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-sankeydiagramaggregatedfieldwells-syntax.json"></a>

```
{
  "[Destination](#cfn-quicksight-template-sankeydiagramaggregatedfieldwells-destination)" : {{[ DimensionField, ... ]}},
  "[Source](#cfn-quicksight-template-sankeydiagramaggregatedfieldwells-source)" : {{[ DimensionField, ... ]}},
  "[Weight](#cfn-quicksight-template-sankeydiagramaggregatedfieldwells-weight)" : {{[ MeasureField, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-template-sankeydiagramaggregatedfieldwells-syntax.yaml"></a>

```
  [Destination](#cfn-quicksight-template-sankeydiagramaggregatedfieldwells-destination): {{
    - DimensionField}}
  [Source](#cfn-quicksight-template-sankeydiagramaggregatedfieldwells-source): {{
    - DimensionField}}
  [Weight](#cfn-quicksight-template-sankeydiagramaggregatedfieldwells-weight): {{
    - MeasureField}}
```

## Properties
<a name="aws-properties-quicksight-template-sankeydiagramaggregatedfieldwells-properties"></a>

`Destination`  <a name="cfn-quicksight-template-sankeydiagramaggregatedfieldwells-destination"></a>
The destination field wells of a sankey diagram.
*Required*: No
*Type*: Array of [DimensionField](aws-properties-quicksight-template-dimensionfield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Source`  <a name="cfn-quicksight-template-sankeydiagramaggregatedfieldwells-source"></a>
The source field wells of a sankey diagram.
*Required*: No
*Type*: Array of [DimensionField](aws-properties-quicksight-template-dimensionfield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Weight`  <a name="cfn-quicksight-template-sankeydiagramaggregatedfieldwells-weight"></a>
The weight field wells of a sankey diagram.
*Required*: No
*Type*: Array of [MeasureField](aws-properties-quicksight-template-measurefield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
