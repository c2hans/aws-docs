---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-mediapackagev2groupsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel MediaPackageV2GroupSettings
<a name="aws-properties-medialive-channel-mediapackagev2groupsettings"></a>

Parameters that apply only if the destination parameter (for the output group) specifies a channel group and channel name. Use of these two parameters indicates that the output group is for MediaPackage V2 (CMAF Ingest).

The parent of this entity is MediaPackageGroupSettings.

## Syntax
<a name="aws-properties-medialive-channel-mediapackagev2groupsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-mediapackagev2groupsettings-syntax.json"></a>

```
{
  "[AdditionalDestinations](#cfn-medialive-channel-mediapackagev2groupsettings-additionaldestinations)" : {{[ MediaPackageAdditionalDestinations, ... ]}},
  "[CaptionLanguageMappings](#cfn-medialive-channel-mediapackagev2groupsettings-captionlanguagemappings)" : {{[ CaptionLanguageMapping, ... ]}},
  "[Id3Behavior](#cfn-medialive-channel-mediapackagev2groupsettings-id3behavior)" : {{String}},
  "[KlvBehavior](#cfn-medialive-channel-mediapackagev2groupsettings-klvbehavior)" : {{String}},
  "[NielsenId3Behavior](#cfn-medialive-channel-mediapackagev2groupsettings-nielsenid3behavior)" : {{String}},
  "[Scte35Type](#cfn-medialive-channel-mediapackagev2groupsettings-scte35type)" : {{String}},
  "[SegmentLength](#cfn-medialive-channel-mediapackagev2groupsettings-segmentlength)" : {{Integer}},
  "[SegmentLengthUnits](#cfn-medialive-channel-mediapackagev2groupsettings-segmentlengthunits)" : {{String}},
  "[TimedMetadataId3Frame](#cfn-medialive-channel-mediapackagev2groupsettings-timedmetadataid3frame)" : {{String}},
  "[TimedMetadataId3Period](#cfn-medialive-channel-mediapackagev2groupsettings-timedmetadataid3period)" : {{Integer}},
  "[TimedMetadataPassthrough](#cfn-medialive-channel-mediapackagev2groupsettings-timedmetadatapassthrough)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-channel-mediapackagev2groupsettings-syntax.yaml"></a>

```
  [AdditionalDestinations](#cfn-medialive-channel-mediapackagev2groupsettings-additionaldestinations): {{
    - MediaPackageAdditionalDestinations}}
  [CaptionLanguageMappings](#cfn-medialive-channel-mediapackagev2groupsettings-captionlanguagemappings): {{
    - CaptionLanguageMapping}}
  [Id3Behavior](#cfn-medialive-channel-mediapackagev2groupsettings-id3behavior): {{String}}
  [KlvBehavior](#cfn-medialive-channel-mediapackagev2groupsettings-klvbehavior): {{String}}
  [NielsenId3Behavior](#cfn-medialive-channel-mediapackagev2groupsettings-nielsenid3behavior): {{String}}
  [Scte35Type](#cfn-medialive-channel-mediapackagev2groupsettings-scte35type): {{String}}
  [SegmentLength](#cfn-medialive-channel-mediapackagev2groupsettings-segmentlength): {{Integer}}
  [SegmentLengthUnits](#cfn-medialive-channel-mediapackagev2groupsettings-segmentlengthunits): {{String}}
  [TimedMetadataId3Frame](#cfn-medialive-channel-mediapackagev2groupsettings-timedmetadataid3frame): {{String}}
  [TimedMetadataId3Period](#cfn-medialive-channel-mediapackagev2groupsettings-timedmetadataid3period): {{Integer}}
  [TimedMetadataPassthrough](#cfn-medialive-channel-mediapackagev2groupsettings-timedmetadatapassthrough): {{String}}
```

## Properties
<a name="aws-properties-medialive-channel-mediapackagev2groupsettings-properties"></a>

`AdditionalDestinations`  <a name="cfn-medialive-channel-mediapackagev2groupsettings-additionaldestinations"></a>
Optional, an array of additional destination HTTP destinations for the output group outputs.
*Required*: No
*Type*: [Array](aws-properties-medialive-channel-additionaldestinations.md) of [MediaPackageAdditionalDestinations](aws-properties-medialive-channel-mediapackageadditionaldestinations.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CaptionLanguageMappings`  <a name="cfn-medialive-channel-mediapackagev2groupsettings-captionlanguagemappings"></a>
Mapping of up to 4 caption channels to caption languages. Each mapping maps a caption channel to an ISO 693-2 language code, with an optional description.
*Required*: No
*Type*: Array of [CaptionLanguageMapping](aws-properties-medialive-channel-captionlanguagemapping.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Id3Behavior`  <a name="cfn-medialive-channel-mediapackagev2groupsettings-id3behavior"></a>
Set to ENABLED to enable ID3 metadata insertion. To include metadata, you configure other parameters in the output group, or you add an ID3 action to the channel schedule.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KlvBehavior`  <a name="cfn-medialive-channel-mediapackagev2groupsettings-klvbehavior"></a>
If set to passthrough, passes any KLV data from the input source to this output.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NielsenId3Behavior`  <a name="cfn-medialive-channel-mediapackagev2groupsettings-nielsenid3behavior"></a>
If set to passthrough, Nielsen inaudible tones for media tracking will be detected in the input audio and an equivalent ID3 tag will be inserted in the output.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Scte35Type`  <a name="cfn-medialive-channel-mediapackagev2groupsettings-scte35type"></a>
Type of SCTE-35 track to add. Specify none or scte35WithoutSegmentation.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SegmentLength`  <a name="cfn-medialive-channel-mediapackagev2groupsettings-segmentlength"></a>
The nominal duration of segments. The units are specified in SegmentLengthUnits. The segments will end on the next keyframe after the specified duration, so the actual segment length might be longer, and it might be a fraction of the units.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SegmentLengthUnits`  <a name="cfn-medialive-channel-mediapackagev2groupsettings-segmentlengthunits"></a>
Time unit for the segment length parameter.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimedMetadataId3Frame`  <a name="cfn-medialive-channel-mediapackagev2groupsettings-timedmetadataid3frame"></a>
Set to none if you don't want to insert a timecode in the output. Otherwise choose the frame type for the timecode.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimedMetadataId3Period`  <a name="cfn-medialive-channel-mediapackagev2groupsettings-timedmetadataid3period"></a>
If you set up to insert a timecode in the output, specify the frequency for the frame, in seconds.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimedMetadataPassthrough`  <a name="cfn-medialive-channel-mediapackagev2groupsettings-timedmetadatapassthrough"></a>
Set to enabled to pass through ID3 metadata from the input sources.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
