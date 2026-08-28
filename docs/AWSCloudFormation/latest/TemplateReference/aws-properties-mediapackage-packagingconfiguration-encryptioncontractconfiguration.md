---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediapackage-packagingconfiguration-encryptioncontractconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaPackage::PackagingConfiguration EncryptionContractConfiguration
<a name="aws-properties-mediapackage-packagingconfiguration-encryptioncontractconfiguration"></a>

Use `encryptionContractConfiguration` to configure one or more content encryption keys for your endpoints that use SPEKE Version 2.0. The encryption contract defines the content keys used to encrypt the audio and video tracks in your stream. To configure the encryption contract, specify which audio and video encryption presets to use. For more information about these presets, see [SPEKE Version 2.0 Presets](https://docs.aws.amazon.com/mediapackage/latest/ug/drm-content-speke-v2-presets.html).

Note the following considerations when using `encryptionContractConfiguration`:
+ You can use `encryptionContractConfiguration` for DASH endpoints that use SPEKE Version 2.0. SPEKE Version 2.0 relies on the CPIX Version 2.3 specification.
+ You cannot combine an `UNENCRYPTED` preset with `UNENCRYPTED` or `SHARED` presets across `presetSpeke20Audio` and `presetSpeke20Video`.
+ When you use a `SHARED` preset, you must use it for both `presetSpeke20Audio` and `presetSpeke20Video`.

## Syntax
<a name="aws-properties-mediapackage-packagingconfiguration-encryptioncontractconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediapackage-packagingconfiguration-encryptioncontractconfiguration-syntax.json"></a>

```
{
  "[PresetSpeke20Audio](#cfn-mediapackage-packagingconfiguration-encryptioncontractconfiguration-presetspeke20audio)" : {{String}},
  "[PresetSpeke20Video](#cfn-mediapackage-packagingconfiguration-encryptioncontractconfiguration-presetspeke20video)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediapackage-packagingconfiguration-encryptioncontractconfiguration-syntax.yaml"></a>

```
  [PresetSpeke20Audio](#cfn-mediapackage-packagingconfiguration-encryptioncontractconfiguration-presetspeke20audio): {{String}}
  [PresetSpeke20Video](#cfn-mediapackage-packagingconfiguration-encryptioncontractconfiguration-presetspeke20video): {{String}}
```

## Properties
<a name="aws-properties-mediapackage-packagingconfiguration-encryptioncontractconfiguration-properties"></a>

`PresetSpeke20Audio`  <a name="cfn-mediapackage-packagingconfiguration-encryptioncontractconfiguration-presetspeke20audio"></a>
A collection of audio encryption presets.
Value description:
+ `PRESET-AUDIO-1` - Use one content key to encrypt all of the audio tracks in your stream.
+ `PRESET-AUDIO-2` - Use one content key to encrypt all of the stereo audio tracks and one content key to encrypt all of the multichannel audio tracks.
+ `PRESET-AUDIO-3` - Use one content key to encrypt all of the stereo audio tracks, one content key to encrypt all of the multichannel audio tracks with 3 to 6 channels, and one content key to encrypt all of the multichannel audio tracks with more than 6 channels.
+ `SHARED` - Use the same content key for all of the audio and video tracks in your stream.
+ `UNENCRYPTED` - Don't encrypt any of the audio tracks in your stream.
*Required*: Yes
*Type*: String
*Allowed values*: `PRESET-AUDIO-1 | PRESET-AUDIO-2 | PRESET-AUDIO-3 | SHARED | UNENCRYPTED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PresetSpeke20Video`  <a name="cfn-mediapackage-packagingconfiguration-encryptioncontractconfiguration-presetspeke20video"></a>
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
*Allowed values*: `PRESET-VIDEO-1 | PRESET-VIDEO-2 | PRESET-VIDEO-3 | PRESET-VIDEO-4 | PRESET-VIDEO-5 | PRESET-VIDEO-6 | PRESET-VIDEO-7 | PRESET-VIDEO-8 | SHARED | UNENCRYPTED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
