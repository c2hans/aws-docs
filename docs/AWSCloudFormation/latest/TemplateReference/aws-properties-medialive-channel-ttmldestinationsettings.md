---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-ttmldestinationsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel TtmlDestinationSettings
<a name="aws-properties-medialive-channel-ttmldestinationsettings"></a>

The setup of TTML captions in the output.

The parent of this entity is CaptionDestinationSettings.

## Syntax
<a name="aws-properties-medialive-channel-ttmldestinationsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-ttmldestinationsettings-syntax.json"></a>

```
{
  "[Position](#cfn-medialive-channel-ttmldestinationsettings-position)" : {{TextCaptionPositionSettings}},
  "[StyleControl](#cfn-medialive-channel-ttmldestinationsettings-stylecontrol)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-channel-ttmldestinationsettings-syntax.yaml"></a>

```
  [Position](#cfn-medialive-channel-ttmldestinationsettings-position): {{
    TextCaptionPositionSettings}}
  [StyleControl](#cfn-medialive-channel-ttmldestinationsettings-stylecontrol): {{String}}
```

## Properties
<a name="aws-properties-medialive-channel-ttmldestinationsettings-properties"></a>

`Position`  <a name="cfn-medialive-channel-ttmldestinationsettings-position"></a>
Specifies the position of the output captions. Applies only when `styleControl` is set to `MANUAL`.
*Required*: No
*Type*: [TextCaptionPositionSettings](aws-properties-medialive-channel-textcaptionpositionsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StyleControl`  <a name="cfn-medialive-channel-ttmldestinationsettings-stylecontrol"></a>
When set to passthrough, passes through style and position information from a TTML-like input source (TTML, SMPTE-TT, CFF-TT) to the CFF-TT output or TTML output.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
