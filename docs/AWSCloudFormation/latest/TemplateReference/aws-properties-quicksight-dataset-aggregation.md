---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-aggregation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet Aggregation
<a name="aws-properties-quicksight-dataset-aggregation"></a>

Defines an aggregation function to be applied to grouped data, creating a new column with the calculated result.

## Syntax
<a name="aws-properties-quicksight-dataset-aggregation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-aggregation-syntax.json"></a>

```
{
  "[AggregationFunction](#cfn-quicksight-dataset-aggregation-aggregationfunction)" : {{DataPrepAggregationFunction}},
  "[NewColumnId](#cfn-quicksight-dataset-aggregation-newcolumnid)" : {{String}},
  "[NewColumnName](#cfn-quicksight-dataset-aggregation-newcolumnname)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-aggregation-syntax.yaml"></a>

```
  [AggregationFunction](#cfn-quicksight-dataset-aggregation-aggregationfunction): {{
    DataPrepAggregationFunction}}
  [NewColumnId](#cfn-quicksight-dataset-aggregation-newcolumnid): {{String}}
  [NewColumnName](#cfn-quicksight-dataset-aggregation-newcolumnname): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dataset-aggregation-properties"></a>

`AggregationFunction`  <a name="cfn-quicksight-dataset-aggregation-aggregationfunction"></a>
The aggregation function to apply, such as `SUM`, `COUNT`, `AVERAGE`, `MIN`, `MAX`
*Required*: Yes
*Type*: [DataPrepAggregationFunction](aws-properties-quicksight-dataset-dataprepaggregationfunction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NewColumnId`  <a name="cfn-quicksight-dataset-aggregation-newcolumnid"></a>
A unique identifier for the new column that will contain the aggregated values.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NewColumnName`  <a name="cfn-quicksight-dataset-aggregation-newcolumnname"></a>
The name for the new column that will contain the aggregated values.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
