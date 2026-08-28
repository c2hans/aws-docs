---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-audiowatermarksettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel AudioWatermarkSettings
<a name="aws-properties-medialive-channel-audiowatermarksettings"></a>

Audio Watermark Settings

The parent of this entity is AudioDescription.

## Syntax
<a name="aws-properties-medialive-channel-audiowatermarksettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-audiowatermarksettings-syntax.json"></a>

```
{
  "[NielsenWatermarksSettings](#cfn-medialive-channel-audiowatermarksettings-nielsenwatermarkssettings)" : {{NielsenWatermarksSettings}}
}
```

### YAML
<a name="aws-properties-medialive-channel-audiowatermarksettings-syntax.yaml"></a>

```
  [NielsenWatermarksSettings](#cfn-medialive-channel-audiowatermarksettings-nielsenwatermarkssettings): {{
    NielsenWatermarksSettings}}
```

## Properties
<a name="aws-properties-medialive-channel-audiowatermarksettings-properties"></a>

`NielsenWatermarksSettings`  <a name="cfn-medialive-channel-audiowatermarksettings-nielsenwatermarkssettings"></a>
Settings to configure Nielsen Watermarks in the audio encode
*Required*: No
*Type*: [NielsenWatermarksSettings](aws-properties-medialive-channel-nielsenwatermarkssettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
