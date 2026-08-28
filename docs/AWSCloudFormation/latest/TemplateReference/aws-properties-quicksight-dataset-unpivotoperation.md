---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-unpivotoperation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet UnpivotOperation
<a name="aws-properties-quicksight-dataset-unpivotoperation"></a>

A transform operation that converts columns into rows, normalizing the data structure.

## Syntax
<a name="aws-properties-quicksight-dataset-unpivotoperation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-unpivotoperation-syntax.json"></a>

```
{
  "[Alias](#cfn-quicksight-dataset-unpivotoperation-alias)" : {{String}},
  "[ColumnsToUnpivot](#cfn-quicksight-dataset-unpivotoperation-columnstounpivot)" : {{[ ColumnToUnpivot, ... ]}},
  "[Source](#cfn-quicksight-dataset-unpivotoperation-source)" : {{TransformOperationSource}},
  "[UnpivotedLabelColumnId](#cfn-quicksight-dataset-unpivotoperation-unpivotedlabelcolumnid)" : {{String}},
  "[UnpivotedLabelColumnName](#cfn-quicksight-dataset-unpivotoperation-unpivotedlabelcolumnname)" : {{String}},
  "[UnpivotedValueColumnId](#cfn-quicksight-dataset-unpivotoperation-unpivotedvaluecolumnid)" : {{String}},
  "[UnpivotedValueColumnName](#cfn-quicksight-dataset-unpivotoperation-unpivotedvaluecolumnname)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-unpivotoperation-syntax.yaml"></a>

```
  [Alias](#cfn-quicksight-dataset-unpivotoperation-alias): {{String}}
  [ColumnsToUnpivot](#cfn-quicksight-dataset-unpivotoperation-columnstounpivot): {{
    - ColumnToUnpivot}}
  [Source](#cfn-quicksight-dataset-unpivotoperation-source): {{
    TransformOperationSource}}
  [UnpivotedLabelColumnId](#cfn-quicksight-dataset-unpivotoperation-unpivotedlabelcolumnid): {{String}}
  [UnpivotedLabelColumnName](#cfn-quicksight-dataset-unpivotoperation-unpivotedlabelcolumnname): {{String}}
  [UnpivotedValueColumnId](#cfn-quicksight-dataset-unpivotoperation-unpivotedvaluecolumnid): {{String}}
  [UnpivotedValueColumnName](#cfn-quicksight-dataset-unpivotoperation-unpivotedvaluecolumnname): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dataset-unpivotoperation-properties"></a>

`Alias`  <a name="cfn-quicksight-dataset-unpivotoperation-alias"></a>
Alias for this operation.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ColumnsToUnpivot`  <a name="cfn-quicksight-dataset-unpivotoperation-columnstounpivot"></a>
The list of columns to unpivot from the source data.
*Required*: Yes
*Type*: Array of [ColumnToUnpivot](aws-properties-quicksight-dataset-columntounpivot.md)
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Source`  <a name="cfn-quicksight-dataset-unpivotoperation-source"></a>
The source transform operation that provides input data for unpivoting.
*Required*: Yes
*Type*: [TransformOperationSource](aws-properties-quicksight-dataset-transformoperationsource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UnpivotedLabelColumnId`  <a name="cfn-quicksight-dataset-unpivotoperation-unpivotedlabelcolumnid"></a>
A unique identifier for the new column that will contain the unpivoted column names.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UnpivotedLabelColumnName`  <a name="cfn-quicksight-dataset-unpivotoperation-unpivotedlabelcolumnname"></a>
The name for the new column that will contain the unpivoted column names.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UnpivotedValueColumnId`  <a name="cfn-quicksight-dataset-unpivotoperation-unpivotedvaluecolumnid"></a>
A unique identifier for the new column that will contain the unpivoted values.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UnpivotedValueColumnName`  <a name="cfn-quicksight-dataset-unpivotoperation-unpivotedvaluecolumnname"></a>
The name for the new column that will contain the unpivoted values.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
