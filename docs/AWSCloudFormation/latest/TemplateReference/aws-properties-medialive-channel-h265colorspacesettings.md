---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-h265colorspacesettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel H265ColorSpaceSettings
<a name="aws-properties-medialive-channel-h265colorspacesettings"></a>

H265 Color Space Settings

The parent of this entity is H265Settings.

## Syntax
<a name="aws-properties-medialive-channel-h265colorspacesettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-h265colorspacesettings-syntax.json"></a>

```
{
  "[ColorSpacePassthroughSettings](#cfn-medialive-channel-h265colorspacesettings-colorspacepassthroughsettings)" : {{Json}},
  "[DolbyVision81Settings](#cfn-medialive-channel-h265colorspacesettings-dolbyvision81settings)" : {{Json}},
  "[Hdr10Settings](#cfn-medialive-channel-h265colorspacesettings-hdr10settings)" : {{Hdr10Settings}},
  "[Hlg2020Settings](#cfn-medialive-channel-h265colorspacesettings-hlg2020settings)" : {{Json}},
  "[Rec601Settings](#cfn-medialive-channel-h265colorspacesettings-rec601settings)" : {{Json}},
  "[Rec709Settings](#cfn-medialive-channel-h265colorspacesettings-rec709settings)" : {{Json}}
}
```

### YAML
<a name="aws-properties-medialive-channel-h265colorspacesettings-syntax.yaml"></a>

```
  [ColorSpacePassthroughSettings](#cfn-medialive-channel-h265colorspacesettings-colorspacepassthroughsettings): {{Json}}
  [DolbyVision81Settings](#cfn-medialive-channel-h265colorspacesettings-dolbyvision81settings): {{Json}}
  [Hdr10Settings](#cfn-medialive-channel-h265colorspacesettings-hdr10settings): {{
    Hdr10Settings}}
  [Hlg2020Settings](#cfn-medialive-channel-h265colorspacesettings-hlg2020settings): {{Json}}
  [Rec601Settings](#cfn-medialive-channel-h265colorspacesettings-rec601settings): {{Json}}
  [Rec709Settings](#cfn-medialive-channel-h265colorspacesettings-rec709settings): {{Json}}
```

## Properties
<a name="aws-properties-medialive-channel-h265colorspacesettings-properties"></a>

`ColorSpacePassthroughSettings`  <a name="cfn-medialive-channel-h265colorspacesettings-colorspacepassthroughsettings"></a>
Passthrough applies no color space conversion to the output.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DolbyVision81Settings`  <a name="cfn-medialive-channel-h265colorspacesettings-dolbyvision81settings"></a>
Dolby Vision 8.1 settings.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Hdr10Settings`  <a name="cfn-medialive-channel-h265colorspacesettings-hdr10settings"></a>
Settings to configure the handling of HDR10 color space.
*Required*: No
*Type*: [Hdr10Settings](aws-properties-medialive-channel-hdr10settings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Hlg2020Settings`  <a name="cfn-medialive-channel-h265colorspacesettings-hlg2020settings"></a>
HLG 2020 settings.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Rec601Settings`  <a name="cfn-medialive-channel-h265colorspacesettings-rec601settings"></a>
Settings to configure the handling of Rec601 color space.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Rec709Settings`  <a name="cfn-medialive-channel-h265colorspacesettings-rec709settings"></a>
Settings to configure the handling of Rec709 color space.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
