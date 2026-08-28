---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-ac3settings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel Ac3Settings
<a name="aws-properties-medialive-channel-ac3settings"></a>

The settings for an AC3 audio encode in the output.

The parent of this entity is AudioCodecSettings.

## Syntax
<a name="aws-properties-medialive-channel-ac3settings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-ac3settings-syntax.json"></a>

```
{
  "[AttenuationControl](#cfn-medialive-channel-ac3settings-attenuationcontrol)" : {{String}},
  "[Bitrate](#cfn-medialive-channel-ac3settings-bitrate)" : {{Number}},
  "[BitstreamMode](#cfn-medialive-channel-ac3settings-bitstreammode)" : {{String}},
  "[CodingMode](#cfn-medialive-channel-ac3settings-codingmode)" : {{String}},
  "[Dialnorm](#cfn-medialive-channel-ac3settings-dialnorm)" : {{Integer}},
  "[DrcProfile](#cfn-medialive-channel-ac3settings-drcprofile)" : {{String}},
  "[LfeFilter](#cfn-medialive-channel-ac3settings-lfefilter)" : {{String}},
  "[MetadataControl](#cfn-medialive-channel-ac3settings-metadatacontrol)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-channel-ac3settings-syntax.yaml"></a>

```
  [AttenuationControl](#cfn-medialive-channel-ac3settings-attenuationcontrol): {{String}}
  [Bitrate](#cfn-medialive-channel-ac3settings-bitrate): {{Number}}
  [BitstreamMode](#cfn-medialive-channel-ac3settings-bitstreammode): {{String}}
  [CodingMode](#cfn-medialive-channel-ac3settings-codingmode): {{String}}
  [Dialnorm](#cfn-medialive-channel-ac3settings-dialnorm): {{Integer}}
  [DrcProfile](#cfn-medialive-channel-ac3settings-drcprofile): {{String}}
  [LfeFilter](#cfn-medialive-channel-ac3settings-lfefilter): {{String}}
  [MetadataControl](#cfn-medialive-channel-ac3settings-metadatacontrol): {{String}}
```

## Properties
<a name="aws-properties-medialive-channel-ac3settings-properties"></a>

`AttenuationControl`  <a name="cfn-medialive-channel-ac3settings-attenuationcontrol"></a>
Applies a 3 dB attenuation to the surround channels. Applies only when the coding mode parameter is CODING\_MODE\_3\_2\_LFE.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Bitrate`  <a name="cfn-medialive-channel-ac3settings-bitrate"></a>
The average bitrate in bits/second. Valid bitrates depend on the coding mode.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BitstreamMode`  <a name="cfn-medialive-channel-ac3settings-bitstreammode"></a>
Specifies the bitstream mode (bsmod) for the emitted AC-3 stream. For more information about these values, see ATSC A/52-2012.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CodingMode`  <a name="cfn-medialive-channel-ac3settings-codingmode"></a>
The Dolby Digital coding mode. This determines the number of channels.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Dialnorm`  <a name="cfn-medialive-channel-ac3settings-dialnorm"></a>
Sets the dialnorm for the output. If excluded and the input audio is Dolby Digital, dialnorm is passed through.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DrcProfile`  <a name="cfn-medialive-channel-ac3settings-drcprofile"></a>
If set to filmStandard, adds dynamic range compression signaling to the output bitstream as defined in the Dolby Digital specification.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LfeFilter`  <a name="cfn-medialive-channel-ac3settings-lfefilter"></a>
When set to enabled, applies a 120Hz lowpass filter to the LFE channel prior to encoding. This is valid only in codingMode32Lfe mode.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetadataControl`  <a name="cfn-medialive-channel-ac3settings-metadatacontrol"></a>
When set to followInput, encoder metadata is sourced from the DD, DD\+, or DolbyE decoder that supplies this audio data. If the audio is supplied from one of these streams, the static metadata settings are used.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
