---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-datasetnumericfiltercondition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet DataSetNumericFilterCondition
<a name="aws-properties-quicksight-dataset-datasetnumericfiltercondition"></a>

A filter condition for numeric columns, supporting both comparison and range-based filtering.

## Syntax
<a name="aws-properties-quicksight-dataset-datasetnumericfiltercondition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-datasetnumericfiltercondition-syntax.json"></a>

```
{
  "[ColumnName](#cfn-quicksight-dataset-datasetnumericfiltercondition-columnname)" : {{String}},
  "[ComparisonFilterCondition](#cfn-quicksight-dataset-datasetnumericfiltercondition-comparisonfiltercondition)" : {{DataSetNumericComparisonFilterCondition}},
  "[RangeFilterCondition](#cfn-quicksight-dataset-datasetnumericfiltercondition-rangefiltercondition)" : {{DataSetNumericRangeFilterCondition}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-datasetnumericfiltercondition-syntax.yaml"></a>

```
  [ColumnName](#cfn-quicksight-dataset-datasetnumericfiltercondition-columnname): {{String}}
  [ComparisonFilterCondition](#cfn-quicksight-dataset-datasetnumericfiltercondition-comparisonfiltercondition): {{
    DataSetNumericComparisonFilterCondition}}
  [RangeFilterCondition](#cfn-quicksight-dataset-datasetnumericfiltercondition-rangefiltercondition): {{
    DataSetNumericRangeFilterCondition}}
```

## Properties
<a name="aws-properties-quicksight-dataset-datasetnumericfiltercondition-properties"></a>

`ColumnName`  <a name="cfn-quicksight-dataset-datasetnumericfiltercondition-columnname"></a>
The name of the numeric column to filter.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ComparisonFilterCondition`  <a name="cfn-quicksight-dataset-datasetnumericfiltercondition-comparisonfiltercondition"></a>
A comparison-based filter condition for the numeric column.
*Required*: No
*Type*: [DataSetNumericComparisonFilterCondition](aws-properties-quicksight-dataset-datasetnumericcomparisonfiltercondition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RangeFilterCondition`  <a name="cfn-quicksight-dataset-datasetnumericfiltercondition-rangefiltercondition"></a>
A range-based filter condition for the numeric column, filtering values between minimum and maximum numbers.
*Required*: No
*Type*: [DataSetNumericRangeFilterCondition](aws-properties-quicksight-dataset-datasetnumericrangefiltercondition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
