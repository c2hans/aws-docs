---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-fmp4hlssettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel Fmp4HlsSettings
<a name="aws-properties-medialive-channel-fmp4hlssettings"></a>

Settings for the fMP4 containers.

The parent of this entity is HlsSettings.

## Syntax
<a name="aws-properties-medialive-channel-fmp4hlssettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-fmp4hlssettings-syntax.json"></a>

```
{
  "[AudioRenditionSets](#cfn-medialive-channel-fmp4hlssettings-audiorenditionsets)" : {{String}},
  "[NielsenId3Behavior](#cfn-medialive-channel-fmp4hlssettings-nielsenid3behavior)" : {{String}},
  "[TimedMetadataBehavior](#cfn-medialive-channel-fmp4hlssettings-timedmetadatabehavior)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-channel-fmp4hlssettings-syntax.yaml"></a>

```
  [AudioRenditionSets](#cfn-medialive-channel-fmp4hlssettings-audiorenditionsets): {{String}}
  [NielsenId3Behavior](#cfn-medialive-channel-fmp4hlssettings-nielsenid3behavior): {{String}}
  [TimedMetadataBehavior](#cfn-medialive-channel-fmp4hlssettings-timedmetadatabehavior): {{String}}
```

## Properties
<a name="aws-properties-medialive-channel-fmp4hlssettings-properties"></a>

`AudioRenditionSets`  <a name="cfn-medialive-channel-fmp4hlssettings-audiorenditionsets"></a>
List all the audio groups that are used with the video output stream. Input all the audio GROUP-IDs that are associated to the video, separate by ','.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NielsenId3Behavior`  <a name="cfn-medialive-channel-fmp4hlssettings-nielsenid3behavior"></a>
If set to passthrough, Nielsen inaudible tones for media tracking will be detected in the input audio and an equivalent ID3 tag will be inserted in the output.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimedMetadataBehavior`  <a name="cfn-medialive-channel-fmp4hlssettings-timedmetadatabehavior"></a>
When set to passthrough, timed metadata is passed through from input to output.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
