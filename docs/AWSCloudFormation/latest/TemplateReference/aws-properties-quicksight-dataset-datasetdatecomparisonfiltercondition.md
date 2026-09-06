---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-datasetdatecomparisonfiltercondition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet DataSetDateComparisonFilterCondition
<a name="aws-properties-quicksight-dataset-datasetdatecomparisonfiltercondition"></a>

A filter condition that compares date values using operators like `BEFORE`, `AFTER`, or their inclusive variants.

## Syntax
<a name="aws-properties-quicksight-dataset-datasetdatecomparisonfiltercondition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-datasetdatecomparisonfiltercondition-syntax.json"></a>

```
{
  "[Operator](#cfn-quicksight-dataset-datasetdatecomparisonfiltercondition-operator)" : {{String}},
  "[Value](#cfn-quicksight-dataset-datasetdatecomparisonfiltercondition-value)" : {{DataSetDateFilterValue}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-datasetdatecomparisonfiltercondition-syntax.yaml"></a>

```
  [Operator](#cfn-quicksight-dataset-datasetdatecomparisonfiltercondition-operator): {{String}}
  [Value](#cfn-quicksight-dataset-datasetdatecomparisonfiltercondition-value): {{
    DataSetDateFilterValue}}
```

## Properties
<a name="aws-properties-quicksight-dataset-datasetdatecomparisonfiltercondition-properties"></a>

`Operator`  <a name="cfn-quicksight-dataset-datasetdatecomparisonfiltercondition-operator"></a>
The comparison operator to use, such as `BEFORE`, `BEFORE_OR_EQUALS_TO`, `AFTER`, or `AFTER_OR_EQUALS_TO`.
*Required*: Yes
*Type*: String
*Allowed values*: `BEFORE | BEFORE_OR_EQUALS_TO | AFTER | AFTER_OR_EQUALS_TO`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-quicksight-dataset-datasetdatecomparisonfiltercondition-value"></a>
The date value to compare against.
*Required*: No
*Type*: [DataSetDateFilterValue](aws-properties-quicksight-dataset-datasetdatefiltervalue.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
