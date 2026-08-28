---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-axisdisplayminmaxrange.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard AxisDisplayMinMaxRange
<a name="aws-properties-quicksight-dashboard-axisdisplayminmaxrange"></a>

The minimum and maximum setup for an axis display range.

## Syntax
<a name="aws-properties-quicksight-dashboard-axisdisplayminmaxrange-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-axisdisplayminmaxrange-syntax.json"></a>

```
{
  "[Maximum](#cfn-quicksight-dashboard-axisdisplayminmaxrange-maximum)" : {{Number}},
  "[Minimum](#cfn-quicksight-dashboard-axisdisplayminmaxrange-minimum)" : {{Number}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-axisdisplayminmaxrange-syntax.yaml"></a>

```
  [Maximum](#cfn-quicksight-dashboard-axisdisplayminmaxrange-maximum): {{Number}}
  [Minimum](#cfn-quicksight-dashboard-axisdisplayminmaxrange-minimum): {{Number}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-axisdisplayminmaxrange-properties"></a>

`Maximum`  <a name="cfn-quicksight-dashboard-axisdisplayminmaxrange-maximum"></a>
The maximum setup for an axis display range.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Minimum`  <a name="cfn-quicksight-dashboard-axisdisplayminmaxrange-minimum"></a>
The minimum setup for an axis display range.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
