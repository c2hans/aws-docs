---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-scatterplotconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard ScatterPlotConfiguration
<a name="aws-properties-quicksight-dashboard-scatterplotconfiguration"></a>

The configuration of a scatter plot.

## Syntax
<a name="aws-properties-quicksight-dashboard-scatterplotconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-scatterplotconfiguration-syntax.json"></a>

```
{
  "[DataLabels](#cfn-quicksight-dashboard-scatterplotconfiguration-datalabels)" : {{DataLabelOptions}},
  "[FieldWells](#cfn-quicksight-dashboard-scatterplotconfiguration-fieldwells)" : {{ScatterPlotFieldWells}},
  "[Interactions](#cfn-quicksight-dashboard-scatterplotconfiguration-interactions)" : {{VisualInteractionOptions}},
  "[Legend](#cfn-quicksight-dashboard-scatterplotconfiguration-legend)" : {{LegendOptions}},
  "[SortConfiguration](#cfn-quicksight-dashboard-scatterplotconfiguration-sortconfiguration)" : {{ScatterPlotSortConfiguration}},
  "[Tooltip](#cfn-quicksight-dashboard-scatterplotconfiguration-tooltip)" : {{TooltipOptions}},
  "[VisualPalette](#cfn-quicksight-dashboard-scatterplotconfiguration-visualpalette)" : {{VisualPalette}},
  "[XAxisDisplayOptions](#cfn-quicksight-dashboard-scatterplotconfiguration-xaxisdisplayoptions)" : {{AxisDisplayOptions}},
  "[XAxisLabelOptions](#cfn-quicksight-dashboard-scatterplotconfiguration-xaxislabeloptions)" : {{ChartAxisLabelOptions}},
  "[YAxisDisplayOptions](#cfn-quicksight-dashboard-scatterplotconfiguration-yaxisdisplayoptions)" : {{AxisDisplayOptions}},
  "[YAxisLabelOptions](#cfn-quicksight-dashboard-scatterplotconfiguration-yaxislabeloptions)" : {{ChartAxisLabelOptions}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-scatterplotconfiguration-syntax.yaml"></a>

```
  [DataLabels](#cfn-quicksight-dashboard-scatterplotconfiguration-datalabels): {{
    DataLabelOptions}}
  [FieldWells](#cfn-quicksight-dashboard-scatterplotconfiguration-fieldwells): {{
    ScatterPlotFieldWells}}
  [Interactions](#cfn-quicksight-dashboard-scatterplotconfiguration-interactions): {{
    VisualInteractionOptions}}
  [Legend](#cfn-quicksight-dashboard-scatterplotconfiguration-legend): {{
    LegendOptions}}
  [SortConfiguration](#cfn-quicksight-dashboard-scatterplotconfiguration-sortconfiguration): {{
    ScatterPlotSortConfiguration}}
  [Tooltip](#cfn-quicksight-dashboard-scatterplotconfiguration-tooltip): {{
    TooltipOptions}}
  [VisualPalette](#cfn-quicksight-dashboard-scatterplotconfiguration-visualpalette): {{
    VisualPalette}}
  [XAxisDisplayOptions](#cfn-quicksight-dashboard-scatterplotconfiguration-xaxisdisplayoptions): {{
    AxisDisplayOptions}}
  [XAxisLabelOptions](#cfn-quicksight-dashboard-scatterplotconfiguration-xaxislabeloptions): {{
    ChartAxisLabelOptions}}
  [YAxisDisplayOptions](#cfn-quicksight-dashboard-scatterplotconfiguration-yaxisdisplayoptions): {{
    AxisDisplayOptions}}
  [YAxisLabelOptions](#cfn-quicksight-dashboard-scatterplotconfiguration-yaxislabeloptions): {{
    ChartAxisLabelOptions}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-scatterplotconfiguration-properties"></a>

`DataLabels`  <a name="cfn-quicksight-dashboard-scatterplotconfiguration-datalabels"></a>
The options that determine if visual data labels are displayed.
*Required*: No
*Type*: [DataLabelOptions](aws-properties-quicksight-dashboard-datalabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FieldWells`  <a name="cfn-quicksight-dashboard-scatterplotconfiguration-fieldwells"></a>
The field wells of the visual.
*Required*: No
*Type*: [ScatterPlotFieldWells](aws-properties-quicksight-dashboard-scatterplotfieldwells.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Interactions`  <a name="cfn-quicksight-dashboard-scatterplotconfiguration-interactions"></a>
The general visual interactions setup for a visual.
*Required*: No
*Type*: [VisualInteractionOptions](aws-properties-quicksight-dashboard-visualinteractionoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Legend`  <a name="cfn-quicksight-dashboard-scatterplotconfiguration-legend"></a>
The legend display setup of the visual.
*Required*: No
*Type*: [LegendOptions](aws-properties-quicksight-dashboard-legendoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SortConfiguration`  <a name="cfn-quicksight-dashboard-scatterplotconfiguration-sortconfiguration"></a>
The sort configuration of a scatter plot.
*Required*: No
*Type*: [ScatterPlotSortConfiguration](aws-properties-quicksight-dashboard-scatterplotsortconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tooltip`  <a name="cfn-quicksight-dashboard-scatterplotconfiguration-tooltip"></a>
The legend display setup of the visual.
*Required*: No
*Type*: [TooltipOptions](aws-properties-quicksight-dashboard-tooltipoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VisualPalette`  <a name="cfn-quicksight-dashboard-scatterplotconfiguration-visualpalette"></a>
The palette (chart color) display setup of the visual.
*Required*: No
*Type*: [VisualPalette](aws-properties-quicksight-dashboard-visualpalette.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`XAxisDisplayOptions`  <a name="cfn-quicksight-dashboard-scatterplotconfiguration-xaxisdisplayoptions"></a>
The label display options (grid line, range, scale, and axis step) of the scatter plot's x-axis.
*Required*: No
*Type*: [AxisDisplayOptions](aws-properties-quicksight-dashboard-axisdisplayoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`XAxisLabelOptions`  <a name="cfn-quicksight-dashboard-scatterplotconfiguration-xaxislabeloptions"></a>
The label options (label text, label visibility, and sort icon visibility) of the scatter plot's x-axis.
*Required*: No
*Type*: [ChartAxisLabelOptions](aws-properties-quicksight-dashboard-chartaxislabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`YAxisDisplayOptions`  <a name="cfn-quicksight-dashboard-scatterplotconfiguration-yaxisdisplayoptions"></a>
The label display options (grid line, range, scale, and axis step) of the scatter plot's y-axis.
*Required*: No
*Type*: [AxisDisplayOptions](aws-properties-quicksight-dashboard-axisdisplayoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`YAxisLabelOptions`  <a name="cfn-quicksight-dashboard-scatterplotconfiguration-yaxislabeloptions"></a>
The label options (label text, label visibility, and sort icon visibility) of the scatter plot's y-axis.
*Required*: No
*Type*: [ChartAxisLabelOptions](aws-properties-quicksight-dashboard-chartaxislabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
