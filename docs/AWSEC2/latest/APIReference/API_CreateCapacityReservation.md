---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateCapacityReservation.html
---

# CreateCapacityReservation
<a name="API_CreateCapacityReservation"></a>

Creates a new Capacity Reservation with the specified attributes. Capacity Reservations enable you to reserve capacity for your Amazon EC2 instances in a specific Availability Zone for any duration.

You can create a Capacity Reservation at any time, and you can choose when it starts. You can create a Capacity Reservation for immediate use or you can request a Capacity Reservation for a future date.

For more information, see [ Reserve compute capacity with On-Demand Capacity Reservations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-reservations.html) in the *Amazon EC2 User Guide*.

Your request to create a Capacity Reservation could fail if:
+ Amazon EC2 does not have sufficient capacity. In this case, try again at a later time, try in a different Availability Zone, or request a smaller Capacity Reservation. If your workload is flexible across instance types and sizes, try with different instance attributes.
+ The requested quantity exceeds your On-Demand Instance quota. In this case, increase your On-Demand Instance quota for the requested instance type and try again. For more information, see [ Amazon EC2 Service Quotas](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_CreateCapacityReservation_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **AvailabilityZone**
The Availability Zone in which to create the Capacity Reservation.
Type: String
Required: No

 **AvailabilityZoneId**
The ID of the Availability Zone in which to create the Capacity Reservation.
Type: String
Required: No

 **ClientToken**
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see [Ensure Idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).
Type: String
Required: No

 **CommitmentDuration**
Required for future-dated Capacity Reservations only. To create a Capacity Reservation for immediate use, omit this parameter.
Specify a commitment duration, in seconds, for the future-dated Capacity Reservation.
The commitment duration is a minimum duration for which you commit to having the future-dated Capacity Reservation in the `active` state in your account after it has been delivered.
For more information, see [ Commitment duration](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cr-concepts.html#cr-commitment-duration).
Type: Long
Valid Range: Minimum value of 1. Maximum value of 200000000.
Required: No

 **DeliveryPreference**
Required for future-dated Capacity Reservations only. To create a Capacity Reservation for immediate use, omit this parameter.
Indicates that the requested capacity will be delivered in addition to any running instances or reserved capacity that you have in your account at the requested date and time.
The only supported value is `incremental`.
Type: String
Valid Values: `fixed | incremental`
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **EbsOptimized**
Indicates whether the Capacity Reservation supports EBS-optimized instances. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal I/O performance. This optimization isn't available with all instance types. Additional usage charges apply when using an EBS- optimized instance.
Type: Boolean
Required: No

 **EndDate**
The date and time at which the Capacity Reservation expires. When a Capacity Reservation expires, the reserved capacity is released and you can no longer launch instances into it. The Capacity Reservation's state changes to `expired` when it reaches its end date and time.
You must provide an `EndDate` value if `EndDateType` is `limited`. Omit `EndDate` if `EndDateType` is `unlimited`.
If the `EndDateType` is `limited`, the Capacity Reservation is cancelled within an hour from the specified time. For example, if you specify 5/31/2019, 13:30:55, the Capacity Reservation is guaranteed to end between 13:30:55 and 14:30:55 on 5/31/2019.
If you are requesting a future-dated Capacity Reservation, you can't specify an end date and time that is within the commitment duration.
Type: Timestamp
Required: No

 **EndDateType**
Indicates the way in which the Capacity Reservation ends. A Capacity Reservation can have one of the following end types:
+  `unlimited` - The Capacity Reservation remains active until you explicitly cancel it. Do not provide an `EndDate` if the `EndDateType` is `unlimited`.
+  `limited` - The Capacity Reservation expires automatically at a specified date and time. You must provide an `EndDate` value if the `EndDateType` value is `limited`.
Type: String
Valid Values: `unlimited | limited`
Required: No

 **EphemeralStorage**
 *Deprecated.*
Type: Boolean
Required: No

 **InstanceCount**
The number of instances for which to reserve capacity.
You can request future-dated Capacity Reservations for an instance count with a minimum of 32 vCPUs. For example, if you request a future-dated Capacity Reservation for `m5.xlarge` instances, you must request at least 8 instances (*8 \* m5.xlarge = 32 vCPUs*).
Valid range: 1 - 1000
Type: Integer
Required: Yes

 **InstanceMatchCriteria**
Indicates the type of instance launches that the Capacity Reservation accepts. The options include:
+  `open` - The Capacity Reservation automatically matches all instances that have matching attributes (instance type, platform, and Availability Zone). Instances that have matching attributes run in the Capacity Reservation automatically without specifying any additional parameters.
+  `targeted` - The Capacity Reservation only accepts instances that have matching attributes (instance type, platform, and Availability Zone), and explicitly target the Capacity Reservation. This ensures that only permitted instances can use the reserved capacity.
If you are requesting a future-dated Capacity Reservation, you must specify `targeted`.
Default: `open`
Type: String
Valid Values: `open | targeted`
Required: No

 **InstancePlatform**
The type of operating system for which to reserve capacity.
Type: String
Valid Values: `Linux/UNIX | Red Hat Enterprise Linux | SUSE Linux | Windows | Windows with SQL Server | Windows with SQL Server Enterprise | Windows with SQL Server Standard | Windows with SQL Server Web | Linux with SQL Server Standard | Linux with SQL Server Web | Linux with SQL Server Enterprise | RHEL with SQL Server Standard | RHEL with SQL Server Enterprise | RHEL with SQL Server Web | RHEL with HA | RHEL with HA and SQL Server Standard | RHEL with HA and SQL Server Enterprise | Ubuntu Pro`
Required: Yes

 **InstanceType**
The instance type for which to reserve capacity.
You can request future-dated Capacity Reservations for instance types in the C, M, R, I, T, and G instance families only.
For more information, see [Instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html) in the *Amazon EC2 User Guide*.
Type: String
Required: Yes

 **OutpostArn**
Not supported for future-dated Capacity Reservations.
The Amazon Resource Name (ARN) of the Outpost on which to create the Capacity Reservation.
Type: String
Pattern: `^arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:outpost/op-[a-f0-9]{17}$`
Required: No

 **PlacementGroupArn**
Not supported for future-dated Capacity Reservations.
The Amazon Resource Name (ARN) of the cluster placement group in which to create the Capacity Reservation. For more information, see [ Capacity Reservations for cluster placement groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cr-cpg.html) in the *Amazon EC2 User Guide*.
Type: String
Pattern: `^arn:aws([a-z-]+)?:ec2:[a-z\d-]+:\d{12}:placement-group/^.{1,255}$`
Required: No

 **StartDate**
Required for future-dated Capacity Reservations only. To create a Capacity Reservation for immediate use, omit this parameter.
The date and time at which the future-dated Capacity Reservation should become available for use, in the ISO8601 format in the UTC time zone (`YYYY-MM-DDThh:mm:ss.sssZ`).
You can request a future-dated Capacity Reservation between 5 and 120 days in advance.
Type: Timestamp
Required: No

 **TagSpecifications.N**
The tags to apply to the Capacity Reservation during launch.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

 **Tenancy**
Indicates the tenancy of the Capacity Reservation. A Capacity Reservation can have one of the following tenancy settings:
+  `default` - The Capacity Reservation is created on hardware that is shared with other AWS accounts.
+  `dedicated` - The Capacity Reservation is created on single-tenant hardware that is dedicated to a single AWS account.
Type: String
Valid Values: `default | dedicated`
Required: No

## Response Elements
<a name="API_CreateCapacityReservation_ResponseElements"></a>

The following elements are returned by the service.

 **capacityReservation**
Information about the Capacity Reservation.
Type: [CapacityReservation](API_CapacityReservation.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_CreateCapacityReservation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_CreateCapacityReservation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateCapacityReservation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateCapacityReservation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateCapacityReservation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateCapacityReservation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateCapacityReservation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateCapacityReservation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateCapacityReservation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateCapacityReservation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateCapacityReservation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateCapacityReservation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
