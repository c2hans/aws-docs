---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-framecapturesettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel FrameCaptureSettings
<a name="aws-properties-medialive-channel-framecapturesettings"></a>

The frame capture settings.

The parent of this entity is VideoCodecSettings.

## Syntax
<a name="aws-properties-medialive-channel-framecapturesettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-framecapturesettings-syntax.json"></a>

```
{
  "[CaptureInterval](#cfn-medialive-channel-framecapturesettings-captureinterval)" : {{Integer}},
  "[CaptureIntervalUnits](#cfn-medialive-channel-framecapturesettings-captureintervalunits)" : {{String}},
  "[TimecodeBurninSettings](#cfn-medialive-channel-framecapturesettings-timecodeburninsettings)" : {{TimecodeBurninSettings}}
}
```

### YAML
<a name="aws-properties-medialive-channel-framecapturesettings-syntax.yaml"></a>

```
  [CaptureInterval](#cfn-medialive-channel-framecapturesettings-captureinterval): {{Integer}}
  [CaptureIntervalUnits](#cfn-medialive-channel-framecapturesettings-captureintervalunits): {{String}}
  [TimecodeBurninSettings](#cfn-medialive-channel-framecapturesettings-timecodeburninsettings): {{
    TimecodeBurninSettings}}
```

## Properties
<a name="aws-properties-medialive-channel-framecapturesettings-properties"></a>

`CaptureInterval`  <a name="cfn-medialive-channel-framecapturesettings-captureinterval"></a>
The frequency, in seconds, for capturing frames for inclusion in the output. For example, "10" means capture a frame every 10 seconds.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CaptureIntervalUnits`  <a name="cfn-medialive-channel-framecapturesettings-captureintervalunits"></a>
Unit for the frame capture interval.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimecodeBurninSettings`  <a name="cfn-medialive-channel-framecapturesettings-timecodeburninsettings"></a>
Timecode burn-in settings for the frame capture output.
*Required*: No
*Type*: [TimecodeBurninSettings](aws-properties-medialive-channel-timecodeburninsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
