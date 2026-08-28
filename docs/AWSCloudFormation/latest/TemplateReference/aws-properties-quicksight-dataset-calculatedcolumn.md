---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-calculatedcolumn.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet CalculatedColumn
<a name="aws-properties-quicksight-dataset-calculatedcolumn"></a>

A calculated column for a dataset.

## Syntax
<a name="aws-properties-quicksight-dataset-calculatedcolumn-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-calculatedcolumn-syntax.json"></a>

```
{
  "[ColumnId](#cfn-quicksight-dataset-calculatedcolumn-columnid)" : {{String}},
  "[ColumnName](#cfn-quicksight-dataset-calculatedcolumn-columnname)" : {{String}},
  "[Expression](#cfn-quicksight-dataset-calculatedcolumn-expression)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-calculatedcolumn-syntax.yaml"></a>

```
  [ColumnId](#cfn-quicksight-dataset-calculatedcolumn-columnid): {{String}}
  [ColumnName](#cfn-quicksight-dataset-calculatedcolumn-columnname): {{String}}
  [Expression](#cfn-quicksight-dataset-calculatedcolumn-expression): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dataset-calculatedcolumn-properties"></a>

`ColumnId`  <a name="cfn-quicksight-dataset-calculatedcolumn-columnid"></a>
A unique ID to identify a calculated column. During a dataset update, if the column ID of a calculated column matches that of an existing calculated column, Quick Sight preserves the existing calculated column.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ColumnName`  <a name="cfn-quicksight-dataset-calculatedcolumn-columnname"></a>
Column name.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Expression`  <a name="cfn-quicksight-dataset-calculatedcolumn-expression"></a>
An expression that defines the calculated column.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `250000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
