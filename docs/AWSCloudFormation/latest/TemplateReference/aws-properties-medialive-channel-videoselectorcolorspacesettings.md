---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-videoselectorcolorspacesettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel VideoSelectorColorSpaceSettings
<a name="aws-properties-medialive-channel-videoselectorcolorspacesettings"></a>

Settings to configure color space settings in the incoming video.

The parent of this entity is VideoSelector.

## Syntax
<a name="aws-properties-medialive-channel-videoselectorcolorspacesettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-videoselectorcolorspacesettings-syntax.json"></a>

```
{
  "[Hdr10Settings](#cfn-medialive-channel-videoselectorcolorspacesettings-hdr10settings)" : {{Hdr10Settings}}
}
```

### YAML
<a name="aws-properties-medialive-channel-videoselectorcolorspacesettings-syntax.yaml"></a>

```
  [Hdr10Settings](#cfn-medialive-channel-videoselectorcolorspacesettings-hdr10settings): {{
    Hdr10Settings}}
```

## Properties
<a name="aws-properties-medialive-channel-videoselectorcolorspacesettings-properties"></a>

`Hdr10Settings`  <a name="cfn-medialive-channel-videoselectorcolorspacesettings-hdr10settings"></a>
Settings to configure color space settings in the incoming video.
*Required*: No
*Type*: [Hdr10Settings](aws-properties-medialive-channel-hdr10settings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
