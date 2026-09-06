---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_InterruptibleCapacityAllocation.html
---

# InterruptibleCapacityAllocation
<a name="API_InterruptibleCapacityAllocation"></a>

 Represents the allocation of capacity from a source reservation to an interruptible reservation, tracking current and target instance counts for allocation management.

## Contents
<a name="API_InterruptibleCapacityAllocation_Contents"></a>

 ** instanceCount **
 The current number of instances allocated to the interruptible reservation.
Type: Integer
Required: No

 ** interruptibleCapacityReservationId **
 The ID of the interruptible Capacity Reservation created from the allocation.
Type: String
Required: No

 ** interruptionType **
 The type of interruption policy applied to the interruptible reservation.
Type: String
Valid Values: `adhoc`
Required: No

 ** status **
 The current status of the allocation (updating during reclamation, active when complete).
Type: String
Valid Values: `pending | active | updating | canceling | canceled | failed`
Required: No

 ** targetInstanceCount **
 After your modify request, the requested number of instances allocated to interruptible reservation.
Type: Integer
Required: No

 ** zeroSizePreference **
 Specifies how Amazon EC2 handles the interruptible Capacity Reservation when you reduce its allocation to zero instances. A value of `retain` keeps the interruptible Capacity Reservation active at zero capacity so that you can allocate instances to it again later. A value of `default` cancels the interruptible Capacity Reservation and returns the capacity to your source Capacity Reservation.
Type: String
Valid Values: `retain | default`
Required: No

## See Also
<a name="API_InterruptibleCapacityAllocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/InterruptibleCapacityAllocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/InterruptibleCapacityAllocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/InterruptibleCapacityAllocation)
