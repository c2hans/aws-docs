---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-autoscaling-autoscalinggroup-availabilityzonedistribution.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AutoScaling::AutoScalingGroup AvailabilityZoneDistribution
<a name="aws-properties-autoscaling-autoscalinggroup-availabilityzonedistribution"></a>

`AvailabilityZoneDistribution` is a property of the [AWS::AutoScaling::AutoScalingGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscaling-autoscalinggroup.html) resource.

## Syntax
<a name="aws-properties-autoscaling-autoscalinggroup-availabilityzonedistribution-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-autoscaling-autoscalinggroup-availabilityzonedistribution-syntax.json"></a>

```
{
  "[CapacityDistributionStrategy](#cfn-autoscaling-autoscalinggroup-availabilityzonedistribution-capacitydistributionstrategy)" : {{String}}
}
```

### YAML
<a name="aws-properties-autoscaling-autoscalinggroup-availabilityzonedistribution-syntax.yaml"></a>

```
  [CapacityDistributionStrategy](#cfn-autoscaling-autoscalinggroup-availabilityzonedistribution-capacitydistributionstrategy): {{String}}
```

## Properties
<a name="aws-properties-autoscaling-autoscalinggroup-availabilityzonedistribution-properties"></a>

`CapacityDistributionStrategy`  <a name="cfn-autoscaling-autoscalinggroup-availabilityzonedistribution-capacitydistributionstrategy"></a>
 If launches fail in an Availability Zone, the following strategies are available. The default is `balanced-best-effort`.
+ `balanced-only` - If launches fail in an Availability Zone, Auto Scaling will continue to attempt to launch in the unhealthy zone to preserve a balanced distribution.
+ `balanced-best-effort` - If launches fail in an Availability Zone, Auto Scaling will attempt to launch in another healthy Availability Zone instead.
+ `reservations-then-balanced` - Auto Scaling will first attempt to launch into your Capacity Reservations, and then balance any remaining capacity across healthy Availability Zones.
*Required*: No
*Type*: String
*Allowed values*: `balanced-best-effort | balanced-only | reservations-then-balanced`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
