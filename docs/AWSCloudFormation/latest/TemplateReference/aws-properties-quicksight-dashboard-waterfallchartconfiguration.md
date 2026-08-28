---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-waterfallchartconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard WaterfallChartConfiguration
<a name="aws-properties-quicksight-dashboard-waterfallchartconfiguration"></a>

The configuration for a waterfall visual.

## Syntax
<a name="aws-properties-quicksight-dashboard-waterfallchartconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-waterfallchartconfiguration-syntax.json"></a>

```
{
  "[CategoryAxisDisplayOptions](#cfn-quicksight-dashboard-waterfallchartconfiguration-categoryaxisdisplayoptions)" : {{AxisDisplayOptions}},
  "[CategoryAxisLabelOptions](#cfn-quicksight-dashboard-waterfallchartconfiguration-categoryaxislabeloptions)" : {{ChartAxisLabelOptions}},
  "[ColorConfiguration](#cfn-quicksight-dashboard-waterfallchartconfiguration-colorconfiguration)" : {{WaterfallChartColorConfiguration}},
  "[DataLabels](#cfn-quicksight-dashboard-waterfallchartconfiguration-datalabels)" : {{DataLabelOptions}},
  "[FieldWells](#cfn-quicksight-dashboard-waterfallchartconfiguration-fieldwells)" : {{WaterfallChartFieldWells}},
  "[Interactions](#cfn-quicksight-dashboard-waterfallchartconfiguration-interactions)" : {{VisualInteractionOptions}},
  "[Legend](#cfn-quicksight-dashboard-waterfallchartconfiguration-legend)" : {{LegendOptions}},
  "[PrimaryYAxisDisplayOptions](#cfn-quicksight-dashboard-waterfallchartconfiguration-primaryyaxisdisplayoptions)" : {{AxisDisplayOptions}},
  "[PrimaryYAxisLabelOptions](#cfn-quicksight-dashboard-waterfallchartconfiguration-primaryyaxislabeloptions)" : {{ChartAxisLabelOptions}},
  "[SortConfiguration](#cfn-quicksight-dashboard-waterfallchartconfiguration-sortconfiguration)" : {{WaterfallChartSortConfiguration}},
  "[VisualPalette](#cfn-quicksight-dashboard-waterfallchartconfiguration-visualpalette)" : {{VisualPalette}},
  "[WaterfallChartOptions](#cfn-quicksight-dashboard-waterfallchartconfiguration-waterfallchartoptions)" : {{WaterfallChartOptions}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-waterfallchartconfiguration-syntax.yaml"></a>

```
  [CategoryAxisDisplayOptions](#cfn-quicksight-dashboard-waterfallchartconfiguration-categoryaxisdisplayoptions): {{
    AxisDisplayOptions}}
  [CategoryAxisLabelOptions](#cfn-quicksight-dashboard-waterfallchartconfiguration-categoryaxislabeloptions): {{
    ChartAxisLabelOptions}}
  [ColorConfiguration](#cfn-quicksight-dashboard-waterfallchartconfiguration-colorconfiguration): {{
    WaterfallChartColorConfiguration}}
  [DataLabels](#cfn-quicksight-dashboard-waterfallchartconfiguration-datalabels): {{
    DataLabelOptions}}
  [FieldWells](#cfn-quicksight-dashboard-waterfallchartconfiguration-fieldwells): {{
    WaterfallChartFieldWells}}
  [Interactions](#cfn-quicksight-dashboard-waterfallchartconfiguration-interactions): {{
    VisualInteractionOptions}}
  [Legend](#cfn-quicksight-dashboard-waterfallchartconfiguration-legend): {{
    LegendOptions}}
  [PrimaryYAxisDisplayOptions](#cfn-quicksight-dashboard-waterfallchartconfiguration-primaryyaxisdisplayoptions): {{
    AxisDisplayOptions}}
  [PrimaryYAxisLabelOptions](#cfn-quicksight-dashboard-waterfallchartconfiguration-primaryyaxislabeloptions): {{
    ChartAxisLabelOptions}}
  [SortConfiguration](#cfn-quicksight-dashboard-waterfallchartconfiguration-sortconfiguration): {{
    WaterfallChartSortConfiguration}}
  [VisualPalette](#cfn-quicksight-dashboard-waterfallchartconfiguration-visualpalette): {{
    VisualPalette}}
  [WaterfallChartOptions](#cfn-quicksight-dashboard-waterfallchartconfiguration-waterfallchartoptions): {{
    WaterfallChartOptions}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-waterfallchartconfiguration-properties"></a>

`CategoryAxisDisplayOptions`  <a name="cfn-quicksight-dashboard-waterfallchartconfiguration-categoryaxisdisplayoptions"></a>
The options that determine the presentation of the category axis.
*Required*: No
*Type*: [AxisDisplayOptions](aws-properties-quicksight-dashboard-axisdisplayoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CategoryAxisLabelOptions`  <a name="cfn-quicksight-dashboard-waterfallchartconfiguration-categoryaxislabeloptions"></a>
The options that determine the presentation of the category axis label.
*Required*: No
*Type*: [ChartAxisLabelOptions](aws-properties-quicksight-dashboard-chartaxislabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ColorConfiguration`  <a name="cfn-quicksight-dashboard-waterfallchartconfiguration-colorconfiguration"></a>
The color configuration of a waterfall visual.
*Required*: No
*Type*: [WaterfallChartColorConfiguration](aws-properties-quicksight-dashboard-waterfallchartcolorconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataLabels`  <a name="cfn-quicksight-dashboard-waterfallchartconfiguration-datalabels"></a>
The data label configuration of a waterfall visual.
*Required*: No
*Type*: [DataLabelOptions](aws-properties-quicksight-dashboard-datalabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FieldWells`  <a name="cfn-quicksight-dashboard-waterfallchartconfiguration-fieldwells"></a>
The field well configuration of a waterfall visual.
*Required*: No
*Type*: [WaterfallChartFieldWells](aws-properties-quicksight-dashboard-waterfallchartfieldwells.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Interactions`  <a name="cfn-quicksight-dashboard-waterfallchartconfiguration-interactions"></a>
The general visual interactions setup for a visual.
*Required*: No
*Type*: [VisualInteractionOptions](aws-properties-quicksight-dashboard-visualinteractionoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Legend`  <a name="cfn-quicksight-dashboard-waterfallchartconfiguration-legend"></a>
The legend configuration of a waterfall visual.
*Required*: No
*Type*: [LegendOptions](aws-properties-quicksight-dashboard-legendoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrimaryYAxisDisplayOptions`  <a name="cfn-quicksight-dashboard-waterfallchartconfiguration-primaryyaxisdisplayoptions"></a>
The options that determine the presentation of the y-axis.
*Required*: No
*Type*: [AxisDisplayOptions](aws-properties-quicksight-dashboard-axisdisplayoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrimaryYAxisLabelOptions`  <a name="cfn-quicksight-dashboard-waterfallchartconfiguration-primaryyaxislabeloptions"></a>
The options that determine the presentation of the y-axis label.
*Required*: No
*Type*: [ChartAxisLabelOptions](aws-properties-quicksight-dashboard-chartaxislabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SortConfiguration`  <a name="cfn-quicksight-dashboard-waterfallchartconfiguration-sortconfiguration"></a>
The sort configuration of a waterfall visual.
*Required*: No
*Type*: [WaterfallChartSortConfiguration](aws-properties-quicksight-dashboard-waterfallchartsortconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VisualPalette`  <a name="cfn-quicksight-dashboard-waterfallchartconfiguration-visualpalette"></a>
The visual palette configuration of a waterfall visual.
*Required*: No
*Type*: [VisualPalette](aws-properties-quicksight-dashboard-visualpalette.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WaterfallChartOptions`  <a name="cfn-quicksight-dashboard-waterfallchartconfiguration-waterfallchartoptions"></a>
The options that determine the presentation of a waterfall visual.
*Required*: No
*Type*: [WaterfallChartOptions](aws-properties-quicksight-dashboard-waterfallchartoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
