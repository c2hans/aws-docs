---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-singleaxisoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard SingleAxisOptions
<a name="aws-properties-quicksight-dashboard-singleaxisoptions"></a>

The settings of a chart's single axis configuration.

## Syntax
<a name="aws-properties-quicksight-dashboard-singleaxisoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-singleaxisoptions-syntax.json"></a>

```
{
  "[YAxisOptions](#cfn-quicksight-dashboard-singleaxisoptions-yaxisoptions)" : {{YAxisOptions}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-singleaxisoptions-syntax.yaml"></a>

```
  [YAxisOptions](#cfn-quicksight-dashboard-singleaxisoptions-yaxisoptions): {{
    YAxisOptions}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-singleaxisoptions-properties"></a>

`YAxisOptions`  <a name="cfn-quicksight-dashboard-singleaxisoptions-yaxisoptions"></a>
The Y axis options of a single axis configuration.
*Required*: No
*Type*: [YAxisOptions](aws-properties-quicksight-dashboard-yaxisoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
