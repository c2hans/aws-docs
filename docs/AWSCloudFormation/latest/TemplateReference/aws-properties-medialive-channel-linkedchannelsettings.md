---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-linkedchannelsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel LinkedChannelSettings
<a name="aws-properties-medialive-channel-linkedchannelsettings"></a>

The linked channel settings for the channel.

## Syntax
<a name="aws-properties-medialive-channel-linkedchannelsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-linkedchannelsettings-syntax.json"></a>

```
{
  "[FollowerChannelSettings](#cfn-medialive-channel-linkedchannelsettings-followerchannelsettings)" : {{FollowerChannelSettings}},
  "[PrimaryChannelSettings](#cfn-medialive-channel-linkedchannelsettings-primarychannelsettings)" : {{PrimaryChannelSettings}}
}
```

### YAML
<a name="aws-properties-medialive-channel-linkedchannelsettings-syntax.yaml"></a>

```
  [FollowerChannelSettings](#cfn-medialive-channel-linkedchannelsettings-followerchannelsettings): {{
    FollowerChannelSettings}}
  [PrimaryChannelSettings](#cfn-medialive-channel-linkedchannelsettings-primarychannelsettings): {{
    PrimaryChannelSettings}}
```

## Properties
<a name="aws-properties-medialive-channel-linkedchannelsettings-properties"></a>

`FollowerChannelSettings`  <a name="cfn-medialive-channel-linkedchannelsettings-followerchannelsettings"></a>
Settings for a follower channel in a linked pair.
*Required*: No
*Type*: [FollowerChannelSettings](aws-properties-medialive-channel-followerchannelsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrimaryChannelSettings`  <a name="cfn-medialive-channel-linkedchannelsettings-primarychannelsettings"></a>
Settings for a primary (leader) channel in a linked pair.
*Required*: No
*Type*: [PrimaryChannelSettings](aws-properties-medialive-channel-primarychannelsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
