---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-mediapackageoutputdestinationsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel MediaPackageOutputDestinationSettings
<a name="aws-properties-medialive-channel-mediapackageoutputdestinationsettings"></a>

Destination settings for a MediaPackage output.

The parent of this entity is OutputDestination.

## Syntax
<a name="aws-properties-medialive-channel-mediapackageoutputdestinationsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-mediapackageoutputdestinationsettings-syntax.json"></a>

```
{
  "[ChannelEndpointId](#cfn-medialive-channel-mediapackageoutputdestinationsettings-channelendpointid)" : {{String}},
  "[ChannelGroup](#cfn-medialive-channel-mediapackageoutputdestinationsettings-channelgroup)" : {{String}},
  "[ChannelId](#cfn-medialive-channel-mediapackageoutputdestinationsettings-channelid)" : {{String}},
  "[ChannelName](#cfn-medialive-channel-mediapackageoutputdestinationsettings-channelname)" : {{String}},
  "[MediaPackageRegionName](#cfn-medialive-channel-mediapackageoutputdestinationsettings-mediapackageregionname)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-channel-mediapackageoutputdestinationsettings-syntax.yaml"></a>

```
  [ChannelEndpointId](#cfn-medialive-channel-mediapackageoutputdestinationsettings-channelendpointid): {{String}}
  [ChannelGroup](#cfn-medialive-channel-mediapackageoutputdestinationsettings-channelgroup): {{String}}
  [ChannelId](#cfn-medialive-channel-mediapackageoutputdestinationsettings-channelid): {{String}}
  [ChannelName](#cfn-medialive-channel-mediapackageoutputdestinationsettings-channelname): {{String}}
  [MediaPackageRegionName](#cfn-medialive-channel-mediapackageoutputdestinationsettings-mediapackageregionname): {{String}}
```

## Properties
<a name="aws-properties-medialive-channel-mediapackageoutputdestinationsettings-properties"></a>

`ChannelEndpointId`  <a name="cfn-medialive-channel-mediapackageoutputdestinationsettings-channelendpointid"></a>
The channel endpoint ID for the MediaPackage V2 destination.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ChannelGroup`  <a name="cfn-medialive-channel-mediapackageoutputdestinationsettings-channelgroup"></a>
The channel group for the MediaPackage V2 destination.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ChannelId`  <a name="cfn-medialive-channel-mediapackageoutputdestinationsettings-channelid"></a>
The ID of the channel in MediaPackage that is the destination for this output group. You don't need to specify the individual inputs in MediaPackage; MediaLive handles the connection of the two MediaLive pipelines to the two MediaPackage inputs. The MediaPackage channel and MediaLive channel must be in the same Region.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ChannelName`  <a name="cfn-medialive-channel-mediapackageoutputdestinationsettings-channelname"></a>
The channel name for the MediaPackage V2 destination.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MediaPackageRegionName`  <a name="cfn-medialive-channel-mediapackageoutputdestinationsettings-mediapackageregionname"></a>
The Region name for the MediaPackage destination.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
