---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-anywheresettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel AnywhereSettings
<a name="aws-properties-medialive-channel-anywheresettings"></a>

The Elemental Anywhere settings for this channel.

## Syntax
<a name="aws-properties-medialive-channel-anywheresettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-anywheresettings-syntax.json"></a>

```
{
  "[ChannelPlacementGroupId](#cfn-medialive-channel-anywheresettings-channelplacementgroupid)" : {{String}},
  "[ClusterId](#cfn-medialive-channel-anywheresettings-clusterid)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-channel-anywheresettings-syntax.yaml"></a>

```
  [ChannelPlacementGroupId](#cfn-medialive-channel-anywheresettings-channelplacementgroupid): {{String}}
  [ClusterId](#cfn-medialive-channel-anywheresettings-clusterid): {{String}}
```

## Properties
<a name="aws-properties-medialive-channel-anywheresettings-properties"></a>

`ChannelPlacementGroupId`  <a name="cfn-medialive-channel-anywheresettings-channelplacementgroupid"></a>
The ID of the channel placement group for the channel.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClusterId`  <a name="cfn-medialive-channel-anywheresettings-clusterid"></a>
The ID of the cluster for the channel.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
