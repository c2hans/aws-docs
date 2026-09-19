---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediapackagev2-channel-multiviewconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaPackageV2::Channel MultiviewConfiguration
<a name="aws-properties-mediapackagev2-channel-multiviewconfiguration"></a>

The multiview configuration for a channel. A multiview channel composites video from several source channels into a single tiled output stream. Players receive one standard HLS or DASH stream instead of several separate streams. This setting is required when `InputType` is `MULTIVIEW`, and can't be set for any other input type.

## Syntax
<a name="aws-properties-mediapackagev2-channel-multiviewconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediapackagev2-channel-multiviewconfiguration-syntax.json"></a>

```
{
  "[AvailableLayouts](#cfn-mediapackagev2-channel-multiviewconfiguration-availablelayouts)" : {{[ String, ... ]}},
  "[AvailableSources](#cfn-mediapackagev2-channel-multiviewconfiguration-availablesources)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-mediapackagev2-channel-multiviewconfiguration-syntax.yaml"></a>

```
  [AvailableLayouts](#cfn-mediapackagev2-channel-multiviewconfiguration-availablelayouts): {{
    - String}}
  [AvailableSources](#cfn-mediapackagev2-channel-multiviewconfiguration-availablesources): {{
    - String}}
```

## Properties
<a name="aws-properties-mediapackagev2-channel-multiviewconfiguration-properties"></a>

`AvailableLayouts`  <a name="cfn-mediapackagev2-channel-multiviewconfiguration-availablelayouts"></a>
The tile layouts that players can request from this multiview channel's origin endpoints. Only the layouts that you list here are available. Each layout must appear at most once.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `6`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AvailableSources`  <a name="cfn-mediapackagev2-channel-multiviewconfiguration-availablesources"></a>
The channels that players can use as tiles in this multiview channel's output. Each source channel must be in the same channel group as the multiview channel, and must have an `InputType` of `CMAF`. Only the channels that you list here are available as tiles.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `256 | 10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
