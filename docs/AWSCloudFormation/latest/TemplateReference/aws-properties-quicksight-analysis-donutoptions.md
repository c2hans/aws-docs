---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-donutoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis DonutOptions
<a name="aws-properties-quicksight-analysis-donutoptions"></a>

The options for configuring a donut chart or pie chart.

## Syntax
<a name="aws-properties-quicksight-analysis-donutoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-donutoptions-syntax.json"></a>

```
{
  "[ArcOptions](#cfn-quicksight-analysis-donutoptions-arcoptions)" : {{ArcOptions}},
  "[DonutCenterOptions](#cfn-quicksight-analysis-donutoptions-donutcenteroptions)" : {{DonutCenterOptions}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-donutoptions-syntax.yaml"></a>

```
  [ArcOptions](#cfn-quicksight-analysis-donutoptions-arcoptions): {{
    ArcOptions}}
  [DonutCenterOptions](#cfn-quicksight-analysis-donutoptions-donutcenteroptions): {{
    DonutCenterOptions}}
```

## Properties
<a name="aws-properties-quicksight-analysis-donutoptions-properties"></a>

`ArcOptions`  <a name="cfn-quicksight-analysis-donutoptions-arcoptions"></a>
The option for define the arc of the chart shape. Valid values are as follows:
+ `WHOLE` - A pie chart
+ `SMALL`- A small-sized donut chart
+ `MEDIUM`- A medium-sized donut chart
+ `LARGE`- A large-sized donut chart
*Required*: No
*Type*: [ArcOptions](aws-properties-quicksight-analysis-arcoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DonutCenterOptions`  <a name="cfn-quicksight-analysis-donutoptions-donutcenteroptions"></a>
The label options of the label that is displayed in the center of a donut chart. This option isn't available for pie charts.
*Required*: No
*Type*: [DonutCenterOptions](aws-properties-quicksight-analysis-donutcenteroptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
