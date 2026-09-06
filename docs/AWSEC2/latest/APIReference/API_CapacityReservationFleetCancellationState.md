---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CapacityReservationFleetCancellationState.html
---

# CapacityReservationFleetCancellationState
<a name="API_CapacityReservationFleetCancellationState"></a>

Describes a Capacity Reservation Fleet that was successfully cancelled.

## Contents
<a name="API_CapacityReservationFleetCancellationState_Contents"></a>

 ** capacityReservationFleetId **
The ID of the Capacity Reservation Fleet that was successfully cancelled.
Type: String
Required: No

 ** currentFleetState **
The current state of the Capacity Reservation Fleet.
Type: String
Valid Values: `submitted | modifying | active | partially_fulfilled | expiring | expired | cancelling | cancelled | failed`
Required: No

 ** previousFleetState **
The previous state of the Capacity Reservation Fleet.
Type: String
Valid Values: `submitted | modifying | active | partially_fulfilled | expiring | expired | cancelling | cancelled | failed`
Required: No

## See Also
<a name="API_CapacityReservationFleetCancellationState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CapacityReservationFleetCancellationState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CapacityReservationFleetCancellationState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CapacityReservationFleetCancellationState)
