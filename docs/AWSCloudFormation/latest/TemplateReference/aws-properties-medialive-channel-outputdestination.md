---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-outputdestination.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel OutputDestination
<a name="aws-properties-medialive-channel-outputdestination"></a>

Configuration information for an output.

This entity is at the top level in the channel.

## Syntax
<a name="aws-properties-medialive-channel-outputdestination-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-outputdestination-syntax.json"></a>

```
{
  "[Id](#cfn-medialive-channel-outputdestination-id)" : {{String}},
  "[LogicalInterfaceNames](#cfn-medialive-channel-outputdestination-logicalinterfacenames)" : {{[ String, ... ]}},
  "[MediaConnectRouterSettings](#cfn-medialive-channel-outputdestination-mediaconnectroutersettings)" : {{[ MediaConnectRouterOutputDestinationSettings, ... ]}},
  "[MediaPackageSettings](#cfn-medialive-channel-outputdestination-mediapackagesettings)" : {{[ MediaPackageOutputDestinationSettings, ... ]}},
  "[MultiplexSettings](#cfn-medialive-channel-outputdestination-multiplexsettings)" : {{MultiplexProgramChannelDestinationSettings}},
  "[Settings](#cfn-medialive-channel-outputdestination-settings)" : {{[ OutputDestinationSettings, ... ]}},
  "[SrtSettings](#cfn-medialive-channel-outputdestination-srtsettings)" : {{[ SrtOutputDestinationSettings, ... ]}}
}
```

### YAML
<a name="aws-properties-medialive-channel-outputdestination-syntax.yaml"></a>

```
  [Id](#cfn-medialive-channel-outputdestination-id): {{String}}
  [LogicalInterfaceNames](#cfn-medialive-channel-outputdestination-logicalinterfacenames): {{
    - String}}
  [MediaConnectRouterSettings](#cfn-medialive-channel-outputdestination-mediaconnectroutersettings): {{
    - MediaConnectRouterOutputDestinationSettings}}
  [MediaPackageSettings](#cfn-medialive-channel-outputdestination-mediapackagesettings): {{
    - MediaPackageOutputDestinationSettings}}
  [MultiplexSettings](#cfn-medialive-channel-outputdestination-multiplexsettings): {{
    MultiplexProgramChannelDestinationSettings}}
  [Settings](#cfn-medialive-channel-outputdestination-settings): {{
    - OutputDestinationSettings}}
  [SrtSettings](#cfn-medialive-channel-outputdestination-srtsettings): {{
    - SrtOutputDestinationSettings}}
```

## Properties
<a name="aws-properties-medialive-channel-outputdestination-properties"></a>

`Id`  <a name="cfn-medialive-channel-outputdestination-id"></a>
The ID for this destination.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LogicalInterfaceNames`  <a name="cfn-medialive-channel-outputdestination-logicalinterfacenames"></a>
Optional assignment of an output to a logical interface on the Node. Only applies to on premises channels.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MediaConnectRouterSettings`  <a name="cfn-medialive-channel-outputdestination-mediaconnectroutersettings"></a>
Destination settings for a MediaConnect Router output; one destination for each redundant encoder.
*Required*: No
*Type*: Array of [MediaConnectRouterOutputDestinationSettings](aws-properties-medialive-channel-mediaconnectrouteroutputdestinationsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MediaPackageSettings`  <a name="cfn-medialive-channel-outputdestination-mediapackagesettings"></a>
The destination settings for a MediaPackage output.
*Required*: No
*Type*: Array of [MediaPackageOutputDestinationSettings](aws-properties-medialive-channel-mediapackageoutputdestinationsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MultiplexSettings`  <a name="cfn-medialive-channel-outputdestination-multiplexsettings"></a>
Destination settings for a Multiplex output; one destination for both encoders.
*Required*: No
*Type*: [MultiplexProgramChannelDestinationSettings](aws-properties-medialive-channel-multiplexprogramchanneldestinationsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Settings`  <a name="cfn-medialive-channel-outputdestination-settings"></a>
The destination settings for an output.
*Required*: No
*Type*: Array of [OutputDestinationSettings](aws-properties-medialive-channel-outputdestinationsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SrtSettings`  <a name="cfn-medialive-channel-outputdestination-srtsettings"></a>
SRT settings for an SRT output; one destination for each redundant encoder.
*Required*: No
*Type*: Array of [SrtOutputDestinationSettings](aws-properties-medialive-channel-srtoutputdestinationsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
