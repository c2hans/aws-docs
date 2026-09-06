---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-hlssettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel HlsSettings
<a name="aws-properties-medialive-channel-hlssettings"></a>

The settings for an HLS output.

The parent of this entity is HlsOutputSettings.

## Syntax
<a name="aws-properties-medialive-channel-hlssettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-hlssettings-syntax.json"></a>

```
{
  "[AudioOnlyHlsSettings](#cfn-medialive-channel-hlssettings-audioonlyhlssettings)" : {{AudioOnlyHlsSettings}},
  "[Fmp4HlsSettings](#cfn-medialive-channel-hlssettings-fmp4hlssettings)" : {{Fmp4HlsSettings}},
  "[FrameCaptureHlsSettings](#cfn-medialive-channel-hlssettings-framecapturehlssettings)" : {{Json}},
  "[StandardHlsSettings](#cfn-medialive-channel-hlssettings-standardhlssettings)" : {{StandardHlsSettings}}
}
```

### YAML
<a name="aws-properties-medialive-channel-hlssettings-syntax.yaml"></a>

```
  [AudioOnlyHlsSettings](#cfn-medialive-channel-hlssettings-audioonlyhlssettings): {{
    AudioOnlyHlsSettings}}
  [Fmp4HlsSettings](#cfn-medialive-channel-hlssettings-fmp4hlssettings): {{
    Fmp4HlsSettings}}
  [FrameCaptureHlsSettings](#cfn-medialive-channel-hlssettings-framecapturehlssettings): {{Json}}
  [StandardHlsSettings](#cfn-medialive-channel-hlssettings-standardhlssettings): {{
    StandardHlsSettings}}
```

## Properties
<a name="aws-properties-medialive-channel-hlssettings-properties"></a>

`AudioOnlyHlsSettings`  <a name="cfn-medialive-channel-hlssettings-audioonlyhlssettings"></a>
The settings for an audio-only output.
*Required*: No
*Type*: [AudioOnlyHlsSettings](aws-properties-medialive-channel-audioonlyhlssettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Fmp4HlsSettings`  <a name="cfn-medialive-channel-hlssettings-fmp4hlssettings"></a>
The settings for an fMP4 container.
*Required*: No
*Type*: [Fmp4HlsSettings](aws-properties-medialive-channel-fmp4hlssettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FrameCaptureHlsSettings`  <a name="cfn-medialive-channel-hlssettings-framecapturehlssettings"></a>
Settings for a frame capture output in an HLS output group.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StandardHlsSettings`  <a name="cfn-medialive-channel-hlssettings-standardhlssettings"></a>
The settings for a standard output (an output that is not audio-only).
*Required*: No
*Type*: [StandardHlsSettings](aws-properties-medialive-channel-standardhlssettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
