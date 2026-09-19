---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-captionselectorsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel CaptionSelectorSettings
<a name="aws-properties-medialive-channel-captionselectorsettings"></a>

Captions Selector Settings

The parent of this entity is CaptionSelector.

## Syntax
<a name="aws-properties-medialive-channel-captionselectorsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-captionselectorsettings-syntax.json"></a>

```
{
  "[AncillarySourceSettings](#cfn-medialive-channel-captionselectorsettings-ancillarysourcesettings)" : {{AncillarySourceSettings}},
  "[AribSourceSettings](#cfn-medialive-channel-captionselectorsettings-aribsourcesettings)" : {{Json}},
  "[DvbSubSourceSettings](#cfn-medialive-channel-captionselectorsettings-dvbsubsourcesettings)" : {{Scte27DvbSubSourceSettings}},
  "[EmbeddedSourceSettings](#cfn-medialive-channel-captionselectorsettings-embeddedsourcesettings)" : {{EmbeddedSourceSettings}},
  "[Scte20SourceSettings](#cfn-medialive-channel-captionselectorsettings-scte20sourcesettings)" : {{Scte20SourceSettings}},
  "[Scte27SourceSettings](#cfn-medialive-channel-captionselectorsettings-scte27sourcesettings)" : {{Scte27DvbSubSourceSettings}},
  "[SmartSubtitleSourceSettings](#cfn-medialive-channel-captionselectorsettings-smartsubtitlesourcesettings)" : {{SmartSubtitleSourceSettings}},
  "[TeletextSourceSettings](#cfn-medialive-channel-captionselectorsettings-teletextsourcesettings)" : {{TeletextSourceSettings}}
}
```

### YAML
<a name="aws-properties-medialive-channel-captionselectorsettings-syntax.yaml"></a>

```
  [AncillarySourceSettings](#cfn-medialive-channel-captionselectorsettings-ancillarysourcesettings): {{
    AncillarySourceSettings}}
  [AribSourceSettings](#cfn-medialive-channel-captionselectorsettings-aribsourcesettings): {{Json}}
  [DvbSubSourceSettings](#cfn-medialive-channel-captionselectorsettings-dvbsubsourcesettings): {{
    Scte27DvbSubSourceSettings}}
  [EmbeddedSourceSettings](#cfn-medialive-channel-captionselectorsettings-embeddedsourcesettings): {{
    EmbeddedSourceSettings}}
  [Scte20SourceSettings](#cfn-medialive-channel-captionselectorsettings-scte20sourcesettings): {{
    Scte20SourceSettings}}
  [Scte27SourceSettings](#cfn-medialive-channel-captionselectorsettings-scte27sourcesettings): {{
    Scte27DvbSubSourceSettings}}
  [SmartSubtitleSourceSettings](#cfn-medialive-channel-captionselectorsettings-smartsubtitlesourcesettings): {{
    SmartSubtitleSourceSettings}}
  [TeletextSourceSettings](#cfn-medialive-channel-captionselectorsettings-teletextsourcesettings): {{
    TeletextSourceSettings}}
```

## Properties
<a name="aws-properties-medialive-channel-captionselectorsettings-properties"></a>

`AncillarySourceSettings`  <a name="cfn-medialive-channel-captionselectorsettings-ancillarysourcesettings"></a>
 Information about the ancillary captions to extract from the input.
*Required*: No
*Type*: [AncillarySourceSettings](aws-properties-medialive-channel-ancillarysourcesettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AribSourceSettings`  <a name="cfn-medialive-channel-captionselectorsettings-aribsourcesettings"></a>
Information about the ARIB captions to extract from the input.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DvbSubSourceSettings`  <a name="cfn-medialive-channel-captionselectorsettings-dvbsubsourcesettings"></a>
Information about the DVB Sub captions to extract from the input.
*Required*: No
*Type*: [Scte27DvbSubSourceSettings](aws-properties-medialive-channel-scte27dvbsubsourcesettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EmbeddedSourceSettings`  <a name="cfn-medialive-channel-captionselectorsettings-embeddedsourcesettings"></a>
Information about the embedded captions to extract from the input.
*Required*: No
*Type*: [EmbeddedSourceSettings](aws-properties-medialive-channel-embeddedsourcesettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Scte20SourceSettings`  <a name="cfn-medialive-channel-captionselectorsettings-scte20sourcesettings"></a>
Information about the SCTE-20 captions to extract from the input.
*Required*: No
*Type*: [Scte20SourceSettings](aws-properties-medialive-channel-scte20sourcesettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Scte27SourceSettings`  <a name="cfn-medialive-channel-captionselectorsettings-scte27sourcesettings"></a>
Information about the SCTE-27 captions to extract from the input.
*Required*: No
*Type*: [Scte27DvbSubSourceSettings](aws-properties-medialive-channel-scte27dvbsubsourcesettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SmartSubtitleSourceSettings`  <a name="cfn-medialive-channel-captionselectorsettings-smartsubtitlesourcesettings"></a>
Property description not available.
*Required*: No
*Type*: [SmartSubtitleSourceSettings](aws-properties-medialive-channel-smartsubtitlesourcesettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TeletextSourceSettings`  <a name="cfn-medialive-channel-captionselectorsettings-teletextsourcesettings"></a>
Information about the Teletext captions to extract from the input.
*Required*: No
*Type*: [TeletextSourceSettings](aws-properties-medialive-channel-teletextsourcesettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
