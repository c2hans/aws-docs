---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-heatmapconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis HeatMapConfiguration
<a name="aws-properties-quicksight-analysis-heatmapconfiguration"></a>

The configuration of a heat map.

## Syntax
<a name="aws-properties-quicksight-analysis-heatmapconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-heatmapconfiguration-syntax.json"></a>

```
{
  "[ColorScale](#cfn-quicksight-analysis-heatmapconfiguration-colorscale)" : {{ColorScale}},
  "[ColumnLabelOptions](#cfn-quicksight-analysis-heatmapconfiguration-columnlabeloptions)" : {{ChartAxisLabelOptions}},
  "[DataLabels](#cfn-quicksight-analysis-heatmapconfiguration-datalabels)" : {{DataLabelOptions}},
  "[FieldWells](#cfn-quicksight-analysis-heatmapconfiguration-fieldwells)" : {{HeatMapFieldWells}},
  "[Interactions](#cfn-quicksight-analysis-heatmapconfiguration-interactions)" : {{VisualInteractionOptions}},
  "[Legend](#cfn-quicksight-analysis-heatmapconfiguration-legend)" : {{LegendOptions}},
  "[RowLabelOptions](#cfn-quicksight-analysis-heatmapconfiguration-rowlabeloptions)" : {{ChartAxisLabelOptions}},
  "[SortConfiguration](#cfn-quicksight-analysis-heatmapconfiguration-sortconfiguration)" : {{HeatMapSortConfiguration}},
  "[Tooltip](#cfn-quicksight-analysis-heatmapconfiguration-tooltip)" : {{TooltipOptions}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-heatmapconfiguration-syntax.yaml"></a>

```
  [ColorScale](#cfn-quicksight-analysis-heatmapconfiguration-colorscale): {{
    ColorScale}}
  [ColumnLabelOptions](#cfn-quicksight-analysis-heatmapconfiguration-columnlabeloptions): {{
    ChartAxisLabelOptions}}
  [DataLabels](#cfn-quicksight-analysis-heatmapconfiguration-datalabels): {{
    DataLabelOptions}}
  [FieldWells](#cfn-quicksight-analysis-heatmapconfiguration-fieldwells): {{
    HeatMapFieldWells}}
  [Interactions](#cfn-quicksight-analysis-heatmapconfiguration-interactions): {{
    VisualInteractionOptions}}
  [Legend](#cfn-quicksight-analysis-heatmapconfiguration-legend): {{
    LegendOptions}}
  [RowLabelOptions](#cfn-quicksight-analysis-heatmapconfiguration-rowlabeloptions): {{
    ChartAxisLabelOptions}}
  [SortConfiguration](#cfn-quicksight-analysis-heatmapconfiguration-sortconfiguration): {{
    HeatMapSortConfiguration}}
  [Tooltip](#cfn-quicksight-analysis-heatmapconfiguration-tooltip): {{
    TooltipOptions}}
```

## Properties
<a name="aws-properties-quicksight-analysis-heatmapconfiguration-properties"></a>

`ColorScale`  <a name="cfn-quicksight-analysis-heatmapconfiguration-colorscale"></a>
The color options (gradient color, point of divergence) in a heat map.
*Required*: No
*Type*: [ColorScale](aws-properties-quicksight-analysis-colorscale.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ColumnLabelOptions`  <a name="cfn-quicksight-analysis-heatmapconfiguration-columnlabeloptions"></a>
The label options of the column that is displayed in a heat map.
*Required*: No
*Type*: [ChartAxisLabelOptions](aws-properties-quicksight-analysis-chartaxislabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataLabels`  <a name="cfn-quicksight-analysis-heatmapconfiguration-datalabels"></a>
The options that determine if visual data labels are displayed.
*Required*: No
*Type*: [DataLabelOptions](aws-properties-quicksight-analysis-datalabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FieldWells`  <a name="cfn-quicksight-analysis-heatmapconfiguration-fieldwells"></a>
The field wells of the visual.
*Required*: No
*Type*: [HeatMapFieldWells](aws-properties-quicksight-analysis-heatmapfieldwells.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Interactions`  <a name="cfn-quicksight-analysis-heatmapconfiguration-interactions"></a>
The general visual interactions setup for a visual.
*Required*: No
*Type*: [VisualInteractionOptions](aws-properties-quicksight-analysis-visualinteractionoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Legend`  <a name="cfn-quicksight-analysis-heatmapconfiguration-legend"></a>
The legend display setup of the visual.
*Required*: No
*Type*: [LegendOptions](aws-properties-quicksight-analysis-legendoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RowLabelOptions`  <a name="cfn-quicksight-analysis-heatmapconfiguration-rowlabeloptions"></a>
The label options of the row that is displayed in a `heat map`.
*Required*: No
*Type*: [ChartAxisLabelOptions](aws-properties-quicksight-analysis-chartaxislabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SortConfiguration`  <a name="cfn-quicksight-analysis-heatmapconfiguration-sortconfiguration"></a>
The sort configuration of a heat map.
*Required*: No
*Type*: [HeatMapSortConfiguration](aws-properties-quicksight-analysis-heatmapsortconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tooltip`  <a name="cfn-quicksight-analysis-heatmapconfiguration-tooltip"></a>
The tooltip display setup of the visual.
*Required*: No
*Type*: [TooltipOptions](aws-properties-quicksight-analysis-tooltipoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
