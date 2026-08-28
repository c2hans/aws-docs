---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-datasetstringcomparisonfiltercondition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet DataSetStringComparisonFilterCondition
<a name="aws-properties-quicksight-dataset-datasetstringcomparisonfiltercondition"></a>

A filter condition that compares string values using operators like `EQUALS`, `CONTAINS`, or `STARTS_WITH`.

## Syntax
<a name="aws-properties-quicksight-dataset-datasetstringcomparisonfiltercondition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-datasetstringcomparisonfiltercondition-syntax.json"></a>

```
{
  "[Operator](#cfn-quicksight-dataset-datasetstringcomparisonfiltercondition-operator)" : {{String}},
  "[Value](#cfn-quicksight-dataset-datasetstringcomparisonfiltercondition-value)" : {{DataSetStringFilterValue}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-datasetstringcomparisonfiltercondition-syntax.yaml"></a>

```
  [Operator](#cfn-quicksight-dataset-datasetstringcomparisonfiltercondition-operator): {{String}}
  [Value](#cfn-quicksight-dataset-datasetstringcomparisonfiltercondition-value): {{
    DataSetStringFilterValue}}
```

## Properties
<a name="aws-properties-quicksight-dataset-datasetstringcomparisonfiltercondition-properties"></a>

`Operator`  <a name="cfn-quicksight-dataset-datasetstringcomparisonfiltercondition-operator"></a>
The comparison operator to use, such as `EQUALS`, `CONTAINS`, `STARTS_WITH`, `ENDS_WITH`, or their negations.
*Required*: Yes
*Type*: String
*Allowed values*: `EQUALS | DOES_NOT_EQUAL | CONTAINS | DOES_NOT_CONTAIN | STARTS_WITH | ENDS_WITH`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-quicksight-dataset-datasetstringcomparisonfiltercondition-value"></a>
The string value to compare against.
*Required*: No
*Type*: [DataSetStringFilterValue](aws-properties-quicksight-dataset-datasetstringfiltervalue.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
