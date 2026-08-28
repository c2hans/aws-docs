---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ec2-ec2fleet-ondemandoptionsrequest.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::EC2Fleet OnDemandOptionsRequest
<a name="aws-properties-ec2-ec2fleet-ondemandoptionsrequest"></a>

Specifies the allocation strategy of On-Demand Instances in an EC2 Fleet.

`OnDemandOptionsRequest` is a property of the [AWS::EC2::EC2Fleet](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-ec2fleet.html) resource.

## Syntax
<a name="aws-properties-ec2-ec2fleet-ondemandoptionsrequest-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ec2-ec2fleet-ondemandoptionsrequest-syntax.json"></a>

```
{
  "[AllocationStrategy](#cfn-ec2-ec2fleet-ondemandoptionsrequest-allocationstrategy)" : {{String}},
  "[CapacityReservationOptions](#cfn-ec2-ec2fleet-ondemandoptionsrequest-capacityreservationoptions)" : {{CapacityReservationOptionsRequest}},
  "[MaxTotalPrice](#cfn-ec2-ec2fleet-ondemandoptionsrequest-maxtotalprice)" : {{String}},
  "[MinTargetCapacity](#cfn-ec2-ec2fleet-ondemandoptionsrequest-mintargetcapacity)" : {{Integer}},
  "[SingleAvailabilityZone](#cfn-ec2-ec2fleet-ondemandoptionsrequest-singleavailabilityzone)" : {{Boolean}},
  "[SingleInstanceType](#cfn-ec2-ec2fleet-ondemandoptionsrequest-singleinstancetype)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-ec2-ec2fleet-ondemandoptionsrequest-syntax.yaml"></a>

```
  [AllocationStrategy](#cfn-ec2-ec2fleet-ondemandoptionsrequest-allocationstrategy): {{String}}
  [CapacityReservationOptions](#cfn-ec2-ec2fleet-ondemandoptionsrequest-capacityreservationoptions): {{
    CapacityReservationOptionsRequest}}
  [MaxTotalPrice](#cfn-ec2-ec2fleet-ondemandoptionsrequest-maxtotalprice): {{String}}
  [MinTargetCapacity](#cfn-ec2-ec2fleet-ondemandoptionsrequest-mintargetcapacity): {{Integer}}
  [SingleAvailabilityZone](#cfn-ec2-ec2fleet-ondemandoptionsrequest-singleavailabilityzone): {{Boolean}}
  [SingleInstanceType](#cfn-ec2-ec2fleet-ondemandoptionsrequest-singleinstancetype): {{Boolean}}
```

## Properties
<a name="aws-properties-ec2-ec2fleet-ondemandoptionsrequest-properties"></a>

`AllocationStrategy`  <a name="cfn-ec2-ec2fleet-ondemandoptionsrequest-allocationstrategy"></a>
The strategy that determines the order of the launch template overrides to use in fulfilling On-Demand capacity.
`lowest-price` - EC2 Fleet uses price to determine the order, launching the lowest price first.
`prioritized` - EC2 Fleet uses the priority that you assigned to each launch template override, launching the highest priority first.
Default: `lowest-price`
*Required*: No
*Type*: String
*Allowed values*: `lowest-price | prioritized`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CapacityReservationOptions`  <a name="cfn-ec2-ec2fleet-ondemandoptionsrequest-capacityreservationoptions"></a>
The strategy for using unused Capacity Reservations for fulfilling On-Demand capacity.
Supported only for fleets of type `instant`.
*Required*: No
*Type*: [CapacityReservationOptionsRequest](aws-properties-ec2-ec2fleet-capacityreservationoptionsrequest.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MaxTotalPrice`  <a name="cfn-ec2-ec2fleet-ondemandoptionsrequest-maxtotalprice"></a>
The maximum amount per hour for On-Demand Instances that you're willing to pay.
If your fleet includes T instances that are configured as `unlimited`, and if their average CPU usage exceeds the baseline utilization, you will incur a charge for surplus credits. The `MaxTotalPrice` does not account for surplus credits, and, if you use surplus credits, your final cost might be higher than what you specified for `MaxTotalPrice`. For more information, see [Surplus credits can incur charges](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances-unlimited-mode-concepts.html#unlimited-mode-surplus-credits) in the *Amazon EC2 User Guide*.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MinTargetCapacity`  <a name="cfn-ec2-ec2fleet-ondemandoptionsrequest-mintargetcapacity"></a>
The minimum target capacity for On-Demand Instances in the fleet. If this minimum capacity isn't reached, no instances are launched.
Constraints: Maximum value of `1000`. Supported only for fleets of type `instant`.
At least one of the following must be specified: `SingleAvailabilityZone` \| `SingleInstanceType`
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SingleAvailabilityZone`  <a name="cfn-ec2-ec2fleet-ondemandoptionsrequest-singleavailabilityzone"></a>
Indicates that the fleet launches all On-Demand Instances into a single Availability Zone.
Supported only for fleets of type `instant`.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SingleInstanceType`  <a name="cfn-ec2-ec2fleet-ondemandoptionsrequest-singleinstancetype"></a>
Indicates that the fleet uses a single instance type to launch all On-Demand Instances in the fleet.
Supported only for fleets of type `instant`.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also
<a name="aws-properties-ec2-ec2fleet-ondemandoptionsrequest--seealso"></a>
+ [ OnDemandOptionsRequest](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_OnDemandOptionsRequest.html) in the *Amazon EC2 API Reference*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
