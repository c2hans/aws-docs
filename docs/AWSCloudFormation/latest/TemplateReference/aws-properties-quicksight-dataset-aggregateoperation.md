---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-aggregateoperation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet AggregateOperation
<a name="aws-properties-quicksight-dataset-aggregateoperation"></a>

A transform operation that groups rows by specified columns and applies aggregation functions to calculate summary values.

## Syntax
<a name="aws-properties-quicksight-dataset-aggregateoperation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-aggregateoperation-syntax.json"></a>

```
{
  "[Aggregations](#cfn-quicksight-dataset-aggregateoperation-aggregations)" : {{[ Aggregation, ... ]}},
  "[Alias](#cfn-quicksight-dataset-aggregateoperation-alias)" : {{String}},
  "[GroupByColumnNames](#cfn-quicksight-dataset-aggregateoperation-groupbycolumnnames)" : {{[ String, ... ]}},
  "[Source](#cfn-quicksight-dataset-aggregateoperation-source)" : {{TransformOperationSource}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-aggregateoperation-syntax.yaml"></a>

```
  [Aggregations](#cfn-quicksight-dataset-aggregateoperation-aggregations): {{
    - Aggregation}}
  [Alias](#cfn-quicksight-dataset-aggregateoperation-alias): {{String}}
  [GroupByColumnNames](#cfn-quicksight-dataset-aggregateoperation-groupbycolumnnames): {{
    - String}}
  [Source](#cfn-quicksight-dataset-aggregateoperation-source): {{
    TransformOperationSource}}
```

## Properties
<a name="aws-properties-quicksight-dataset-aggregateoperation-properties"></a>

`Aggregations`  <a name="cfn-quicksight-dataset-aggregateoperation-aggregations"></a>
The list of aggregation functions to apply to the grouped data, such as `SUM`, `COUNT`, or `AVERAGE`.
*Required*: Yes
*Type*: Array of [Aggregation](aws-properties-quicksight-dataset-aggregation.md)
*Minimum*: `0`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Alias`  <a name="cfn-quicksight-dataset-aggregateoperation-alias"></a>
Alias for this operation.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GroupByColumnNames`  <a name="cfn-quicksight-dataset-aggregateoperation-groupbycolumnnames"></a>
The list of column names to group by when performing the aggregation. Rows with the same values in these columns will be grouped together.
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 0`
*Maximum*: `127 | 128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Source`  <a name="cfn-quicksight-dataset-aggregateoperation-source"></a>
The source transform operation that provides input data for the aggregation.
*Required*: Yes
*Type*: [TransformOperationSource](aws-properties-quicksight-dataset-transformoperationsource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
