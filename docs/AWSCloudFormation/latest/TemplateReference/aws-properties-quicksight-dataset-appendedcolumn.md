---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-appendedcolumn.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet AppendedColumn
<a name="aws-properties-quicksight-dataset-appendedcolumn"></a>

Represents a column that will be included in the result of an append operation, combining data from multiple sources.

## Syntax
<a name="aws-properties-quicksight-dataset-appendedcolumn-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-appendedcolumn-syntax.json"></a>

```
{
  "[ColumnName](#cfn-quicksight-dataset-appendedcolumn-columnname)" : {{String}},
  "[NewColumnId](#cfn-quicksight-dataset-appendedcolumn-newcolumnid)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-appendedcolumn-syntax.yaml"></a>

```
  [ColumnName](#cfn-quicksight-dataset-appendedcolumn-columnname): {{String}}
  [NewColumnId](#cfn-quicksight-dataset-appendedcolumn-newcolumnid): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dataset-appendedcolumn-properties"></a>

`ColumnName`  <a name="cfn-quicksight-dataset-appendedcolumn-columnname"></a>
The name of the column to include in the appended result.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NewColumnId`  <a name="cfn-quicksight-dataset-appendedcolumn-newcolumnid"></a>
A unique identifier for the column in the appended result.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
