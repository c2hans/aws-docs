---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-appendoperation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet AppendOperation
<a name="aws-properties-quicksight-dataset-appendoperation"></a>

A transform operation that combines rows from two data sources by stacking them vertically (union operation).

## Syntax
<a name="aws-properties-quicksight-dataset-appendoperation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-appendoperation-syntax.json"></a>

```
{
  "[Alias](#cfn-quicksight-dataset-appendoperation-alias)" : {{String}},
  "[AppendedColumns](#cfn-quicksight-dataset-appendoperation-appendedcolumns)" : {{[ AppendedColumn, ... ]}},
  "[FirstSource](#cfn-quicksight-dataset-appendoperation-firstsource)" : {{TransformOperationSource}},
  "[SecondSource](#cfn-quicksight-dataset-appendoperation-secondsource)" : {{TransformOperationSource}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-appendoperation-syntax.yaml"></a>

```
  [Alias](#cfn-quicksight-dataset-appendoperation-alias): {{String}}
  [AppendedColumns](#cfn-quicksight-dataset-appendoperation-appendedcolumns): {{
    - AppendedColumn}}
  [FirstSource](#cfn-quicksight-dataset-appendoperation-firstsource): {{
    TransformOperationSource}}
  [SecondSource](#cfn-quicksight-dataset-appendoperation-secondsource): {{
    TransformOperationSource}}
```

## Properties
<a name="aws-properties-quicksight-dataset-appendoperation-properties"></a>

`Alias`  <a name="cfn-quicksight-dataset-appendoperation-alias"></a>
Alias for this operation.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AppendedColumns`  <a name="cfn-quicksight-dataset-appendoperation-appendedcolumns"></a>
The list of columns to include in the appended result, mapping columns from both sources.
*Required*: Yes
*Type*: Array of [AppendedColumn](aws-properties-quicksight-dataset-appendedcolumn.md)
*Minimum*: `0`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FirstSource`  <a name="cfn-quicksight-dataset-appendoperation-firstsource"></a>
The first data source to be included in the append operation.
*Required*: No
*Type*: [TransformOperationSource](aws-properties-quicksight-dataset-transformoperationsource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecondSource`  <a name="cfn-quicksight-dataset-appendoperation-secondsource"></a>
The second data source to be appended to the first source.
*Required*: No
*Type*: [TransformOperationSource](aws-properties-quicksight-dataset-transformoperationsource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
