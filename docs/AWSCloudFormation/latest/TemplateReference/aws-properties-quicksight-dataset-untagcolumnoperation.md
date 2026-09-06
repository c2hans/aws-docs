---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-untagcolumnoperation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet UntagColumnOperation
<a name="aws-properties-quicksight-dataset-untagcolumnoperation"></a>

A transform operation that removes tags associated with a column.

## Syntax
<a name="aws-properties-quicksight-dataset-untagcolumnoperation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-untagcolumnoperation-syntax.json"></a>

```
{
  "[ColumnName](#cfn-quicksight-dataset-untagcolumnoperation-columnname)" : {{String}},
  "[TagNames](#cfn-quicksight-dataset-untagcolumnoperation-tagnames)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-untagcolumnoperation-syntax.yaml"></a>

```
  [ColumnName](#cfn-quicksight-dataset-untagcolumnoperation-columnname): {{String}}
  [TagNames](#cfn-quicksight-dataset-untagcolumnoperation-tagnames): {{
    - String}}
```

## Properties
<a name="aws-properties-quicksight-dataset-untagcolumnoperation-properties"></a>

`ColumnName`  <a name="cfn-quicksight-dataset-untagcolumnoperation-columnname"></a>
The column that this operation acts on.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TagNames`  <a name="cfn-quicksight-dataset-untagcolumnoperation-tagnames"></a>
The column tags to remove from this column.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
