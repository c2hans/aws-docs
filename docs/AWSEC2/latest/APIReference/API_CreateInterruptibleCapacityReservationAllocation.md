---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateInterruptibleCapacityReservationAllocation.html
---

# CreateInterruptibleCapacityReservationAllocation
<a name="API_CreateInterruptibleCapacityReservationAllocation"></a>

 Creates an interruptible Capacity Reservation by specifying the number of unused instances you want to allocate from your source reservation. This helps you make unused capacity available for other workloads within your account while maintaining control to reclaim it.

## Request Parameters
<a name="API_CreateInterruptibleCapacityReservationAllocation_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **CapacityReservationId**
 The ID of the source Capacity Reservation from which to create the interruptible Capacity Reservation. Your Capacity Reservation must be in active state with no end date set and have available capacity for allocation.
Type: String
Required: Yes

 **ClientToken**
 Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Required: No

 **DryRun**
 Checks whether you have the required permissions for the action, without actually making the request, and provides an error response.
Type: Boolean
Required: No

 **InstanceCount**
 The number of instances to allocate from your source reservation. You can only allocate available instances (also called unused capacity).
Type: Integer
Required: Yes

 **TagSpecification.N**
 The tags to apply to the interruptible Capacity Reservation during creation.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

 **ZeroSizePreference**
 Specifies the behavior for the interruptible Capacity Reservation when you reduce its allocation to zero instances. Specify `retain` to keep the interruptible Capacity Reservation active at zero capacity so that you can allocate instances to it again later. Specify `default` to cancel the interruptible Capacity Reservation and return the capacity to your source Capacity Reservation. The default value is `default`.
Type: String
Valid Values: `retain | default`
Required: No

## Response Elements
<a name="API_CreateInterruptibleCapacityReservationAllocation_ResponseElements"></a>

The following elements are returned by the service.

 **interruptionType**
 The type of interruption applied to the interruptible reservation.
Type: String
Valid Values: `adhoc`

 **requestId**
The ID of the request.
Type: String

 **sourceCapacityReservationId**
 The ID of the source Capacity Reservation from which the interruptible Capacity Reservation was created.
Type: String

 **status**
 The current status of the allocation request (creating, active, updating).
Type: String
Valid Values: `pending | active | updating | canceling | canceled | failed`

 **targetInstanceCount**
 The number of instances allocated to the interruptible reservation.
Type: Integer

## Errors
<a name="API_CreateInterruptibleCapacityReservationAllocation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_CreateInterruptibleCapacityReservationAllocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateInterruptibleCapacityReservationAllocation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateInterruptibleCapacityReservationAllocation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateInterruptibleCapacityReservationAllocation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateInterruptibleCapacityReservationAllocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateInterruptibleCapacityReservationAllocation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateInterruptibleCapacityReservationAllocation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateInterruptibleCapacityReservationAllocation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateInterruptibleCapacityReservationAllocation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateInterruptibleCapacityReservationAllocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateInterruptibleCapacityReservationAllocation)
