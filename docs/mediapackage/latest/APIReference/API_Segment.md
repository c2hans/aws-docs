---
source_url: https://docs.aws.amazon.com/mediapackage/latest/APIReference/API_Segment.html
---

# Segment
<a name="API_Segment"></a>

The segment configuration, including the segment name, duration, and other configuration values.

## Contents
<a name="API_Segment_Contents"></a>

 ** Encryption **   <a name="mediapackage-Type-Segment-Encryption"></a>
The parameters for encrypting content.
Type: [Encryption](API_Encryption.md) object
Required: No

 ** IncludeIframeOnlyStreams **   <a name="mediapackage-Type-Segment-IncludeIframeOnlyStreams"></a>
When selected, the stream set includes an additional I-frame only stream, along with the other tracks. If false, this extra stream is not included. MediaPackage generates an I-frame only stream from the first rendition in the manifest. The service inserts EXT-I-FRAMES-ONLY tags in the output manifest, and then generates and includes an I-frames only playlist in the stream. This playlist permits player functionality like fast forward and rewind.
Type: Boolean
Required: No

 ** OutputTimestampMode **   <a name="mediapackage-Type-Segment-OutputTimestampMode"></a>
The output timestamp mode for the origin endpoint's segments. This setting is only configurable on channels with `OutputLockingMode` set to `NON_EPOCH_LOCKED`. This value is immutable after endpoint creation. If you don't specify a value, the default is `PASSTHROUGH`.
The allowed values are:
+  `PASSTHROUGH` - Output PTS (Presentation Timestamp) values pass through unchanged from the input.
+  `REBASED_TO_CHANNEL_START` - Output PTS is rebased relative to the channel start time.
Type: String
Valid Values: `PASSTHROUGH | REBASED_TO_CHANNEL_START`
Required: No

 ** Scte **   <a name="mediapackage-Type-Segment-Scte"></a>
The SCTE configuration options in the segment settings.
Type: [Scte](API_Scte.md) object
Required: No

 ** SegmentDurationSeconds **   <a name="mediapackage-Type-Segment-SegmentDurationSeconds"></a>
The duration (in seconds) of each segment. Enter a value equal to, or a multiple of, the input segment duration. If the value that you enter is different from the input segment duration, MediaPackage rounds segments to the nearest multiple of the input segment duration.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 30.
Required: No

 ** SegmentName **   <a name="mediapackage-Type-Segment-SegmentName"></a>
The name that describes the segment. The name is the base name of the segment used in all content manifests inside of the endpoint. You can't use spaces in the name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

 ** TsIncludeDvbSubtitles **   <a name="mediapackage-Type-Segment-TsIncludeDvbSubtitles"></a>
By default, MediaPackage excludes all digital video broadcasting (DVB) subtitles from the output. When selected, MediaPackage passes through DVB subtitles into the output.
Type: Boolean
Required: No

 ** TsUseAudioRenditionGroup **   <a name="mediapackage-Type-Segment-TsUseAudioRenditionGroup"></a>
When selected, MediaPackage bundles all audio tracks in a rendition group. All other tracks in the stream can be used with any audio rendition from the group.
Type: Boolean
Required: No

## See Also
<a name="API_Segment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediapackagev2-2022-12-25/Segment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediapackagev2-2022-12-25/Segment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediapackagev2-2022-12-25/Segment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage V2 Live API. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
