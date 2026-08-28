---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dataset-datasetnumericrangefiltercondition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DataSet DataSetNumericRangeFilterCondition
<a name="aws-properties-quicksight-dataset-datasetnumericrangefiltercondition"></a>

A filter condition that filters numeric values within a specified range.

## Syntax
<a name="aws-properties-quicksight-dataset-datasetnumericrangefiltercondition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dataset-datasetnumericrangefiltercondition-syntax.json"></a>

```
{
  "[IncludeMaximum](#cfn-quicksight-dataset-datasetnumericrangefiltercondition-includemaximum)" : {{Boolean}},
  "[IncludeMinimum](#cfn-quicksight-dataset-datasetnumericrangefiltercondition-includeminimum)" : {{Boolean}},
  "[RangeMaximum](#cfn-quicksight-dataset-datasetnumericrangefiltercondition-rangemaximum)" : {{DataSetNumericFilterValue}},
  "[RangeMinimum](#cfn-quicksight-dataset-datasetnumericrangefiltercondition-rangeminimum)" : {{DataSetNumericFilterValue}}
}
```

### YAML
<a name="aws-properties-quicksight-dataset-datasetnumericrangefiltercondition-syntax.yaml"></a>

```
  [IncludeMaximum](#cfn-quicksight-dataset-datasetnumericrangefiltercondition-includemaximum): {{Boolean}}
  [IncludeMinimum](#cfn-quicksight-dataset-datasetnumericrangefiltercondition-includeminimum): {{Boolean}}
  [RangeMaximum](#cfn-quicksight-dataset-datasetnumericrangefiltercondition-rangemaximum): {{
    DataSetNumericFilterValue}}
  [RangeMinimum](#cfn-quicksight-dataset-datasetnumericrangefiltercondition-rangeminimum): {{
    DataSetNumericFilterValue}}
```

## Properties
<a name="aws-properties-quicksight-dataset-datasetnumericrangefiltercondition-properties"></a>

`IncludeMaximum`  <a name="cfn-quicksight-dataset-datasetnumericrangefiltercondition-includemaximum"></a>
Whether to include the maximum value in the filter range.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IncludeMinimum`  <a name="cfn-quicksight-dataset-datasetnumericrangefiltercondition-includeminimum"></a>
Whether to include the minimum value in the filter range.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RangeMaximum`  <a name="cfn-quicksight-dataset-datasetnumericrangefiltercondition-rangemaximum"></a>
The maximum numeric value for the range filter.
*Required*: No
*Type*: [DataSetNumericFilterValue](aws-properties-quicksight-dataset-datasetnumericfiltervalue.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RangeMinimum`  <a name="cfn-quicksight-dataset-datasetnumericrangefiltercondition-rangeminimum"></a>
The minimum numeric value for the range filter.
*Required*: No
*Type*: [DataSetNumericFilterValue](aws-properties-quicksight-dataset-datasetnumericfiltervalue.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
