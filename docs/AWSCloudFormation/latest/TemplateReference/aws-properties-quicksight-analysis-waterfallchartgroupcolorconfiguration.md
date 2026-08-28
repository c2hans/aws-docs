---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-waterfallchartgroupcolorconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis WaterfallChartGroupColorConfiguration
<a name="aws-properties-quicksight-analysis-waterfallchartgroupcolorconfiguration"></a>

The color configuration for individual groups within a waterfall visual.

## Syntax
<a name="aws-properties-quicksight-analysis-waterfallchartgroupcolorconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-waterfallchartgroupcolorconfiguration-syntax.json"></a>

```
{
  "[NegativeBarColor](#cfn-quicksight-analysis-waterfallchartgroupcolorconfiguration-negativebarcolor)" : {{String}},
  "[PositiveBarColor](#cfn-quicksight-analysis-waterfallchartgroupcolorconfiguration-positivebarcolor)" : {{String}},
  "[TotalBarColor](#cfn-quicksight-analysis-waterfallchartgroupcolorconfiguration-totalbarcolor)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-waterfallchartgroupcolorconfiguration-syntax.yaml"></a>

```
  [NegativeBarColor](#cfn-quicksight-analysis-waterfallchartgroupcolorconfiguration-negativebarcolor): {{String}}
  [PositiveBarColor](#cfn-quicksight-analysis-waterfallchartgroupcolorconfiguration-positivebarcolor): {{String}}
  [TotalBarColor](#cfn-quicksight-analysis-waterfallchartgroupcolorconfiguration-totalbarcolor): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-waterfallchartgroupcolorconfiguration-properties"></a>

`NegativeBarColor`  <a name="cfn-quicksight-analysis-waterfallchartgroupcolorconfiguration-negativebarcolor"></a>
Defines the color for the negative bars of a waterfall chart.
*Required*: No
*Type*: String
*Pattern*: `^#[A-F0-9]{6}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PositiveBarColor`  <a name="cfn-quicksight-analysis-waterfallchartgroupcolorconfiguration-positivebarcolor"></a>
Defines the color for the positive bars of a waterfall chart.
*Required*: No
*Type*: String
*Pattern*: `^#[A-F0-9]{6}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TotalBarColor`  <a name="cfn-quicksight-analysis-waterfallchartgroupcolorconfiguration-totalbarcolor"></a>
Defines the color for the total bars of a waterfall chart.
*Required*: No
*Type*: String
*Pattern*: `^#[A-F0-9]{6}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
