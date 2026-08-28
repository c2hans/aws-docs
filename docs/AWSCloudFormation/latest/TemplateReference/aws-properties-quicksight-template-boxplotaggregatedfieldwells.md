---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-boxplotaggregatedfieldwells.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template BoxPlotAggregatedFieldWells
<a name="aws-properties-quicksight-template-boxplotaggregatedfieldwells"></a>

The aggregated field well for a box plot.

## Syntax
<a name="aws-properties-quicksight-template-boxplotaggregatedfieldwells-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-boxplotaggregatedfieldwells-syntax.json"></a>

```
{
  "[GroupBy](#cfn-quicksight-template-boxplotaggregatedfieldwells-groupby)" : {{[ DimensionField, ... ]}},
  "[Values](#cfn-quicksight-template-boxplotaggregatedfieldwells-values)" : {{[ MeasureField, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-template-boxplotaggregatedfieldwells-syntax.yaml"></a>

```
  [GroupBy](#cfn-quicksight-template-boxplotaggregatedfieldwells-groupby): {{
    - DimensionField}}
  [Values](#cfn-quicksight-template-boxplotaggregatedfieldwells-values): {{
    - MeasureField}}
```

## Properties
<a name="aws-properties-quicksight-template-boxplotaggregatedfieldwells-properties"></a>

`GroupBy`  <a name="cfn-quicksight-template-boxplotaggregatedfieldwells-groupby"></a>
The group by field well of a box plot chart. Values are grouped based on group by fields.
*Required*: No
*Type*: Array of [DimensionField](aws-properties-quicksight-template-dimensionfield.md)
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-quicksight-template-boxplotaggregatedfieldwells-values"></a>
The value field well of a box plot chart. Values are aggregated based on group by fields.
*Required*: No
*Type*: Array of [MeasureField](aws-properties-quicksight-template-measurefield.md)
*Minimum*: `0`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
