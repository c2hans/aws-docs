---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-yaxisoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard YAxisOptions
<a name="aws-properties-quicksight-dashboard-yaxisoptions"></a>

The options that are available for a single Y axis in a chart.

## Syntax
<a name="aws-properties-quicksight-dashboard-yaxisoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-yaxisoptions-syntax.json"></a>

```
{
  "[YAxis](#cfn-quicksight-dashboard-yaxisoptions-yaxis)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-yaxisoptions-syntax.yaml"></a>

```
  [YAxis](#cfn-quicksight-dashboard-yaxisoptions-yaxis): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-yaxisoptions-properties"></a>

`YAxis`  <a name="cfn-quicksight-dashboard-yaxisoptions-yaxis"></a>
The Y axis type to be used in the chart.
If you choose `PRIMARY_Y_AXIS`, the primary Y Axis is located on the leftmost vertical axis of the chart.
*Required*: Yes
*Type*: String
*Allowed values*: `PRIMARY_Y_AXIS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
