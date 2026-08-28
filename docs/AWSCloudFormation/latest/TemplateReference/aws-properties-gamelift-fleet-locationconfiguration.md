---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-gamelift-fleet-locationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GameLift::Fleet LocationConfiguration
<a name="aws-properties-gamelift-fleet-locationconfiguration"></a>

A remote location where a multi-location fleet can deploy game servers for game hosting.

## Syntax
<a name="aws-properties-gamelift-fleet-locationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-gamelift-fleet-locationconfiguration-syntax.json"></a>

```
{
  "[Location](#cfn-gamelift-fleet-locationconfiguration-location)" : {{String}},
  "[LocationCapacity](#cfn-gamelift-fleet-locationconfiguration-locationcapacity)" : {{LocationCapacity}},
  "[PlayerGatewayStatus](#cfn-gamelift-fleet-locationconfiguration-playergatewaystatus)" : {{String}}
}
```

### YAML
<a name="aws-properties-gamelift-fleet-locationconfiguration-syntax.yaml"></a>

```
  [Location](#cfn-gamelift-fleet-locationconfiguration-location): {{String}}
  [LocationCapacity](#cfn-gamelift-fleet-locationconfiguration-locationcapacity): {{
    LocationCapacity}}
  [PlayerGatewayStatus](#cfn-gamelift-fleet-locationconfiguration-playergatewaystatus): {{String}}
```

## Properties
<a name="aws-properties-gamelift-fleet-locationconfiguration-properties"></a>

`Location`  <a name="cfn-gamelift-fleet-locationconfiguration-location"></a>
An AWS Region code, such as `us-west-2`. For a list of supported Regions and Local Zones, see [ Amazon GameLift Servers service locations](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-regions.html) for managed hosting.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9\-]+`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LocationCapacity`  <a name="cfn-gamelift-fleet-locationconfiguration-locationcapacity"></a>
Current resource capacity settings for managed EC2 fleets and managed container fleets. For multi-location fleets, location values might refer to a fleet's remote location or its home Region.
**Returned by:**[DescribeFleetCapacity](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetCapacity.html), [DescribeFleetLocationCapacity](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetLocationCapacity.html), [UpdateFleetCapacity](https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateFleetCapacity.html)
*Required*: No
*Type*: [LocationCapacity](aws-properties-gamelift-fleet-locationcapacity.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PlayerGatewayStatus`  <a name="cfn-gamelift-fleet-locationconfiguration-playergatewaystatus"></a>
The current status of player gateway in this location for this fleet. Note, even if a fleet has PlayerGatewayMode configured as `ENABLED`, player gateway might not be available in a specific location. For more information about locations where player gateway is supported, see [Amazon GameLift Servers service locations](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-regions.html).
Possible values include:
+ `ENABLED` -- Player gateway is available for this fleet location.
+ `DISABLED` -- Player gateway is not available for this fleet location.
*Required*: No
*Type*: String
*Allowed values*: `DISABLED | ENABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
