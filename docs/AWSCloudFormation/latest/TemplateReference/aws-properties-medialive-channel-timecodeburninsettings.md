---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-timecodeburninsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel TimecodeBurninSettings
<a name="aws-properties-medialive-channel-timecodeburninsettings"></a>

Timecode burn-in settings.

The parent of this entity is the codec settings (H264Settings, H265Settings, Mpeg2Settings, or FrameCaptureSettings).

## Syntax
<a name="aws-properties-medialive-channel-timecodeburninsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-timecodeburninsettings-syntax.json"></a>

```
{
  "[FontSize](#cfn-medialive-channel-timecodeburninsettings-fontsize)" : {{String}},
  "[Position](#cfn-medialive-channel-timecodeburninsettings-position)" : {{String}},
  "[Prefix](#cfn-medialive-channel-timecodeburninsettings-prefix)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-channel-timecodeburninsettings-syntax.yaml"></a>

```
  [FontSize](#cfn-medialive-channel-timecodeburninsettings-fontsize): {{String}}
  [Position](#cfn-medialive-channel-timecodeburninsettings-position): {{String}}
  [Prefix](#cfn-medialive-channel-timecodeburninsettings-prefix): {{String}}
```

## Properties
<a name="aws-properties-medialive-channel-timecodeburninsettings-properties"></a>

`FontSize`  <a name="cfn-medialive-channel-timecodeburninsettings-fontsize"></a>
Required. Choose a timecode burn-in font size.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Position`  <a name="cfn-medialive-channel-timecodeburninsettings-position"></a>
Required. Choose a timecode burn-in output position.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Prefix`  <a name="cfn-medialive-channel-timecodeburninsettings-prefix"></a>
Create a timecode burn-in prefix (optional).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
