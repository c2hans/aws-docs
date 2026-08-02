---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-multiplexm2tssettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel MultiplexM2tsSettings
<a name="aws-properties-medialive-channel-multiplexm2tssettings"></a>

Multiplex M2TS settings.

The parent of this entity is MultiplexContainerSettings.

## Syntax
<a name="aws-properties-medialive-channel-multiplexm2tssettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-multiplexm2tssettings-syntax.json"></a>

```
{
  "[AbsentInputAudioBehavior](#cfn-medialive-channel-multiplexm2tssettings-absentinputaudiobehavior)" : {{String}},
  "[Arib](#cfn-medialive-channel-multiplexm2tssettings-arib)" : {{String}},
  "[AudioBufferModel](#cfn-medialive-channel-multiplexm2tssettings-audiobuffermodel)" : {{String}},
  "[AudioFramesPerPes](#cfn-medialive-channel-multiplexm2tssettings-audioframesperpes)" : {{Integer}},
  "[AudioStreamType](#cfn-medialive-channel-multiplexm2tssettings-audiostreamtype)" : {{String}},
  "[CcDescriptor](#cfn-medialive-channel-multiplexm2tssettings-ccdescriptor)" : {{String}},
  "[Ebif](#cfn-medialive-channel-multiplexm2tssettings-ebif)" : {{String}},
  "[EsRateInPes](#cfn-medialive-channel-multiplexm2tssettings-esrateinpes)" : {{String}},
  "[Klv](#cfn-medialive-channel-multiplexm2tssettings-klv)" : {{String}},
  "[NielsenId3Behavior](#cfn-medialive-channel-multiplexm2tssettings-nielsenid3behavior)" : {{String}},
  "[PcrControl](#cfn-medialive-channel-multiplexm2tssettings-pcrcontrol)" : {{String}},
  "[PcrPeriod](#cfn-medialive-channel-multiplexm2tssettings-pcrperiod)" : {{Integer}},
  "[Scte35Control](#cfn-medialive-channel-multiplexm2tssettings-scte35control)" : {{String}},
  "[Scte35PrerollPullupMilliseconds](#cfn-medialive-channel-multiplexm2tssettings-scte35prerollpullupmilliseconds)" : {{Number}}
}
```

### YAML
<a name="aws-properties-medialive-channel-multiplexm2tssettings-syntax.yaml"></a>

```
  [AbsentInputAudioBehavior](#cfn-medialive-channel-multiplexm2tssettings-absentinputaudiobehavior): {{String}}
  [Arib](#cfn-medialive-channel-multiplexm2tssettings-arib): {{String}}
  [AudioBufferModel](#cfn-medialive-channel-multiplexm2tssettings-audiobuffermodel): {{String}}
  [AudioFramesPerPes](#cfn-medialive-channel-multiplexm2tssettings-audioframesperpes): {{Integer}}
  [AudioStreamType](#cfn-medialive-channel-multiplexm2tssettings-audiostreamtype): {{String}}
  [CcDescriptor](#cfn-medialive-channel-multiplexm2tssettings-ccdescriptor): {{String}}
  [Ebif](#cfn-medialive-channel-multiplexm2tssettings-ebif): {{String}}
  [EsRateInPes](#cfn-medialive-channel-multiplexm2tssettings-esrateinpes): {{String}}
  [Klv](#cfn-medialive-channel-multiplexm2tssettings-klv): {{String}}
  [NielsenId3Behavior](#cfn-medialive-channel-multiplexm2tssettings-nielsenid3behavior): {{String}}
  [PcrControl](#cfn-medialive-channel-multiplexm2tssettings-pcrcontrol): {{String}}
  [PcrPeriod](#cfn-medialive-channel-multiplexm2tssettings-pcrperiod): {{Integer}}
  [Scte35Control](#cfn-medialive-channel-multiplexm2tssettings-scte35control): {{String}}
  [Scte35PrerollPullupMilliseconds](#cfn-medialive-channel-multiplexm2tssettings-scte35prerollpullupmilliseconds): {{Number}}
```

## Properties
<a name="aws-properties-medialive-channel-multiplexm2tssettings-properties"></a>

`AbsentInputAudioBehavior`  <a name="cfn-medialive-channel-multiplexm2tssettings-absentinputaudiobehavior"></a>
When set to drop, output audio streams will be removed from the program if the selected input audio stream is removed from the input. This allows the output audio configuration to dynamically change based on input configuration. If this is set to encodeSilence, all output audio streams will output encoded silence when not connected to an active input stream.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Arib`  <a name="cfn-medialive-channel-multiplexm2tssettings-arib"></a>
When set to enabled, uses ARIB-compliant field muxing and removes video descriptor.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AudioBufferModel`  <a name="cfn-medialive-channel-multiplexm2tssettings-audiobuffermodel"></a>
When set to dvb, uses DVB buffer model for Dolby Digital audio. When set to atsc, the ATSC model is used.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AudioFramesPerPes`  <a name="cfn-medialive-channel-multiplexm2tssettings-audioframesperpes"></a>
The number of audio frames to insert for each PES packet.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AudioStreamType`  <a name="cfn-medialive-channel-multiplexm2tssettings-audiostreamtype"></a>
When set to atsc, uses stream type = 0x81 for AC3 and stream type = 0x87 for EAC3. When set to dvb, uses stream type = 0x06.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CcDescriptor`  <a name="cfn-medialive-channel-multiplexm2tssettings-ccdescriptor"></a>
When set to enabled, generates captionServiceDescriptor in PMT.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Ebif`  <a name="cfn-medialive-channel-multiplexm2tssettings-ebif"></a>
If set to passthrough, passes any EBIF data from the input source to this output.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EsRateInPes`  <a name="cfn-medialive-channel-multiplexm2tssettings-esrateinpes"></a>
Include or exclude the ES Rate field in the PES header.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Klv`  <a name="cfn-medialive-channel-multiplexm2tssettings-klv"></a>
If set to passthrough, passes any KLV data from the input source to this output.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NielsenId3Behavior`  <a name="cfn-medialive-channel-multiplexm2tssettings-nielsenid3behavior"></a>
If set to passthrough, Nielsen inaudible tones for media tracking will be detected in the input audio and an equivalent ID3 tag will be inserted in the output.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PcrControl`  <a name="cfn-medialive-channel-multiplexm2tssettings-pcrcontrol"></a>
When set to pcrEveryPesPacket, a Program Clock Reference value is inserted for every Packetized Elementary Stream (PES) header. This parameter is effective only when the PCR PID is the same as the video or audio elementary stream.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PcrPeriod`  <a name="cfn-medialive-channel-multiplexm2tssettings-pcrperiod"></a>
Maximum time in milliseconds between Program Clock Reference (PCRs) inserted into the transport stream.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Scte35Control`  <a name="cfn-medialive-channel-multiplexm2tssettings-scte35control"></a>
Optionally pass SCTE-35 signals from the input source to this output.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Scte35PrerollPullupMilliseconds`  <a name="cfn-medialive-channel-multiplexm2tssettings-scte35prerollpullupmilliseconds"></a>
Defines the amount SCTE-35 preroll will be increased (in milliseconds) on the output. Preroll is the amount of time between the presence of a SCTE-35 indication in a transport stream and the PTS of the video frame it references. Zero means don't add pullup (it doesn't mean set the preroll to zero). Negative pullup is not supported, which means that you can't make the preroll shorter. Be aware that latency in the output will increase by the pullup amount.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
