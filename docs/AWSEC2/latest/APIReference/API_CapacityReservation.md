---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CapacityReservation.html
---

# CapacityReservation
<a name="API_CapacityReservation"></a>

Describes a Capacity Reservation.

## Contents
<a name="API_CapacityReservation_Contents"></a>

 ** availabilityZone **
The Availability Zone in which the capacity is reserved.
Type: String
Required: No

 ** availabilityZoneId **
The ID of the Availability Zone in which the capacity is reserved.
Type: String
Required: No

 ** availableInstanceCount **
The remaining capacity. Indicates the number of instances that can be launched in the Capacity Reservation.
Type: Integer
Required: No

 ** CapacityAllocationSet.N **
Information about instance capacity usage.
Type: Array of [CapacityAllocation](API_CapacityAllocation.md) objects
Required: No

 ** capacityBlockId **
The ID of the Capacity Block.
Type: String
Required: No

 ** capacityReservationArn **
The Amazon Resource Name (ARN) of the Capacity Reservation.
Type: String
Required: No

 ** capacityReservationFleetId **
The ID of the Capacity Reservation Fleet to which the Capacity Reservation belongs. Only valid for Capacity Reservations that were created by a Capacity Reservation Fleet.
Type: String
Required: No

 ** capacityReservationId **
The ID of the Capacity Reservation.
Type: String
Required: No

 ** commitmentInfo **
Information about your commitment for a future-dated Capacity Reservation.
Type: [CapacityReservationCommitmentInfo](API_CapacityReservationCommitmentInfo.md) object
Required: No

 ** createDate **
The date and time the Capacity Reservation was created.
Type: Timestamp
Required: No

 ** deliveryPreference **
The delivery method for a future-dated Capacity Reservation. `incremental` indicates that the requested capacity is delivered in addition to any running instances and reserved capacity that you have in your account at the requested date and time.
Type: String
Valid Values: `fixed | incremental`
Required: No

 ** ebsOptimized **
Indicates whether the Capacity Reservation supports EBS-optimized instances. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal I/O performance. This optimization isn't available with all instance types. Additional usage charges apply when using an EBS- optimized instance.
Type: Boolean
Required: No

 ** endDate **
The date and time the Capacity Reservation expires. When a Capacity Reservation expires, the reserved capacity is released and you can no longer launch instances into it. The Capacity Reservation's state changes to `expired` when it reaches its end date and time.
Type: Timestamp
Required: No

 ** endDateType **
Indicates the way in which the Capacity Reservation ends. A Capacity Reservation can have one of the following end types:
+  `unlimited` - The Capacity Reservation remains active until you explicitly cancel it.
+  `limited` - The Capacity Reservation expires automatically at a specified date and time.
Type: String
Valid Values: `unlimited | limited`
Required: No

 ** ephemeralStorage **
 *Deprecated.*
Type: Boolean
Required: No

 ** instanceMatchCriteria **
Indicates the type of instance launches that the Capacity Reservation accepts. The options include:
+  `open` - The Capacity Reservation accepts all instances that have matching attributes (instance type, platform, and Availability Zone). Instances that have matching attributes launch into the Capacity Reservation automatically without specifying any additional parameters.
+  `targeted` - The Capacity Reservation only accepts instances that have matching attributes (instance type, platform, and Availability Zone), and explicitly target the Capacity Reservation. This ensures that only permitted instances can use the reserved capacity.
Type: String
Valid Values: `open | targeted`
Required: No

 ** instancePlatform **
The type of operating system for which the Capacity Reservation reserves capacity.
Type: String
Valid Values: `Linux/UNIX | Red Hat Enterprise Linux | SUSE Linux | Windows | Windows with SQL Server | Windows with SQL Server Enterprise | Windows with SQL Server Standard | Windows with SQL Server Web | Linux with SQL Server Standard | Linux with SQL Server Web | Linux with SQL Server Enterprise | RHEL with SQL Server Standard | RHEL with SQL Server Enterprise | RHEL with SQL Server Web | RHEL with HA | RHEL with HA and SQL Server Standard | RHEL with HA and SQL Server Enterprise | Ubuntu Pro`
Required: No

 ** instanceType **
The type of instance for which the Capacity Reservation reserves capacity.
Type: String
Required: No

 ** interruptible **
 Indicates whether this Capacity Reservation is interruptible, meaning instances may be terminated when the owner reclaims capacity.
Type: Boolean
Required: No

 ** interruptibleCapacityAllocation **
 Contains allocation details for interruptible reservations, including current allocated instances and target instance counts within the interruptibleCapacityAllocation object.
Type: [InterruptibleCapacityAllocation](API_InterruptibleCapacityAllocation.md) object
Required: No

 ** interruptionInfo **
 Information about the interruption configuration and association with the source reservation for interruptible Capacity Reservations.
Type: [InterruptionInfo](API_InterruptionInfo.md) object
Required: No

 ** outpostArn **
The Amazon Resource Name (ARN) of the Outpost on which the Capacity Reservation was created.
Type: String
Pattern: `^arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:outpost/op-[a-f0-9]{17}$`
Required: No

 ** ownerId **
The ID of the AWS account that owns the Capacity Reservation.
Type: String
Required: No

 ** placementGroupArn **
The Amazon Resource Name (ARN) of the cluster placement group in which the Capacity Reservation was created. For more information, see [ Capacity Reservations for cluster placement groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cr-cpg.html) in the *Amazon EC2 User Guide*.
Type: String
Pattern: `^arn:aws([a-z-]+)?:ec2:[a-z\d-]+:\d{12}:placement-group/^.{1,255}$`
Required: No

 ** reservationType **
The type of Capacity Reservation.
Type: String
Valid Values: `default | capacity-block`
Required: No

 ** startDate **
The date and time the Capacity Reservation was started.
Type: Timestamp
Required: No

 ** state **
The current state of the Capacity Reservation. A Capacity Reservation can be in one of the following states:
+  `active` - The capacity is available for use.
+  `expired` - The Capacity Reservation expired automatically at the date and time specified in your reservation request. The reserved capacity is no longer available for your use.
+  `cancelled` - The Capacity Reservation was canceled. The reserved capacity is no longer available for your use.
+  `pending` - The Capacity Reservation request was successful but the capacity provisioning is still pending.
+  `failed` - The Capacity Reservation request has failed. A request can fail due to request parameters that are not valid, capacity constraints, or instance limit constraints. You can view a failed request for 60 minutes.
+  `scheduled` - (*Future-dated Capacity Reservations*) The future-dated Capacity Reservation request was approved and the Capacity Reservation is scheduled for delivery on the requested start date.
+  `payment-pending` - (*Capacity Blocks*) The upfront payment has not been processed yet.
+  `payment-failed` - (*Capacity Blocks*) The upfront payment was not processed in the 12-hour time frame. Your Capacity Block was released.
+  `assessing` - (*Future-dated Capacity Reservations*) Amazon EC2 is assessing your request for a future-dated Capacity Reservation.
+  `delayed` - (*Future-dated Capacity Reservations*) Amazon EC2 encountered a delay in provisioning the requested future-dated Capacity Reservation. Amazon EC2 is unable to deliver the requested capacity by the requested start date and time.
+  `unsupported` - (*Future-dated Capacity Reservations*) Amazon EC2 can't support the future-dated Capacity Reservation request due to capacity constraints. You can view unsupported requests for 30 days. The Capacity Reservation will not be delivered.
+  `cancelling` - (*Future-dated Capacity Reservations*) The Capacity Reservation is being cancelled. Capacity has been released but charges continue for the commitment wind-down period. The reservation transitions to `cancelled` when the wind-down completes.
Type: String
Valid Values: `active | expired | cancelled | pending | failed | scheduled | payment-pending | payment-failed | assessing | delayed | unsupported | cancelling | unavailable`
Required: No

 ** TagSet.N **
Any tags assigned to the Capacity Reservation.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** tenancy **
Indicates the tenancy of the Capacity Reservation. A Capacity Reservation can have one of the following tenancy settings:
+  `default` - The Capacity Reservation is created on hardware that is shared with other AWS accounts.
+  `dedicated` - The Capacity Reservation is created on single-tenant hardware that is dedicated to a single AWS account.
Type: String
Valid Values: `default | dedicated`
Required: No

 ** totalInstanceCount **
The total number of instances for which the Capacity Reservation reserves capacity.
Type: Integer
Required: No

 ** unusedReservationBillingOwnerId **
The ID of the AWS account to which billing of the unused capacity of the Capacity Reservation is assigned.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: No

## See Also
<a name="API_CapacityReservation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CapacityReservation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CapacityReservation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CapacityReservation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
