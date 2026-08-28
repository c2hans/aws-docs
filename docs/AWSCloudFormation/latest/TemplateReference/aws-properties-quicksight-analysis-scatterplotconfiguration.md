---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-scatterplotconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis ScatterPlotConfiguration
<a name="aws-properties-quicksight-analysis-scatterplotconfiguration"></a>

The configuration of a scatter plot.

## Syntax
<a name="aws-properties-quicksight-analysis-scatterplotconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-scatterplotconfiguration-syntax.json"></a>

```
{
  "[DataLabels](#cfn-quicksight-analysis-scatterplotconfiguration-datalabels)" : {{DataLabelOptions}},
  "[FieldWells](#cfn-quicksight-analysis-scatterplotconfiguration-fieldwells)" : {{ScatterPlotFieldWells}},
  "[Interactions](#cfn-quicksight-analysis-scatterplotconfiguration-interactions)" : {{VisualInteractionOptions}},
  "[Legend](#cfn-quicksight-analysis-scatterplotconfiguration-legend)" : {{LegendOptions}},
  "[SortConfiguration](#cfn-quicksight-analysis-scatterplotconfiguration-sortconfiguration)" : {{ScatterPlotSortConfiguration}},
  "[Tooltip](#cfn-quicksight-analysis-scatterplotconfiguration-tooltip)" : {{TooltipOptions}},
  "[VisualPalette](#cfn-quicksight-analysis-scatterplotconfiguration-visualpalette)" : {{VisualPalette}},
  "[XAxisDisplayOptions](#cfn-quicksight-analysis-scatterplotconfiguration-xaxisdisplayoptions)" : {{AxisDisplayOptions}},
  "[XAxisLabelOptions](#cfn-quicksight-analysis-scatterplotconfiguration-xaxislabeloptions)" : {{ChartAxisLabelOptions}},
  "[YAxisDisplayOptions](#cfn-quicksight-analysis-scatterplotconfiguration-yaxisdisplayoptions)" : {{AxisDisplayOptions}},
  "[YAxisLabelOptions](#cfn-quicksight-analysis-scatterplotconfiguration-yaxislabeloptions)" : {{ChartAxisLabelOptions}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-scatterplotconfiguration-syntax.yaml"></a>

```
  [DataLabels](#cfn-quicksight-analysis-scatterplotconfiguration-datalabels): {{
    DataLabelOptions}}
  [FieldWells](#cfn-quicksight-analysis-scatterplotconfiguration-fieldwells): {{
    ScatterPlotFieldWells}}
  [Interactions](#cfn-quicksight-analysis-scatterplotconfiguration-interactions): {{
    VisualInteractionOptions}}
  [Legend](#cfn-quicksight-analysis-scatterplotconfiguration-legend): {{
    LegendOptions}}
  [SortConfiguration](#cfn-quicksight-analysis-scatterplotconfiguration-sortconfiguration): {{
    ScatterPlotSortConfiguration}}
  [Tooltip](#cfn-quicksight-analysis-scatterplotconfiguration-tooltip): {{
    TooltipOptions}}
  [VisualPalette](#cfn-quicksight-analysis-scatterplotconfiguration-visualpalette): {{
    VisualPalette}}
  [XAxisDisplayOptions](#cfn-quicksight-analysis-scatterplotconfiguration-xaxisdisplayoptions): {{
    AxisDisplayOptions}}
  [XAxisLabelOptions](#cfn-quicksight-analysis-scatterplotconfiguration-xaxislabeloptions): {{
    ChartAxisLabelOptions}}
  [YAxisDisplayOptions](#cfn-quicksight-analysis-scatterplotconfiguration-yaxisdisplayoptions): {{
    AxisDisplayOptions}}
  [YAxisLabelOptions](#cfn-quicksight-analysis-scatterplotconfiguration-yaxislabeloptions): {{
    ChartAxisLabelOptions}}
```

## Properties
<a name="aws-properties-quicksight-analysis-scatterplotconfiguration-properties"></a>

`DataLabels`  <a name="cfn-quicksight-analysis-scatterplotconfiguration-datalabels"></a>
The options that determine if visual data labels are displayed.
*Required*: No
*Type*: [DataLabelOptions](aws-properties-quicksight-analysis-datalabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FieldWells`  <a name="cfn-quicksight-analysis-scatterplotconfiguration-fieldwells"></a>
The field wells of the visual.
*Required*: No
*Type*: [ScatterPlotFieldWells](aws-properties-quicksight-analysis-scatterplotfieldwells.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Interactions`  <a name="cfn-quicksight-analysis-scatterplotconfiguration-interactions"></a>
The general visual interactions setup for a visual.
*Required*: No
*Type*: [VisualInteractionOptions](aws-properties-quicksight-analysis-visualinteractionoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Legend`  <a name="cfn-quicksight-analysis-scatterplotconfiguration-legend"></a>
The legend display setup of the visual.
*Required*: No
*Type*: [LegendOptions](aws-properties-quicksight-analysis-legendoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SortConfiguration`  <a name="cfn-quicksight-analysis-scatterplotconfiguration-sortconfiguration"></a>
The sort configuration of a scatter plot.
*Required*: No
*Type*: [ScatterPlotSortConfiguration](aws-properties-quicksight-analysis-scatterplotsortconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tooltip`  <a name="cfn-quicksight-analysis-scatterplotconfiguration-tooltip"></a>
The legend display setup of the visual.
*Required*: No
*Type*: [TooltipOptions](aws-properties-quicksight-analysis-tooltipoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VisualPalette`  <a name="cfn-quicksight-analysis-scatterplotconfiguration-visualpalette"></a>
The palette (chart color) display setup of the visual.
*Required*: No
*Type*: [VisualPalette](aws-properties-quicksight-analysis-visualpalette.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`XAxisDisplayOptions`  <a name="cfn-quicksight-analysis-scatterplotconfiguration-xaxisdisplayoptions"></a>
The label display options (grid line, range, scale, and axis step) of the scatter plot's x-axis.
*Required*: No
*Type*: [AxisDisplayOptions](aws-properties-quicksight-analysis-axisdisplayoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`XAxisLabelOptions`  <a name="cfn-quicksight-analysis-scatterplotconfiguration-xaxislabeloptions"></a>
The label options (label text, label visibility, and sort icon visibility) of the scatter plot's x-axis.
*Required*: No
*Type*: [ChartAxisLabelOptions](aws-properties-quicksight-analysis-chartaxislabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`YAxisDisplayOptions`  <a name="cfn-quicksight-analysis-scatterplotconfiguration-yaxisdisplayoptions"></a>
The label display options (grid line, range, scale, and axis step) of the scatter plot's y-axis.
*Required*: No
*Type*: [AxisDisplayOptions](aws-properties-quicksight-analysis-axisdisplayoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`YAxisLabelOptions`  <a name="cfn-quicksight-analysis-scatterplotconfiguration-yaxislabeloptions"></a>
The label options (label text, label visibility, and sort icon visibility) of the scatter plot's y-axis.
*Required*: No
*Type*: [ChartAxisLabelOptions](aws-properties-quicksight-analysis-chartaxislabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
