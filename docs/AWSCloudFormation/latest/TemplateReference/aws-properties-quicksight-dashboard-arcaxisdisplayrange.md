---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-arcaxisdisplayrange.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard ArcAxisDisplayRange
<a name="aws-properties-quicksight-dashboard-arcaxisdisplayrange"></a>

The arc axis range of a `GaugeChartVisual`.

## Syntax
<a name="aws-properties-quicksight-dashboard-arcaxisdisplayrange-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-arcaxisdisplayrange-syntax.json"></a>

```
{
  "[Max](#cfn-quicksight-dashboard-arcaxisdisplayrange-max)" : {{Number}},
  "[Min](#cfn-quicksight-dashboard-arcaxisdisplayrange-min)" : {{Number}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-arcaxisdisplayrange-syntax.yaml"></a>

```
  [Max](#cfn-quicksight-dashboard-arcaxisdisplayrange-max): {{Number}}
  [Min](#cfn-quicksight-dashboard-arcaxisdisplayrange-min): {{Number}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-arcaxisdisplayrange-properties"></a>

`Max`  <a name="cfn-quicksight-dashboard-arcaxisdisplayrange-max"></a>
The maximum value of the arc axis range.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Min`  <a name="cfn-quicksight-dashboard-arcaxisdisplayrange-min"></a>
The minimum value of the arc axis range.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
