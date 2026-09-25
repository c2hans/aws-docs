---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-linechartseriessettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template LineChartSeriesSettings
<a name="aws-properties-quicksight-template-linechartseriessettings"></a>

The options that determine the presentation of a line series in the visual

## Syntax
<a name="aws-properties-quicksight-template-linechartseriessettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-linechartseriessettings-syntax.json"></a>

```
{
  "[DecalSettings](#cfn-quicksight-template-linechartseriessettings-decalsettings)" : {{DecalSettings}},
  "[LineStyleSettings](#cfn-quicksight-template-linechartseriessettings-linestylesettings)" : {{LineChartLineStyleSettings}},
  "[MarkerStyleSettings](#cfn-quicksight-template-linechartseriessettings-markerstylesettings)" : {{LineChartMarkerStyleSettings}}
}
```

### YAML
<a name="aws-properties-quicksight-template-linechartseriessettings-syntax.yaml"></a>

```
  [DecalSettings](#cfn-quicksight-template-linechartseriessettings-decalsettings): {{
    DecalSettings}}
  [LineStyleSettings](#cfn-quicksight-template-linechartseriessettings-linestylesettings): {{
    LineChartLineStyleSettings}}
  [MarkerStyleSettings](#cfn-quicksight-template-linechartseriessettings-markerstylesettings): {{
    LineChartMarkerStyleSettings}}
```

## Properties
<a name="aws-properties-quicksight-template-linechartseriessettings-properties"></a>

`DecalSettings`  <a name="cfn-quicksight-template-linechartseriessettings-decalsettings"></a>
Decal settings for a line series in `LineChartVisual`.
*Required*: No
*Type*: [DecalSettings](aws-properties-quicksight-template-decalsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LineStyleSettings`  <a name="cfn-quicksight-template-linechartseriessettings-linestylesettings"></a>
Line styles options for a line series in `LineChartVisual`.
*Required*: No
*Type*: [LineChartLineStyleSettings](aws-properties-quicksight-template-linechartlinestylesettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MarkerStyleSettings`  <a name="cfn-quicksight-template-linechartseriessettings-markerstylesettings"></a>
Marker styles options for a line series in `LineChartVisual`.
*Required*: No
*Type*: [LineChartMarkerStyleSettings](aws-properties-quicksight-template-linechartmarkerstylesettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
