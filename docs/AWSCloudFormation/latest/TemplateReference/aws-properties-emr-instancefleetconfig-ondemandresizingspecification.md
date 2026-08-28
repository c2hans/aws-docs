---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emr-instancefleetconfig-ondemandresizingspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMR::InstanceFleetConfig OnDemandResizingSpecification
<a name="aws-properties-emr-instancefleetconfig-ondemandresizingspecification"></a>

The resize specification for On-Demand Instances in the instance fleet, which contains the resize timeout period.

## Syntax
<a name="aws-properties-emr-instancefleetconfig-ondemandresizingspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emr-instancefleetconfig-ondemandresizingspecification-syntax.json"></a>

```
{
  "[AllocationStrategy](#cfn-emr-instancefleetconfig-ondemandresizingspecification-allocationstrategy)" : {{String}},
  "[CapacityReservationOptions](#cfn-emr-instancefleetconfig-ondemandresizingspecification-capacityreservationoptions)" : {{OnDemandCapacityReservationOptions}},
  "[TimeoutDurationMinutes](#cfn-emr-instancefleetconfig-ondemandresizingspecification-timeoutdurationminutes)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-emr-instancefleetconfig-ondemandresizingspecification-syntax.yaml"></a>

```
  [AllocationStrategy](#cfn-emr-instancefleetconfig-ondemandresizingspecification-allocationstrategy): {{String}}
  [CapacityReservationOptions](#cfn-emr-instancefleetconfig-ondemandresizingspecification-capacityreservationoptions): {{
    OnDemandCapacityReservationOptions}}
  [TimeoutDurationMinutes](#cfn-emr-instancefleetconfig-ondemandresizingspecification-timeoutdurationminutes): {{Integer}}
```

## Properties
<a name="aws-properties-emr-instancefleetconfig-ondemandresizingspecification-properties"></a>

`AllocationStrategy`  <a name="cfn-emr-instancefleetconfig-ondemandresizingspecification-allocationstrategy"></a>
Specifies the allocation strategy to use to launch On-Demand instances during a resize. The default is `lowest-price`.
*Required*: No
*Type*: String
*Allowed values*: `lowest-price | prioritized`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CapacityReservationOptions`  <a name="cfn-emr-instancefleetconfig-ondemandresizingspecification-capacityreservationoptions"></a>
Property description not available.
*Required*: No
*Type*: [OnDemandCapacityReservationOptions](aws-properties-emr-instancefleetconfig-ondemandcapacityreservationoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeoutDurationMinutes`  <a name="cfn-emr-instancefleetconfig-ondemandresizingspecification-timeoutdurationminutes"></a>
On-Demand resize timeout in minutes. If On-Demand Instances are not provisioned within this time, the resize workflow stops. The minimum value is 5 minutes, and the maximum value is 10,080 minutes (7 days). The timeout applies to all resize workflows on the Instance Fleet. The resize could be triggered by Amazon EMR Managed Scaling or by the customer (via Amazon EMR Console, Amazon EMR CLI modify-instance-fleet or Amazon EMR SDK ModifyInstanceFleet API) or by Amazon EMR due to Amazon EC2 Spot Reclamation.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
