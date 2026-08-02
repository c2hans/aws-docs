---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-gamelift-containerfleet-locationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GameLift::ContainerFleet LocationConfiguration
<a name="aws-properties-gamelift-containerfleet-locationconfiguration"></a>

A remote location where a multi-location fleet can deploy game servers for game hosting.

## Syntax
<a name="aws-properties-gamelift-containerfleet-locationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-gamelift-containerfleet-locationconfiguration-syntax.json"></a>

```
{
  "[Location](#cfn-gamelift-containerfleet-locationconfiguration-location)" : {{String}},
  "[LocationCapacity](#cfn-gamelift-containerfleet-locationconfiguration-locationcapacity)" : {{LocationCapacity}},
  "[PlayerGatewayStatus](#cfn-gamelift-containerfleet-locationconfiguration-playergatewaystatus)" : {{String}},
  "[StoppedActions](#cfn-gamelift-containerfleet-locationconfiguration-stoppedactions)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-gamelift-containerfleet-locationconfiguration-syntax.yaml"></a>

```
  [Location](#cfn-gamelift-containerfleet-locationconfiguration-location): {{String}}
  [LocationCapacity](#cfn-gamelift-containerfleet-locationconfiguration-locationcapacity): {{
    LocationCapacity}}
  [PlayerGatewayStatus](#cfn-gamelift-containerfleet-locationconfiguration-playergatewaystatus): {{String}}
  [StoppedActions](#cfn-gamelift-containerfleet-locationconfiguration-stoppedactions): {{
    - String}}
```

## Properties
<a name="aws-properties-gamelift-containerfleet-locationconfiguration-properties"></a>

`Location`  <a name="cfn-gamelift-containerfleet-locationconfiguration-location"></a>
An AWS Region code, such as `us-west-2`. For a list of supported Regions and Local Zones, see [ Amazon GameLift Servers service locations](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-regions.html) for managed hosting.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9\-]+`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LocationCapacity`  <a name="cfn-gamelift-containerfleet-locationconfiguration-locationcapacity"></a>
Current resource capacity settings for managed EC2 fleets and managed container fleets. For multi-location fleets, location values might refer to a fleet's remote location or its home Region.
**Returned by:**[DescribeFleetCapacity](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetCapacity.html), [DescribeFleetLocationCapacity](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetLocationCapacity.html), [UpdateFleetCapacity](https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateFleetCapacity.html)
*Required*: No
*Type*: [LocationCapacity](aws-properties-gamelift-containerfleet-locationcapacity.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PlayerGatewayStatus`  <a name="cfn-gamelift-containerfleet-locationconfiguration-playergatewaystatus"></a>
The current status of player gateway in this location for this container fleet. Note, even if a container fleet has PlayerGatewayMode configured as `ENABLED`, player gateway might not be available in a specific location. For more information about locations where player gateway is supported, see [Amazon GameLift Servers service locations](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-regions.html).
Possible values include:
+ `ENABLED` -- Player gateway is available for this container fleet location.
+ `DISABLED` -- Player gateway is not available for this container fleet location.
*Required*: No
*Type*: String
*Allowed values*: `DISABLED | ENABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StoppedActions`  <a name="cfn-gamelift-containerfleet-locationconfiguration-stoppedactions"></a>
A list of fleet actions that have been suspended in the fleet location.
*Required*: No
*Type*: Array of String
*Allowed values*: `AUTO_SCALING`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
