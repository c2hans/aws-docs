---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-capacityreservation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::CapacityReservation
<a name="aws-resource-ec2-capacityreservation"></a>

Creates a new Capacity Reservation with the specified attributes. For more information, see [Capacity Reservations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-reservations.html) in the *Amazon EC2 User Guide*.

## Syntax
<a name="aws-resource-ec2-capacityreservation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-capacityreservation-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::CapacityReservation",
  "Properties" : {
      "[AvailabilityZone](#cfn-ec2-capacityreservation-availabilityzone)" : {{String}},
      "[AvailabilityZoneId](#cfn-ec2-capacityreservation-availabilityzoneid)" : {{String}},
      "[EbsOptimized](#cfn-ec2-capacityreservation-ebsoptimized)" : {{Boolean}},
      "[EndDate](#cfn-ec2-capacityreservation-enddate)" : {{String}},
      "[EndDateType](#cfn-ec2-capacityreservation-enddatetype)" : {{String}},
      "[EphemeralStorage](#cfn-ec2-capacityreservation-ephemeralstorage)" : {{Boolean}},
      "[InstanceCount](#cfn-ec2-capacityreservation-instancecount)" : {{Integer}},
      "[InstanceMatchCriteria](#cfn-ec2-capacityreservation-instancematchcriteria)" : {{String}},
      "[InstancePlatform](#cfn-ec2-capacityreservation-instanceplatform)" : {{String}},
      "[InstanceType](#cfn-ec2-capacityreservation-instancetype)" : {{String}},
      "[OutPostArn](#cfn-ec2-capacityreservation-outpostarn)" : {{String}},
      "[PlacementGroupArn](#cfn-ec2-capacityreservation-placementgrouparn)" : {{String}},
      "[TagSpecifications](#cfn-ec2-capacityreservation-tagspecifications)" : {{[ TagSpecification, ... ]}},
      "[Tenancy](#cfn-ec2-capacityreservation-tenancy)" : {{String}},
      "[UnusedReservationBillingOwnerId](#cfn-ec2-capacityreservation-unusedreservationbillingownerid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ec2-capacityreservation-syntax.yaml"></a>

```
Type: AWS::EC2::CapacityReservation
Properties:
  [AvailabilityZone](#cfn-ec2-capacityreservation-availabilityzone): {{String}}
  [AvailabilityZoneId](#cfn-ec2-capacityreservation-availabilityzoneid): {{String}}
  [EbsOptimized](#cfn-ec2-capacityreservation-ebsoptimized): {{Boolean}}
  [EndDate](#cfn-ec2-capacityreservation-enddate): {{String}}
  [EndDateType](#cfn-ec2-capacityreservation-enddatetype): {{String}}
  [EphemeralStorage](#cfn-ec2-capacityreservation-ephemeralstorage): {{Boolean}}
  [InstanceCount](#cfn-ec2-capacityreservation-instancecount): {{Integer}}
  [InstanceMatchCriteria](#cfn-ec2-capacityreservation-instancematchcriteria): {{String}}
  [InstancePlatform](#cfn-ec2-capacityreservation-instanceplatform): {{String}}
  [InstanceType](#cfn-ec2-capacityreservation-instancetype): {{String}}
  [OutPostArn](#cfn-ec2-capacityreservation-outpostarn): {{String}}
  [PlacementGroupArn](#cfn-ec2-capacityreservation-placementgrouparn): {{String}}
  [TagSpecifications](#cfn-ec2-capacityreservation-tagspecifications): {{
    - TagSpecification}}
  [Tenancy](#cfn-ec2-capacityreservation-tenancy): {{String}}
  [UnusedReservationBillingOwnerId](#cfn-ec2-capacityreservation-unusedreservationbillingownerid): {{String}}
```

## Properties
<a name="aws-resource-ec2-capacityreservation-properties"></a>

`AvailabilityZone`  <a name="cfn-ec2-capacityreservation-availabilityzone"></a>
The Availability Zone in which to create the Capacity Reservation.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AvailabilityZoneId`  <a name="cfn-ec2-capacityreservation-availabilityzoneid"></a>
The ID of the Availability Zone in which the capacity is reserved.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EbsOptimized`  <a name="cfn-ec2-capacityreservation-ebsoptimized"></a>
Indicates whether the Capacity Reservation supports EBS-optimized instances. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal I/O performance. This optimization isn't available with all instance types. Additional usage charges apply when using an EBS- optimized instance.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EndDate`  <a name="cfn-ec2-capacityreservation-enddate"></a>
The date and time at which the Capacity Reservation expires. When a Capacity Reservation expires, the reserved capacity is released and you can no longer launch instances into it. The Capacity Reservation's state changes to `expired` when it reaches its end date and time.
You must provide an `EndDate` value if `EndDateType` is `limited`. Omit `EndDate` if `EndDateType` is `unlimited`.
If the `EndDateType` is `limited`, the Capacity Reservation is cancelled within an hour from the specified time. For example, if you specify 5/31/2019, 13:30:55, the Capacity Reservation is guaranteed to end between 13:30:55 and 14:30:55 on 5/31/2019.
If you are requesting a future-dated Capacity Reservation, you can't specify an end date and time that is within the commitment duration.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EndDateType`  <a name="cfn-ec2-capacityreservation-enddatetype"></a>
Indicates the way in which the Capacity Reservation ends. A Capacity Reservation can have one of the following end types:
+ `unlimited` - The Capacity Reservation remains active until you explicitly cancel it. Do not provide an `EndDate` if the `EndDateType` is `unlimited`.
+ `limited` - The Capacity Reservation expires automatically at a specified date and time. You must provide an `EndDate` value if the `EndDateType` value is `limited`.
*Required*: No
*Type*: String
*Allowed values*: `unlimited | limited`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EphemeralStorage`  <a name="cfn-ec2-capacityreservation-ephemeralstorage"></a>
 *Deprecated.*
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InstanceCount`  <a name="cfn-ec2-capacityreservation-instancecount"></a>
The number of instances for which to reserve capacity.
You can request future-dated Capacity Reservations for an instance count with a minimum of 32 vCPUs. For example, if you request a future-dated Capacity Reservation for `m5.xlarge` instances, you must request at least 8 instances (*8 \* m5.xlarge = 32 vCPUs*).
Valid range: 1 - 1000
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceMatchCriteria`  <a name="cfn-ec2-capacityreservation-instancematchcriteria"></a>
Indicates the type of instance launches that the Capacity Reservation accepts. The options include:
+ `open` - The Capacity Reservation automatically matches all instances that have matching attributes (instance type, platform, and Availability Zone). Instances that have matching attributes run in the Capacity Reservation automatically without specifying any additional parameters.
+ `targeted` - The Capacity Reservation only accepts instances that have matching attributes (instance type, platform, and Availability Zone), and explicitly target the Capacity Reservation. This ensures that only permitted instances can use the reserved capacity.
If you are requesting a future-dated Capacity Reservation, you must specify `targeted`.
Default: `open`
*Required*: No
*Type*: String
*Allowed values*: `open | targeted`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstancePlatform`  <a name="cfn-ec2-capacityreservation-instanceplatform"></a>
The type of operating system for which to reserve capacity.
*Required*: Yes
*Type*: String
*Allowed values*: `Linux/UNIX | Red Hat Enterprise Linux | SUSE Linux | Windows | Windows with SQL Server | Windows with SQL Server Enterprise | Windows with SQL Server Standard | Windows with SQL Server Web | Linux with SQL Server Standard | Linux with SQL Server Web | Linux with SQL Server Enterprise | RHEL with SQL Server Standard | RHEL with SQL Server Enterprise | RHEL with SQL Server Web | RHEL with HA | RHEL with HA and SQL Server Standard | RHEL with HA and SQL Server Enterprise | Ubuntu Pro`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InstanceType`  <a name="cfn-ec2-capacityreservation-instancetype"></a>
The instance type for which to reserve capacity.
You can request future-dated Capacity Reservations for instance types in the C, M, R, I, T, and G instance families only.
For more information, see [Instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html) in the *Amazon EC2 User Guide*.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OutPostArn`  <a name="cfn-ec2-capacityreservation-outpostarn"></a>
Not supported for future-dated Capacity Reservations.
The Amazon Resource Name (ARN) of the Outpost on which to create the Capacity Reservation.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:outpost/op-[a-f0-9]{17}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PlacementGroupArn`  <a name="cfn-ec2-capacityreservation-placementgrouparn"></a>
Not supported for future-dated Capacity Reservations.
The Amazon Resource Name (ARN) of the cluster placement group in which to create the Capacity Reservation. For more information, see [ Capacity Reservations for cluster placement groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cr-cpg.html) in the *Amazon EC2 User Guide*.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws([a-z-]+)?:ec2:[a-z\d-]+:\d{12}:placement-group/^.{1,255}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TagSpecifications`  <a name="cfn-ec2-capacityreservation-tagspecifications"></a>
The tags to apply to the Capacity Reservation during launch.
*Required*: No
*Type*: Array of [TagSpecification](aws-properties-ec2-capacityreservation-tagspecification.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tenancy`  <a name="cfn-ec2-capacityreservation-tenancy"></a>
Indicates the tenancy of the Capacity Reservation. A Capacity Reservation can have one of the following tenancy settings:
+ `default` - The Capacity Reservation is created on hardware that is shared with other AWS accounts.
+ `dedicated` - The Capacity Reservation is created on single-tenant hardware that is dedicated to a single AWS account.
*Required*: No
*Type*: String
*Allowed values*: `default | dedicated`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`UnusedReservationBillingOwnerId`  <a name="cfn-ec2-capacityreservation-unusedreservationbillingownerid"></a>
The ID of the AWS account to which to assign billing of the unused capacity of the Capacity Reservation. A request will be sent to the specified account. That account must accept the request for the billing to be assigned to their account. For more information, see [ Billing assignment for shared Amazon EC2 Capacity Reservations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/assign-billing.html).
You can assign billing only for shared Capacity Reservations. To share a Capacity Reservation, you must add it to a resource share. For more information, see [AWS::RAM::ResourceShare](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ram-resourceshare.html).
*Required*: No
*Type*: String
*Pattern*: `[0-9]{12}`
*Minimum*: `12`
*Maximum*: `12`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ec2-capacityreservation-return-values"></a>

### Ref
<a name="aws-resource-ec2-capacityreservation-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the resource ID, such as `cr-1234ab5cd6789e0f1`.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-ec2-capacityreservation-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-ec2-capacityreservation-return-values-fn--getatt-fn--getatt"></a>

`AvailabilityZone`  <a name="AvailabilityZone-fn::getatt"></a>
Returns the Availability Zone in which the capacity is reserved. For example: `us-east-1a`.

`AvailableInstanceCount`  <a name="AvailableInstanceCount-fn::getatt"></a>
Returns the remaining capacity, which indicates the number of instances that can be launched in the Capacity Reservation. For example: `9`.

`CapacityAllocationSet`  <a name="CapacityAllocationSet-fn::getatt"></a>
Property description not available.

`CapacityReservationArn`  <a name="CapacityReservationArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the Capacity Reservation.

`CapacityReservationFleetId`  <a name="CapacityReservationFleetId-fn::getatt"></a>
The ID of the Capacity Reservation Fleet to which the Capacity Reservation belongs. Only valid for Capacity Reservations that were created by a Capacity Reservation Fleet.

`CreateDate`  <a name="CreateDate-fn::getatt"></a>
The date and time the Capacity Reservation was created.

`DeliveryPreference`  <a name="DeliveryPreference-fn::getatt"></a>
The delivery method for a future-dated Capacity Reservation. `incremental` indicates that the requested capacity is delivered in addition to any running instances and reserved capacity that you have in your account at the requested date and time.

`Id`  <a name="Id-fn::getatt"></a>
The ID of the Capacity Reservation.

`InstanceType`  <a name="InstanceType-fn::getatt"></a>
Returns the type of instance for which the capacity is reserved. For example: `m4.large`.

`OwnerId`  <a name="OwnerId-fn::getatt"></a>
The ID of the AWS account that owns the Capacity Reservation.

`ReservationType`  <a name="ReservationType-fn::getatt"></a>
The type of Capacity Reservation.

`StartDate`  <a name="StartDate-fn::getatt"></a>
The date and time the Capacity Reservation was started.

`State`  <a name="State-fn::getatt"></a>
The current state of the Capacity Reservation. A Capacity Reservation can be in one of the following states:
+ `active` - The capacity is available for use.
+ `expired` - The Capacity Reservation expired automatically at the date and time specified in your reservation request. The reserved capacity is no longer available for your use.
+ `cancelled` - The Capacity Reservation was canceled. The reserved capacity is no longer available for your use.
+ `pending` - The Capacity Reservation request was successful but the capacity provisioning is still pending.
+ `failed` - The Capacity Reservation request has failed. A request can fail due to request parameters that are not valid, capacity constraints, or instance limit constraints. You can view a failed request for 60 minutes.
+ `scheduled` - (*Future-dated Capacity Reservations*) The future-dated Capacity Reservation request was approved and the Capacity Reservation is scheduled for delivery on the requested start date.
+ `payment-pending` - (*Capacity Blocks*) The upfront payment has not been processed yet.
+ `payment-failed` - (*Capacity Blocks*) The upfront payment was not processed in the 12-hour time frame. Your Capacity Block was released.
+ `assessing` - (*Future-dated Capacity Reservations*) Amazon EC2 is assessing your request for a future-dated Capacity Reservation.
+ `delayed` - (*Future-dated Capacity Reservations*) Amazon EC2 encountered a delay in provisioning the requested future-dated Capacity Reservation. Amazon EC2 is unable to deliver the requested capacity by the requested start date and time.
+ `unsupported` - (*Future-dated Capacity Reservations*) Amazon EC2 can't support the future-dated Capacity Reservation request due to capacity constraints. You can view unsupported requests for 30 days. The Capacity Reservation will not be delivered.
+ `cancelling` - (*Future-dated Capacity Reservations*) The Capacity Reservation is being cancelled. Capacity has been released but charges continue for the commitment wind-down period. The reservation transitions to `cancelled` when the wind-down completes.

`Tenancy`  <a name="Tenancy-fn::getatt"></a>
Returns the tenancy of the Capacity Reservation. For example: `dedicated`.

`TotalInstanceCount`  <a name="TotalInstanceCount-fn::getatt"></a>
Returns the total number of instances for which the Capacity Reservation reserves capacity. For example: `15`.

## See also
<a name="aws-resource-ec2-capacityreservation--seealso"></a>
+ [ On-Demand Capacity Reservations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-reservations.html) in the *Amazon EC2 User Guide*
