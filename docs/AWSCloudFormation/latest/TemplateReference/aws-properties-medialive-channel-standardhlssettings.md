---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-standardhlssettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel StandardHlsSettings
<a name="aws-properties-medialive-channel-standardhlssettings"></a>

The configuration of an HLS output that is a standard output (not an audio-only output).

The parent of this entity is HlsSettings.

## Syntax
<a name="aws-properties-medialive-channel-standardhlssettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-standardhlssettings-syntax.json"></a>

```
{
  "[AudioRenditionSets](#cfn-medialive-channel-standardhlssettings-audiorenditionsets)" : {{String}},
  "[M3u8Settings](#cfn-medialive-channel-standardhlssettings-m3u8settings)" : {{M3u8Settings}}
}
```

### YAML
<a name="aws-properties-medialive-channel-standardhlssettings-syntax.yaml"></a>

```
  [AudioRenditionSets](#cfn-medialive-channel-standardhlssettings-audiorenditionsets): {{String}}
  [M3u8Settings](#cfn-medialive-channel-standardhlssettings-m3u8settings): {{
    M3u8Settings}}
```

## Properties
<a name="aws-properties-medialive-channel-standardhlssettings-properties"></a>

`AudioRenditionSets`  <a name="cfn-medialive-channel-standardhlssettings-audiorenditionsets"></a>
Lists all the audio groups that are used with the video output stream. This inputs all the audio GROUP-IDs that are associated with the video, separated by a comma (,).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`M3u8Settings`  <a name="cfn-medialive-channel-standardhlssettings-m3u8settings"></a>
Settings for the M3U8 container.
*Required*: No
*Type*: [M3u8Settings](aws-properties-medialive-channel-m3u8settings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
