---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-wordcloudchartconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard WordCloudChartConfiguration
<a name="aws-properties-quicksight-dashboard-wordcloudchartconfiguration"></a>

The configuration of a word cloud visual.

## Syntax
<a name="aws-properties-quicksight-dashboard-wordcloudchartconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-wordcloudchartconfiguration-syntax.json"></a>

```
{
  "[CategoryLabelOptions](#cfn-quicksight-dashboard-wordcloudchartconfiguration-categorylabeloptions)" : {{ChartAxisLabelOptions}},
  "[FieldWells](#cfn-quicksight-dashboard-wordcloudchartconfiguration-fieldwells)" : {{WordCloudFieldWells}},
  "[Interactions](#cfn-quicksight-dashboard-wordcloudchartconfiguration-interactions)" : {{VisualInteractionOptions}},
  "[SortConfiguration](#cfn-quicksight-dashboard-wordcloudchartconfiguration-sortconfiguration)" : {{WordCloudSortConfiguration}},
  "[WordCloudOptions](#cfn-quicksight-dashboard-wordcloudchartconfiguration-wordcloudoptions)" : {{WordCloudOptions}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-wordcloudchartconfiguration-syntax.yaml"></a>

```
  [CategoryLabelOptions](#cfn-quicksight-dashboard-wordcloudchartconfiguration-categorylabeloptions): {{
    ChartAxisLabelOptions}}
  [FieldWells](#cfn-quicksight-dashboard-wordcloudchartconfiguration-fieldwells): {{
    WordCloudFieldWells}}
  [Interactions](#cfn-quicksight-dashboard-wordcloudchartconfiguration-interactions): {{
    VisualInteractionOptions}}
  [SortConfiguration](#cfn-quicksight-dashboard-wordcloudchartconfiguration-sortconfiguration): {{
    WordCloudSortConfiguration}}
  [WordCloudOptions](#cfn-quicksight-dashboard-wordcloudchartconfiguration-wordcloudoptions): {{
    WordCloudOptions}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-wordcloudchartconfiguration-properties"></a>

`CategoryLabelOptions`  <a name="cfn-quicksight-dashboard-wordcloudchartconfiguration-categorylabeloptions"></a>
The label options (label text, label visibility, and sort icon visibility) for the word cloud category.
*Required*: No
*Type*: [ChartAxisLabelOptions](aws-properties-quicksight-dashboard-chartaxislabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FieldWells`  <a name="cfn-quicksight-dashboard-wordcloudchartconfiguration-fieldwells"></a>
The field wells of the visual.
*Required*: No
*Type*: [WordCloudFieldWells](aws-properties-quicksight-dashboard-wordcloudfieldwells.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Interactions`  <a name="cfn-quicksight-dashboard-wordcloudchartconfiguration-interactions"></a>
The general visual interactions setup for a visual.
*Required*: No
*Type*: [VisualInteractionOptions](aws-properties-quicksight-dashboard-visualinteractionoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SortConfiguration`  <a name="cfn-quicksight-dashboard-wordcloudchartconfiguration-sortconfiguration"></a>
The sort configuration of a word cloud visual.
*Required*: No
*Type*: [WordCloudSortConfiguration](aws-properties-quicksight-dashboard-wordcloudsortconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WordCloudOptions`  <a name="cfn-quicksight-dashboard-wordcloudchartconfiguration-wordcloudoptions"></a>
The options for a word cloud visual.
*Required*: No
*Type*: [WordCloudOptions](aws-properties-quicksight-dashboard-wordcloudoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
