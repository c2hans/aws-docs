---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-columnsort.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis ColumnSort
<a name="aws-properties-quicksight-analysis-columnsort"></a>

The sort configuration for a column that is not used in a field well.

## Syntax
<a name="aws-properties-quicksight-analysis-columnsort-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-columnsort-syntax.json"></a>

```
{
  "[AggregationFunction](#cfn-quicksight-analysis-columnsort-aggregationfunction)" : {{AggregationFunction}},
  "[Direction](#cfn-quicksight-analysis-columnsort-direction)" : {{String}},
  "[SortBy](#cfn-quicksight-analysis-columnsort-sortby)" : {{ColumnIdentifier}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-columnsort-syntax.yaml"></a>

```
  [AggregationFunction](#cfn-quicksight-analysis-columnsort-aggregationfunction): {{
    AggregationFunction}}
  [Direction](#cfn-quicksight-analysis-columnsort-direction): {{String}}
  [SortBy](#cfn-quicksight-analysis-columnsort-sortby): {{
    ColumnIdentifier}}
```

## Properties
<a name="aws-properties-quicksight-analysis-columnsort-properties"></a>

`AggregationFunction`  <a name="cfn-quicksight-analysis-columnsort-aggregationfunction"></a>
The aggregation function that is defined in the column sort.
*Required*: No
*Type*: [AggregationFunction](aws-properties-quicksight-analysis-aggregationfunction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Direction`  <a name="cfn-quicksight-analysis-columnsort-direction"></a>
The sort direction.
*Required*: Yes
*Type*: String
*Allowed values*: `ASC | DESC`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SortBy`  <a name="cfn-quicksight-analysis-columnsort-sortby"></a>
Property description not available.
*Required*: Yes
*Type*: [ColumnIdentifier](aws-properties-quicksight-analysis-columnidentifier.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
