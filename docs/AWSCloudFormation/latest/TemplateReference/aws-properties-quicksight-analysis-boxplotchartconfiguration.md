---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-boxplotchartconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis BoxPlotChartConfiguration
<a name="aws-properties-quicksight-analysis-boxplotchartconfiguration"></a>

The configuration of a `BoxPlotVisual`.

## Syntax
<a name="aws-properties-quicksight-analysis-boxplotchartconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-boxplotchartconfiguration-syntax.json"></a>

```
{
  "[BoxPlotOptions](#cfn-quicksight-analysis-boxplotchartconfiguration-boxplotoptions)" : {{BoxPlotOptions}},
  "[CategoryAxis](#cfn-quicksight-analysis-boxplotchartconfiguration-categoryaxis)" : {{AxisDisplayOptions}},
  "[CategoryLabelOptions](#cfn-quicksight-analysis-boxplotchartconfiguration-categorylabeloptions)" : {{ChartAxisLabelOptions}},
  "[FieldWells](#cfn-quicksight-analysis-boxplotchartconfiguration-fieldwells)" : {{BoxPlotFieldWells}},
  "[Interactions](#cfn-quicksight-analysis-boxplotchartconfiguration-interactions)" : {{VisualInteractionOptions}},
  "[Legend](#cfn-quicksight-analysis-boxplotchartconfiguration-legend)" : {{LegendOptions}},
  "[PrimaryYAxisDisplayOptions](#cfn-quicksight-analysis-boxplotchartconfiguration-primaryyaxisdisplayoptions)" : {{AxisDisplayOptions}},
  "[PrimaryYAxisLabelOptions](#cfn-quicksight-analysis-boxplotchartconfiguration-primaryyaxislabeloptions)" : {{ChartAxisLabelOptions}},
  "[ReferenceLines](#cfn-quicksight-analysis-boxplotchartconfiguration-referencelines)" : {{[ ReferenceLine, ... ]}},
  "[SortConfiguration](#cfn-quicksight-analysis-boxplotchartconfiguration-sortconfiguration)" : {{BoxPlotSortConfiguration}},
  "[Tooltip](#cfn-quicksight-analysis-boxplotchartconfiguration-tooltip)" : {{TooltipOptions}},
  "[VisualPalette](#cfn-quicksight-analysis-boxplotchartconfiguration-visualpalette)" : {{VisualPalette}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-boxplotchartconfiguration-syntax.yaml"></a>

```
  [BoxPlotOptions](#cfn-quicksight-analysis-boxplotchartconfiguration-boxplotoptions): {{
    BoxPlotOptions}}
  [CategoryAxis](#cfn-quicksight-analysis-boxplotchartconfiguration-categoryaxis): {{
    AxisDisplayOptions}}
  [CategoryLabelOptions](#cfn-quicksight-analysis-boxplotchartconfiguration-categorylabeloptions): {{
    ChartAxisLabelOptions}}
  [FieldWells](#cfn-quicksight-analysis-boxplotchartconfiguration-fieldwells): {{
    BoxPlotFieldWells}}
  [Interactions](#cfn-quicksight-analysis-boxplotchartconfiguration-interactions): {{
    VisualInteractionOptions}}
  [Legend](#cfn-quicksight-analysis-boxplotchartconfiguration-legend): {{
    LegendOptions}}
  [PrimaryYAxisDisplayOptions](#cfn-quicksight-analysis-boxplotchartconfiguration-primaryyaxisdisplayoptions): {{
    AxisDisplayOptions}}
  [PrimaryYAxisLabelOptions](#cfn-quicksight-analysis-boxplotchartconfiguration-primaryyaxislabeloptions): {{
    ChartAxisLabelOptions}}
  [ReferenceLines](#cfn-quicksight-analysis-boxplotchartconfiguration-referencelines): {{
    - ReferenceLine}}
  [SortConfiguration](#cfn-quicksight-analysis-boxplotchartconfiguration-sortconfiguration): {{
    BoxPlotSortConfiguration}}
  [Tooltip](#cfn-quicksight-analysis-boxplotchartconfiguration-tooltip): {{
    TooltipOptions}}
  [VisualPalette](#cfn-quicksight-analysis-boxplotchartconfiguration-visualpalette): {{
    VisualPalette}}
```

## Properties
<a name="aws-properties-quicksight-analysis-boxplotchartconfiguration-properties"></a>

`BoxPlotOptions`  <a name="cfn-quicksight-analysis-boxplotchartconfiguration-boxplotoptions"></a>
The box plot chart options for a box plot visual
*Required*: No
*Type*: [BoxPlotOptions](aws-properties-quicksight-analysis-boxplotoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CategoryAxis`  <a name="cfn-quicksight-analysis-boxplotchartconfiguration-categoryaxis"></a>
The label display options (grid line, range, scale, axis step) of a box plot category.
*Required*: No
*Type*: [AxisDisplayOptions](aws-properties-quicksight-analysis-axisdisplayoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CategoryLabelOptions`  <a name="cfn-quicksight-analysis-boxplotchartconfiguration-categorylabeloptions"></a>
The label options (label text, label visibility and sort Icon visibility) of a box plot category.
*Required*: No
*Type*: [ChartAxisLabelOptions](aws-properties-quicksight-analysis-chartaxislabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FieldWells`  <a name="cfn-quicksight-analysis-boxplotchartconfiguration-fieldwells"></a>
The field wells of the visual.
*Required*: No
*Type*: [BoxPlotFieldWells](aws-properties-quicksight-analysis-boxplotfieldwells.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Interactions`  <a name="cfn-quicksight-analysis-boxplotchartconfiguration-interactions"></a>
The general visual interactions setup for a visual.
*Required*: No
*Type*: [VisualInteractionOptions](aws-properties-quicksight-analysis-visualinteractionoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Legend`  <a name="cfn-quicksight-analysis-boxplotchartconfiguration-legend"></a>
Property description not available.
*Required*: No
*Type*: [LegendOptions](aws-properties-quicksight-analysis-legendoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrimaryYAxisDisplayOptions`  <a name="cfn-quicksight-analysis-boxplotchartconfiguration-primaryyaxisdisplayoptions"></a>
The label display options (grid line, range, scale, axis step) of a box plot category.
*Required*: No
*Type*: [AxisDisplayOptions](aws-properties-quicksight-analysis-axisdisplayoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrimaryYAxisLabelOptions`  <a name="cfn-quicksight-analysis-boxplotchartconfiguration-primaryyaxislabeloptions"></a>
The label options (label text, label visibility and sort icon visibility) of a box plot value.
*Required*: No
*Type*: [ChartAxisLabelOptions](aws-properties-quicksight-analysis-chartaxislabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReferenceLines`  <a name="cfn-quicksight-analysis-boxplotchartconfiguration-referencelines"></a>
The reference line setup of the visual.
*Required*: No
*Type*: Array of [ReferenceLine](aws-properties-quicksight-analysis-referenceline.md)
*Minimum*: `0`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SortConfiguration`  <a name="cfn-quicksight-analysis-boxplotchartconfiguration-sortconfiguration"></a>
The sort configuration of a `BoxPlotVisual`.
*Required*: No
*Type*: [BoxPlotSortConfiguration](aws-properties-quicksight-analysis-boxplotsortconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tooltip`  <a name="cfn-quicksight-analysis-boxplotchartconfiguration-tooltip"></a>
The tooltip display setup of the visual.
*Required*: No
*Type*: [TooltipOptions](aws-properties-quicksight-analysis-tooltipoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VisualPalette`  <a name="cfn-quicksight-analysis-boxplotchartconfiguration-visualpalette"></a>
The palette (chart color) display setup of the visual.
*Required*: No
*Type*: [VisualPalette](aws-properties-quicksight-analysis-visualpalette.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
