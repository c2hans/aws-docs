---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-channel-mediaconnectrouteroutputsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Channel MediaConnectRouterOutputSettings
<a name="aws-properties-medialive-channel-mediaconnectrouteroutputsettings"></a>

MediaConnect Router output settings.

The parent of this entity is OutputSettings.

## Syntax
<a name="aws-properties-medialive-channel-mediaconnectrouteroutputsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-channel-mediaconnectrouteroutputsettings-syntax.json"></a>

```
{
  "[ConnectedRouterInputs](#cfn-medialive-channel-mediaconnectrouteroutputsettings-connectedrouterinputs)" : {{MediaConnectRouterOutputConnectionMap}},
  "[ContainerSettings](#cfn-medialive-channel-mediaconnectrouteroutputsettings-containersettings)" : {{MediaConnectRouterContainerSettings}},
  "[Destination](#cfn-medialive-channel-mediaconnectrouteroutputsettings-destination)" : {{OutputLocationRef}}
}
```

### YAML
<a name="aws-properties-medialive-channel-mediaconnectrouteroutputsettings-syntax.yaml"></a>

```
  [ConnectedRouterInputs](#cfn-medialive-channel-mediaconnectrouteroutputsettings-connectedrouterinputs): {{
    MediaConnectRouterOutputConnectionMap}}
  [ContainerSettings](#cfn-medialive-channel-mediaconnectrouteroutputsettings-containersettings): {{
    MediaConnectRouterContainerSettings}}
  [Destination](#cfn-medialive-channel-mediaconnectrouteroutputsettings-destination): {{
    OutputLocationRef}}
```

## Properties
<a name="aws-properties-medialive-channel-mediaconnectrouteroutputsettings-properties"></a>

`ConnectedRouterInputs`  <a name="cfn-medialive-channel-mediaconnectrouteroutputsettings-connectedrouterinputs"></a>
This parameter is deprecated and unused.
*Required*: No
*Type*: [MediaConnectRouterOutputConnectionMap](aws-properties-medialive-channel-mediaconnectrouteroutputconnectionmap.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ContainerSettings`  <a name="cfn-medialive-channel-mediaconnectrouteroutputsettings-containersettings"></a>
Required. MediaConnect Router container settings.
*Required*: No
*Type*: [MediaConnectRouterContainerSettings](aws-properties-medialive-channel-mediaconnectroutercontainersettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Destination`  <a name="cfn-medialive-channel-mediaconnectrouteroutputsettings-destination"></a>
Required. Destination for this MediaConnect Router output. The referenced OutputDestination must have MediaConnect Router settings configured.
*Required*: No
*Type*: [OutputLocationRef](aws-properties-medialive-channel-outputlocationref.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
