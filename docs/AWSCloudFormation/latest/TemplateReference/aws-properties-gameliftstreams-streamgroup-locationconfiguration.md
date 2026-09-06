---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-gameliftstreams-streamgroup-locationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GameLiftStreams::StreamGroup LocationConfiguration
<a name="aws-properties-gameliftstreams-streamgroup-locationconfiguration"></a>

Configuration settings that define a stream group's stream capacity for a location. When configuring a location for the first time, you must specify a numeric value for at least one of the two capacity types.

## Syntax
<a name="aws-properties-gameliftstreams-streamgroup-locationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-gameliftstreams-streamgroup-locationconfiguration-syntax.json"></a>

```
{
  "[AlwaysOnCapacity](#cfn-gameliftstreams-streamgroup-locationconfiguration-alwaysoncapacity)" : {{Integer}},
  "[LocationName](#cfn-gameliftstreams-streamgroup-locationconfiguration-locationname)" : {{String}},
  "[MaximumCapacity](#cfn-gameliftstreams-streamgroup-locationconfiguration-maximumcapacity)" : {{Integer}},
  "[OnDemandCapacity](#cfn-gameliftstreams-streamgroup-locationconfiguration-ondemandcapacity)" : {{Integer}},
  "[TargetIdleCapacity](#cfn-gameliftstreams-streamgroup-locationconfiguration-targetidlecapacity)" : {{Integer}},
  "[VpcTransitConfiguration](#cfn-gameliftstreams-streamgroup-locationconfiguration-vpctransitconfiguration)" : {{VpcTransitConfiguration}}
}
```

### YAML
<a name="aws-properties-gameliftstreams-streamgroup-locationconfiguration-syntax.yaml"></a>

```
  [AlwaysOnCapacity](#cfn-gameliftstreams-streamgroup-locationconfiguration-alwaysoncapacity): {{Integer}}
  [LocationName](#cfn-gameliftstreams-streamgroup-locationconfiguration-locationname): {{String}}
  [MaximumCapacity](#cfn-gameliftstreams-streamgroup-locationconfiguration-maximumcapacity): {{Integer}}
  [OnDemandCapacity](#cfn-gameliftstreams-streamgroup-locationconfiguration-ondemandcapacity): {{Integer}}
  [TargetIdleCapacity](#cfn-gameliftstreams-streamgroup-locationconfiguration-targetidlecapacity): {{Integer}}
  [VpcTransitConfiguration](#cfn-gameliftstreams-streamgroup-locationconfiguration-vpctransitconfiguration): {{
    VpcTransitConfiguration}}
```

## Properties
<a name="aws-properties-gameliftstreams-streamgroup-locationconfiguration-properties"></a>

`AlwaysOnCapacity`  <a name="cfn-gameliftstreams-streamgroup-locationconfiguration-alwaysoncapacity"></a>
This setting, if non-zero, indicates minimum streaming capacity which is allocated to you and is never released back to the service. You pay for this base level of capacity at all times, whether used or idle.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LocationName`  <a name="cfn-gameliftstreams-streamgroup-locationconfiguration-locationname"></a>
 A location's name. For example, `us-east-1`. For a complete list of locations that Amazon GameLift Streams supports, refer to [Regions, quotas, and limitations](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/regions-quotas.html) in the *Amazon GameLift Streams Developer Guide*.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9-]+$`
*Minimum*: `1`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaximumCapacity`  <a name="cfn-gameliftstreams-streamgroup-locationconfiguration-maximumcapacity"></a>
This indicates the maximum capacity that the service can allocate for you. Newly created streams may take a few minutes to start. Capacity is released back to the service when idle. You pay for capacity that is allocated to you until it is released.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OnDemandCapacity`  <a name="cfn-gameliftstreams-streamgroup-locationconfiguration-ondemandcapacity"></a>
This field is deprecated. Use MaximumCapacity instead. This parameter is ignored when MaximumCapacity is specified.
The streaming capacity that Amazon GameLift Streams can allocate in response to stream requests, and then de-allocate when the session has terminated. This offers a cost control measure at the expense of a greater startup time (typically under 5 minutes). Default is 0 when you create a stream group or add a location.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetIdleCapacity`  <a name="cfn-gameliftstreams-streamgroup-locationconfiguration-targetidlecapacity"></a>
This indicates idle capacity which the service pre-allocates and holds for you in anticipation of future activity. This helps to insulate your users from capacity-allocation delays. You pay for capacity which is held in this intentional idle state.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcTransitConfiguration`  <a name="cfn-gameliftstreams-streamgroup-locationconfiguration-vpctransitconfiguration"></a>
Configuration for connecting the stream group to resources in your Amazon VPC using a Transit Gateway. This setting is optional. If specified, Amazon GameLift Streams creates a Transit Gateway to enable private network connectivity between the service VPC and your VPC. The VPC ID cannot be changed after the stream group is created, but you can update the CIDR blocks.
*Required*: No
*Type*: [VpcTransitConfiguration](aws-properties-gameliftstreams-streamgroup-vpctransitconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
