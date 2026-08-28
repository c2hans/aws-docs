---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-numericrangefiltervalue.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard NumericRangeFilterValue
<a name="aws-properties-quicksight-dashboard-numericrangefiltervalue"></a>

The value input pf the numeric range filter.

## Syntax
<a name="aws-properties-quicksight-dashboard-numericrangefiltervalue-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-numericrangefiltervalue-syntax.json"></a>

```
{
  "[Parameter](#cfn-quicksight-dashboard-numericrangefiltervalue-parameter)" : {{String}},
  "[StaticValue](#cfn-quicksight-dashboard-numericrangefiltervalue-staticvalue)" : {{Number}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-numericrangefiltervalue-syntax.yaml"></a>

```
  [Parameter](#cfn-quicksight-dashboard-numericrangefiltervalue-parameter): {{String}}
  [StaticValue](#cfn-quicksight-dashboard-numericrangefiltervalue-staticvalue): {{Number}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-numericrangefiltervalue-properties"></a>

`Parameter`  <a name="cfn-quicksight-dashboard-numericrangefiltervalue-parameter"></a>
The parameter that is used in the numeric range.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9]+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StaticValue`  <a name="cfn-quicksight-dashboard-numericrangefiltervalue-staticvalue"></a>
The static value of the numeric range filter.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
