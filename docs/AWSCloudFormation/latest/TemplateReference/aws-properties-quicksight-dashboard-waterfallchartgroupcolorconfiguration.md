---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-waterfallchartgroupcolorconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard WaterfallChartGroupColorConfiguration
<a name="aws-properties-quicksight-dashboard-waterfallchartgroupcolorconfiguration"></a>

The color configuration for individual groups within a waterfall visual.

## Syntax
<a name="aws-properties-quicksight-dashboard-waterfallchartgroupcolorconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-waterfallchartgroupcolorconfiguration-syntax.json"></a>

```
{
  "[NegativeBarColor](#cfn-quicksight-dashboard-waterfallchartgroupcolorconfiguration-negativebarcolor)" : {{String}},
  "[PositiveBarColor](#cfn-quicksight-dashboard-waterfallchartgroupcolorconfiguration-positivebarcolor)" : {{String}},
  "[TotalBarColor](#cfn-quicksight-dashboard-waterfallchartgroupcolorconfiguration-totalbarcolor)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-waterfallchartgroupcolorconfiguration-syntax.yaml"></a>

```
  [NegativeBarColor](#cfn-quicksight-dashboard-waterfallchartgroupcolorconfiguration-negativebarcolor): {{String}}
  [PositiveBarColor](#cfn-quicksight-dashboard-waterfallchartgroupcolorconfiguration-positivebarcolor): {{String}}
  [TotalBarColor](#cfn-quicksight-dashboard-waterfallchartgroupcolorconfiguration-totalbarcolor): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-waterfallchartgroupcolorconfiguration-properties"></a>

`NegativeBarColor`  <a name="cfn-quicksight-dashboard-waterfallchartgroupcolorconfiguration-negativebarcolor"></a>
Defines the color for the negative bars of a waterfall chart.
*Required*: No
*Type*: String
*Pattern*: `^#[A-F0-9]{6}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PositiveBarColor`  <a name="cfn-quicksight-dashboard-waterfallchartgroupcolorconfiguration-positivebarcolor"></a>
Defines the color for the positive bars of a waterfall chart.
*Required*: No
*Type*: String
*Pattern*: `^#[A-F0-9]{6}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TotalBarColor`  <a name="cfn-quicksight-dashboard-waterfallchartgroupcolorconfiguration-totalbarcolor"></a>
Defines the color for the total bars of a waterfall chart.
*Required*: No
*Type*: String
*Pattern*: `^#[A-F0-9]{6}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
