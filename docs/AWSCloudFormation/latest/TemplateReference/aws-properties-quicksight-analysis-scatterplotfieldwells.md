---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-scatterplotfieldwells.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis ScatterPlotFieldWells
<a name="aws-properties-quicksight-analysis-scatterplotfieldwells"></a>

The field well configuration of a scatter plot.

This is a union type structure. For this structure to be valid, only one of the attributes can be defined.

## Syntax
<a name="aws-properties-quicksight-analysis-scatterplotfieldwells-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-scatterplotfieldwells-syntax.json"></a>

```
{
  "[ScatterPlotCategoricallyAggregatedFieldWells](#cfn-quicksight-analysis-scatterplotfieldwells-scatterplotcategoricallyaggregatedfieldwells)" : {{ScatterPlotCategoricallyAggregatedFieldWells}},
  "[ScatterPlotUnaggregatedFieldWells](#cfn-quicksight-analysis-scatterplotfieldwells-scatterplotunaggregatedfieldwells)" : {{ScatterPlotUnaggregatedFieldWells}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-scatterplotfieldwells-syntax.yaml"></a>

```
  [ScatterPlotCategoricallyAggregatedFieldWells](#cfn-quicksight-analysis-scatterplotfieldwells-scatterplotcategoricallyaggregatedfieldwells): {{
    ScatterPlotCategoricallyAggregatedFieldWells}}
  [ScatterPlotUnaggregatedFieldWells](#cfn-quicksight-analysis-scatterplotfieldwells-scatterplotunaggregatedfieldwells): {{
    ScatterPlotUnaggregatedFieldWells}}
```

## Properties
<a name="aws-properties-quicksight-analysis-scatterplotfieldwells-properties"></a>

`ScatterPlotCategoricallyAggregatedFieldWells`  <a name="cfn-quicksight-analysis-scatterplotfieldwells-scatterplotcategoricallyaggregatedfieldwells"></a>
The aggregated field wells of a scatter plot. The x and y-axes of scatter plots with aggregated field wells are aggregated by category, label, or both.
*Required*: No
*Type*: [ScatterPlotCategoricallyAggregatedFieldWells](aws-properties-quicksight-analysis-scatterplotcategoricallyaggregatedfieldwells.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScatterPlotUnaggregatedFieldWells`  <a name="cfn-quicksight-analysis-scatterplotfieldwells-scatterplotunaggregatedfieldwells"></a>
The unaggregated field wells of a scatter plot. The x and y-axes of these scatter plots are unaggregated.
*Required*: No
*Type*: [ScatterPlotUnaggregatedFieldWells](aws-properties-quicksight-analysis-scatterplotunaggregatedfieldwells.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
