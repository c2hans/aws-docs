---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-fontconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis FontConfiguration
<a name="aws-properties-quicksight-analysis-fontconfiguration"></a>

Configures the display properties of the given text.

## Syntax
<a name="aws-properties-quicksight-analysis-fontconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-fontconfiguration-syntax.json"></a>

```
{
  "[FontColor](#cfn-quicksight-analysis-fontconfiguration-fontcolor)" : {{String}},
  "[FontDecoration](#cfn-quicksight-analysis-fontconfiguration-fontdecoration)" : {{String}},
  "[FontFamily](#cfn-quicksight-analysis-fontconfiguration-fontfamily)" : {{String}},
  "[FontSize](#cfn-quicksight-analysis-fontconfiguration-fontsize)" : {{FontSize}},
  "[FontStyle](#cfn-quicksight-analysis-fontconfiguration-fontstyle)" : {{String}},
  "[FontWeight](#cfn-quicksight-analysis-fontconfiguration-fontweight)" : {{FontWeight}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-fontconfiguration-syntax.yaml"></a>

```
  [FontColor](#cfn-quicksight-analysis-fontconfiguration-fontcolor): {{String}}
  [FontDecoration](#cfn-quicksight-analysis-fontconfiguration-fontdecoration): {{String}}
  [FontFamily](#cfn-quicksight-analysis-fontconfiguration-fontfamily): {{String}}
  [FontSize](#cfn-quicksight-analysis-fontconfiguration-fontsize): {{
    FontSize}}
  [FontStyle](#cfn-quicksight-analysis-fontconfiguration-fontstyle): {{String}}
  [FontWeight](#cfn-quicksight-analysis-fontconfiguration-fontweight): {{
    FontWeight}}
```

## Properties
<a name="aws-properties-quicksight-analysis-fontconfiguration-properties"></a>

`FontColor`  <a name="cfn-quicksight-analysis-fontconfiguration-fontcolor"></a>
Determines the color of the text.
*Required*: No
*Type*: String
*Pattern*: `^#[A-F0-9]{6}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FontDecoration`  <a name="cfn-quicksight-analysis-fontconfiguration-fontdecoration"></a>
Determines the appearance of decorative lines on the text.
*Required*: No
*Type*: String
*Allowed values*: `UNDERLINE | NONE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FontFamily`  <a name="cfn-quicksight-analysis-fontconfiguration-fontfamily"></a>
The font family that you want to use.
*Required*: No
*Type*: String
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FontSize`  <a name="cfn-quicksight-analysis-fontconfiguration-fontsize"></a>
The option that determines the text display size.
*Required*: No
*Type*: [FontSize](aws-properties-quicksight-analysis-fontsize.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FontStyle`  <a name="cfn-quicksight-analysis-fontconfiguration-fontstyle"></a>
Determines the text display face that is inherited by the given font family.
*Required*: No
*Type*: String
*Allowed values*: `NORMAL | ITALIC`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FontWeight`  <a name="cfn-quicksight-analysis-fontconfiguration-fontweight"></a>
The option that determines the text display weight, or boldness.
*Required*: No
*Type*: [FontWeight](aws-properties-quicksight-analysis-fontweight.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
