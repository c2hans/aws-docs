---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediapackagev2-originendpoint-encryptioncontractconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaPackageV2::OriginEndpoint EncryptionContractConfiguration
<a name="aws-properties-mediapackagev2-originendpoint-encryptioncontractconfiguration"></a>

Use `encryptionContractConfiguration` to configure one or more content encryption keys for your endpoints that use SPEKE Version 2.0. The encryption contract defines which content keys are used to encrypt the audio and video tracks in your stream. To configure the encryption contract, specify which audio and video encryption presets to use.

## Syntax
<a name="aws-properties-mediapackagev2-originendpoint-encryptioncontractconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediapackagev2-originendpoint-encryptioncontractconfiguration-syntax.json"></a>

```
{
  "[PresetSpeke20Audio](#cfn-mediapackagev2-originendpoint-encryptioncontractconfiguration-presetspeke20audio)" : {{String}},
  "[PresetSpeke20Video](#cfn-mediapackagev2-originendpoint-encryptioncontractconfiguration-presetspeke20video)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediapackagev2-originendpoint-encryptioncontractconfiguration-syntax.yaml"></a>

```
  [PresetSpeke20Audio](#cfn-mediapackagev2-originendpoint-encryptioncontractconfiguration-presetspeke20audio): {{String}}
  [PresetSpeke20Video](#cfn-mediapackagev2-originendpoint-encryptioncontractconfiguration-presetspeke20video): {{String}}
```

## Properties
<a name="aws-properties-mediapackagev2-originendpoint-encryptioncontractconfiguration-properties"></a>

`PresetSpeke20Audio`  <a name="cfn-mediapackagev2-originendpoint-encryptioncontractconfiguration-presetspeke20audio"></a>
A collection of audio encryption presets.
Value description:
+ `PRESET-AUDIO-1` - Use one content key to encrypt all of the audio tracks in your stream.
+ `PRESET-AUDIO-2` - Use one content key to encrypt all of the stereo audio tracks and one content key to encrypt all of the multichannel audio tracks.
+ `PRESET-AUDIO-3` - Use one content key to encrypt all of the stereo audio tracks, one content key to encrypt all of the multichannel audio tracks with 3 to 6 channels, and one content key to encrypt all of the multichannel audio tracks with more than 6 channels.
+ `SHARED` - Use the same content key for all of the audio and video tracks in your stream.
+ `UNENCRYPTED` - Don't encrypt any of the audio tracks in your stream.
*Required*: Yes
*Type*: String
*Allowed values*: `PRESET_AUDIO_1 | PRESET_AUDIO_2 | PRESET_AUDIO_3 | SHARED | UNENCRYPTED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PresetSpeke20Video`  <a name="cfn-mediapackagev2-originendpoint-encryptioncontractconfiguration-presetspeke20video"></a>
The SPEKE Version 2.0 preset video associated with the encryption contract configuration of the origin endpoint.
A collection of video encryption presets.
Value description:
+ `PRESET-VIDEO-1` - Use one content key to encrypt all of the video tracks in your stream.
+ `PRESET-VIDEO-2` - Use one content key to encrypt all of the SD video tracks and one content key for all HD and higher resolutions video tracks.
+ `PRESET-VIDEO-3` - Use one content key to encrypt all of the SD video tracks, one content key for HD video tracks and one content key for all UHD video tracks.
+ `PRESET-VIDEO-4` - Use one content key to encrypt all of the SD video tracks, one content key for HD video tracks, one content key for all UHD1 video tracks and one content key for all UHD2 video tracks.
+ `PRESET-VIDEO-5` - Use one content key to encrypt all of the SD video tracks, one content key for HD1 video tracks, one content key for HD2 video tracks, one content key for all UHD1 video tracks and one content key for all UHD2 video tracks.
+ `PRESET-VIDEO-6` - Use one content key to encrypt all of the SD video tracks, one content key for HD1 video tracks, one content key for HD2 video tracks and one content key for all UHD video tracks.
+ `PRESET-VIDEO-7` - Use one content key to encrypt all of the SD\+HD1 video tracks, one content key for HD2 video tracks and one content key for all UHD video tracks.
+ `PRESET-VIDEO-8` - Use one content key to encrypt all of the SD\+HD1 video tracks, one content key for HD2 video tracks, one content key for all UHD1 video tracks and one content key for all UHD2 video tracks.
+ `SHARED` - Use the same content key for all of the video and audio tracks in your stream.
+ `UNENCRYPTED` - Don't encrypt any of the video tracks in your stream.
*Required*: Yes
*Type*: String
*Allowed values*: `PRESET_VIDEO_1 | PRESET_VIDEO_2 | PRESET_VIDEO_3 | PRESET_VIDEO_4 | PRESET_VIDEO_5 | PRESET_VIDEO_6 | PRESET_VIDEO_7 | PRESET_VIDEO_8 | SHARED | UNENCRYPTED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
