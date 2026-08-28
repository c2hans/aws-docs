---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-av1colorspacesettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel Av1ColorSpaceSettings
<a name="aws-properties-medialive-channel-av1colorspacesettings"></a>

Specify the type of color space to apply or choose to pass through. The default is to pass through the color space that is in the source.

## Syntax
<a name="aws-properties-medialive-channel-av1colorspacesettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-av1colorspacesettings-syntax.json"></a>

```
{
  "[ColorSpacePassthroughSettings](#cfn-medialive-channel-av1colorspacesettings-colorspacepassthroughsettings)" : {{Json}},
  "[Hdr10Settings](#cfn-medialive-channel-av1colorspacesettings-hdr10settings)" : {{Hdr10Settings}},
  "[Hlg2020Settings](#cfn-medialive-channel-av1colorspacesettings-hlg2020settings)" : {{Json}},
  "[Rec601Settings](#cfn-medialive-channel-av1colorspacesettings-rec601settings)" : {{Json}},
  "[Rec709Settings](#cfn-medialive-channel-av1colorspacesettings-rec709settings)" : {{Json}}
}
```

### YAML
<a name="aws-properties-medialive-channel-av1colorspacesettings-syntax.yaml"></a>

```
  [ColorSpacePassthroughSettings](#cfn-medialive-channel-av1colorspacesettings-colorspacepassthroughsettings): {{Json}}
  [Hdr10Settings](#cfn-medialive-channel-av1colorspacesettings-hdr10settings): {{
    Hdr10Settings}}
  [Hlg2020Settings](#cfn-medialive-channel-av1colorspacesettings-hlg2020settings): {{Json}}
  [Rec601Settings](#cfn-medialive-channel-av1colorspacesettings-rec601settings): {{Json}}
  [Rec709Settings](#cfn-medialive-channel-av1colorspacesettings-rec709settings): {{Json}}
```

## Properties
<a name="aws-properties-medialive-channel-av1colorspacesettings-properties"></a>

`ColorSpacePassthroughSettings`  <a name="cfn-medialive-channel-av1colorspacesettings-colorspacepassthroughsettings"></a>
Passthrough applies no color space conversion to the output.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Hdr10Settings`  <a name="cfn-medialive-channel-av1colorspacesettings-hdr10settings"></a>
Hdr10 Settings
*Required*: No
*Type*: [Hdr10Settings](aws-properties-medialive-channel-hdr10settings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Hlg2020Settings`  <a name="cfn-medialive-channel-av1colorspacesettings-hlg2020settings"></a>
Hlg2020 Settings
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Rec601Settings`  <a name="cfn-medialive-channel-av1colorspacesettings-rec601settings"></a>
Rec601 Settings
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Rec709Settings`  <a name="cfn-medialive-channel-av1colorspacesettings-rec709settings"></a>
Rec709 Settings
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
