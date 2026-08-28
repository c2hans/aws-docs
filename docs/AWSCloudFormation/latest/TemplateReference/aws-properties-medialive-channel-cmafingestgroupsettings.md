---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-cmafingestgroupsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel CmafIngestGroupSettings
<a name="aws-properties-medialive-channel-cmafingestgroupsettings"></a>

Cmaf Ingest Group Settings

## Syntax
<a name="aws-properties-medialive-channel-cmafingestgroupsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-cmafingestgroupsettings-syntax.json"></a>

```
{
  "[AdditionalDestinations](#cfn-medialive-channel-cmafingestgroupsettings-additionaldestinations)" : {{[ AdditionalDestinations, ... ]}},
  "[CaptionLanguageMappings](#cfn-medialive-channel-cmafingestgroupsettings-captionlanguagemappings)" : {{[ CmafIngestCaptionLanguageMapping, ... ]}},
  "[Destination](#cfn-medialive-channel-cmafingestgroupsettings-destination)" : {{OutputLocationRef}},
  "[Id3Behavior](#cfn-medialive-channel-cmafingestgroupsettings-id3behavior)" : {{String}},
  "[Id3NameModifier](#cfn-medialive-channel-cmafingestgroupsettings-id3namemodifier)" : {{String}},
  "[KlvBehavior](#cfn-medialive-channel-cmafingestgroupsettings-klvbehavior)" : {{String}},
  "[KlvNameModifier](#cfn-medialive-channel-cmafingestgroupsettings-klvnamemodifier)" : {{String}},
  "[NielsenId3Behavior](#cfn-medialive-channel-cmafingestgroupsettings-nielsenid3behavior)" : {{String}},
  "[NielsenId3NameModifier](#cfn-medialive-channel-cmafingestgroupsettings-nielsenid3namemodifier)" : {{String}},
  "[Scte35NameModifier](#cfn-medialive-channel-cmafingestgroupsettings-scte35namemodifier)" : {{String}},
  "[Scte35Type](#cfn-medialive-channel-cmafingestgroupsettings-scte35type)" : {{String}},
  "[SegmentLength](#cfn-medialive-channel-cmafingestgroupsettings-segmentlength)" : {{Integer}},
  "[SegmentLengthUnits](#cfn-medialive-channel-cmafingestgroupsettings-segmentlengthunits)" : {{String}},
  "[SendDelayMs](#cfn-medialive-channel-cmafingestgroupsettings-senddelayms)" : {{Integer}},
  "[TimedMetadataId3Frame](#cfn-medialive-channel-cmafingestgroupsettings-timedmetadataid3frame)" : {{String}},
  "[TimedMetadataId3Period](#cfn-medialive-channel-cmafingestgroupsettings-timedmetadataid3period)" : {{Integer}},
  "[TimedMetadataPassthrough](#cfn-medialive-channel-cmafingestgroupsettings-timedmetadatapassthrough)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-channel-cmafingestgroupsettings-syntax.yaml"></a>

```
  [AdditionalDestinations](#cfn-medialive-channel-cmafingestgroupsettings-additionaldestinations): {{
    - AdditionalDestinations}}
  [CaptionLanguageMappings](#cfn-medialive-channel-cmafingestgroupsettings-captionlanguagemappings): {{
    - CmafIngestCaptionLanguageMapping}}
  [Destination](#cfn-medialive-channel-cmafingestgroupsettings-destination): {{
    OutputLocationRef}}
  [Id3Behavior](#cfn-medialive-channel-cmafingestgroupsettings-id3behavior): {{String}}
  [Id3NameModifier](#cfn-medialive-channel-cmafingestgroupsettings-id3namemodifier): {{String}}
  [KlvBehavior](#cfn-medialive-channel-cmafingestgroupsettings-klvbehavior): {{String}}
  [KlvNameModifier](#cfn-medialive-channel-cmafingestgroupsettings-klvnamemodifier): {{String}}
  [NielsenId3Behavior](#cfn-medialive-channel-cmafingestgroupsettings-nielsenid3behavior): {{String}}
  [NielsenId3NameModifier](#cfn-medialive-channel-cmafingestgroupsettings-nielsenid3namemodifier): {{String}}
  [Scte35NameModifier](#cfn-medialive-channel-cmafingestgroupsettings-scte35namemodifier): {{String}}
  [Scte35Type](#cfn-medialive-channel-cmafingestgroupsettings-scte35type): {{String}}
  [SegmentLength](#cfn-medialive-channel-cmafingestgroupsettings-segmentlength): {{Integer}}
  [SegmentLengthUnits](#cfn-medialive-channel-cmafingestgroupsettings-segmentlengthunits): {{String}}
  [SendDelayMs](#cfn-medialive-channel-cmafingestgroupsettings-senddelayms): {{Integer}}
  [TimedMetadataId3Frame](#cfn-medialive-channel-cmafingestgroupsettings-timedmetadataid3frame): {{String}}
  [TimedMetadataId3Period](#cfn-medialive-channel-cmafingestgroupsettings-timedmetadataid3period): {{Integer}}
  [TimedMetadataPassthrough](#cfn-medialive-channel-cmafingestgroupsettings-timedmetadatapassthrough): {{String}}
```

## Properties
<a name="aws-properties-medialive-channel-cmafingestgroupsettings-properties"></a>

`AdditionalDestinations`  <a name="cfn-medialive-channel-cmafingestgroupsettings-additionaldestinations"></a>
Optional an array of additional destinational HTTP destinations for the OutputGroup outputs.
*Required*: No
*Type*: [Array](aws-properties-medialive-channel-additionaldestinations.md) of [AdditionalDestinations](aws-properties-medialive-channel-additionaldestinations.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CaptionLanguageMappings`  <a name="cfn-medialive-channel-cmafingestgroupsettings-captionlanguagemappings"></a>
An array that identifies the languages in the four caption channels in the embedded captions.
*Required*: No
*Type*: Array of [CmafIngestCaptionLanguageMapping](aws-properties-medialive-channel-cmafingestcaptionlanguagemapping.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Destination`  <a name="cfn-medialive-channel-cmafingestgroupsettings-destination"></a>
A HTTP destination for the tracks.
*Required*: No
*Type*: [OutputLocationRef](aws-properties-medialive-channel-outputlocationref.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Id3Behavior`  <a name="cfn-medialive-channel-cmafingestgroupsettings-id3behavior"></a>
Set to ENABLED to enable ID3 metadata insertion. To include metadata, you configure other parameters in the output group, or you add an ID3 action to the channel schedule.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Id3NameModifier`  <a name="cfn-medialive-channel-cmafingestgroupsettings-id3namemodifier"></a>
Change the modifier that MediaLive automatically adds to the Streams() name that identifies an ID3 track. The default is "id3", which means the default name will be Streams(id3.cmfm).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KlvBehavior`  <a name="cfn-medialive-channel-cmafingestgroupsettings-klvbehavior"></a>
If set to passthrough, passes any KLV data from the input source to this output.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KlvNameModifier`  <a name="cfn-medialive-channel-cmafingestgroupsettings-klvnamemodifier"></a>
Change the modifier that MediaLive automatically adds to the Streams() name that identifies a KLV track. The default is "klv", which means the default name will be Streams(klv.cmfm).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NielsenId3Behavior`  <a name="cfn-medialive-channel-cmafingestgroupsettings-nielsenid3behavior"></a>
If set to passthrough, Nielsen inaudible tones for media tracking will be detected in the input audio and an equivalent ID3 tag will be inserted in the output.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NielsenId3NameModifier`  <a name="cfn-medialive-channel-cmafingestgroupsettings-nielsenid3namemodifier"></a>
Change the modifier that MediaLive automatically adds to the Streams() name that identifies a Nielsen ID3 track. The default is "nid3", which means the default name will be Streams(nid3.cmfm).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Scte35NameModifier`  <a name="cfn-medialive-channel-cmafingestgroupsettings-scte35namemodifier"></a>
Change the modifier that MediaLive automatically adds to the Streams() name for a SCTE 35 track. The default is "scte", which means the default name will be Streams(scte.cmfm).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Scte35Type`  <a name="cfn-medialive-channel-cmafingestgroupsettings-scte35type"></a>
Type of scte35 track to add. none or scte35WithoutSegmentation.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SegmentLength`  <a name="cfn-medialive-channel-cmafingestgroupsettings-segmentlength"></a>
The nominal duration of segments. The units are specified in SegmentLengthUnits. The segments will end on the next keyframe after the specified duration, so the actual segment length might be longer, and it might be a fraction of the units.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SegmentLengthUnits`  <a name="cfn-medialive-channel-cmafingestgroupsettings-segmentlengthunits"></a>
Time unit for segment length parameter.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SendDelayMs`  <a name="cfn-medialive-channel-cmafingestgroupsettings-senddelayms"></a>
Number of milliseconds to delay the output from the second pipeline.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimedMetadataId3Frame`  <a name="cfn-medialive-channel-cmafingestgroupsettings-timedmetadataid3frame"></a>
Set to none if you don't want to insert a timecode in the output. Otherwise choose the frame type for the timecode.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimedMetadataId3Period`  <a name="cfn-medialive-channel-cmafingestgroupsettings-timedmetadataid3period"></a>
If you set up to insert a timecode in the output, specify the frequency for the frame, in seconds.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimedMetadataPassthrough`  <a name="cfn-medialive-channel-cmafingestgroupsettings-timedmetadatapassthrough"></a>
Set to enabled to pass through ID3 metadata from the input sources.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
