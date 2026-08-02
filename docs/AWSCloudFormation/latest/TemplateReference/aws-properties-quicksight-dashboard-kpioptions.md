---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-kpioptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard KPIOptions
<a name="aws-properties-quicksight-dashboard-kpioptions"></a>

The options that determine the presentation of a KPI visual.

## Syntax
<a name="aws-properties-quicksight-dashboard-kpioptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-kpioptions-syntax.json"></a>

```
{
  "[Comparison](#cfn-quicksight-dashboard-kpioptions-comparison)" : {{ComparisonConfiguration}},
  "[PrimaryValueDisplayType](#cfn-quicksight-dashboard-kpioptions-primaryvaluedisplaytype)" : {{String}},
  "[PrimaryValueFontConfiguration](#cfn-quicksight-dashboard-kpioptions-primaryvaluefontconfiguration)" : {{FontConfiguration}},
  "[ProgressBar](#cfn-quicksight-dashboard-kpioptions-progressbar)" : {{ProgressBarOptions}},
  "[SecondaryValue](#cfn-quicksight-dashboard-kpioptions-secondaryvalue)" : {{SecondaryValueOptions}},
  "[SecondaryValueFontConfiguration](#cfn-quicksight-dashboard-kpioptions-secondaryvaluefontconfiguration)" : {{FontConfiguration}},
  "[Sparkline](#cfn-quicksight-dashboard-kpioptions-sparkline)" : {{KPISparklineOptions}},
  "[TrendArrows](#cfn-quicksight-dashboard-kpioptions-trendarrows)" : {{TrendArrowOptions}},
  "[VisualLayoutOptions](#cfn-quicksight-dashboard-kpioptions-visuallayoutoptions)" : {{KPIVisualLayoutOptions}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-kpioptions-syntax.yaml"></a>

```
  [Comparison](#cfn-quicksight-dashboard-kpioptions-comparison): {{
    ComparisonConfiguration}}
  [PrimaryValueDisplayType](#cfn-quicksight-dashboard-kpioptions-primaryvaluedisplaytype): {{String}}
  [PrimaryValueFontConfiguration](#cfn-quicksight-dashboard-kpioptions-primaryvaluefontconfiguration): {{
    FontConfiguration}}
  [ProgressBar](#cfn-quicksight-dashboard-kpioptions-progressbar): {{
    ProgressBarOptions}}
  [SecondaryValue](#cfn-quicksight-dashboard-kpioptions-secondaryvalue): {{
    SecondaryValueOptions}}
  [SecondaryValueFontConfiguration](#cfn-quicksight-dashboard-kpioptions-secondaryvaluefontconfiguration): {{
    FontConfiguration}}
  [Sparkline](#cfn-quicksight-dashboard-kpioptions-sparkline): {{
    KPISparklineOptions}}
  [TrendArrows](#cfn-quicksight-dashboard-kpioptions-trendarrows): {{
    TrendArrowOptions}}
  [VisualLayoutOptions](#cfn-quicksight-dashboard-kpioptions-visuallayoutoptions): {{
    KPIVisualLayoutOptions}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-kpioptions-properties"></a>

`Comparison`  <a name="cfn-quicksight-dashboard-kpioptions-comparison"></a>
The comparison configuration of a KPI visual.
*Required*: No
*Type*: [ComparisonConfiguration](aws-properties-quicksight-dashboard-comparisonconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrimaryValueDisplayType`  <a name="cfn-quicksight-dashboard-kpioptions-primaryvaluedisplaytype"></a>
The options that determine the primary value display type.
*Required*: No
*Type*: String
*Allowed values*: `HIDDEN | COMPARISON | ACTUAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrimaryValueFontConfiguration`  <a name="cfn-quicksight-dashboard-kpioptions-primaryvaluefontconfiguration"></a>
The options that determine the primary value font configuration.
*Required*: No
*Type*: [FontConfiguration](aws-properties-quicksight-dashboard-fontconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProgressBar`  <a name="cfn-quicksight-dashboard-kpioptions-progressbar"></a>
The options that determine the presentation of the progress bar of a KPI visual.
*Required*: No
*Type*: [ProgressBarOptions](aws-properties-quicksight-dashboard-progressbaroptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecondaryValue`  <a name="cfn-quicksight-dashboard-kpioptions-secondaryvalue"></a>
The options that determine the presentation of the secondary value of a KPI visual.
*Required*: No
*Type*: [SecondaryValueOptions](aws-properties-quicksight-dashboard-secondaryvalueoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecondaryValueFontConfiguration`  <a name="cfn-quicksight-dashboard-kpioptions-secondaryvaluefontconfiguration"></a>
The options that determine the secondary value font configuration.
*Required*: No
*Type*: [FontConfiguration](aws-properties-quicksight-dashboard-fontconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Sparkline`  <a name="cfn-quicksight-dashboard-kpioptions-sparkline"></a>
The options that determine the visibility, color, type, and tooltip visibility of the sparkline of a KPI visual.
*Required*: No
*Type*: [KPISparklineOptions](aws-properties-quicksight-dashboard-kpisparklineoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TrendArrows`  <a name="cfn-quicksight-dashboard-kpioptions-trendarrows"></a>
The options that determine the presentation of trend arrows in a KPI visual.
*Required*: No
*Type*: [TrendArrowOptions](aws-properties-quicksight-dashboard-trendarrowoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VisualLayoutOptions`  <a name="cfn-quicksight-dashboard-kpioptions-visuallayoutoptions"></a>
The options that determine the layout a KPI visual.
*Required*: No
*Type*: [KPIVisualLayoutOptions](aws-properties-quicksight-dashboard-kpivisuallayoutoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
