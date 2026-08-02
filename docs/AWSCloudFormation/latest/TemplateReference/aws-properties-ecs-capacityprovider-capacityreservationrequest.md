---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ecs-capacityprovider-capacityreservationrequest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ECS::CapacityProvider CapacityReservationRequest
<a name="aws-properties-ecs-capacityprovider-capacityreservationrequest"></a>

The Capacity Reservation configurations to be used when using the `RESERVED` capacity option type.

## Syntax
<a name="aws-properties-ecs-capacityprovider-capacityreservationrequest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ecs-capacityprovider-capacityreservationrequest-syntax.json"></a>

```
{
  "[ReservationGroupArn](#cfn-ecs-capacityprovider-capacityreservationrequest-reservationgrouparn)" : {{String}},
  "[ReservationPreference](#cfn-ecs-capacityprovider-capacityreservationrequest-reservationpreference)" : {{String}}
}
```

### YAML
<a name="aws-properties-ecs-capacityprovider-capacityreservationrequest-syntax.yaml"></a>

```
  [ReservationGroupArn](#cfn-ecs-capacityprovider-capacityreservationrequest-reservationgrouparn): {{String}}
  [ReservationPreference](#cfn-ecs-capacityprovider-capacityreservationrequest-reservationpreference): {{String}}
```

## Properties
<a name="aws-properties-ecs-capacityprovider-capacityreservationrequest-properties"></a>

`ReservationGroupArn`  <a name="cfn-ecs-capacityprovider-capacityreservationrequest-reservationgrouparn"></a>
The ARN of the Capacity Reservation resource group in which to run the instance.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReservationPreference`  <a name="cfn-ecs-capacityprovider-capacityreservationrequest-reservationpreference"></a>
The preference on when capacity reservations should be used.
Valid values are:
+ `RESERVATIONS_ONLY` - Exclusively launch instances into capacity reservations that match the instance requirements configured for the capacity provider. If none exist, instances will fail to provision.
+ `RESERVATIONS_FIRST` - Prefer to launch instances into a capacity reservation if any exist that match the instance requirements configured for the capacity provider. If none exist, fall back to launching instances On-Demand.
+ `RESERVATIONS_EXCLUDED` - Avoid using capacity reservations and launch exclusively On-Demand.
*Required*: No
*Type*: String
*Allowed values*: `RESERVATIONS_ONLY | RESERVATIONS_FIRST | RESERVATIONS_EXCLUDED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
