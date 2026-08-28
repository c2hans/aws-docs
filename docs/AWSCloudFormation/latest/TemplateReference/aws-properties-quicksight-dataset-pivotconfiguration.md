---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-pivotconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet PivotConfiguration
<a name="aws-properties-quicksight-dataset-pivotconfiguration"></a>

Configuration for a pivot operation, specifying which column contains labels and how to pivot them.

## Syntax
<a name="aws-properties-quicksight-dataset-pivotconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-pivotconfiguration-syntax.json"></a>

```
{
  "[LabelColumnName](#cfn-quicksight-dataset-pivotconfiguration-labelcolumnname)" : {{String}},
  "[PivotedLabels](#cfn-quicksight-dataset-pivotconfiguration-pivotedlabels)" : {{[ PivotedLabel, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-pivotconfiguration-syntax.yaml"></a>

```
  [LabelColumnName](#cfn-quicksight-dataset-pivotconfiguration-labelcolumnname): {{String}}
  [PivotedLabels](#cfn-quicksight-dataset-pivotconfiguration-pivotedlabels): {{
    - PivotedLabel}}
```

## Properties
<a name="aws-properties-quicksight-dataset-pivotconfiguration-properties"></a>

`LabelColumnName`  <a name="cfn-quicksight-dataset-pivotconfiguration-labelcolumnname"></a>
The name of the column that contains the labels to be pivoted into separate columns.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PivotedLabels`  <a name="cfn-quicksight-dataset-pivotconfiguration-pivotedlabels"></a>
The list of specific label values to pivot into separate columns.
*Required*: Yes
*Type*: Array of [PivotedLabel](aws-properties-quicksight-dataset-pivotedlabel.md)
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
