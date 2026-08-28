---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ivs-encoderconfiguration-video.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IVS::EncoderConfiguration Video
<a name="aws-properties-ivs-encoderconfiguration-video"></a>

The Video property type describes a stream's video configuration.

## Syntax
<a name="aws-properties-ivs-encoderconfiguration-video-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ivs-encoderconfiguration-video-syntax.json"></a>

```
{
  "[Bitrate](#cfn-ivs-encoderconfiguration-video-bitrate)" : {{Integer}},
  "[Framerate](#cfn-ivs-encoderconfiguration-video-framerate)" : {{Number}},
  "[Height](#cfn-ivs-encoderconfiguration-video-height)" : {{Integer}},
  "[Width](#cfn-ivs-encoderconfiguration-video-width)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-ivs-encoderconfiguration-video-syntax.yaml"></a>

```
  [Bitrate](#cfn-ivs-encoderconfiguration-video-bitrate): {{Integer}}
  [Framerate](#cfn-ivs-encoderconfiguration-video-framerate): {{Number}}
  [Height](#cfn-ivs-encoderconfiguration-video-height): {{Integer}}
  [Width](#cfn-ivs-encoderconfiguration-video-width): {{Integer}}
```

## Properties
<a name="aws-properties-ivs-encoderconfiguration-video-properties"></a>

`Bitrate`  <a name="cfn-ivs-encoderconfiguration-video-bitrate"></a>
Bitrate for generated output, in bps. Default: 2500000.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `8500000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Framerate`  <a name="cfn-ivs-encoderconfiguration-video-framerate"></a>
Video frame rate, in fps. Default: 30.
*Required*: No
*Type*: Number
*Minimum*: `1`
*Maximum*: `60`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Height`  <a name="cfn-ivs-encoderconfiguration-video-height"></a>
Video-resolution height. Note that the maximum value is determined by width times height, such that the maximum total pixels is 2073600 (1920x1080 or 1080x1920). Default: 720.
*Required*: No
*Type*: Integer
*Minimum*: `2`
*Maximum*: `1920`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Width`  <a name="cfn-ivs-encoderconfiguration-video-width"></a>
Video-resolution width. Note that the maximum value is determined by width times height, such that the maximum total pixels is 2073600 (1920x1080 or 1080x1920). Default: 1280.
*Required*: No
*Type*: Integer
*Minimum*: `2`
*Maximum*: `1920`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
