---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-audiopremixersettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel AudioPreMixerSettings
<a name="aws-properties-medialive-channel-audiopremixersettings"></a>

Contains settings for preprocessing audio before interleaving, including loudness normalization, channel remixing, and gain adjustment. Apply these settings to individual PIDs or audio tracks to control audio output characteristics before the tracks are combined.

## Syntax
<a name="aws-properties-medialive-channel-audiopremixersettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-audiopremixersettings-syntax.json"></a>

```
{
  "[AudioNormalizationSettings](#cfn-medialive-channel-audiopremixersettings-audionormalizationsettings)" : {{AudioNormalizationSettings}},
  "[Channels](#cfn-medialive-channel-audiopremixersettings-channels)" : {{Integer}},
  "[GainDb](#cfn-medialive-channel-audiopremixersettings-gaindb)" : {{Number}},
  "[RemixSettings](#cfn-medialive-channel-audiopremixersettings-remixsettings)" : {{RemixSettings}}
}
```

### YAML
<a name="aws-properties-medialive-channel-audiopremixersettings-syntax.yaml"></a>

```
  [AudioNormalizationSettings](#cfn-medialive-channel-audiopremixersettings-audionormalizationsettings): {{
    AudioNormalizationSettings}}
  [Channels](#cfn-medialive-channel-audiopremixersettings-channels): {{Integer}}
  [GainDb](#cfn-medialive-channel-audiopremixersettings-gaindb): {{Number}}
  [RemixSettings](#cfn-medialive-channel-audiopremixersettings-remixsettings): {{
    RemixSettings}}
```

## Properties
<a name="aws-properties-medialive-channel-audiopremixersettings-properties"></a>

`AudioNormalizationSettings`  <a name="cfn-medialive-channel-audiopremixersettings-audionormalizationsettings"></a>
The audio normalization settings for loudness control. When specified, the service normalizes audio loudness according to the chosen algorithm.
*Required*: No
*Type*: [AudioNormalizationSettings](aws-properties-medialive-channel-audionormalizationsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Channels`  <a name="cfn-medialive-channel-audiopremixersettings-channels"></a>
The number of audio channels to remix the audio to. If you don't specify a value, the service passes through the original channel count. The remixSettings setting overrides this value when specified.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GainDb`  <a name="cfn-medialive-channel-audiopremixersettings-gaindb"></a>
The gain adjustment, in decibels (dB), to apply to this audio.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RemixSettings`  <a name="cfn-medialive-channel-audiopremixersettings-remixsettings"></a>
The settings that control how the service remixes input audio channels. When specified, these settings provide fine-grained control over channel mapping and gain levels, and take precedence over the channels setting.
*Required*: No
*Type*: [RemixSettings](aws-properties-medialive-channel-remixsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
