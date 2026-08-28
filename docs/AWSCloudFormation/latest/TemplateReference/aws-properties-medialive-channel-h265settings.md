---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-h265settings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel H265Settings
<a name="aws-properties-medialive-channel-h265settings"></a>

H265 Settings

The parent of this entity is VideoCodecSettings.

## Syntax
<a name="aws-properties-medialive-channel-h265settings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-h265settings-syntax.json"></a>

```
{
  "[AdaptiveQuantization](#cfn-medialive-channel-h265settings-adaptivequantization)" : {{String}},
  "[AfdSignaling](#cfn-medialive-channel-h265settings-afdsignaling)" : {{String}},
  "[AlternativeTransferFunction](#cfn-medialive-channel-h265settings-alternativetransferfunction)" : {{String}},
  "[Bitrate](#cfn-medialive-channel-h265settings-bitrate)" : {{Integer}},
  "[BufSize](#cfn-medialive-channel-h265settings-bufsize)" : {{Integer}},
  "[ColorMetadata](#cfn-medialive-channel-h265settings-colormetadata)" : {{String}},
  "[ColorSpaceSettings](#cfn-medialive-channel-h265settings-colorspacesettings)" : {{H265ColorSpaceSettings}},
  "[Deblocking](#cfn-medialive-channel-h265settings-deblocking)" : {{String}},
  "[FilterSettings](#cfn-medialive-channel-h265settings-filtersettings)" : {{H265FilterSettings}},
  "[FixedAfd](#cfn-medialive-channel-h265settings-fixedafd)" : {{String}},
  "[FlickerAq](#cfn-medialive-channel-h265settings-flickeraq)" : {{String}},
  "[FramerateDenominator](#cfn-medialive-channel-h265settings-frameratedenominator)" : {{Integer}},
  "[FramerateNumerator](#cfn-medialive-channel-h265settings-frameratenumerator)" : {{Integer}},
  "[GopBReference](#cfn-medialive-channel-h265settings-gopbreference)" : {{String}},
  "[GopClosedCadence](#cfn-medialive-channel-h265settings-gopclosedcadence)" : {{Integer}},
  "[GopNumBFrames](#cfn-medialive-channel-h265settings-gopnumbframes)" : {{Integer}},
  "[GopSize](#cfn-medialive-channel-h265settings-gopsize)" : {{Number}},
  "[GopSizeUnits](#cfn-medialive-channel-h265settings-gopsizeunits)" : {{String}},
  "[Level](#cfn-medialive-channel-h265settings-level)" : {{String}},
  "[LookAheadRateControl](#cfn-medialive-channel-h265settings-lookaheadratecontrol)" : {{String}},
  "[MaxBitrate](#cfn-medialive-channel-h265settings-maxbitrate)" : {{Integer}},
  "[MinBitrate](#cfn-medialive-channel-h265settings-minbitrate)" : {{Integer}},
  "[MinIInterval](#cfn-medialive-channel-h265settings-miniinterval)" : {{Integer}},
  "[MinQp](#cfn-medialive-channel-h265settings-minqp)" : {{Integer}},
  "[MvOverPictureBoundaries](#cfn-medialive-channel-h265settings-mvoverpictureboundaries)" : {{String}},
  "[MvTemporalPredictor](#cfn-medialive-channel-h265settings-mvtemporalpredictor)" : {{String}},
  "[ParDenominator](#cfn-medialive-channel-h265settings-pardenominator)" : {{Integer}},
  "[ParNumerator](#cfn-medialive-channel-h265settings-parnumerator)" : {{Integer}},
  "[Profile](#cfn-medialive-channel-h265settings-profile)" : {{String}},
  "[QvbrQualityLevel](#cfn-medialive-channel-h265settings-qvbrqualitylevel)" : {{Integer}},
  "[RateControlMode](#cfn-medialive-channel-h265settings-ratecontrolmode)" : {{String}},
  "[ScanType](#cfn-medialive-channel-h265settings-scantype)" : {{String}},
  "[SceneChangeDetect](#cfn-medialive-channel-h265settings-scenechangedetect)" : {{String}},
  "[Slices](#cfn-medialive-channel-h265settings-slices)" : {{Integer}},
  "[SubgopLength](#cfn-medialive-channel-h265settings-subgoplength)" : {{String}},
  "[Tier](#cfn-medialive-channel-h265settings-tier)" : {{String}},
  "[TileHeight](#cfn-medialive-channel-h265settings-tileheight)" : {{Integer}},
  "[TilePadding](#cfn-medialive-channel-h265settings-tilepadding)" : {{String}},
  "[TileWidth](#cfn-medialive-channel-h265settings-tilewidth)" : {{Integer}},
  "[TimecodeBurninSettings](#cfn-medialive-channel-h265settings-timecodeburninsettings)" : {{TimecodeBurninSettings}},
  "[TimecodeInsertion](#cfn-medialive-channel-h265settings-timecodeinsertion)" : {{String}},
  "[TreeblockSize](#cfn-medialive-channel-h265settings-treeblocksize)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-channel-h265settings-syntax.yaml"></a>

```
  [AdaptiveQuantization](#cfn-medialive-channel-h265settings-adaptivequantization): {{String}}
  [AfdSignaling](#cfn-medialive-channel-h265settings-afdsignaling): {{String}}
  [AlternativeTransferFunction](#cfn-medialive-channel-h265settings-alternativetransferfunction): {{String}}
  [Bitrate](#cfn-medialive-channel-h265settings-bitrate): {{Integer}}
  [BufSize](#cfn-medialive-channel-h265settings-bufsize): {{Integer}}
  [ColorMetadata](#cfn-medialive-channel-h265settings-colormetadata): {{String}}
  [ColorSpaceSettings](#cfn-medialive-channel-h265settings-colorspacesettings): {{
    H265ColorSpaceSettings}}
  [Deblocking](#cfn-medialive-channel-h265settings-deblocking): {{String}}
  [FilterSettings](#cfn-medialive-channel-h265settings-filtersettings): {{
    H265FilterSettings}}
  [FixedAfd](#cfn-medialive-channel-h265settings-fixedafd): {{String}}
  [FlickerAq](#cfn-medialive-channel-h265settings-flickeraq): {{String}}
  [FramerateDenominator](#cfn-medialive-channel-h265settings-frameratedenominator): {{Integer}}
  [FramerateNumerator](#cfn-medialive-channel-h265settings-frameratenumerator): {{Integer}}
  [GopBReference](#cfn-medialive-channel-h265settings-gopbreference): {{String}}
  [GopClosedCadence](#cfn-medialive-channel-h265settings-gopclosedcadence): {{Integer}}
  [GopNumBFrames](#cfn-medialive-channel-h265settings-gopnumbframes): {{Integer}}
  [GopSize](#cfn-medialive-channel-h265settings-gopsize): {{Number}}
  [GopSizeUnits](#cfn-medialive-channel-h265settings-gopsizeunits): {{String}}
  [Level](#cfn-medialive-channel-h265settings-level): {{String}}
  [LookAheadRateControl](#cfn-medialive-channel-h265settings-lookaheadratecontrol): {{String}}
  [MaxBitrate](#cfn-medialive-channel-h265settings-maxbitrate): {{Integer}}
  [MinBitrate](#cfn-medialive-channel-h265settings-minbitrate): {{Integer}}
  [MinIInterval](#cfn-medialive-channel-h265settings-miniinterval): {{Integer}}
  [MinQp](#cfn-medialive-channel-h265settings-minqp): {{Integer}}
  [MvOverPictureBoundaries](#cfn-medialive-channel-h265settings-mvoverpictureboundaries): {{String}}
  [MvTemporalPredictor](#cfn-medialive-channel-h265settings-mvtemporalpredictor): {{String}}
  [ParDenominator](#cfn-medialive-channel-h265settings-pardenominator): {{Integer}}
  [ParNumerator](#cfn-medialive-channel-h265settings-parnumerator): {{Integer}}
  [Profile](#cfn-medialive-channel-h265settings-profile): {{String}}
  [QvbrQualityLevel](#cfn-medialive-channel-h265settings-qvbrqualitylevel): {{Integer}}
  [RateControlMode](#cfn-medialive-channel-h265settings-ratecontrolmode): {{String}}
  [ScanType](#cfn-medialive-channel-h265settings-scantype): {{String}}
  [SceneChangeDetect](#cfn-medialive-channel-h265settings-scenechangedetect): {{String}}
  [Slices](#cfn-medialive-channel-h265settings-slices): {{Integer}}
  [SubgopLength](#cfn-medialive-channel-h265settings-subgoplength): {{String}}
  [Tier](#cfn-medialive-channel-h265settings-tier): {{String}}
  [TileHeight](#cfn-medialive-channel-h265settings-tileheight): {{Integer}}
  [TilePadding](#cfn-medialive-channel-h265settings-tilepadding): {{String}}
  [TileWidth](#cfn-medialive-channel-h265settings-tilewidth): {{Integer}}
  [TimecodeBurninSettings](#cfn-medialive-channel-h265settings-timecodeburninsettings): {{
    TimecodeBurninSettings}}
  [TimecodeInsertion](#cfn-medialive-channel-h265settings-timecodeinsertion): {{String}}
  [TreeblockSize](#cfn-medialive-channel-h265settings-treeblocksize): {{String}}
```

## Properties
<a name="aws-properties-medialive-channel-h265settings-properties"></a>

`AdaptiveQuantization`  <a name="cfn-medialive-channel-h265settings-adaptivequantization"></a>
Adaptive quantization. Allows intra-frame quantizers to vary to improve visual quality.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AfdSignaling`  <a name="cfn-medialive-channel-h265settings-afdsignaling"></a>
Indicates that AFD values will be written into the output stream. If afdSignaling is "auto", the system will try to preserve the input AFD value (in cases where multiple AFD values are valid). If set to "fixed", the AFD value will be the value configured in the fixedAfd parameter.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AlternativeTransferFunction`  <a name="cfn-medialive-channel-h265settings-alternativetransferfunction"></a>
Whether or not EML should insert an Alternative Transfer Function SEI message to support backwards compatibility with non-HDR decoders and displays.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Bitrate`  <a name="cfn-medialive-channel-h265settings-bitrate"></a>
Average bitrate in bits/second. Required when the rate control mode is VBR or CBR. Not used for QVBR. In an MS Smooth output group, each output must have a unique value when its bitrate is rounded down to the nearest multiple of 1000.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BufSize`  <a name="cfn-medialive-channel-h265settings-bufsize"></a>
Size of buffer (HRD buffer model) in bits.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ColorMetadata`  <a name="cfn-medialive-channel-h265settings-colormetadata"></a>
Includes colorspace metadata in the output.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ColorSpaceSettings`  <a name="cfn-medialive-channel-h265settings-colorspacesettings"></a>
Color Space settings
*Required*: No
*Type*: [H265ColorSpaceSettings](aws-properties-medialive-channel-h265colorspacesettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Deblocking`  <a name="cfn-medialive-channel-h265settings-deblocking"></a>
Enable or disable the deblocking filter for this codec. The filter reduces blocking artifacts at block boundaries, which improves overall video quality. If the filter is disabled, visible block edges might appear in the output, especially at lower bitrates.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FilterSettings`  <a name="cfn-medialive-channel-h265settings-filtersettings"></a>
Optional filters that you can apply to an encode.
*Required*: No
*Type*: [H265FilterSettings](aws-properties-medialive-channel-h265filtersettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FixedAfd`  <a name="cfn-medialive-channel-h265settings-fixedafd"></a>
Four bit AFD value to write on all frames of video in the output stream. Only valid when afdSignaling is set to 'Fixed'.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FlickerAq`  <a name="cfn-medialive-channel-h265settings-flickeraq"></a>
If set to enabled, adjust quantization within each frame to reduce flicker or 'pop' on I-frames.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FramerateDenominator`  <a name="cfn-medialive-channel-h265settings-frameratedenominator"></a>
Framerate denominator.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FramerateNumerator`  <a name="cfn-medialive-channel-h265settings-frameratenumerator"></a>
Framerate numerator - framerate is a fraction, e.g. 24000 / 1001 = 23.976 fps.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GopBReference`  <a name="cfn-medialive-channel-h265settings-gopbreference"></a>
Allows the encoder to use a B-Frame as a reference frame as well. ENABLED: B-frames will also serve as reference frames. DISABLED: B-frames won't be reference frames. Must be DISABLED if resolution is greater than 1080p or when using tiled HEVC encoding.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GopClosedCadence`  <a name="cfn-medialive-channel-h265settings-gopclosedcadence"></a>
Frequency of closed GOPs. In streaming applications, it is recommended that this be set to 1 so a decoder joining mid-stream will receive an IDR frame as quickly as possible. Setting this value to 0 will break output segmenting.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GopNumBFrames`  <a name="cfn-medialive-channel-h265settings-gopnumbframes"></a>
Sets the number of B-frames between reference frames. Set to 2 if resolution is greater than 1080p or when using tiled HEVC encoding.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GopSize`  <a name="cfn-medialive-channel-h265settings-gopsize"></a>
GOP size (keyframe interval) in units of either frames or seconds per gopSizeUnits. If gopSizeUnits is frames, gopSize must be an integer and must be greater than or equal to 1. If gopSizeUnits is seconds, gopSize must be greater than 0, but need not be an integer.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GopSizeUnits`  <a name="cfn-medialive-channel-h265settings-gopsizeunits"></a>
Indicates if the gopSize is specified in frames or seconds. If seconds the system will convert the gopSize into a frame count at run time.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Level`  <a name="cfn-medialive-channel-h265settings-level"></a>
H.265 Level.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LookAheadRateControl`  <a name="cfn-medialive-channel-h265settings-lookaheadratecontrol"></a>
Amount of lookahead. A value of low can decrease latency and memory usage, while high can produce better quality for certain content.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxBitrate`  <a name="cfn-medialive-channel-h265settings-maxbitrate"></a>
For QVBR: See the tooltip for Quality level
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinBitrate`  <a name="cfn-medialive-channel-h265settings-minbitrate"></a>
Used for QVBR rate control mode only. Optional. Enter a minimum bitrate if you want to keep the output bitrate above a threshold, in order to prevent the downstream system from de-allocating network bandwidth for this output.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinIInterval`  <a name="cfn-medialive-channel-h265settings-miniinterval"></a>
Only meaningful if sceneChangeDetect is set to enabled. Defaults to 5 if multiplex rate control is used. Enforces separation between repeated (cadence) I-frames and I-frames inserted by Scene Change Detection. If a scene change I-frame is within I-interval frames of a cadence I-frame, the GOP is shrunk and/or stretched to the scene change I-frame. GOP stretch requires enabling lookahead as well as setting I-interval. The normal cadence resumes for the next GOP. Note: Maximum GOP stretch = GOP size \+ Min-I-interval - 1
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinQp`  <a name="cfn-medialive-channel-h265settings-minqp"></a>
Sets the minimum QP. If you aren't familiar with quantization adjustment, leave the field empty. MediaLive will apply an appropriate value.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MvOverPictureBoundaries`  <a name="cfn-medialive-channel-h265settings-mvoverpictureboundaries"></a>
If you are setting up the picture as a tile, you must set this to disabled. In all other configurations, you typically enter enabled.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MvTemporalPredictor`  <a name="cfn-medialive-channel-h265settings-mvtemporalpredictor"></a>
If you are setting up the picture as a tile, you must set this to disabled. In other configurations, you typically enter enabled.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParDenominator`  <a name="cfn-medialive-channel-h265settings-pardenominator"></a>
Pixel Aspect Ratio denominator.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParNumerator`  <a name="cfn-medialive-channel-h265settings-parnumerator"></a>
Pixel Aspect Ratio numerator.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Profile`  <a name="cfn-medialive-channel-h265settings-profile"></a>
H.265 Profile.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`QvbrQualityLevel`  <a name="cfn-medialive-channel-h265settings-qvbrqualitylevel"></a>
Controls the target quality for the video encode. Applies only when the rate control mode is QVBR. Set values for the QVBR quality level field and Max bitrate field that suit your most important viewing devices. Recommended values are: - Primary screen: Quality level: 8 to 10. Max bitrate: 4M - PC or tablet: Quality level: 7. Max bitrate: 1.5M to 3M - Smartphone: Quality level: 6. Max bitrate: 1M to 1.5M
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RateControlMode`  <a name="cfn-medialive-channel-h265settings-ratecontrolmode"></a>
Rate control mode. QVBR: Quality will match the specified quality level except when it is constrained by the maximum bitrate. Recommended if you or your viewers pay for bandwidth. CBR: Quality varies, depending on the video complexity. Recommended only if you distribute your assets to devices that cannot handle variable bitrates. Multiplex: This rate control mode is only supported (and is required) when the video is being delivered to a MediaLive Multiplex in which case the rate control configuration is controlled by the properties within the Multiplex Program.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScanType`  <a name="cfn-medialive-channel-h265settings-scantype"></a>
Sets the scan type of the output to progressive or top-field-first interlaced.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SceneChangeDetect`  <a name="cfn-medialive-channel-h265settings-scenechangedetect"></a>
Scene change detection.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Slices`  <a name="cfn-medialive-channel-h265settings-slices"></a>
Number of slices per picture. Must be less than or equal to the number of macroblock rows for progressive pictures, and less than or equal to half the number of macroblock rows for interlaced pictures. This field is optional; when no value is specified the encoder will choose the number of slices based on encode resolution.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubgopLength`  <a name="cfn-medialive-channel-h265settings-subgoplength"></a>
Sets the number of B-frames in each sub-GOP. FIXED: Use the value in Num B-frames. DYNAMIC: Optimizes the number of B-frames in each sub-GOP to improve visual quality. Must be FIXED if resolution is greater than 1080p or when using tiled HEVC encoding.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tier`  <a name="cfn-medialive-channel-h265settings-tier"></a>
H.265 Tier.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TileHeight`  <a name="cfn-medialive-channel-h265settings-tileheight"></a>
Set this field to set up the picture as a tile. You must also set TileWidth. The tile height must result in 22 or fewer rows in the frame. The tile width must result in 20 or fewer columns in the frame. And finally, the product of the column count and row count must be 64 or less. If the tile width and height are specified, MediaLive will override the video codec slices field with a value that MediaLive calculates.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TilePadding`  <a name="cfn-medialive-channel-h265settings-tilepadding"></a>
Set to padded to force MediaLive to add padding to the frame, to obtain a frame that is a whole multiple of the tile size. If you are setting up the picture as a tile, you must enter padded. In all other configurations, you typically enter none.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TileWidth`  <a name="cfn-medialive-channel-h265settings-tilewidth"></a>
Set this field to set up the picture as a tile. See TileHeight for more information.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimecodeBurninSettings`  <a name="cfn-medialive-channel-h265settings-timecodeburninsettings"></a>
Timecode burn-in settings for the H.265 codec.
*Required*: No
*Type*: [TimecodeBurninSettings](aws-properties-medialive-channel-timecodeburninsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimecodeInsertion`  <a name="cfn-medialive-channel-h265settings-timecodeinsertion"></a>
Determines how timecodes should be inserted into the video elementary stream. - 'disabled': Do not include timecodes - 'picTimingSei': Pass through picture timing SEI messages from the source specified in Timecode Config
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TreeblockSize`  <a name="cfn-medialive-channel-h265settings-treeblocksize"></a>
Select the tree block size used for encoding. If you enter auto, the encoder will pick the best size. If you are setting up the picture as a tile, you must set this to 32x32. In all other configurations, you typically enter auto.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
