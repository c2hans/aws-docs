---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-datasetnumericcomparisonfiltercondition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet DataSetNumericComparisonFilterCondition
<a name="aws-properties-quicksight-dataset-datasetnumericcomparisonfiltercondition"></a>

A filter condition that compares numeric values using operators like `EQUALS`, `GREATER_THAN`, or `LESS_THAN`.

## Syntax
<a name="aws-properties-quicksight-dataset-datasetnumericcomparisonfiltercondition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-datasetnumericcomparisonfiltercondition-syntax.json"></a>

```
{
  "[Operator](#cfn-quicksight-dataset-datasetnumericcomparisonfiltercondition-operator)" : {{String}},
  "[Value](#cfn-quicksight-dataset-datasetnumericcomparisonfiltercondition-value)" : {{DataSetNumericFilterValue}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-datasetnumericcomparisonfiltercondition-syntax.yaml"></a>

```
  [Operator](#cfn-quicksight-dataset-datasetnumericcomparisonfiltercondition-operator): {{String}}
  [Value](#cfn-quicksight-dataset-datasetnumericcomparisonfiltercondition-value): {{
    DataSetNumericFilterValue}}
```

## Properties
<a name="aws-properties-quicksight-dataset-datasetnumericcomparisonfiltercondition-properties"></a>

`Operator`  <a name="cfn-quicksight-dataset-datasetnumericcomparisonfiltercondition-operator"></a>
The comparison operator to use, such as `EQUALS`, `GREATER_THAN`, `LESS_THAN`, or their variants.
*Required*: Yes
*Type*: String
*Allowed values*: `EQUALS | DOES_NOT_EQUAL | GREATER_THAN | GREATER_THAN_OR_EQUALS_TO | LESS_THAN | LESS_THAN_OR_EQUALS_TO`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-quicksight-dataset-datasetnumericcomparisonfiltercondition-value"></a>
The numeric value to compare against.
*Required*: No
*Type*: [DataSetNumericFilterValue](aws-properties-quicksight-dataset-datasetnumericfiltervalue.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
