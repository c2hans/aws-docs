---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eventsv2-subscriber-pointintimeconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EventsV2::Subscriber PointInTimeConfiguration
<a name="aws-properties-eventsv2-subscriber-pointintimeconfiguration"></a>

The point in time to start delivering events from, used when StartingPosition is POINT\_IN\_TIME.

## Syntax
<a name="aws-properties-eventsv2-subscriber-pointintimeconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eventsv2-subscriber-pointintimeconfiguration-syntax.json"></a>

```
{
  "[EndPoint](#cfn-eventsv2-subscriber-pointintimeconfiguration-endpoint)" : {{Integer}},
  "[PointType](#cfn-eventsv2-subscriber-pointintimeconfiguration-pointtype)" : {{String}},
  "[StartingPoint](#cfn-eventsv2-subscriber-pointintimeconfiguration-startingpoint)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-eventsv2-subscriber-pointintimeconfiguration-syntax.yaml"></a>

```
  [EndPoint](#cfn-eventsv2-subscriber-pointintimeconfiguration-endpoint): {{Integer}}
  [PointType](#cfn-eventsv2-subscriber-pointintimeconfiguration-pointtype): {{String}}
  [StartingPoint](#cfn-eventsv2-subscriber-pointintimeconfiguration-startingpoint): {{Integer}}
```

## Properties
<a name="aws-properties-eventsv2-subscriber-pointintimeconfiguration-properties"></a>

`EndPoint`  <a name="cfn-eventsv2-subscriber-pointintimeconfiguration-endpoint"></a>
An optional time to stop delivering events at, in seconds since the Unix epoch.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PointType`  <a name="cfn-eventsv2-subscriber-pointintimeconfiguration-pointtype"></a>
Where to start: HORIZON starts from the earliest available event; TIMESTAMP starts from the StartingPoint timestamp.
*Required*: Yes
*Type*: String
*Allowed values*: `HORIZON | TIMESTAMP`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StartingPoint`  <a name="cfn-eventsv2-subscriber-pointintimeconfiguration-startingpoint"></a>
The time to start delivering events from, in seconds since the Unix epoch. Required when PointType is TIMESTAMP.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
