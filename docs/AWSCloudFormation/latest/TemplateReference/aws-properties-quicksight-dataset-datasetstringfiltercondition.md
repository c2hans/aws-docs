---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-datasetstringfiltercondition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet DataSetStringFilterCondition
<a name="aws-properties-quicksight-dataset-datasetstringfiltercondition"></a>

A filter condition for string columns, supporting both comparison and list-based filtering.

## Syntax
<a name="aws-properties-quicksight-dataset-datasetstringfiltercondition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-datasetstringfiltercondition-syntax.json"></a>

```
{
  "[ColumnName](#cfn-quicksight-dataset-datasetstringfiltercondition-columnname)" : {{String}},
  "[ComparisonFilterCondition](#cfn-quicksight-dataset-datasetstringfiltercondition-comparisonfiltercondition)" : {{DataSetStringComparisonFilterCondition}},
  "[ListFilterCondition](#cfn-quicksight-dataset-datasetstringfiltercondition-listfiltercondition)" : {{DataSetStringListFilterCondition}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-datasetstringfiltercondition-syntax.yaml"></a>

```
  [ColumnName](#cfn-quicksight-dataset-datasetstringfiltercondition-columnname): {{String}}
  [ComparisonFilterCondition](#cfn-quicksight-dataset-datasetstringfiltercondition-comparisonfiltercondition): {{
    DataSetStringComparisonFilterCondition}}
  [ListFilterCondition](#cfn-quicksight-dataset-datasetstringfiltercondition-listfiltercondition): {{
    DataSetStringListFilterCondition}}
```

## Properties
<a name="aws-properties-quicksight-dataset-datasetstringfiltercondition-properties"></a>

`ColumnName`  <a name="cfn-quicksight-dataset-datasetstringfiltercondition-columnname"></a>
The name of the string column to filter.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ComparisonFilterCondition`  <a name="cfn-quicksight-dataset-datasetstringfiltercondition-comparisonfiltercondition"></a>
A comparison-based filter condition for the string column.
*Required*: No
*Type*: [DataSetStringComparisonFilterCondition](aws-properties-quicksight-dataset-datasetstringcomparisonfiltercondition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ListFilterCondition`  <a name="cfn-quicksight-dataset-datasetstringfiltercondition-listfiltercondition"></a>
A list-based filter condition that includes or excludes values from a specified list.
*Required*: No
*Type*: [DataSetStringListFilterCondition](aws-properties-quicksight-dataset-datasetstringlistfiltercondition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
