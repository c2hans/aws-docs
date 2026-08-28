---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-wordcloudchartconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis WordCloudChartConfiguration
<a name="aws-properties-quicksight-analysis-wordcloudchartconfiguration"></a>

The configuration of a word cloud visual.

## Syntax
<a name="aws-properties-quicksight-analysis-wordcloudchartconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-wordcloudchartconfiguration-syntax.json"></a>

```
{
  "[CategoryLabelOptions](#cfn-quicksight-analysis-wordcloudchartconfiguration-categorylabeloptions)" : {{ChartAxisLabelOptions}},
  "[FieldWells](#cfn-quicksight-analysis-wordcloudchartconfiguration-fieldwells)" : {{WordCloudFieldWells}},
  "[Interactions](#cfn-quicksight-analysis-wordcloudchartconfiguration-interactions)" : {{VisualInteractionOptions}},
  "[SortConfiguration](#cfn-quicksight-analysis-wordcloudchartconfiguration-sortconfiguration)" : {{WordCloudSortConfiguration}},
  "[WordCloudOptions](#cfn-quicksight-analysis-wordcloudchartconfiguration-wordcloudoptions)" : {{WordCloudOptions}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-wordcloudchartconfiguration-syntax.yaml"></a>

```
  [CategoryLabelOptions](#cfn-quicksight-analysis-wordcloudchartconfiguration-categorylabeloptions): {{
    ChartAxisLabelOptions}}
  [FieldWells](#cfn-quicksight-analysis-wordcloudchartconfiguration-fieldwells): {{
    WordCloudFieldWells}}
  [Interactions](#cfn-quicksight-analysis-wordcloudchartconfiguration-interactions): {{
    VisualInteractionOptions}}
  [SortConfiguration](#cfn-quicksight-analysis-wordcloudchartconfiguration-sortconfiguration): {{
    WordCloudSortConfiguration}}
  [WordCloudOptions](#cfn-quicksight-analysis-wordcloudchartconfiguration-wordcloudoptions): {{
    WordCloudOptions}}
```

## Properties
<a name="aws-properties-quicksight-analysis-wordcloudchartconfiguration-properties"></a>

`CategoryLabelOptions`  <a name="cfn-quicksight-analysis-wordcloudchartconfiguration-categorylabeloptions"></a>
The label options (label text, label visibility, and sort icon visibility) for the word cloud category.
*Required*: No
*Type*: [ChartAxisLabelOptions](aws-properties-quicksight-analysis-chartaxislabeloptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FieldWells`  <a name="cfn-quicksight-analysis-wordcloudchartconfiguration-fieldwells"></a>
The field wells of the visual.
*Required*: No
*Type*: [WordCloudFieldWells](aws-properties-quicksight-analysis-wordcloudfieldwells.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Interactions`  <a name="cfn-quicksight-analysis-wordcloudchartconfiguration-interactions"></a>
The general visual interactions setup for a visual.
*Required*: No
*Type*: [VisualInteractionOptions](aws-properties-quicksight-analysis-visualinteractionoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SortConfiguration`  <a name="cfn-quicksight-analysis-wordcloudchartconfiguration-sortconfiguration"></a>
The sort configuration of a word cloud visual.
*Required*: No
*Type*: [WordCloudSortConfiguration](aws-properties-quicksight-analysis-wordcloudsortconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WordCloudOptions`  <a name="cfn-quicksight-analysis-wordcloudchartconfiguration-wordcloudoptions"></a>
The options for a word cloud visual.
*Required*: No
*Type*: [WordCloudOptions](aws-properties-quicksight-analysis-wordcloudoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
