---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-waterfallchartcolorconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard WaterfallChartColorConfiguration
<a name="aws-properties-quicksight-dashboard-waterfallchartcolorconfiguration"></a>

The color configuration of a waterfall visual.

## Syntax
<a name="aws-properties-quicksight-dashboard-waterfallchartcolorconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-waterfallchartcolorconfiguration-syntax.json"></a>

```
{
  "[GroupColorConfiguration](#cfn-quicksight-dashboard-waterfallchartcolorconfiguration-groupcolorconfiguration)" : {{WaterfallChartGroupColorConfiguration}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-waterfallchartcolorconfiguration-syntax.yaml"></a>

```
  [GroupColorConfiguration](#cfn-quicksight-dashboard-waterfallchartcolorconfiguration-groupcolorconfiguration): {{
    WaterfallChartGroupColorConfiguration}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-waterfallchartcolorconfiguration-properties"></a>

`GroupColorConfiguration`  <a name="cfn-quicksight-dashboard-waterfallchartcolorconfiguration-groupcolorconfiguration"></a>
The color configuration for individual groups within a waterfall visual.
*Required*: No
*Type*: [WaterfallChartGroupColorConfiguration](aws-properties-quicksight-dashboard-waterfallchartgroupcolorconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
