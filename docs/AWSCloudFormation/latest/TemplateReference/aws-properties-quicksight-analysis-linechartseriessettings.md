---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-linechartseriessettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis LineChartSeriesSettings
<a name="aws-properties-quicksight-analysis-linechartseriessettings"></a>

The options that determine the presentation of a line series in the visual

## Syntax
<a name="aws-properties-quicksight-analysis-linechartseriessettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-linechartseriessettings-syntax.json"></a>

```
{
  "[LineStyleSettings](#cfn-quicksight-analysis-linechartseriessettings-linestylesettings)" : {{LineChartLineStyleSettings}},
  "[MarkerStyleSettings](#cfn-quicksight-analysis-linechartseriessettings-markerstylesettings)" : {{LineChartMarkerStyleSettings}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-linechartseriessettings-syntax.yaml"></a>

```
  [LineStyleSettings](#cfn-quicksight-analysis-linechartseriessettings-linestylesettings): {{
    LineChartLineStyleSettings}}
  [MarkerStyleSettings](#cfn-quicksight-analysis-linechartseriessettings-markerstylesettings): {{
    LineChartMarkerStyleSettings}}
```

## Properties
<a name="aws-properties-quicksight-analysis-linechartseriessettings-properties"></a>

`LineStyleSettings`  <a name="cfn-quicksight-analysis-linechartseriessettings-linestylesettings"></a>
Line styles options for a line series in `LineChartVisual`.
*Required*: No
*Type*: [LineChartLineStyleSettings](aws-properties-quicksight-analysis-linechartlinestylesettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MarkerStyleSettings`  <a name="cfn-quicksight-analysis-linechartseriessettings-markerstylesettings"></a>
Marker styles options for a line series in `LineChartVisual`.
*Required*: No
*Type*: [LineChartMarkerStyleSettings](aws-properties-quicksight-analysis-linechartmarkerstylesettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
