---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CapacityReservationRequest.html
---

# CapacityReservationRequest
<a name="API_CapacityReservationRequest"></a>

The Capacity Reservation configurations to be used when using the `RESERVED` capacity option type.

## Contents
<a name="API_CapacityReservationRequest_Contents"></a>

 ** reservationGroupArn **   <a name="ECS-Type-CapacityReservationRequest-reservationGroupArn"></a>
The ARN of the Capacity Reservation resource group in which to run the instance.
Type: String
Required: No

 ** reservationPreference **   <a name="ECS-Type-CapacityReservationRequest-reservationPreference"></a>
The preference on when capacity reservations should be used.
Valid values are:
+  `RESERVATIONS_ONLY` - Exclusively launch instances into capacity reservations that match the instance requirements configured for the capacity provider. If none exist, instances will fail to provision.
+  `RESERVATIONS_FIRST` - Prefer to launch instances into a capacity reservation if any exist that match the instance requirements configured for the capacity provider. If none exist, fall back to launching instances On-Demand.
+  `RESERVATIONS_EXCLUDED` - Avoid using capacity reservations and launch exclusively On-Demand.
Type: String
Valid Values: `RESERVATIONS_ONLY | RESERVATIONS_FIRST | RESERVATIONS_EXCLUDED`
Required: No

## See Also
<a name="API_CapacityReservationRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/CapacityReservationRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/CapacityReservationRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/CapacityReservationRequest)
