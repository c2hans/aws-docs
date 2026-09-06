---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ivs-stage-autoparticipantrecordingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IVS::Stage AutoParticipantRecordingConfiguration
<a name="aws-properties-ivs-stage-autoparticipantrecordingconfiguration"></a>

The `AWS::IVS::AutoParticipantRecordingConfiguration` property type describes a configuration for individual participant recording.

## Syntax
<a name="aws-properties-ivs-stage-autoparticipantrecordingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ivs-stage-autoparticipantrecordingconfiguration-syntax.json"></a>

```
{
  "[HlsConfiguration](#cfn-ivs-stage-autoparticipantrecordingconfiguration-hlsconfiguration)" : {{HlsConfiguration}},
  "[MediaTypes](#cfn-ivs-stage-autoparticipantrecordingconfiguration-mediatypes)" : {{[ String, ... ]}},
  "[RecordingReconnectWindowSeconds](#cfn-ivs-stage-autoparticipantrecordingconfiguration-recordingreconnectwindowseconds)" : {{Integer}},
  "[StorageConfigurationArn](#cfn-ivs-stage-autoparticipantrecordingconfiguration-storageconfigurationarn)" : {{String}},
  "[ThumbnailConfiguration](#cfn-ivs-stage-autoparticipantrecordingconfiguration-thumbnailconfiguration)" : {{ThumbnailConfiguration}}
}
```

### YAML
<a name="aws-properties-ivs-stage-autoparticipantrecordingconfiguration-syntax.yaml"></a>

```
  [HlsConfiguration](#cfn-ivs-stage-autoparticipantrecordingconfiguration-hlsconfiguration): {{
    HlsConfiguration}}
  [MediaTypes](#cfn-ivs-stage-autoparticipantrecordingconfiguration-mediatypes): {{
    - String}}
  [RecordingReconnectWindowSeconds](#cfn-ivs-stage-autoparticipantrecordingconfiguration-recordingreconnectwindowseconds): {{Integer}}
  [StorageConfigurationArn](#cfn-ivs-stage-autoparticipantrecordingconfiguration-storageconfigurationarn): {{String}}
  [ThumbnailConfiguration](#cfn-ivs-stage-autoparticipantrecordingconfiguration-thumbnailconfiguration): {{
    ThumbnailConfiguration}}
```

## Properties
<a name="aws-properties-ivs-stage-autoparticipantrecordingconfiguration-properties"></a>

`HlsConfiguration`  <a name="cfn-ivs-stage-autoparticipantrecordingconfiguration-hlsconfiguration"></a>
HLS configuration object for individual participant recording.
*Required*: No
*Type*: [HlsConfiguration](aws-properties-ivs-stage-hlsconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MediaTypes`  <a name="cfn-ivs-stage-autoparticipantrecordingconfiguration-mediatypes"></a>
Types of media to be recorded. Default: `AUDIO_VIDEO`.
*Required*: No
*Type*: Array of String
*Allowed values*: `AUDIO_VIDEO | AUDIO_ONLY`
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RecordingReconnectWindowSeconds`  <a name="cfn-ivs-stage-autoparticipantrecordingconfiguration-recordingreconnectwindowseconds"></a>
If a stage publisher disconnects and then reconnects within the specified interval, the multiple recordings will be considered a single recording and merged together.
The default value is 0, which disables merging.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `300`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StorageConfigurationArn`  <a name="cfn-ivs-stage-autoparticipantrecordingconfiguration-storageconfigurationarn"></a>
ARN of the [StorageConfiguration](aws-resource-ivs-storageconfiguration.md) resource to use for individual participant recording. Default: "" (empty string, no storage configuration is specified). Individual participant recording cannot be started unless a storage configuration is specified, when a [Stage](aws-resource-ivs-stage.md) is created or updated.
*Required*: Yes
*Type*: String
*Pattern*: `^$|^arn:aws:ivs:[a-z0-9-]+:[0-9]+:storage-configuration/[a-zA-Z0-9-]+$`
*Minimum*: `0`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ThumbnailConfiguration`  <a name="cfn-ivs-stage-autoparticipantrecordingconfiguration-thumbnailconfiguration"></a>
A complex type that allows you to enable/disable the recording of thumbnails for individual participant recording and modify the interval at which thumbnails are generated for the live session.
*Required*: No
*Type*: [ThumbnailConfiguration](aws-properties-ivs-stage-thumbnailconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
