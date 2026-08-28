---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-tableaggregatedfieldwells.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template TableAggregatedFieldWells
<a name="aws-properties-quicksight-template-tableaggregatedfieldwells"></a>

The aggregated field well for the table.

## Syntax
<a name="aws-properties-quicksight-template-tableaggregatedfieldwells-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-tableaggregatedfieldwells-syntax.json"></a>

```
{
  "[GroupBy](#cfn-quicksight-template-tableaggregatedfieldwells-groupby)" : {{[ DimensionField, ... ]}},
  "[Values](#cfn-quicksight-template-tableaggregatedfieldwells-values)" : {{[ MeasureField, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-template-tableaggregatedfieldwells-syntax.yaml"></a>

```
  [GroupBy](#cfn-quicksight-template-tableaggregatedfieldwells-groupby): {{
    - DimensionField}}
  [Values](#cfn-quicksight-template-tableaggregatedfieldwells-values): {{
    - MeasureField}}
```

## Properties
<a name="aws-properties-quicksight-template-tableaggregatedfieldwells-properties"></a>

`GroupBy`  <a name="cfn-quicksight-template-tableaggregatedfieldwells-groupby"></a>
The group by field well for a pivot table. Values are grouped by group by fields.
*Required*: No
*Type*: Array of [DimensionField](aws-properties-quicksight-template-dimensionfield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-quicksight-template-tableaggregatedfieldwells-values"></a>
The values field well for a pivot table. Values are aggregated based on group by fields.
*Required*: No
*Type*: Array of [MeasureField](aws-properties-quicksight-template-measurefield.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
