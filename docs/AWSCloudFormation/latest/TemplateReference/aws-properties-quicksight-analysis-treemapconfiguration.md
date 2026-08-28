---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-treemapconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis TreeMapConfiguration
<a name="aws-properties-quicksight-analysis-treemapconfiguration"></a>

The configuration of a tree map.

## Syntax
<a name="aws-properties-quicksight-analysis-treemapconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-treemapconfiguration-syntax.json"></a>

```
{
  "[ColorLabelOptions](#cfn-quicksight-analysis-treemapconfiguration-colorlabeloptions)" : {{ChartAxisLabelOptions}},
  "[ColorScale](#cfn-quicksight-analysis-treemapconfiguration-colorscale)" : {{ColorScale}},
  "[DataLabels](#cfn-quicksight-analysis-treemapconfiguration-datalabels)" : {{DataLabelOptions}},
  "[FieldWells](#cfn-quicksight-analysis-treemapconfiguration-fieldwells)" : {{TreeMapFieldWells}},
  "[GroupLabelOptions](#cfn-quicksight-analysis-treemapconfiguration-grouplabeloptions)" : {{ChartAxisLabelOptions}},
  "[Interactions](#cfn-quicksight-analysis-treemapconfiguration-interactions)" : {{VisualInteractionOptions}},
  "[Legend](#cfn-quicksight-analysis-treemapconfiguration-legend)" : {{LegendOptions}},
  "[SizeLabelOptions](#cfn-quicksight-analysis-treemapconfiguration-sizelabeloptions)" : {{ChartAxisLabelOptions}},
  "[SortConfiguration](#cfn-quicksight-analysis-treemapconfiguration-sortconfiguration)" : {{TreeMapSortConfiguration}},
  "[Tooltip](#cfn-quicksight-analysis-treemapconfiguration-tooltip)" : {{TooltipOptions}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-treemapconfiguration-syntax.yaml"></a>

```
  [ColorLabelOptions](#cfn-quicksight-analysis-treemapconfiguration-colorlabeloptions): {{
    ChartAxisLabelOptions}}
  [ColorScale](#cfn-quicksight-analysis-treemapconfiguration-colorscale): {{
    ColorScale}}
  [DataLabels](#cfn-quicksight-analysis-treemapconfiguration-datalabels): {{
    DataLabelOptions}}
  [FieldWells](#cfn-quicksight-analysis-treemapconfiguration-fieldwells): {{
    TreeMapFieldWells}}
  [GroupLabelOptions](#cfn-quicksight-analysis-treemapconfiguration-grouplabeloptions): {{
    ChartAxisLabelOptions}}
  [Interactions](#cfn-quicksight-analysis-treemapconfiguration-interactions): {{
    VisualInteractionOptions}}
  [Legend](#cfn-quicksight-analysis-treemapconfiguration-legend): {{
    LegendOptions}}
  [SizeLabelOptions](#cfn-quicksight-analysis-treemapconfiguration-sizelabeloptions): {{
    ChartAxisLabelOptions}}
  [SortConfiguration](#cfn-quicksight-analysis-treemapconfiguration-sortconfiguration): {{
    TreeMapSortConfiguration}}
  [Tooltip](#cfn-quicksight-analysis-treemapconfiguration-tooltip): {{
    TooltipOptions}}
```

## Properties
<a name="aws-properties-quicksight-analysis-treemapconfiguration-properties"></a>

`ColorLabelOptions`  <a name="cfn-quicksight-analysis-treemapconfiguration-colorlabeloptions"></a>
The label options (label text, label visibility) for the colors displayed in a tree map.
*Required*: No
*Type*: [ChartAxisLabelOptions](aws-properties-quicksight-analysis-chartaxislabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ColorScale`  <a name="cfn-quicksight-analysis-treemapconfiguration-colorscale"></a>
The color options (gradient color, point of divergence) of a tree map.
*Required*: No
*Type*: [ColorScale](aws-properties-quicksight-analysis-colorscale.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataLabels`  <a name="cfn-quicksight-analysis-treemapconfiguration-datalabels"></a>
The options that determine if visual data labels are displayed.
*Required*: No
*Type*: [DataLabelOptions](aws-properties-quicksight-analysis-datalabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FieldWells`  <a name="cfn-quicksight-analysis-treemapconfiguration-fieldwells"></a>
The field wells of the visual.
*Required*: No
*Type*: [TreeMapFieldWells](aws-properties-quicksight-analysis-treemapfieldwells.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GroupLabelOptions`  <a name="cfn-quicksight-analysis-treemapconfiguration-grouplabeloptions"></a>
The label options (label text, label visibility) of the groups that are displayed in a tree map.
*Required*: No
*Type*: [ChartAxisLabelOptions](aws-properties-quicksight-analysis-chartaxislabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Interactions`  <a name="cfn-quicksight-analysis-treemapconfiguration-interactions"></a>
The general visual interactions setup for a visual.
*Required*: No
*Type*: [VisualInteractionOptions](aws-properties-quicksight-analysis-visualinteractionoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Legend`  <a name="cfn-quicksight-analysis-treemapconfiguration-legend"></a>
The legend display setup of the visual.
*Required*: No
*Type*: [LegendOptions](aws-properties-quicksight-analysis-legendoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SizeLabelOptions`  <a name="cfn-quicksight-analysis-treemapconfiguration-sizelabeloptions"></a>
The label options (label text, label visibility) of the sizes that are displayed in a tree map.
*Required*: No
*Type*: [ChartAxisLabelOptions](aws-properties-quicksight-analysis-chartaxislabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SortConfiguration`  <a name="cfn-quicksight-analysis-treemapconfiguration-sortconfiguration"></a>
The sort configuration of a tree map.
*Required*: No
*Type*: [TreeMapSortConfiguration](aws-properties-quicksight-analysis-treemapsortconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tooltip`  <a name="cfn-quicksight-analysis-treemapconfiguration-tooltip"></a>
The tooltip display setup of the visual.
*Required*: No
*Type*: [TooltipOptions](aws-properties-quicksight-analysis-tooltipoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
