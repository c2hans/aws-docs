---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-renamecolumnsoperation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet RenameColumnsOperation
<a name="aws-properties-quicksight-dataset-renamecolumnsoperation"></a>

A transform operation that renames one or more columns in the dataset.

## Syntax
<a name="aws-properties-quicksight-dataset-renamecolumnsoperation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-renamecolumnsoperation-syntax.json"></a>

```
{
  "[Alias](#cfn-quicksight-dataset-renamecolumnsoperation-alias)" : {{String}},
  "[RenameColumnOperations](#cfn-quicksight-dataset-renamecolumnsoperation-renamecolumnoperations)" : {{[ RenameColumnOperation, ... ]}},
  "[Source](#cfn-quicksight-dataset-renamecolumnsoperation-source)" : {{TransformOperationSource}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-renamecolumnsoperation-syntax.yaml"></a>

```
  [Alias](#cfn-quicksight-dataset-renamecolumnsoperation-alias): {{String}}
  [RenameColumnOperations](#cfn-quicksight-dataset-renamecolumnsoperation-renamecolumnoperations): {{
    - RenameColumnOperation}}
  [Source](#cfn-quicksight-dataset-renamecolumnsoperation-source): {{
    TransformOperationSource}}
```

## Properties
<a name="aws-properties-quicksight-dataset-renamecolumnsoperation-properties"></a>

`Alias`  <a name="cfn-quicksight-dataset-renamecolumnsoperation-alias"></a>
Alias for this operation.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RenameColumnOperations`  <a name="cfn-quicksight-dataset-renamecolumnsoperation-renamecolumnoperations"></a>
The list of column rename operations to perform, specifying old and new column names.
*Required*: Yes
*Type*: Array of [RenameColumnOperation](aws-properties-quicksight-dataset-renamecolumnoperation.md)
*Minimum*: `0`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Source`  <a name="cfn-quicksight-dataset-renamecolumnsoperation-source"></a>
The source transform operation that provides input data for column renaming.
*Required*: Yes
*Type*: [TransformOperationSource](aws-properties-quicksight-dataset-transformoperationsource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
