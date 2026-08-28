---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-wavsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel WavSettings
<a name="aws-properties-medialive-channel-wavsettings"></a>

The setup of WAV audio in the output.

The parent of this entity is AudioCodecSettings.

## Syntax
<a name="aws-properties-medialive-channel-wavsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-wavsettings-syntax.json"></a>

```
{
  "[BitDepth](#cfn-medialive-channel-wavsettings-bitdepth)" : {{Number}},
  "[CodingMode](#cfn-medialive-channel-wavsettings-codingmode)" : {{String}},
  "[SampleRate](#cfn-medialive-channel-wavsettings-samplerate)" : {{Number}}
}
```

### YAML
<a name="aws-properties-medialive-channel-wavsettings-syntax.yaml"></a>

```
  [BitDepth](#cfn-medialive-channel-wavsettings-bitdepth): {{Number}}
  [CodingMode](#cfn-medialive-channel-wavsettings-codingmode): {{String}}
  [SampleRate](#cfn-medialive-channel-wavsettings-samplerate): {{Number}}
```

## Properties
<a name="aws-properties-medialive-channel-wavsettings-properties"></a>

`BitDepth`  <a name="cfn-medialive-channel-wavsettings-bitdepth"></a>
Bits per sample.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CodingMode`  <a name="cfn-medialive-channel-wavsettings-codingmode"></a>
The audio coding mode for the WAV audio. The mode determines the number of channels in the audio.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SampleRate`  <a name="cfn-medialive-channel-wavsettings-samplerate"></a>
Sample rate in Hz.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
