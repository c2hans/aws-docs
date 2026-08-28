---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-axisdisplayrange.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard AxisDisplayRange
<a name="aws-properties-quicksight-dashboard-axisdisplayrange"></a>

The range setup of a numeric axis display range.

This is a union type structure. For this structure to be valid, only one of the attributes can be defined.

## Syntax
<a name="aws-properties-quicksight-dashboard-axisdisplayrange-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-axisdisplayrange-syntax.json"></a>

```
{
  "[DataDriven](#cfn-quicksight-dashboard-axisdisplayrange-datadriven)" : {{Json}},
  "[MinMax](#cfn-quicksight-dashboard-axisdisplayrange-minmax)" : {{AxisDisplayMinMaxRange}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-axisdisplayrange-syntax.yaml"></a>

```
  [DataDriven](#cfn-quicksight-dashboard-axisdisplayrange-datadriven): {{Json}}
  [MinMax](#cfn-quicksight-dashboard-axisdisplayrange-minmax): {{
    AxisDisplayMinMaxRange}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-axisdisplayrange-properties"></a>

`DataDriven`  <a name="cfn-quicksight-dashboard-axisdisplayrange-datadriven"></a>
The data-driven setup of an axis display range.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinMax`  <a name="cfn-quicksight-dashboard-axisdisplayrange-minmax"></a>
The minimum and maximum setup of an axis display range.
*Required*: No
*Type*: [AxisDisplayMinMaxRange](aws-properties-quicksight-dashboard-axisdisplayminmaxrange.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
