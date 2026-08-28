---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-eac3atmossettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel Eac3AtmosSettings
<a name="aws-properties-medialive-channel-eac3atmossettings"></a>

Eac3 Atmos Settings

## Syntax
<a name="aws-properties-medialive-channel-eac3atmossettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-eac3atmossettings-syntax.json"></a>

```
{
  "[Bitrate](#cfn-medialive-channel-eac3atmossettings-bitrate)" : {{Number}},
  "[CodingMode](#cfn-medialive-channel-eac3atmossettings-codingmode)" : {{String}},
  "[Dialnorm](#cfn-medialive-channel-eac3atmossettings-dialnorm)" : {{Integer}},
  "[DrcLine](#cfn-medialive-channel-eac3atmossettings-drcline)" : {{String}},
  "[DrcRf](#cfn-medialive-channel-eac3atmossettings-drcrf)" : {{String}},
  "[HeightTrim](#cfn-medialive-channel-eac3atmossettings-heighttrim)" : {{Number}},
  "[SurroundTrim](#cfn-medialive-channel-eac3atmossettings-surroundtrim)" : {{Number}}
}
```

### YAML
<a name="aws-properties-medialive-channel-eac3atmossettings-syntax.yaml"></a>

```
  [Bitrate](#cfn-medialive-channel-eac3atmossettings-bitrate): {{Number}}
  [CodingMode](#cfn-medialive-channel-eac3atmossettings-codingmode): {{String}}
  [Dialnorm](#cfn-medialive-channel-eac3atmossettings-dialnorm): {{Integer}}
  [DrcLine](#cfn-medialive-channel-eac3atmossettings-drcline): {{String}}
  [DrcRf](#cfn-medialive-channel-eac3atmossettings-drcrf): {{String}}
  [HeightTrim](#cfn-medialive-channel-eac3atmossettings-heighttrim): {{Number}}
  [SurroundTrim](#cfn-medialive-channel-eac3atmossettings-surroundtrim): {{Number}}
```

## Properties
<a name="aws-properties-medialive-channel-eac3atmossettings-properties"></a>

`Bitrate`  <a name="cfn-medialive-channel-eac3atmossettings-bitrate"></a>
Average bitrate in bits/second. Valid bitrates depend on the coding mode.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CodingMode`  <a name="cfn-medialive-channel-eac3atmossettings-codingmode"></a>
Dolby Digital Plus with Dolby Atmos coding mode. Determines number of channels.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Dialnorm`  <a name="cfn-medialive-channel-eac3atmossettings-dialnorm"></a>
Sets the dialnorm for the output. Default 23.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DrcLine`  <a name="cfn-medialive-channel-eac3atmossettings-drcline"></a>
Sets the Dolby dynamic range compression profile.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DrcRf`  <a name="cfn-medialive-channel-eac3atmossettings-drcrf"></a>
Sets the profile for heavy Dolby dynamic range compression, ensures that the instantaneous signal peaks do not exceed specified levels.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HeightTrim`  <a name="cfn-medialive-channel-eac3atmossettings-heighttrim"></a>
Height dimensional trim. Sets the maximum amount to attenuate the height channels when the downstream player isn't configured to handle Dolby Digital Plus with Dolby Atmos and must remix the channels.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SurroundTrim`  <a name="cfn-medialive-channel-eac3atmossettings-surroundtrim"></a>
Surround dimensional trim. Sets the maximum amount to attenuate the surround channels when the downstream player isn't configured to handle Dolby Digital Plus with Dolby Atmos and must remix the channels.
*Required*: No
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
