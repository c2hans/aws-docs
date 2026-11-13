---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-audiofeedinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel AudioFeedInput
<a name="aws-properties-medialive-channel-audiofeedinput"></a>

A mapping of an audio selector in the channel to a feed input on the associated AWS Elemental Inference feed.

The parent of this entity is InferenceSettings.

## Syntax
<a name="aws-properties-medialive-channel-audiofeedinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-audiofeedinput-syntax.json"></a>

```
{
  "[AudioSelectorName](#cfn-medialive-channel-audiofeedinput-audioselectorname)" : {{String}},
  "[FeedInput](#cfn-medialive-channel-audiofeedinput-feedinput)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-channel-audiofeedinput-syntax.yaml"></a>

```
  [AudioSelectorName](#cfn-medialive-channel-audiofeedinput-audioselectorname): {{String}}
  [FeedInput](#cfn-medialive-channel-audiofeedinput-feedinput): {{String}}
```

## Properties
<a name="aws-properties-medialive-channel-audiofeedinput-properties"></a>

`AudioSelectorName`  <a name="cfn-medialive-channel-audiofeedinput-audioselectorname"></a>
The name of an audio selector in the channel's input attachment whose audio MediaLive sends to the specified feed input.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FeedInput`  <a name="cfn-medialive-channel-audiofeedinput-feedinput"></a>
The name of the feed input on the Elemental Inference feed that receives the audio from the specified audio selector.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
