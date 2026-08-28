---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-columnidentifier.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis ColumnIdentifier
<a name="aws-properties-quicksight-analysis-columnidentifier"></a>

A column of a data set.

## Syntax
<a name="aws-properties-quicksight-analysis-columnidentifier-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-columnidentifier-syntax.json"></a>

```
{
  "[ColumnName](#cfn-quicksight-analysis-columnidentifier-columnname)" : {{String}},
  "[DataSetIdentifier](#cfn-quicksight-analysis-columnidentifier-datasetidentifier)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-columnidentifier-syntax.yaml"></a>

```
  [ColumnName](#cfn-quicksight-analysis-columnidentifier-columnname): {{String}}
  [DataSetIdentifier](#cfn-quicksight-analysis-columnidentifier-datasetidentifier): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-columnidentifier-properties"></a>

`ColumnName`  <a name="cfn-quicksight-analysis-columnidentifier-columnname"></a>
The name of the column.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataSetIdentifier`  <a name="cfn-quicksight-analysis-columnidentifier-datasetidentifier"></a>
The data set that the column belongs to.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
