---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-theme-visualsubtitlefontconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Theme VisualSubtitleFontConfiguration
<a name="aws-properties-quicksight-theme-visualsubtitlefontconfiguration"></a>

Configures the display properties of the visual sub-title.

## Syntax
<a name="aws-properties-quicksight-theme-visualsubtitlefontconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-theme-visualsubtitlefontconfiguration-syntax.json"></a>

```
{
  "[FontConfiguration](#cfn-quicksight-theme-visualsubtitlefontconfiguration-fontconfiguration)" : {{FontConfiguration}},
  "[TextAlignment](#cfn-quicksight-theme-visualsubtitlefontconfiguration-textalignment)" : {{String}},
  "[TextTransform](#cfn-quicksight-theme-visualsubtitlefontconfiguration-texttransform)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-theme-visualsubtitlefontconfiguration-syntax.yaml"></a>

```
  [FontConfiguration](#cfn-quicksight-theme-visualsubtitlefontconfiguration-fontconfiguration): {{
    FontConfiguration}}
  [TextAlignment](#cfn-quicksight-theme-visualsubtitlefontconfiguration-textalignment): {{String}}
  [TextTransform](#cfn-quicksight-theme-visualsubtitlefontconfiguration-texttransform): {{String}}
```

## Properties
<a name="aws-properties-quicksight-theme-visualsubtitlefontconfiguration-properties"></a>

`FontConfiguration`  <a name="cfn-quicksight-theme-visualsubtitlefontconfiguration-fontconfiguration"></a>
Property description not available.
*Required*: No
*Type*: [FontConfiguration](aws-properties-quicksight-theme-fontconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TextAlignment`  <a name="cfn-quicksight-theme-visualsubtitlefontconfiguration-textalignment"></a>
Determines the alignment of visual sub-title.
*Required*: No
*Type*: String
*Allowed values*: `LEFT | CENTER | RIGHT | AUTO`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TextTransform`  <a name="cfn-quicksight-theme-visualsubtitlefontconfiguration-texttransform"></a>
Determines the text transformation of visual sub-title.
*Required*: No
*Type*: String
*Allowed values*: `CAPITALIZE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
