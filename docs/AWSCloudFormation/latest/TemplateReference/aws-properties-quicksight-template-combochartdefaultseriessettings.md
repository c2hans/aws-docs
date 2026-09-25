---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-combochartdefaultseriessettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template ComboChartDefaultSeriesSettings
<a name="aws-properties-quicksight-template-combochartdefaultseriessettings"></a>

The options that determine the default presentation of all series in `ComboChartVisual`.

## Syntax
<a name="aws-properties-quicksight-template-combochartdefaultseriessettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-combochartdefaultseriessettings-syntax.json"></a>

```
{
  "[BorderSettings](#cfn-quicksight-template-combochartdefaultseriessettings-bordersettings)" : {{BorderSettings}},
  "[DecalSettings](#cfn-quicksight-template-combochartdefaultseriessettings-decalsettings)" : {{DecalSettings}},
  "[LineStyleSettings](#cfn-quicksight-template-combochartdefaultseriessettings-linestylesettings)" : {{LineChartLineStyleSettings}},
  "[MarkerStyleSettings](#cfn-quicksight-template-combochartdefaultseriessettings-markerstylesettings)" : {{LineChartMarkerStyleSettings}}
}
```

### YAML
<a name="aws-properties-quicksight-template-combochartdefaultseriessettings-syntax.yaml"></a>

```
  [BorderSettings](#cfn-quicksight-template-combochartdefaultseriessettings-bordersettings): {{
    BorderSettings}}
  [DecalSettings](#cfn-quicksight-template-combochartdefaultseriessettings-decalsettings): {{
    DecalSettings}}
  [LineStyleSettings](#cfn-quicksight-template-combochartdefaultseriessettings-linestylesettings): {{
    LineChartLineStyleSettings}}
  [MarkerStyleSettings](#cfn-quicksight-template-combochartdefaultseriessettings-markerstylesettings): {{
    LineChartMarkerStyleSettings}}
```

## Properties
<a name="aws-properties-quicksight-template-combochartdefaultseriessettings-properties"></a>

`BorderSettings`  <a name="cfn-quicksight-template-combochartdefaultseriessettings-bordersettings"></a>
Border settings for all bar series in the visual.
*Required*: No
*Type*: [BorderSettings](aws-properties-quicksight-template-bordersettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DecalSettings`  <a name="cfn-quicksight-template-combochartdefaultseriessettings-decalsettings"></a>
Decal settings for all series in the visual.
*Required*: No
*Type*: [DecalSettings](aws-properties-quicksight-template-decalsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LineStyleSettings`  <a name="cfn-quicksight-template-combochartdefaultseriessettings-linestylesettings"></a>
Line styles options for all line series in the visual.
*Required*: No
*Type*: [LineChartLineStyleSettings](aws-properties-quicksight-template-linechartlinestylesettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MarkerStyleSettings`  <a name="cfn-quicksight-template-combochartdefaultseriessettings-markerstylesettings"></a>
Marker styles options for all line series in the visual.
*Required*: No
*Type*: [LineChartMarkerStyleSettings](aws-properties-quicksight-template-linechartmarkerstylesettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
