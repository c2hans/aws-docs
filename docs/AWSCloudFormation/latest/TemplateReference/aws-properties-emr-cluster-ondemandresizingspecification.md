---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emr-cluster-ondemandresizingspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMR::Cluster OnDemandResizingSpecification
<a name="aws-properties-emr-cluster-ondemandresizingspecification"></a>

The resize specification for On-Demand Instances in the instance fleet, which contains the resize timeout period.

## Syntax
<a name="aws-properties-emr-cluster-ondemandresizingspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emr-cluster-ondemandresizingspecification-syntax.json"></a>

```
{
  "[AllocationStrategy](#cfn-emr-cluster-ondemandresizingspecification-allocationstrategy)" : {{String}},
  "[CapacityReservationOptions](#cfn-emr-cluster-ondemandresizingspecification-capacityreservationoptions)" : {{OnDemandCapacityReservationOptions}},
  "[TimeoutDurationMinutes](#cfn-emr-cluster-ondemandresizingspecification-timeoutdurationminutes)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-emr-cluster-ondemandresizingspecification-syntax.yaml"></a>

```
  [AllocationStrategy](#cfn-emr-cluster-ondemandresizingspecification-allocationstrategy): {{String}}
  [CapacityReservationOptions](#cfn-emr-cluster-ondemandresizingspecification-capacityreservationoptions): {{
    OnDemandCapacityReservationOptions}}
  [TimeoutDurationMinutes](#cfn-emr-cluster-ondemandresizingspecification-timeoutdurationminutes): {{Integer}}
```

## Properties
<a name="aws-properties-emr-cluster-ondemandresizingspecification-properties"></a>

`AllocationStrategy`  <a name="cfn-emr-cluster-ondemandresizingspecification-allocationstrategy"></a>
Specifies the allocation strategy to use to launch On-Demand instances during a resize. The default is `lowest-price`.
*Required*: No
*Type*: String
*Allowed values*: `lowest-price | prioritized`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CapacityReservationOptions`  <a name="cfn-emr-cluster-ondemandresizingspecification-capacityreservationoptions"></a>
Property description not available.
*Required*: No
*Type*: [OnDemandCapacityReservationOptions](aws-properties-emr-cluster-ondemandcapacityreservationoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TimeoutDurationMinutes`  <a name="cfn-emr-cluster-ondemandresizingspecification-timeoutdurationminutes"></a>
On-Demand resize timeout in minutes. If On-Demand Instances are not provisioned within this time, the resize workflow stops. The minimum value is 5 minutes, and the maximum value is 10,080 minutes (7 days). The timeout applies to all resize workflows on the Instance Fleet. The resize could be triggered by Amazon EMR Managed Scaling or by the customer (via Amazon EMR Console, Amazon EMR CLI modify-instance-fleet or Amazon EMR SDK ModifyInstanceFleet API) or by Amazon EMR due to Amazon EC2 Spot Reclamation.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
