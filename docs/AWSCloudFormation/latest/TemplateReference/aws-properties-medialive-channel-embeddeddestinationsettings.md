---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-embeddeddestinationsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel EmbeddedDestinationSettings
<a name="aws-properties-medialive-channel-embeddeddestinationsettings"></a>

The configuration of embedded captions in the output.

The parent of this entity is CaptionDestinationSettings.

## Syntax
<a name="aws-properties-medialive-channel-embeddeddestinationsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-embeddeddestinationsettings-syntax.json"></a>

```
{
  "[Position](#cfn-medialive-channel-embeddeddestinationsettings-position)" : {{EmbeddedCaptionPositionSettings}},
  "[StyleControl](#cfn-medialive-channel-embeddeddestinationsettings-stylecontrol)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-channel-embeddeddestinationsettings-syntax.yaml"></a>

```
  [Position](#cfn-medialive-channel-embeddeddestinationsettings-position): {{
    EmbeddedCaptionPositionSettings}}
  [StyleControl](#cfn-medialive-channel-embeddeddestinationsettings-stylecontrol): {{String}}
```

## Properties
<a name="aws-properties-medialive-channel-embeddeddestinationsettings-properties"></a>

`Position`  <a name="cfn-medialive-channel-embeddeddestinationsettings-position"></a>
Specifies the position of the output captions. Applies only when `styleControl` is set to `MANUAL`.
*Required*: No
*Type*: [EmbeddedCaptionPositionSettings](aws-properties-medialive-channel-embeddedcaptionpositionsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StyleControl`  <a name="cfn-medialive-channel-embeddeddestinationsettings-stylecontrol"></a>
Controls the source of position and style information for the output captions. Valid values:
+ `PASSTHROUGH` – Carry the caption position and style from the source captions. When the source captions are embedded, SCTE-20, or ancillary, the position and style are preserved exactly. When the source captions are another format, the position and any supported style are carried over.
+ `MANUAL` – Applies the specified styling and positioning. All other styling and positioning is given default values.
If you don't specify this field, the default is `PASSTHROUGH`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
