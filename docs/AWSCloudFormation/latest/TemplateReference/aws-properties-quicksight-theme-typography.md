---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-theme-typography.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Theme Typography
<a name="aws-properties-quicksight-theme-typography"></a>

Determines the typography options.

## Syntax
<a name="aws-properties-quicksight-theme-typography-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-theme-typography-syntax.json"></a>

```
{
  "[AxisLabelFontConfiguration](#cfn-quicksight-theme-typography-axislabelfontconfiguration)" : {{FontConfiguration}},
  "[AxisTitleFontConfiguration](#cfn-quicksight-theme-typography-axistitlefontconfiguration)" : {{FontConfiguration}},
  "[DataLabelFontConfiguration](#cfn-quicksight-theme-typography-datalabelfontconfiguration)" : {{FontConfiguration}},
  "[FontFamilies](#cfn-quicksight-theme-typography-fontfamilies)" : {{[ Font, ... ]}},
  "[LegendTitleFontConfiguration](#cfn-quicksight-theme-typography-legendtitlefontconfiguration)" : {{FontConfiguration}},
  "[LegendValueFontConfiguration](#cfn-quicksight-theme-typography-legendvaluefontconfiguration)" : {{FontConfiguration}},
  "[VisualSubtitleFontConfiguration](#cfn-quicksight-theme-typography-visualsubtitlefontconfiguration)" : {{VisualSubtitleFontConfiguration}},
  "[VisualTitleFontConfiguration](#cfn-quicksight-theme-typography-visualtitlefontconfiguration)" : {{VisualTitleFontConfiguration}}
}
```

### YAML
<a name="aws-properties-quicksight-theme-typography-syntax.yaml"></a>

```
  [AxisLabelFontConfiguration](#cfn-quicksight-theme-typography-axislabelfontconfiguration): {{
    FontConfiguration}}
  [AxisTitleFontConfiguration](#cfn-quicksight-theme-typography-axistitlefontconfiguration): {{
    FontConfiguration}}
  [DataLabelFontConfiguration](#cfn-quicksight-theme-typography-datalabelfontconfiguration): {{
    FontConfiguration}}
  [FontFamilies](#cfn-quicksight-theme-typography-fontfamilies): {{
    - Font}}
  [LegendTitleFontConfiguration](#cfn-quicksight-theme-typography-legendtitlefontconfiguration): {{
    FontConfiguration}}
  [LegendValueFontConfiguration](#cfn-quicksight-theme-typography-legendvaluefontconfiguration): {{
    FontConfiguration}}
  [VisualSubtitleFontConfiguration](#cfn-quicksight-theme-typography-visualsubtitlefontconfiguration): {{
    VisualSubtitleFontConfiguration}}
  [VisualTitleFontConfiguration](#cfn-quicksight-theme-typography-visualtitlefontconfiguration): {{
    VisualTitleFontConfiguration}}
```

## Properties
<a name="aws-properties-quicksight-theme-typography-properties"></a>

`AxisLabelFontConfiguration`  <a name="cfn-quicksight-theme-typography-axislabelfontconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [FontConfiguration](aws-properties-quicksight-theme-fontconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AxisTitleFontConfiguration`  <a name="cfn-quicksight-theme-typography-axistitlefontconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [FontConfiguration](aws-properties-quicksight-theme-fontconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataLabelFontConfiguration`  <a name="cfn-quicksight-theme-typography-datalabelfontconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [FontConfiguration](aws-properties-quicksight-theme-fontconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FontFamilies`  <a name="cfn-quicksight-theme-typography-fontfamilies"></a>
Determines the list of font families.
*Required*: No
*Type*: Array of [Font](aws-properties-quicksight-theme-font.md)
*Minimum*: `0`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LegendTitleFontConfiguration`  <a name="cfn-quicksight-theme-typography-legendtitlefontconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [FontConfiguration](aws-properties-quicksight-theme-fontconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LegendValueFontConfiguration`  <a name="cfn-quicksight-theme-typography-legendvaluefontconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [FontConfiguration](aws-properties-quicksight-theme-fontconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VisualSubtitleFontConfiguration`  <a name="cfn-quicksight-theme-typography-visualsubtitlefontconfiguration"></a>
Configures the display properties of the visual sub-title.
*Required*: No
*Type*: [VisualSubtitleFontConfiguration](aws-properties-quicksight-theme-visualsubtitlefontconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VisualTitleFontConfiguration`  <a name="cfn-quicksight-theme-typography-visualtitlefontconfiguration"></a>
Configures the display properties of the visual title.
*Required*: No
*Type*: [VisualTitleFontConfiguration](aws-properties-quicksight-theme-visualtitlefontconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
