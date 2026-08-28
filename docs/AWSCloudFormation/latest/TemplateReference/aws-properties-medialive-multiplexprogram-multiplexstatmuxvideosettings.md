---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-multiplexprogram-multiplexstatmuxvideosettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Multiplexprogram MultiplexStatmuxVideoSettings
<a name="aws-properties-medialive-multiplexprogram-multiplexstatmuxvideosettings"></a>

Statmux rate control settings

## Syntax
<a name="aws-properties-medialive-multiplexprogram-multiplexstatmuxvideosettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-multiplexprogram-multiplexstatmuxvideosettings-syntax.json"></a>

```
{
  "[MaximumBitrate](#cfn-medialive-multiplexprogram-multiplexstatmuxvideosettings-maximumbitrate)" : {{Integer}},
  "[MinimumBitrate](#cfn-medialive-multiplexprogram-multiplexstatmuxvideosettings-minimumbitrate)" : {{Integer}},
  "[Priority](#cfn-medialive-multiplexprogram-multiplexstatmuxvideosettings-priority)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-medialive-multiplexprogram-multiplexstatmuxvideosettings-syntax.yaml"></a>

```
  [MaximumBitrate](#cfn-medialive-multiplexprogram-multiplexstatmuxvideosettings-maximumbitrate): {{Integer}}
  [MinimumBitrate](#cfn-medialive-multiplexprogram-multiplexstatmuxvideosettings-minimumbitrate): {{Integer}}
  [Priority](#cfn-medialive-multiplexprogram-multiplexstatmuxvideosettings-priority): {{Integer}}
```

## Properties
<a name="aws-properties-medialive-multiplexprogram-multiplexstatmuxvideosettings-properties"></a>

`MaximumBitrate`  <a name="cfn-medialive-multiplexprogram-multiplexstatmuxvideosettings-maximumbitrate"></a>
Maximum statmux bitrate.
*Required*: No
*Type*: Integer
*Minimum*: `100000`
*Maximum*: `100000000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinimumBitrate`  <a name="cfn-medialive-multiplexprogram-multiplexstatmuxvideosettings-minimumbitrate"></a>
Minimum statmux bitrate.
*Required*: No
*Type*: Integer
*Minimum*: `100000`
*Maximum*: `100000000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Priority`  <a name="cfn-medialive-multiplexprogram-multiplexstatmuxvideosettings-priority"></a>
The purpose of the priority is to use a combination of the\\nmultiplex rate control algorithm and the QVBR capability of the\\nencoder to prioritize the video quality of some channels in a\\nmultiplex over others. Channels that have a higher priority will\\nget higher video quality at the expense of the video quality of\\nother channels in the multiplex with lower priority.
*Required*: No
*Type*: Integer
*Minimum*: `-5`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
