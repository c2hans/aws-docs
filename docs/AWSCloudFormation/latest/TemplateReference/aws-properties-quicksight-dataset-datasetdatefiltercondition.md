---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-datasetdatefiltercondition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet DataSetDateFilterCondition
<a name="aws-properties-quicksight-dataset-datasetdatefiltercondition"></a>

A filter condition for date columns, supporting both comparison and range-based filtering.

## Syntax
<a name="aws-properties-quicksight-dataset-datasetdatefiltercondition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-datasetdatefiltercondition-syntax.json"></a>

```
{
  "[ColumnName](#cfn-quicksight-dataset-datasetdatefiltercondition-columnname)" : {{String}},
  "[ComparisonFilterCondition](#cfn-quicksight-dataset-datasetdatefiltercondition-comparisonfiltercondition)" : {{DataSetDateComparisonFilterCondition}},
  "[RangeFilterCondition](#cfn-quicksight-dataset-datasetdatefiltercondition-rangefiltercondition)" : {{DataSetDateRangeFilterCondition}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-datasetdatefiltercondition-syntax.yaml"></a>

```
  [ColumnName](#cfn-quicksight-dataset-datasetdatefiltercondition-columnname): {{String}}
  [ComparisonFilterCondition](#cfn-quicksight-dataset-datasetdatefiltercondition-comparisonfiltercondition): {{
    DataSetDateComparisonFilterCondition}}
  [RangeFilterCondition](#cfn-quicksight-dataset-datasetdatefiltercondition-rangefiltercondition): {{
    DataSetDateRangeFilterCondition}}
```

## Properties
<a name="aws-properties-quicksight-dataset-datasetdatefiltercondition-properties"></a>

`ColumnName`  <a name="cfn-quicksight-dataset-datasetdatefiltercondition-columnname"></a>
The name of the date column to filter.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ComparisonFilterCondition`  <a name="cfn-quicksight-dataset-datasetdatefiltercondition-comparisonfiltercondition"></a>
A comparison-based filter condition for the date column.
*Required*: No
*Type*: [DataSetDateComparisonFilterCondition](aws-properties-quicksight-dataset-datasetdatecomparisonfiltercondition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RangeFilterCondition`  <a name="cfn-quicksight-dataset-datasetdatefiltercondition-rangefiltercondition"></a>
A range-based filter condition for the date column, filtering values between minimum and maximum dates.
*Required*: No
*Type*: [DataSetDateRangeFilterCondition](aws-properties-quicksight-dataset-datasetdaterangefiltercondition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
