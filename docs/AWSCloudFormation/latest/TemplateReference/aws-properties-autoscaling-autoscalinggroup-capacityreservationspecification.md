---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-autoscaling-autoscalinggroup-capacityreservationspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AutoScaling::AutoScalingGroup CapacityReservationSpecification
<a name="aws-properties-autoscaling-autoscalinggroup-capacityreservationspecification"></a>

 Describes the Capacity Reservation preference and targeting options. If you specify `open` or `none` for `CapacityReservationPreference`, do not specify a `CapacityReservationTarget`.

## Syntax
<a name="aws-properties-autoscaling-autoscalinggroup-capacityreservationspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-autoscaling-autoscalinggroup-capacityreservationspecification-syntax.json"></a>

```
{
  "[CapacityReservationPreference](#cfn-autoscaling-autoscalinggroup-capacityreservationspecification-capacityreservationpreference)" : {{String}},
  "[CapacityReservationTarget](#cfn-autoscaling-autoscalinggroup-capacityreservationspecification-capacityreservationtarget)" : {{CapacityReservationTarget}}
}
```

### YAML
<a name="aws-properties-autoscaling-autoscalinggroup-capacityreservationspecification-syntax.yaml"></a>

```
  [CapacityReservationPreference](#cfn-autoscaling-autoscalinggroup-capacityreservationspecification-capacityreservationpreference): {{String}}
  [CapacityReservationTarget](#cfn-autoscaling-autoscalinggroup-capacityreservationspecification-capacityreservationtarget): {{
    CapacityReservationTarget}}
```

## Properties
<a name="aws-properties-autoscaling-autoscalinggroup-capacityreservationspecification-properties"></a>

`CapacityReservationPreference`  <a name="cfn-autoscaling-autoscalinggroup-capacityreservationspecification-capacityreservationpreference"></a>
 The capacity reservation preference. The following options are available:
+ `capacity-reservations-only` - Auto Scaling will only launch instances into a Capacity Reservation or Capacity Reservation resource group. If capacity isn't available, instances will fail to launch.
+ `capacity-reservations-first` - Auto Scaling will try to launch instances into a Capacity Reservation or Capacity Reservation resource group first. If capacity isn't available, instances will run in On-Demand capacity.
+ `none` - Auto Scaling will not launch instances into a Capacity Reservation. Instances will run in On-Demand capacity.
+ `default` - Auto Scaling uses the Capacity Reservation preference from your launch template or an open Capacity Reservation.
*Required*: Yes
*Type*: String
*Allowed values*: `capacity-reservations-only | capacity-reservations-first | none | default`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CapacityReservationTarget`  <a name="cfn-autoscaling-autoscalinggroup-capacityreservationspecification-capacityreservationtarget"></a>
 Describes a target Capacity Reservation or Capacity Reservation resource group.
*Required*: No
*Type*: [CapacityReservationTarget](aws-properties-autoscaling-autoscalinggroup-capacityreservationtarget.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
