---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-arcaxisconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis ArcAxisConfiguration
<a name="aws-properties-quicksight-analysis-arcaxisconfiguration"></a>

The arc axis configuration of a `GaugeChartVisual`.

## Syntax
<a name="aws-properties-quicksight-analysis-arcaxisconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-arcaxisconfiguration-syntax.json"></a>

```
{
  "[Range](#cfn-quicksight-analysis-arcaxisconfiguration-range)" : {{ArcAxisDisplayRange}},
  "[ReserveRange](#cfn-quicksight-analysis-arcaxisconfiguration-reserverange)" : {{Number}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-arcaxisconfiguration-syntax.yaml"></a>

```
  [Range](#cfn-quicksight-analysis-arcaxisconfiguration-range): {{
    ArcAxisDisplayRange}}
  [ReserveRange](#cfn-quicksight-analysis-arcaxisconfiguration-reserverange): {{Number}}
```

## Properties
<a name="aws-properties-quicksight-analysis-arcaxisconfiguration-properties"></a>

`Range`  <a name="cfn-quicksight-analysis-arcaxisconfiguration-range"></a>
The arc axis range of a `GaugeChartVisual`.
*Required*: No
*Type*: [ArcAxisDisplayRange](aws-properties-quicksight-analysis-arcaxisdisplayrange.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReserveRange`  <a name="cfn-quicksight-analysis-arcaxisconfiguration-reserverange"></a>
The reserved range of the arc axis.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
