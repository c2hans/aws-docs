---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediapackagev2-originendpoint-segment.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaPackageV2::OriginEndpoint Segment
<a name="aws-properties-mediapackagev2-originendpoint-segment"></a>

The segment configuration, including the segment name, duration, and other configuration values.

## Syntax
<a name="aws-properties-mediapackagev2-originendpoint-segment-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediapackagev2-originendpoint-segment-syntax.json"></a>

```
{
  "[Encryption](#cfn-mediapackagev2-originendpoint-segment-encryption)" : {{Encryption}},
  "[IncludeIframeOnlyStreams](#cfn-mediapackagev2-originendpoint-segment-includeiframeonlystreams)" : {{Boolean}},
  "[OutputTimestampMode](#cfn-mediapackagev2-originendpoint-segment-outputtimestampmode)" : {{String}},
  "[Scte](#cfn-mediapackagev2-originendpoint-segment-scte)" : {{Scte}},
  "[SegmentDurationSeconds](#cfn-mediapackagev2-originendpoint-segment-segmentdurationseconds)" : {{Integer}},
  "[SegmentName](#cfn-mediapackagev2-originendpoint-segment-segmentname)" : {{String}},
  "[TsIncludeDvbSubtitles](#cfn-mediapackagev2-originendpoint-segment-tsincludedvbsubtitles)" : {{Boolean}},
  "[TsUseAudioRenditionGroup](#cfn-mediapackagev2-originendpoint-segment-tsuseaudiorenditiongroup)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-mediapackagev2-originendpoint-segment-syntax.yaml"></a>

```
  [Encryption](#cfn-mediapackagev2-originendpoint-segment-encryption): {{
    Encryption}}
  [IncludeIframeOnlyStreams](#cfn-mediapackagev2-originendpoint-segment-includeiframeonlystreams): {{Boolean}}
  [OutputTimestampMode](#cfn-mediapackagev2-originendpoint-segment-outputtimestampmode): {{String}}
  [Scte](#cfn-mediapackagev2-originendpoint-segment-scte): {{
    Scte}}
  [SegmentDurationSeconds](#cfn-mediapackagev2-originendpoint-segment-segmentdurationseconds): {{Integer}}
  [SegmentName](#cfn-mediapackagev2-originendpoint-segment-segmentname): {{String}}
  [TsIncludeDvbSubtitles](#cfn-mediapackagev2-originendpoint-segment-tsincludedvbsubtitles): {{Boolean}}
  [TsUseAudioRenditionGroup](#cfn-mediapackagev2-originendpoint-segment-tsuseaudiorenditiongroup): {{Boolean}}
```

## Properties
<a name="aws-properties-mediapackagev2-originendpoint-segment-properties"></a>

`Encryption`  <a name="cfn-mediapackagev2-originendpoint-segment-encryption"></a>
Whether to use encryption for the segment.
*Required*: No
*Type*: [Encryption](aws-properties-mediapackagev2-originendpoint-encryption.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IncludeIframeOnlyStreams`  <a name="cfn-mediapackagev2-originendpoint-segment-includeiframeonlystreams"></a>
Whether the segment includes I-frame-only streams.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OutputTimestampMode`  <a name="cfn-mediapackagev2-originendpoint-segment-outputtimestampmode"></a>
The output timestamp mode for the origin endpoint's segments. This setting is only configurable on channels with `OutputLockingMode` set to `NON_EPOCH_LOCKED`. This value is immutable after endpoint creation. If you don't specify a value, the default is `PASSTHROUGH`.
The allowed values are:
+ `PASSTHROUGH` - Output PTS (Presentation Timestamp) values pass through unchanged from the input.
+ `REBASED_TO_CHANNEL_START` - Output PTS is rebased relative to the channel start time.
*Required*: No
*Type*: String
*Allowed values*: `PASSTHROUGH | REBASED_TO_CHANNEL_START`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Scte`  <a name="cfn-mediapackagev2-originendpoint-segment-scte"></a>
The SCTE-35 configuration associated with the segment.
*Required*: No
*Type*: [Scte](aws-properties-mediapackagev2-originendpoint-scte.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SegmentDurationSeconds`  <a name="cfn-mediapackagev2-originendpoint-segment-segmentdurationseconds"></a>
The duration of the segment, in seconds.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `30`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SegmentName`  <a name="cfn-mediapackagev2-originendpoint-segment-segmentname"></a>
The name of the segment associated with the origin endpoint.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TsIncludeDvbSubtitles`  <a name="cfn-mediapackagev2-originendpoint-segment-tsincludedvbsubtitles"></a>
Whether the segment includes DVB subtitles.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TsUseAudioRenditionGroup`  <a name="cfn-mediapackagev2-originendpoint-segment-tsuseaudiorenditiongroup"></a>
Whether the segment is an audio rendition group.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
