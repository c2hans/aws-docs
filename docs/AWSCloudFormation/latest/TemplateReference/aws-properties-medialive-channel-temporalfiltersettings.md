---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-temporalfiltersettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel TemporalFilterSettings
<a name="aws-properties-medialive-channel-temporalfiltersettings"></a>

Settings for the temporal filter to apply to the video.

The parents of this entity are H264FilterSettings, H265FilterSettings, and Mpeg2FilterSettings.

## Syntax
<a name="aws-properties-medialive-channel-temporalfiltersettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-temporalfiltersettings-syntax.json"></a>

```
{
  "[PostFilterSharpening](#cfn-medialive-channel-temporalfiltersettings-postfiltersharpening)" : {{String}},
  "[Strength](#cfn-medialive-channel-temporalfiltersettings-strength)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-channel-temporalfiltersettings-syntax.yaml"></a>

```
  [PostFilterSharpening](#cfn-medialive-channel-temporalfiltersettings-postfiltersharpening): {{String}}
  [Strength](#cfn-medialive-channel-temporalfiltersettings-strength): {{String}}
```

## Properties
<a name="aws-properties-medialive-channel-temporalfiltersettings-properties"></a>

`PostFilterSharpening`  <a name="cfn-medialive-channel-temporalfiltersettings-postfiltersharpening"></a>
If you enable this filter, the results are the following: - If the source content is noisy (it contains excessive digital artifacts), the filter cleans up the source. - If the source content is already clean, the filter tends to decrease the bitrate, especially when the rate control mode is QVBR.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Strength`  <a name="cfn-medialive-channel-temporalfiltersettings-strength"></a>
Choose a filter strength. We recommend a strength of 1 or 2. A higher strength might take out good information, resulting in an image that is overly soft.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
