---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-pivotoperation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet PivotOperation
<a name="aws-properties-quicksight-dataset-pivotoperation"></a>

A transform operation that pivots data by converting row values into columns.

## Syntax
<a name="aws-properties-quicksight-dataset-pivotoperation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-pivotoperation-syntax.json"></a>

```
{
  "[Alias](#cfn-quicksight-dataset-pivotoperation-alias)" : {{String}},
  "[GroupByColumnNames](#cfn-quicksight-dataset-pivotoperation-groupbycolumnnames)" : {{[ String, ... ]}},
  "[PivotConfiguration](#cfn-quicksight-dataset-pivotoperation-pivotconfiguration)" : {{PivotConfiguration}},
  "[Source](#cfn-quicksight-dataset-pivotoperation-source)" : {{TransformOperationSource}},
  "[ValueColumnConfiguration](#cfn-quicksight-dataset-pivotoperation-valuecolumnconfiguration)" : {{ValueColumnConfiguration}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-pivotoperation-syntax.yaml"></a>

```
  [Alias](#cfn-quicksight-dataset-pivotoperation-alias): {{String}}
  [GroupByColumnNames](#cfn-quicksight-dataset-pivotoperation-groupbycolumnnames): {{
    - String}}
  [PivotConfiguration](#cfn-quicksight-dataset-pivotoperation-pivotconfiguration): {{
    PivotConfiguration}}
  [Source](#cfn-quicksight-dataset-pivotoperation-source): {{
    TransformOperationSource}}
  [ValueColumnConfiguration](#cfn-quicksight-dataset-pivotoperation-valuecolumnconfiguration): {{
    ValueColumnConfiguration}}
```

## Properties
<a name="aws-properties-quicksight-dataset-pivotoperation-properties"></a>

`Alias`  <a name="cfn-quicksight-dataset-pivotoperation-alias"></a>
Alias for this operation.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GroupByColumnNames`  <a name="cfn-quicksight-dataset-pivotoperation-groupbycolumnnames"></a>
The list of column names to group by when performing the pivot operation.
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 0`
*Maximum*: `127 | 128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PivotConfiguration`  <a name="cfn-quicksight-dataset-pivotoperation-pivotconfiguration"></a>
Configuration that specifies which labels to pivot and how to structure the resulting columns.
*Required*: Yes
*Type*: [PivotConfiguration](aws-properties-quicksight-dataset-pivotconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Source`  <a name="cfn-quicksight-dataset-pivotoperation-source"></a>
The source transform operation that provides input data for pivoting.
*Required*: Yes
*Type*: [TransformOperationSource](aws-properties-quicksight-dataset-transformoperationsource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ValueColumnConfiguration`  <a name="cfn-quicksight-dataset-pivotoperation-valuecolumnconfiguration"></a>
Configuration for how to aggregate values when multiple rows map to the same pivoted column.
*Required*: Yes
*Type*: [ValueColumnConfiguration](aws-properties-quicksight-dataset-valuecolumnconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
