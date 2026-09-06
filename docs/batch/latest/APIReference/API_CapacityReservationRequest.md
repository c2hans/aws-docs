---
source_url: https://docs.aws.amazon.com/batch/latest/APIReference/API_CapacityReservationRequest.html
---

# CapacityReservationRequest
<a name="API_CapacityReservationRequest"></a>

The capacity reservation configuration for Amazon ECS Managed Instances. Use this to target On-Demand Capacity Reservations or Reserved Instances.

## Contents
<a name="API_CapacityReservationRequest_Contents"></a>

 ** reservationGroupArn **   <a name="Batch-Type-CapacityReservationRequest-reservationGroupArn"></a>
The Amazon Resource Name (ARN) of the capacity reservation group to target.
Type: String
Required: No

 ** reservationPreference **   <a name="Batch-Type-CapacityReservationRequest-reservationPreference"></a>
The capacity reservation preference. Valid values:
+  `RESERVATIONS_ONLY` — Use only capacity reservations.
+  `RESERVATIONS_FIRST` — Prefer capacity reservations but fall back to On-Demand if unavailable.
+  `RESERVATIONS_EXCLUDED` — Do not use capacity reservations.
Type: String
Required: No

## See Also
<a name="API_CapacityReservationRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/CapacityReservationRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/CapacityReservationRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/CapacityReservationRequest)
