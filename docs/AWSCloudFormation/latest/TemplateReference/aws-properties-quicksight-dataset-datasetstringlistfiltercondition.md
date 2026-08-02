---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-datasetstringlistfiltercondition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet DataSetStringListFilterCondition
<a name="aws-properties-quicksight-dataset-datasetstringlistfiltercondition"></a>

A filter condition that includes or excludes string values from a specified list.

## Syntax
<a name="aws-properties-quicksight-dataset-datasetstringlistfiltercondition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-datasetstringlistfiltercondition-syntax.json"></a>

```
{
  "[Operator](#cfn-quicksight-dataset-datasetstringlistfiltercondition-operator)" : {{String}},
  "[Values](#cfn-quicksight-dataset-datasetstringlistfiltercondition-values)" : {{DataSetStringListFilterValue}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-datasetstringlistfiltercondition-syntax.yaml"></a>

```
  [Operator](#cfn-quicksight-dataset-datasetstringlistfiltercondition-operator): {{String}}
  [Values](#cfn-quicksight-dataset-datasetstringlistfiltercondition-values): {{
    DataSetStringListFilterValue}}
```

## Properties
<a name="aws-properties-quicksight-dataset-datasetstringlistfiltercondition-properties"></a>

`Operator`  <a name="cfn-quicksight-dataset-datasetstringlistfiltercondition-operator"></a>
The list operator to use, either `INCLUDE` to match values in the list or `EXCLUDE` to filter out values in the list.
*Required*: Yes
*Type*: String
*Allowed values*: `INCLUDE | EXCLUDE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-quicksight-dataset-datasetstringlistfiltercondition-values"></a>
The list of string values to include or exclude in the filter.
*Required*: No
*Type*: [DataSetStringListFilterValue](aws-properties-quicksight-dataset-datasetstringlistfiltervalue.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
