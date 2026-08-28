---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-castcolumntypeoperation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet CastColumnTypeOperation
<a name="aws-properties-quicksight-dataset-castcolumntypeoperation"></a>

A transform operation that casts a column to a different type.

## Syntax
<a name="aws-properties-quicksight-dataset-castcolumntypeoperation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-castcolumntypeoperation-syntax.json"></a>

```
{
  "[ColumnName](#cfn-quicksight-dataset-castcolumntypeoperation-columnname)" : {{String}},
  "[Format](#cfn-quicksight-dataset-castcolumntypeoperation-format)" : {{String}},
  "[NewColumnType](#cfn-quicksight-dataset-castcolumntypeoperation-newcolumntype)" : {{String}},
  "[SubType](#cfn-quicksight-dataset-castcolumntypeoperation-subtype)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-castcolumntypeoperation-syntax.yaml"></a>

```
  [ColumnName](#cfn-quicksight-dataset-castcolumntypeoperation-columnname): {{String}}
  [Format](#cfn-quicksight-dataset-castcolumntypeoperation-format): {{String}}
  [NewColumnType](#cfn-quicksight-dataset-castcolumntypeoperation-newcolumntype): {{String}}
  [SubType](#cfn-quicksight-dataset-castcolumntypeoperation-subtype): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dataset-castcolumntypeoperation-properties"></a>

`ColumnName`  <a name="cfn-quicksight-dataset-castcolumntypeoperation-columnname"></a>
Column name.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Format`  <a name="cfn-quicksight-dataset-castcolumntypeoperation-format"></a>
When casting a column from string to datetime type, you can supply a string in a format supported by Quick Sight to denote the source data format.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `32`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NewColumnType`  <a name="cfn-quicksight-dataset-castcolumntypeoperation-newcolumntype"></a>
New column data type.
*Required*: Yes
*Type*: String
*Allowed values*: `STRING | INTEGER | DECIMAL | DATETIME`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubType`  <a name="cfn-quicksight-dataset-castcolumntypeoperation-subtype"></a>
The sub data type of the new column. Sub types are only available for decimal columns that are part of a SPICE dataset.
*Required*: No
*Type*: String
*Allowed values*: `FLOAT | FIXED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
