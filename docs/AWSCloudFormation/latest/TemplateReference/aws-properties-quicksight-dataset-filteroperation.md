---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-filteroperation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet FilterOperation
<a name="aws-properties-quicksight-dataset-filteroperation"></a>

A transform operation that filters rows based on a condition.

## Syntax
<a name="aws-properties-quicksight-dataset-filteroperation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-filteroperation-syntax.json"></a>

```
{
  "[ConditionExpression](#cfn-quicksight-dataset-filteroperation-conditionexpression)" : {{String}},
  "[DateFilterCondition](#cfn-quicksight-dataset-filteroperation-datefiltercondition)" : {{DataSetDateFilterCondition}},
  "[NumericFilterCondition](#cfn-quicksight-dataset-filteroperation-numericfiltercondition)" : {{DataSetNumericFilterCondition}},
  "[StringFilterCondition](#cfn-quicksight-dataset-filteroperation-stringfiltercondition)" : {{DataSetStringFilterCondition}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-filteroperation-syntax.yaml"></a>

```
  [ConditionExpression](#cfn-quicksight-dataset-filteroperation-conditionexpression): {{String}}
  [DateFilterCondition](#cfn-quicksight-dataset-filteroperation-datefiltercondition): {{
    DataSetDateFilterCondition}}
  [NumericFilterCondition](#cfn-quicksight-dataset-filteroperation-numericfiltercondition): {{
    DataSetNumericFilterCondition}}
  [StringFilterCondition](#cfn-quicksight-dataset-filteroperation-stringfiltercondition): {{
    DataSetStringFilterCondition}}
```

## Properties
<a name="aws-properties-quicksight-dataset-filteroperation-properties"></a>

`ConditionExpression`  <a name="cfn-quicksight-dataset-filteroperation-conditionexpression"></a>
An expression that must evaluate to a Boolean value. Rows for which the expression evaluates to true are kept in the dataset.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DateFilterCondition`  <a name="cfn-quicksight-dataset-filteroperation-datefiltercondition"></a>
A date-based filter condition within a filter operation.
*Required*: No
*Type*: [DataSetDateFilterCondition](aws-properties-quicksight-dataset-datasetdatefiltercondition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NumericFilterCondition`  <a name="cfn-quicksight-dataset-filteroperation-numericfiltercondition"></a>
A numeric-based filter condition within a filter operation.
*Required*: No
*Type*: [DataSetNumericFilterCondition](aws-properties-quicksight-dataset-datasetnumericfiltercondition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StringFilterCondition`  <a name="cfn-quicksight-dataset-filteroperation-stringfiltercondition"></a>
A string-based filter condition within a filter operation.
*Required*: No
*Type*: [DataSetStringFilterCondition](aws-properties-quicksight-dataset-datasetstringfiltercondition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
