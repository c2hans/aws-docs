---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-webvttdestinationsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel WebvttDestinationSettings
<a name="aws-properties-medialive-channel-webvttdestinationsettings"></a>

The configuration of Web VTT captions in the output.

The parent of this entity is CaptionDestinationSettings.

## Syntax
<a name="aws-properties-medialive-channel-webvttdestinationsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-webvttdestinationsettings-syntax.json"></a>

```
{
  "[Position](#cfn-medialive-channel-webvttdestinationsettings-position)" : {{TextCaptionPositionSettings}},
  "[StyleControl](#cfn-medialive-channel-webvttdestinationsettings-stylecontrol)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-channel-webvttdestinationsettings-syntax.yaml"></a>

```
  [Position](#cfn-medialive-channel-webvttdestinationsettings-position): {{
    TextCaptionPositionSettings}}
  [StyleControl](#cfn-medialive-channel-webvttdestinationsettings-stylecontrol): {{String}}
```

## Properties
<a name="aws-properties-medialive-channel-webvttdestinationsettings-properties"></a>

`Position`  <a name="cfn-medialive-channel-webvttdestinationsettings-position"></a>
Specifies the position of the output captions. Applies only when `styleControl` is set to `MANUAL`.
*Required*: No
*Type*: [TextCaptionPositionSettings](aws-properties-medialive-channel-textcaptionpositionsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StyleControl`  <a name="cfn-medialive-channel-webvttdestinationsettings-stylecontrol"></a>
Controls whether the color and position of the source captions is passed through to the WebVTT output captions. Valid values:
+ `PASSTHROUGH` – Valid only if the source captions are EMBEDDED, TELETEXT, or SMART SUBTITLES.
+ `NO_STYLE_DATA` – Don't pass through the style. The output captions will not contain any font styling information.
+ `MANUAL` – Applies the specified styling and positioning. All other styling and positioning is given default values.
If you don't specify this field, the default is `NO_STYLE_DATA`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
