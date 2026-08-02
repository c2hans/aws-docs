---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-gamelift-containerfleet-locationcapacity.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GameLift::ContainerFleet LocationCapacity
<a name="aws-properties-gamelift-containerfleet-locationcapacity"></a>

Current resource capacity settings for managed EC2 fleets and managed container fleets. For multi-location fleets, location values might refer to a fleet's remote location or its home Region.

**Returned by:**[DescribeFleetCapacity](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetCapacity.html), [DescribeFleetLocationCapacity](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetLocationCapacity.html), [UpdateFleetCapacity](https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateFleetCapacity.html)

## Syntax
<a name="aws-properties-gamelift-containerfleet-locationcapacity-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-gamelift-containerfleet-locationcapacity-syntax.json"></a>

```
{
  "[DesiredEC2Instances](#cfn-gamelift-containerfleet-locationcapacity-desiredec2instances)" : {{Integer}},
  "[ManagedCapacityConfiguration](#cfn-gamelift-containerfleet-locationcapacity-managedcapacityconfiguration)" : {{ManagedCapacityConfiguration}},
  "[MaxSize](#cfn-gamelift-containerfleet-locationcapacity-maxsize)" : {{Integer}},
  "[MinSize](#cfn-gamelift-containerfleet-locationcapacity-minsize)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-gamelift-containerfleet-locationcapacity-syntax.yaml"></a>

```
  [DesiredEC2Instances](#cfn-gamelift-containerfleet-locationcapacity-desiredec2instances): {{Integer}}
  [ManagedCapacityConfiguration](#cfn-gamelift-containerfleet-locationcapacity-managedcapacityconfiguration): {{
    ManagedCapacityConfiguration}}
  [MaxSize](#cfn-gamelift-containerfleet-locationcapacity-maxsize): {{Integer}}
  [MinSize](#cfn-gamelift-containerfleet-locationcapacity-minsize): {{Integer}}
```

## Properties
<a name="aws-properties-gamelift-containerfleet-locationcapacity-properties"></a>

`DesiredEC2Instances`  <a name="cfn-gamelift-containerfleet-locationcapacity-desiredec2instances"></a>
The number of Amazon EC2 instances you want to maintain in the specified fleet location. This value must fall between the minimum and maximum size limits. Changes in desired instance value can take up to 1 minute to be reflected when viewing the fleet's capacity settings.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ManagedCapacityConfiguration`  <a name="cfn-gamelift-containerfleet-locationcapacity-managedcapacityconfiguration"></a>
Use ManagedCapacityConfiguration with the "SCALE\_TO\_AND\_FROM\_ZERO" ZeroCapacityStrategy to enable Amazon GameLift Servers to fully manage the MinSize value, switching between 0 and 1 based on game session activity. This is ideal for eliminating compute costs during periods of no game activity. It is particularly beneficial during development when you're away from your desk, iterating on builds for extended periods, in production environments serving low-traffic locations, or for games with long, predictable downtime windows. By automatically managing capacity between 0 and 1 instances, you avoid paying for idle instances while maintaining the ability to serve game sessions when demand arrives. Note that while scale-out is triggered immediately upon receiving a game session request, actual game session availability depends on your server process startup time, so this approach works best with multi-location Fleets where cold-start latency is tolerable. With a "MANUAL" ZeroCapacityStrategy Amazon GameLift Servers will not modify Fleet MinSize values automatically and will not scale out from zero instances in response to game sessions.
*Required*: No
*Type*: [ManagedCapacityConfiguration](aws-properties-gamelift-containerfleet-managedcapacityconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxSize`  <a name="cfn-gamelift-containerfleet-locationcapacity-maxsize"></a>
The maximum number of instances that are allowed in the specified fleet location. If this parameter is not set, the default is 1.
*Required*: Yes
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MinSize`  <a name="cfn-gamelift-containerfleet-locationcapacity-minsize"></a>
The minimum number of instances that are allowed in the specified fleet location. If this parameter is not set, the default is 0. This parameter's value will be ignored when using a ManagedCapacityConfiguration where ZeroCapacityStrategy has a value of SCALE\_TO\_AND\_FROM\_ZERO.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
