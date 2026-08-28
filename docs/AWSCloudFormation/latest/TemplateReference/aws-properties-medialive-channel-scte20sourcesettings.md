---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-scte20sourcesettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel Scte20SourceSettings
<a name="aws-properties-medialive-channel-scte20sourcesettings"></a>

Information about the SCTE-20 captions to extract from the input.

The parent of this entity is CaptionSelectorSettings.

## Syntax
<a name="aws-properties-medialive-channel-scte20sourcesettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-scte20sourcesettings-syntax.json"></a>

```
{
  "[Convert608To708](#cfn-medialive-channel-scte20sourcesettings-convert608to708)" : {{String}},
  "[Source608ChannelNumber](#cfn-medialive-channel-scte20sourcesettings-source608channelnumber)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-medialive-channel-scte20sourcesettings-syntax.yaml"></a>

```
  [Convert608To708](#cfn-medialive-channel-scte20sourcesettings-convert608to708): {{String}}
  [Source608ChannelNumber](#cfn-medialive-channel-scte20sourcesettings-source608channelnumber): {{Integer}}
```

## Properties
<a name="aws-properties-medialive-channel-scte20sourcesettings-properties"></a>

`Convert608To708`  <a name="cfn-medialive-channel-scte20sourcesettings-convert608to708"></a>
If upconvert, 608 data is both passed through the "608 compatibility bytes" fields of the 708 wrapper as well as translated into 708. Any 708 data present in the source content is discarded.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Source608ChannelNumber`  <a name="cfn-medialive-channel-scte20sourcesettings-source608channelnumber"></a>
Specifies the 608/708 channel number within the video track from which to extract captions.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
