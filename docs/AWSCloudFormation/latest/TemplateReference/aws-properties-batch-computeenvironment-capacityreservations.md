---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-batch-computeenvironment-capacityreservations.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Batch::ComputeEnvironment CapacityReservations
<a name="aws-properties-batch-computeenvironment-capacityreservations"></a>

The capacity reservation configuration for Amazon ECS Managed Instances. Use this to target On-Demand Capacity Reservations or Reserved Instances.

## Syntax
<a name="aws-properties-batch-computeenvironment-capacityreservations-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-batch-computeenvironment-capacityreservations-syntax.json"></a>

```
{
  "[ReservationGroupArn](#cfn-batch-computeenvironment-capacityreservations-reservationgrouparn)" : {{String}},
  "[ReservationPreference](#cfn-batch-computeenvironment-capacityreservations-reservationpreference)" : {{String}}
}
```

### YAML
<a name="aws-properties-batch-computeenvironment-capacityreservations-syntax.yaml"></a>

```
  [ReservationGroupArn](#cfn-batch-computeenvironment-capacityreservations-reservationgrouparn): {{String}}
  [ReservationPreference](#cfn-batch-computeenvironment-capacityreservations-reservationpreference): {{String}}
```

## Properties
<a name="aws-properties-batch-computeenvironment-capacityreservations-properties"></a>

`ReservationGroupArn`  <a name="cfn-batch-computeenvironment-capacityreservations-reservationgrouparn"></a>
The Amazon Resource Name (ARN) of the capacity reservation group to target.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReservationPreference`  <a name="cfn-batch-computeenvironment-capacityreservations-reservationpreference"></a>
The capacity reservation preference. Valid values:
+ `RESERVATIONS_ONLY` — Use only capacity reservations.
+ `RESERVATIONS_FIRST` — Prefer capacity reservations but fall back to On-Demand if unavailable.
+ `RESERVATIONS_EXCLUDED` — Do not use capacity reservations.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
