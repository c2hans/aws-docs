---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-input-smpte2110receivergroupsdpsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Input Smpte2110ReceiverGroupSdpSettings
<a name="aws-properties-medialive-input-smpte2110receivergroupsdpsettings"></a>

The SDP settings that identify the video, audio, and ancillary streams for an SMPTE 2110 receiver group.

The parent of this entity is Smpte2110ReceiverGroup.

## Syntax
<a name="aws-properties-medialive-input-smpte2110receivergroupsdpsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-input-smpte2110receivergroupsdpsettings-syntax.json"></a>

```
{
  "[AncillarySdps](#cfn-medialive-input-smpte2110receivergroupsdpsettings-ancillarysdps)" : {{[ InputSdpLocation, ... ]}},
  "[AudioSdps](#cfn-medialive-input-smpte2110receivergroupsdpsettings-audiosdps)" : {{[ InputSdpLocation, ... ]}},
  "[VideoSdp](#cfn-medialive-input-smpte2110receivergroupsdpsettings-videosdp)" : {{InputSdpLocation}}
}
```

### YAML
<a name="aws-properties-medialive-input-smpte2110receivergroupsdpsettings-syntax.yaml"></a>

```
  [AncillarySdps](#cfn-medialive-input-smpte2110receivergroupsdpsettings-ancillarysdps): {{
    - InputSdpLocation}}
  [AudioSdps](#cfn-medialive-input-smpte2110receivergroupsdpsettings-audiosdps): {{
    - InputSdpLocation}}
  [VideoSdp](#cfn-medialive-input-smpte2110receivergroupsdpsettings-videosdp): {{
    InputSdpLocation}}
```

## Properties
<a name="aws-properties-medialive-input-smpte2110receivergroupsdpsettings-properties"></a>

`AncillarySdps`  <a name="cfn-medialive-input-smpte2110receivergroupsdpsettings-ancillarysdps"></a>
A list of InputSdpLocations. Each item in the list specifies the SDP file and index for one ancillary SMPTE 2110 stream. Each stream encapsulates one captions stream (out of any number you can include) or the single SCTE 35 stream that you can include.
*Required*: No
*Type*: Array of [InputSdpLocation](aws-properties-medialive-input-inputsdplocation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AudioSdps`  <a name="cfn-medialive-input-smpte2110receivergroupsdpsettings-audiosdps"></a>
A list of InputSdpLocations. Each item in the list specifies the SDP file and index for one audio SMPTE 2110 stream.
*Required*: No
*Type*: Array of [InputSdpLocation](aws-properties-medialive-input-inputsdplocation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VideoSdp`  <a name="cfn-medialive-input-smpte2110receivergroupsdpsettings-videosdp"></a>
The InputSdpLocation that specifies the SDP file and index for the single video SMPTE 2110 stream for this 2110 input.
*Required*: No
*Type*: [InputSdpLocation](aws-properties-medialive-input-inputsdplocation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
