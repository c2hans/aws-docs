---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-gaugechartconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template GaugeChartConfiguration
<a name="aws-properties-quicksight-template-gaugechartconfiguration"></a>

The configuration of a `GaugeChartVisual`.

## Syntax
<a name="aws-properties-quicksight-template-gaugechartconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-gaugechartconfiguration-syntax.json"></a>

```
{
  "[ColorConfiguration](#cfn-quicksight-template-gaugechartconfiguration-colorconfiguration)" : {{GaugeChartColorConfiguration}},
  "[DataLabels](#cfn-quicksight-template-gaugechartconfiguration-datalabels)" : {{DataLabelOptions}},
  "[FieldWells](#cfn-quicksight-template-gaugechartconfiguration-fieldwells)" : {{GaugeChartFieldWells}},
  "[GaugeChartOptions](#cfn-quicksight-template-gaugechartconfiguration-gaugechartoptions)" : {{GaugeChartOptions}},
  "[Interactions](#cfn-quicksight-template-gaugechartconfiguration-interactions)" : {{VisualInteractionOptions}},
  "[TooltipOptions](#cfn-quicksight-template-gaugechartconfiguration-tooltipoptions)" : {{TooltipOptions}},
  "[VisualPalette](#cfn-quicksight-template-gaugechartconfiguration-visualpalette)" : {{VisualPalette}}
}
```

### YAML
<a name="aws-properties-quicksight-template-gaugechartconfiguration-syntax.yaml"></a>

```
  [ColorConfiguration](#cfn-quicksight-template-gaugechartconfiguration-colorconfiguration): {{
    GaugeChartColorConfiguration}}
  [DataLabels](#cfn-quicksight-template-gaugechartconfiguration-datalabels): {{
    DataLabelOptions}}
  [FieldWells](#cfn-quicksight-template-gaugechartconfiguration-fieldwells): {{
    GaugeChartFieldWells}}
  [GaugeChartOptions](#cfn-quicksight-template-gaugechartconfiguration-gaugechartoptions): {{
    GaugeChartOptions}}
  [Interactions](#cfn-quicksight-template-gaugechartconfiguration-interactions): {{
    VisualInteractionOptions}}
  [TooltipOptions](#cfn-quicksight-template-gaugechartconfiguration-tooltipoptions): {{
    TooltipOptions}}
  [VisualPalette](#cfn-quicksight-template-gaugechartconfiguration-visualpalette): {{
    VisualPalette}}
```

## Properties
<a name="aws-properties-quicksight-template-gaugechartconfiguration-properties"></a>

`ColorConfiguration`  <a name="cfn-quicksight-template-gaugechartconfiguration-colorconfiguration"></a>
The color configuration of a `GaugeChartVisual`.
*Required*: No
*Type*: [GaugeChartColorConfiguration](aws-properties-quicksight-template-gaugechartcolorconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataLabels`  <a name="cfn-quicksight-template-gaugechartconfiguration-datalabels"></a>
The data label configuration of a `GaugeChartVisual`.
*Required*: No
*Type*: [DataLabelOptions](aws-properties-quicksight-template-datalabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FieldWells`  <a name="cfn-quicksight-template-gaugechartconfiguration-fieldwells"></a>
The field well configuration of a `GaugeChartVisual`.
*Required*: No
*Type*: [GaugeChartFieldWells](aws-properties-quicksight-template-gaugechartfieldwells.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GaugeChartOptions`  <a name="cfn-quicksight-template-gaugechartconfiguration-gaugechartoptions"></a>
The options that determine the presentation of the `GaugeChartVisual`.
*Required*: No
*Type*: [GaugeChartOptions](aws-properties-quicksight-template-gaugechartoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Interactions`  <a name="cfn-quicksight-template-gaugechartconfiguration-interactions"></a>
The general visual interactions setup for a visual.
*Required*: No
*Type*: [VisualInteractionOptions](aws-properties-quicksight-template-visualinteractionoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TooltipOptions`  <a name="cfn-quicksight-template-gaugechartconfiguration-tooltipoptions"></a>
The tooltip configuration of a `GaugeChartVisual`.
*Required*: No
*Type*: [TooltipOptions](aws-properties-quicksight-template-tooltipoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VisualPalette`  <a name="cfn-quicksight-template-gaugechartconfiguration-visualpalette"></a>
The visual palette configuration of a `GaugeChartVisual`.
*Required*: No
*Type*: [VisualPalette](aws-properties-quicksight-template-visualpalette.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
