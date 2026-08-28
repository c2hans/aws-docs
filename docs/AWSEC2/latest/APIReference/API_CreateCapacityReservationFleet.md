---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateCapacityReservationFleet.html
---

# CreateCapacityReservationFleet
<a name="API_CreateCapacityReservationFleet"></a>

Creates a Capacity Reservation Fleet. For more information, see [Create a Capacity Reservation Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/work-with-cr-fleets.html#create-crfleet) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_CreateCapacityReservationFleet_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **AllocationStrategy**
The strategy used by the Capacity Reservation Fleet to determine which of the specified instance types to use. Currently, only the `prioritized` allocation strategy is supported. For more information, see [ Allocation strategy](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/crfleet-concepts.html#allocation-strategy) in the *Amazon EC2 User Guide*.
Valid values: `prioritized`
Type: String
Required: No

 **ClientToken**
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see [Ensure Idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **EndDate**
The date and time at which the Capacity Reservation Fleet expires. When the Capacity Reservation Fleet expires, its state changes to `expired` and all of the Capacity Reservations in the Fleet expire.
The Capacity Reservation Fleet expires within an hour after the specified time. For example, if you specify `5/31/2019`, `13:30:55`, the Capacity Reservation Fleet is guaranteed to expire between `13:30:55` and `14:30:55` on `5/31/2019`.
Type: Timestamp
Required: No

 **InstanceMatchCriteria**
Indicates the type of instance launches that the Capacity Reservation Fleet accepts. All Capacity Reservations in the Fleet inherit this instance matching criteria.
Currently, Capacity Reservation Fleets support `open` instance matching criteria only. This means that instances that have matching attributes (instance type, platform, and Availability Zone) run in the Capacity Reservations automatically. Instances do not need to explicitly target a Capacity Reservation Fleet to use its reserved capacity.
Type: String
Valid Values: `open`
Required: No

 **InstanceTypeSpecification.N**
Information about the instance types for which to reserve the capacity.
Type: Array of [ReservationFleetInstanceSpecification](API_ReservationFleetInstanceSpecification.md) objects
Required: No

 **TagSpecification.N**
The tags to assign to the Capacity Reservation Fleet. The tags are automatically assigned to the Capacity Reservations in the Fleet.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

 **Tenancy**
Indicates the tenancy of the Capacity Reservation Fleet. All Capacity Reservations in the Fleet inherit this tenancy. The Capacity Reservation Fleet can have one of the following tenancy settings:
+  `default` - The Capacity Reservation Fleet is created on hardware that is shared with other AWS accounts.
+  `dedicated` - The Capacity Reservations are created on single-tenant hardware that is dedicated to a single AWS account.
Type: String
Valid Values: `default`
Required: No

 **TotalTargetCapacity**
The total number of capacity units to be reserved by the Capacity Reservation Fleet. This value, together with the instance type weights that you assign to each instance type used by the Fleet determine the number of instances for which the Fleet reserves capacity. Both values are based on units that make sense for your workload. For more information, see [Total target capacity](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/crfleet-concepts.html#target-capacity) in the *Amazon EC2 User Guide*.
Type: Integer
Required: Yes

## Response Elements
<a name="API_CreateCapacityReservationFleet_ResponseElements"></a>

The following elements are returned by the service.

 **allocationStrategy**
The allocation strategy used by the Capacity Reservation Fleet.
Type: String

 **capacityReservationFleetId**
The ID of the Capacity Reservation Fleet.
Type: String

 **createTime**
The date and time at which the Capacity Reservation Fleet was created.
Type: Timestamp

 **endDate**
The date and time at which the Capacity Reservation Fleet expires.
Type: Timestamp

 **fleetCapacityReservationSet**
Information about the individual Capacity Reservations in the Capacity Reservation Fleet.
Type: Array of [FleetCapacityReservation](API_FleetCapacityReservation.md) objects

 **instanceMatchCriteria**
The instance matching criteria for the Capacity Reservation Fleet.
Type: String
Valid Values: `open`

 **requestId**
The ID of the request.
Type: String

 **state**
The status of the Capacity Reservation Fleet.
Type: String
Valid Values: `submitted | modifying | active | partially_fulfilled | expiring | expired | cancelling | cancelled | failed`

 **tagSet**
The tags assigned to the Capacity Reservation Fleet.
Type: Array of [Tag](API_Tag.md) objects

 **tenancy**
Indicates the tenancy of Capacity Reservation Fleet.
Type: String
Valid Values: `default`

 **totalFulfilledCapacity**
The requested capacity units that have been successfully reserved.
Type: Double

 **totalTargetCapacity**
The total number of capacity units for which the Capacity Reservation Fleet reserves capacity.
Type: Integer

## Errors
<a name="API_CreateCapacityReservationFleet_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_CreateCapacityReservationFleet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateCapacityReservationFleet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateCapacityReservationFleet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateCapacityReservationFleet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateCapacityReservationFleet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateCapacityReservationFleet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateCapacityReservationFleet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateCapacityReservationFleet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateCapacityReservationFleet)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateCapacityReservationFleet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateCapacityReservationFleet)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
