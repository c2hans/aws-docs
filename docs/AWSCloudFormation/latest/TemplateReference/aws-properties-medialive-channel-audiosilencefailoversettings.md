---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-audiosilencefailoversettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel AudioSilenceFailoverSettings
<a name="aws-properties-medialive-channel-audiosilencefailoversettings"></a>

MediaLive will perform a failover if audio is not detected in this input for the specified period.

The parent of this entity is FailoverConditionSettings.

## Syntax
<a name="aws-properties-medialive-channel-audiosilencefailoversettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-audiosilencefailoversettings-syntax.json"></a>

```
{
  "[AudioSelectorName](#cfn-medialive-channel-audiosilencefailoversettings-audioselectorname)" : {{String}},
  "[AudioSilenceThresholdMsec](#cfn-medialive-channel-audiosilencefailoversettings-audiosilencethresholdmsec)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-medialive-channel-audiosilencefailoversettings-syntax.yaml"></a>

```
  [AudioSelectorName](#cfn-medialive-channel-audiosilencefailoversettings-audioselectorname): {{String}}
  [AudioSilenceThresholdMsec](#cfn-medialive-channel-audiosilencefailoversettings-audiosilencethresholdmsec): {{Integer}}
```

## Properties
<a name="aws-properties-medialive-channel-audiosilencefailoversettings-properties"></a>

`AudioSelectorName`  <a name="cfn-medialive-channel-audiosilencefailoversettings-audioselectorname"></a>
The name of the audio selector in the input that MediaLive should monitor to detect silence. Select your most important rendition. If you didn't create an audio selector in this input, leave blank.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AudioSilenceThresholdMsec`  <a name="cfn-medialive-channel-audiosilencefailoversettings-audiosilencethresholdmsec"></a>
The amount of time (in milliseconds) that the active input must be silent before automatic input failover occurs. Silence is defined as audio loss or audio quieter than -50 dBFS.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
