---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-av1settings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel Av1Settings
<a name="aws-properties-medialive-channel-av1settings"></a>

Av1 Settings

## Syntax
<a name="aws-properties-medialive-channel-av1settings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-av1settings-syntax.json"></a>

```
{
  "[AfdSignaling](#cfn-medialive-channel-av1settings-afdsignaling)" : {{String}},
  "[BitDepth](#cfn-medialive-channel-av1settings-bitdepth)" : {{String}},
  "[Bitrate](#cfn-medialive-channel-av1settings-bitrate)" : {{Integer}},
  "[BufSize](#cfn-medialive-channel-av1settings-bufsize)" : {{Integer}},
  "[ColorSpaceSettings](#cfn-medialive-channel-av1settings-colorspacesettings)" : {{Av1ColorSpaceSettings}},
  "[FixedAfd](#cfn-medialive-channel-av1settings-fixedafd)" : {{String}},
  "[FramerateDenominator](#cfn-medialive-channel-av1settings-frameratedenominator)" : {{Integer}},
  "[FramerateNumerator](#cfn-medialive-channel-av1settings-frameratenumerator)" : {{Integer}},
  "[GopSize](#cfn-medialive-channel-av1settings-gopsize)" : {{Number}},
  "[GopSizeUnits](#cfn-medialive-channel-av1settings-gopsizeunits)" : {{String}},
  "[Level](#cfn-medialive-channel-av1settings-level)" : {{String}},
  "[LookAheadRateControl](#cfn-medialive-channel-av1settings-lookaheadratecontrol)" : {{String}},
  "[MaxBitrate](#cfn-medialive-channel-av1settings-maxbitrate)" : {{Integer}},
  "[MinBitrate](#cfn-medialive-channel-av1settings-minbitrate)" : {{Integer}},
  "[MinIInterval](#cfn-medialive-channel-av1settings-miniinterval)" : {{Integer}},
  "[ParDenominator](#cfn-medialive-channel-av1settings-pardenominator)" : {{Integer}},
  "[ParNumerator](#cfn-medialive-channel-av1settings-parnumerator)" : {{Integer}},
  "[QvbrQualityLevel](#cfn-medialive-channel-av1settings-qvbrqualitylevel)" : {{Integer}},
  "[RateControlMode](#cfn-medialive-channel-av1settings-ratecontrolmode)" : {{String}},
  "[SceneChangeDetect](#cfn-medialive-channel-av1settings-scenechangedetect)" : {{String}},
  "[SpatialAq](#cfn-medialive-channel-av1settings-spatialaq)" : {{String}},
  "[TemporalAq](#cfn-medialive-channel-av1settings-temporalaq)" : {{String}},
  "[TimecodeBurninSettings](#cfn-medialive-channel-av1settings-timecodeburninsettings)" : {{TimecodeBurninSettings}},
  "[TimecodeInsertion](#cfn-medialive-channel-av1settings-timecodeinsertion)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-channel-av1settings-syntax.yaml"></a>

```
  [AfdSignaling](#cfn-medialive-channel-av1settings-afdsignaling): {{String}}
  [BitDepth](#cfn-medialive-channel-av1settings-bitdepth): {{String}}
  [Bitrate](#cfn-medialive-channel-av1settings-bitrate): {{Integer}}
  [BufSize](#cfn-medialive-channel-av1settings-bufsize): {{Integer}}
  [ColorSpaceSettings](#cfn-medialive-channel-av1settings-colorspacesettings): {{
    Av1ColorSpaceSettings}}
  [FixedAfd](#cfn-medialive-channel-av1settings-fixedafd): {{String}}
  [FramerateDenominator](#cfn-medialive-channel-av1settings-frameratedenominator): {{Integer}}
  [FramerateNumerator](#cfn-medialive-channel-av1settings-frameratenumerator): {{Integer}}
  [GopSize](#cfn-medialive-channel-av1settings-gopsize): {{Number}}
  [GopSizeUnits](#cfn-medialive-channel-av1settings-gopsizeunits): {{String}}
  [Level](#cfn-medialive-channel-av1settings-level): {{String}}
  [LookAheadRateControl](#cfn-medialive-channel-av1settings-lookaheadratecontrol): {{String}}
  [MaxBitrate](#cfn-medialive-channel-av1settings-maxbitrate): {{Integer}}
  [MinBitrate](#cfn-medialive-channel-av1settings-minbitrate): {{Integer}}
  [MinIInterval](#cfn-medialive-channel-av1settings-miniinterval): {{Integer}}
  [ParDenominator](#cfn-medialive-channel-av1settings-pardenominator): {{Integer}}
  [ParNumerator](#cfn-medialive-channel-av1settings-parnumerator): {{Integer}}
  [QvbrQualityLevel](#cfn-medialive-channel-av1settings-qvbrqualitylevel): {{Integer}}
  [RateControlMode](#cfn-medialive-channel-av1settings-ratecontrolmode): {{String}}
  [SceneChangeDetect](#cfn-medialive-channel-av1settings-scenechangedetect): {{String}}
  [SpatialAq](#cfn-medialive-channel-av1settings-spatialaq): {{String}}
  [TemporalAq](#cfn-medialive-channel-av1settings-temporalaq): {{String}}
  [TimecodeBurninSettings](#cfn-medialive-channel-av1settings-timecodeburninsettings): {{
    TimecodeBurninSettings}}
  [TimecodeInsertion](#cfn-medialive-channel-av1settings-timecodeinsertion): {{String}}
```

## Properties
<a name="aws-properties-medialive-channel-av1settings-properties"></a>

`AfdSignaling`  <a name="cfn-medialive-channel-av1settings-afdsignaling"></a>
Configures whether MediaLive will write AFD values into the video. AUTO: MediaLive will try to preserve the input AFD value (in cases where multiple AFD values are valid). FIXED: the AFD value will be the value configured in the fixedAfd parameter. NONE: MediaLive won't write AFD into the video.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BitDepth`  <a name="cfn-medialive-channel-av1settings-bitdepth"></a>
Specifies the bit depth for the output encode. Choose a value. Or leave the field empty to use the default, which is 8 bit.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Bitrate`  <a name="cfn-medialive-channel-av1settings-bitrate"></a>
Average bitrate in bits/second. Required when the rate control mode is CBR. Not used for QVBR.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BufSize`  <a name="cfn-medialive-channel-av1settings-bufsize"></a>
The size of the buffer (HRD buffer model) in bits.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ColorSpaceSettings`  <a name="cfn-medialive-channel-av1settings-colorspacesettings"></a>
Specify the type of color space to apply or choose to pass through. The default is to pass through the color space that is in the source.
*Required*: No
*Type*: [Av1ColorSpaceSettings](aws-properties-medialive-channel-av1colorspacesettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FixedAfd`  <a name="cfn-medialive-channel-av1settings-fixedafd"></a>
Complete this property only if you set the afdSignaling property to FIXED. Choose the AFD value (4 bits) to write on all frames of the video encode.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FramerateDenominator`  <a name="cfn-medialive-channel-av1settings-frameratedenominator"></a>
The denominator for the framerate. Framerate is a fraction, for example, 24000 / 1001.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FramerateNumerator`  <a name="cfn-medialive-channel-av1settings-frameratenumerator"></a>
The numerator for the framerate. Framerate is a fraction, for example, 24000 / 1001.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GopSize`  <a name="cfn-medialive-channel-av1settings-gopsize"></a>
The GOP size (keyframe interval). If GopSizeUnits is frames, GopSize must be a whole number and must be greater than or equal to 1. If GopSizeUnits is seconds, GopSize must be greater than 0, but it can be a decimal.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GopSizeUnits`  <a name="cfn-medialive-channel-av1settings-gopsizeunits"></a>
Choose the units for the GOP size: FRAMES or SECONDS. For SECONDS, MediaLive converts the size into a frame count at run time.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Level`  <a name="cfn-medialive-channel-av1settings-level"></a>
Sets the level. This parameter is one of the properties of the encoding scheme for AV1.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LookAheadRateControl`  <a name="cfn-medialive-channel-av1settings-lookaheadratecontrol"></a>
Sets the amount of lookahead. A value of LOW can decrease latency and memory usage. A value of HIGH can produce better quality for certain content.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxBitrate`  <a name="cfn-medialive-channel-av1settings-maxbitrate"></a>
The maximum bitrate to assign. For recommendations, see the description for qvbrQualityLevel.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinBitrate`  <a name="cfn-medialive-channel-av1settings-minbitrate"></a>
Used for QVBR rate control mode only. Optional. Enter a minimum bitrate if you want to keep the output bitrate about a threshold, in order to prevent the downstream system from de-allocating network bandwidth for this output.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinIInterval`  <a name="cfn-medialive-channel-av1settings-miniinterval"></a>
Applies only if you enable SceneChangeDetect. Sets the interval between frames. This property ensures a minimum separation between repeated (cadence) I-frames and any I-frames inserted by scene change detection (SCD frames). Enter a number for the interval, measured in number of frames.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParDenominator`  <a name="cfn-medialive-channel-av1settings-pardenominator"></a>
The denominator for the output pixel aspect ratio (PAR).
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParNumerator`  <a name="cfn-medialive-channel-av1settings-parnumerator"></a>
The numerator for the output pixel aspect ratio (PAR).
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`QvbrQualityLevel`  <a name="cfn-medialive-channel-av1settings-qvbrqualitylevel"></a>
Controls the target quality for the video encode. With QVBR rate control mode, the final quality is the target quality, constrained by the maxBitrate. Set values for the qvbrQualityLevel property and maxBitrate property that suit your most important viewing devices.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RateControlMode`  <a name="cfn-medialive-channel-av1settings-ratecontrolmode"></a>
Rate control mode. QVBR: Quality will match the specified quality level except when it is constrained by the maximum bitrate. Recommended if you or your viewers pay for bandwidth. CBR: Quality varies, depending on the video complexity. Recommended only if you distribute your assets to devices that cannot handle variable bitrates.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SceneChangeDetect`  <a name="cfn-medialive-channel-av1settings-scenechangedetect"></a>
Controls whether MediaLive inserts I-frames when it detects a scene change. ENABLED or DISABLED.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SpatialAq`  <a name="cfn-medialive-channel-av1settings-spatialaq"></a>
Spatial AQ makes adjustments within each frame based on spatial variation of content complexity. Enabled: MediaLive will determine the appropriate level of spatial AQ to apply. Disabled: No spatial AQ.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TemporalAq`  <a name="cfn-medialive-channel-av1settings-temporalaq"></a>
Temporal AQ makes adjustments within each frame based on variations in content complexity over time. Enabled: MediaLive will determine the appropriate level of temporal AQ to apply. Disabled: No temporal AQ.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimecodeBurninSettings`  <a name="cfn-medialive-channel-av1settings-timecodeburninsettings"></a>
Configures the timecode burn-in feature. If you enable this feature, the timecode will become part of the video.
*Required*: No
*Type*: [TimecodeBurninSettings](aws-properties-medialive-channel-timecodeburninsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimecodeInsertion`  <a name="cfn-medialive-channel-av1settings-timecodeinsertion"></a>
Controls how MediaLive inserts timecodes into the video output encode. DISABLED: Do not insert timecodes. METADATA\_OBU: Include timecodes. MediaLive inserts timecode metadata based on the timecode from the source specified in the Timecode Config property.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
