---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-autoscaling-autoscalinggroup-capacityreservationtarget.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AutoScaling::AutoScalingGroup CapacityReservationTarget
<a name="aws-properties-autoscaling-autoscalinggroup-capacityreservationtarget"></a>

 The target for the Capacity Reservation. Specify Capacity Reservations IDs or Capacity Reservation resource group ARNs.

## Syntax
<a name="aws-properties-autoscaling-autoscalinggroup-capacityreservationtarget-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-autoscaling-autoscalinggroup-capacityreservationtarget-syntax.json"></a>

```
{
  "[CapacityReservationIds](#cfn-autoscaling-autoscalinggroup-capacityreservationtarget-capacityreservationids)" : {{[ String, ... ]}},
  "[CapacityReservationResourceGroupArns](#cfn-autoscaling-autoscalinggroup-capacityreservationtarget-capacityreservationresourcegrouparns)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-autoscaling-autoscalinggroup-capacityreservationtarget-syntax.yaml"></a>

```
  [CapacityReservationIds](#cfn-autoscaling-autoscalinggroup-capacityreservationtarget-capacityreservationids): {{
    - String}}
  [CapacityReservationResourceGroupArns](#cfn-autoscaling-autoscalinggroup-capacityreservationtarget-capacityreservationresourcegrouparns): {{
    - String}}
```

## Properties
<a name="aws-properties-autoscaling-autoscalinggroup-capacityreservationtarget-properties"></a>

`CapacityReservationIds`  <a name="cfn-autoscaling-autoscalinggroup-capacityreservationtarget-capacityreservationids"></a>
 The Capacity Reservation IDs to launch instances into.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CapacityReservationResourceGroupArns`  <a name="cfn-autoscaling-autoscalinggroup-capacityreservationtarget-capacityreservationresourcegrouparns"></a>
 The resource group ARNs of the Capacity Reservation to launch instances into.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
