---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-combochartdefaultseriessettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard ComboChartDefaultSeriesSettings
<a name="aws-properties-quicksight-dashboard-combochartdefaultseriessettings"></a>

The options that determine the default presentation of all series in `ComboChartVisual`.

## Syntax
<a name="aws-properties-quicksight-dashboard-combochartdefaultseriessettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-combochartdefaultseriessettings-syntax.json"></a>

```
{
  "[BorderSettings](#cfn-quicksight-dashboard-combochartdefaultseriessettings-bordersettings)" : {{BorderSettings}},
  "[DecalSettings](#cfn-quicksight-dashboard-combochartdefaultseriessettings-decalsettings)" : {{DecalSettings}},
  "[LineStyleSettings](#cfn-quicksight-dashboard-combochartdefaultseriessettings-linestylesettings)" : {{LineChartLineStyleSettings}},
  "[MarkerStyleSettings](#cfn-quicksight-dashboard-combochartdefaultseriessettings-markerstylesettings)" : {{LineChartMarkerStyleSettings}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-combochartdefaultseriessettings-syntax.yaml"></a>

```
  [BorderSettings](#cfn-quicksight-dashboard-combochartdefaultseriessettings-bordersettings): {{
    BorderSettings}}
  [DecalSettings](#cfn-quicksight-dashboard-combochartdefaultseriessettings-decalsettings): {{
    DecalSettings}}
  [LineStyleSettings](#cfn-quicksight-dashboard-combochartdefaultseriessettings-linestylesettings): {{
    LineChartLineStyleSettings}}
  [MarkerStyleSettings](#cfn-quicksight-dashboard-combochartdefaultseriessettings-markerstylesettings): {{
    LineChartMarkerStyleSettings}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-combochartdefaultseriessettings-properties"></a>

`BorderSettings`  <a name="cfn-quicksight-dashboard-combochartdefaultseriessettings-bordersettings"></a>
Border settings for all bar series in the visual.
*Required*: No
*Type*: [BorderSettings](aws-properties-quicksight-dashboard-bordersettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DecalSettings`  <a name="cfn-quicksight-dashboard-combochartdefaultseriessettings-decalsettings"></a>
Decal settings for all series in the visual.
*Required*: No
*Type*: [DecalSettings](aws-properties-quicksight-dashboard-decalsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LineStyleSettings`  <a name="cfn-quicksight-dashboard-combochartdefaultseriessettings-linestylesettings"></a>
Line styles options for all line series in the visual.
*Required*: No
*Type*: [LineChartLineStyleSettings](aws-properties-quicksight-dashboard-linechartlinestylesettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MarkerStyleSettings`  <a name="cfn-quicksight-dashboard-combochartdefaultseriessettings-markerstylesettings"></a>
Marker styles options for all line series in the visual.
*Required*: No
*Type*: [LineChartMarkerStyleSettings](aws-properties-quicksight-dashboard-linechartmarkerstylesettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
