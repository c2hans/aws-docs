---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-mp2settings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel Mp2Settings
<a name="aws-properties-medialive-channel-mp2settings"></a>

The configuration for this MP2 audio.

The parent of this entity is AudioCodecSettings.

## Syntax
<a name="aws-properties-medialive-channel-mp2settings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-mp2settings-syntax.json"></a>

```
{
  "[Bitrate](#cfn-medialive-channel-mp2settings-bitrate)" : {{Number}},
  "[CodingMode](#cfn-medialive-channel-mp2settings-codingmode)" : {{String}},
  "[SampleRate](#cfn-medialive-channel-mp2settings-samplerate)" : {{Number}}
}
```

### YAML
<a name="aws-properties-medialive-channel-mp2settings-syntax.yaml"></a>

```
  [Bitrate](#cfn-medialive-channel-mp2settings-bitrate): {{Number}}
  [CodingMode](#cfn-medialive-channel-mp2settings-codingmode): {{String}}
  [SampleRate](#cfn-medialive-channel-mp2settings-samplerate): {{Number}}
```

## Properties
<a name="aws-properties-medialive-channel-mp2settings-properties"></a>

`Bitrate`  <a name="cfn-medialive-channel-mp2settings-bitrate"></a>
The average bitrate in bits/second.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CodingMode`  <a name="cfn-medialive-channel-mp2settings-codingmode"></a>
The MPEG2 Audio coding mode. Valid values are codingMode10 (for mono) or codingMode20 (for stereo).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SampleRate`  <a name="cfn-medialive-channel-mp2settings-samplerate"></a>
The sample rate in Hz.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
