---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-audiopid.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel AudioPid
<a name="aws-properties-medialive-channel-audiopid"></a>

Contains the packet identifier (PID) value and optional pre-mixer settings for a single audio stream within a source.

## Syntax
<a name="aws-properties-medialive-channel-audiopid-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-audiopid-syntax.json"></a>

```
{
  "[DolbyEDecode](#cfn-medialive-channel-audiopid-dolbyedecode)" : {{AudioDolbyEDecode}},
  "[Pid](#cfn-medialive-channel-audiopid-pid)" : {{Integer}},
  "[PremixSettings](#cfn-medialive-channel-audiopid-premixsettings)" : {{AudioPreMixerSettings}}
}
```

### YAML
<a name="aws-properties-medialive-channel-audiopid-syntax.yaml"></a>

```
  [DolbyEDecode](#cfn-medialive-channel-audiopid-dolbyedecode): {{
    AudioDolbyEDecode}}
  [Pid](#cfn-medialive-channel-audiopid-pid): {{Integer}}
  [PremixSettings](#cfn-medialive-channel-audiopid-premixsettings): {{
    AudioPreMixerSettings}}
```

## Properties
<a name="aws-properties-medialive-channel-audiopid-properties"></a>

`DolbyEDecode`  <a name="cfn-medialive-channel-audiopid-dolbyedecode"></a>
Configure decoding options for Dolby E streams - these should be Dolby E frames carried in PCM streams tagged with SMPTE-337. When using the 'pids' array, if this field is not specified and Dolby E content is present, the decoder will extract the specified program. To maintain legacy behavior (allPrograms), explicitly set programSelection to "allChannels".
*Required*: No
*Type*: [AudioDolbyEDecode](aws-properties-medialive-channel-audiodolbyedecode.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Pid`  <a name="cfn-medialive-channel-audiopid-pid"></a>
The packet identifier (PID) value from within the source.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PremixSettings`  <a name="cfn-medialive-channel-audiopid-premixsettings"></a>
The optional audio pre-mixer settings for this PID. When specified, the service applies channel remixing, gain adjustment, and loudness normalization to this PID before interleaving.
*Required*: No
*Type*: [AudioPreMixerSettings](aws-properties-medialive-channel-audiopremixersettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
