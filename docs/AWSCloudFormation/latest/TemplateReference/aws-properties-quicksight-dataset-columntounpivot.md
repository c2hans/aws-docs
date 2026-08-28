---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-columntounpivot.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet ColumnToUnpivot
<a name="aws-properties-quicksight-dataset-columntounpivot"></a>

Specifies a column to be unpivoted, transforming it from a column into rows with associated values.

## Syntax
<a name="aws-properties-quicksight-dataset-columntounpivot-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-columntounpivot-syntax.json"></a>

```
{
  "[ColumnName](#cfn-quicksight-dataset-columntounpivot-columnname)" : {{String}},
  "[NewValue](#cfn-quicksight-dataset-columntounpivot-newvalue)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-columntounpivot-syntax.yaml"></a>

```
  [ColumnName](#cfn-quicksight-dataset-columntounpivot-columnname): {{String}}
  [NewValue](#cfn-quicksight-dataset-columntounpivot-newvalue): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dataset-columntounpivot-properties"></a>

`ColumnName`  <a name="cfn-quicksight-dataset-columntounpivot-columnname"></a>
The name of the column to unpivot from the source data.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NewValue`  <a name="cfn-quicksight-dataset-columntounpivot-newvalue"></a>
The value to assign to this column in the unpivoted result, typically the column name or a descriptive label.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `2047`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
