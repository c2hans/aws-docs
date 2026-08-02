---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-gaugechartcolorconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard GaugeChartColorConfiguration
<a name="aws-properties-quicksight-dashboard-gaugechartcolorconfiguration"></a>

The color configuration of a `GaugeChartVisual`.

## Syntax
<a name="aws-properties-quicksight-dashboard-gaugechartcolorconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-gaugechartcolorconfiguration-syntax.json"></a>

```
{
  "[BackgroundColor](#cfn-quicksight-dashboard-gaugechartcolorconfiguration-backgroundcolor)" : {{String}},
  "[ForegroundColor](#cfn-quicksight-dashboard-gaugechartcolorconfiguration-foregroundcolor)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-gaugechartcolorconfiguration-syntax.yaml"></a>

```
  [BackgroundColor](#cfn-quicksight-dashboard-gaugechartcolorconfiguration-backgroundcolor): {{String}}
  [ForegroundColor](#cfn-quicksight-dashboard-gaugechartcolorconfiguration-foregroundcolor): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-gaugechartcolorconfiguration-properties"></a>

`BackgroundColor`  <a name="cfn-quicksight-dashboard-gaugechartcolorconfiguration-backgroundcolor"></a>
The background color configuration of a `GaugeChartVisual`.
*Required*: No
*Type*: String
*Pattern*: `^#[A-F0-9]{6}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ForegroundColor`  <a name="cfn-quicksight-dashboard-gaugechartcolorconfiguration-foregroundcolor"></a>
The foreground color configuration of a `GaugeChartVisual`.
*Required*: No
*Type*: String
*Pattern*: `^#[A-F0-9]{6}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
