---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-combochartdefaultseriessettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis ComboChartDefaultSeriesSettings
<a name="aws-properties-quicksight-analysis-combochartdefaultseriessettings"></a>

The options that determine the default presentation of all series in `ComboChartVisual`.

## Syntax
<a name="aws-properties-quicksight-analysis-combochartdefaultseriessettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-combochartdefaultseriessettings-syntax.json"></a>

```
{
  "[BorderSettings](#cfn-quicksight-analysis-combochartdefaultseriessettings-bordersettings)" : {{BorderSettings}},
  "[DecalSettings](#cfn-quicksight-analysis-combochartdefaultseriessettings-decalsettings)" : {{DecalSettings}},
  "[LineStyleSettings](#cfn-quicksight-analysis-combochartdefaultseriessettings-linestylesettings)" : {{LineChartLineStyleSettings}},
  "[MarkerStyleSettings](#cfn-quicksight-analysis-combochartdefaultseriessettings-markerstylesettings)" : {{LineChartMarkerStyleSettings}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-combochartdefaultseriessettings-syntax.yaml"></a>

```
  [BorderSettings](#cfn-quicksight-analysis-combochartdefaultseriessettings-bordersettings): {{
    BorderSettings}}
  [DecalSettings](#cfn-quicksight-analysis-combochartdefaultseriessettings-decalsettings): {{
    DecalSettings}}
  [LineStyleSettings](#cfn-quicksight-analysis-combochartdefaultseriessettings-linestylesettings): {{
    LineChartLineStyleSettings}}
  [MarkerStyleSettings](#cfn-quicksight-analysis-combochartdefaultseriessettings-markerstylesettings): {{
    LineChartMarkerStyleSettings}}
```

## Properties
<a name="aws-properties-quicksight-analysis-combochartdefaultseriessettings-properties"></a>

`BorderSettings`  <a name="cfn-quicksight-analysis-combochartdefaultseriessettings-bordersettings"></a>
Border settings for all bar series in the visual.
*Required*: No
*Type*: [BorderSettings](aws-properties-quicksight-analysis-bordersettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DecalSettings`  <a name="cfn-quicksight-analysis-combochartdefaultseriessettings-decalsettings"></a>
Decal settings for all series in the visual.
*Required*: No
*Type*: [DecalSettings](aws-properties-quicksight-analysis-decalsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LineStyleSettings`  <a name="cfn-quicksight-analysis-combochartdefaultseriessettings-linestylesettings"></a>
Line styles options for all line series in the visual.
*Required*: No
*Type*: [LineChartLineStyleSettings](aws-properties-quicksight-analysis-linechartlinestylesettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MarkerStyleSettings`  <a name="cfn-quicksight-analysis-combochartdefaultseriessettings-markerstylesettings"></a>
Marker styles options for all line series in the visual.
*Required*: No
*Type*: [LineChartMarkerStyleSettings](aws-properties-quicksight-analysis-linechartmarkerstylesettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
