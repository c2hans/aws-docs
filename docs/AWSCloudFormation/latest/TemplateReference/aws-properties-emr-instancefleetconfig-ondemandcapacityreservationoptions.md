---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emr-instancefleetconfig-ondemandcapacityreservationoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMR::InstanceFleetConfig OnDemandCapacityReservationOptions
<a name="aws-properties-emr-instancefleetconfig-ondemandcapacityreservationoptions"></a>

Describes the strategy for using unused Capacity Reservations for fulfilling On-Demand capacity.

## Syntax
<a name="aws-properties-emr-instancefleetconfig-ondemandcapacityreservationoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emr-instancefleetconfig-ondemandcapacityreservationoptions-syntax.json"></a>

```
{
  "[CapacityReservationPreference](#cfn-emr-instancefleetconfig-ondemandcapacityreservationoptions-capacityreservationpreference)" : {{String}},
  "[CapacityReservationResourceGroupArn](#cfn-emr-instancefleetconfig-ondemandcapacityreservationoptions-capacityreservationresourcegrouparn)" : {{String}},
  "[UsageStrategy](#cfn-emr-instancefleetconfig-ondemandcapacityreservationoptions-usagestrategy)" : {{String}}
}
```

### YAML
<a name="aws-properties-emr-instancefleetconfig-ondemandcapacityreservationoptions-syntax.yaml"></a>

```
  [CapacityReservationPreference](#cfn-emr-instancefleetconfig-ondemandcapacityreservationoptions-capacityreservationpreference): {{String}}
  [CapacityReservationResourceGroupArn](#cfn-emr-instancefleetconfig-ondemandcapacityreservationoptions-capacityreservationresourcegrouparn): {{String}}
  [UsageStrategy](#cfn-emr-instancefleetconfig-ondemandcapacityreservationoptions-usagestrategy): {{String}}
```

## Properties
<a name="aws-properties-emr-instancefleetconfig-ondemandcapacityreservationoptions-properties"></a>

`CapacityReservationPreference`  <a name="cfn-emr-instancefleetconfig-ondemandcapacityreservationoptions-capacityreservationpreference"></a>
Indicates the instance's Capacity Reservation preferences. Possible preferences include:
+ `open` - The instance can run in any open Capacity Reservation that has matching attributes (instance type, platform, Availability Zone).
+ `none` - The instance avoids running in a Capacity Reservation even if one is available. The instance runs as an On-Demand Instance.
*Required*: No
*Type*: String
*Allowed values*: `open | none`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CapacityReservationResourceGroupArn`  <a name="cfn-emr-instancefleetconfig-ondemandcapacityreservationoptions-capacityreservationresourcegrouparn"></a>
The ARN of the Capacity Reservation resource group in which to run the instance.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UsageStrategy`  <a name="cfn-emr-instancefleetconfig-ondemandcapacityreservationoptions-usagestrategy"></a>
Indicates whether to use unused Capacity Reservations for fulfilling On-Demand capacity.
If you specify `use-capacity-reservations-first`, the fleet uses unused Capacity Reservations to fulfill On-Demand capacity up to the target On-Demand capacity. If multiple instance pools have unused Capacity Reservations, the On-Demand allocation strategy (`lowest-price`) is applied. If the number of unused Capacity Reservations is less than the On-Demand target capacity, the remaining On-Demand target capacity is launched according to the On-Demand allocation strategy (`lowest-price`).
If you do not specify a value, the fleet fulfills the On-Demand capacity according to the chosen On-Demand allocation strategy.
*Required*: No
*Type*: String
*Allowed values*: `use-capacity-reservations-first`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
