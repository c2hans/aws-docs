---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteChargeStepDetails.html
---

# RouteChargeStepDetails
<a name="API_RouteChargeStepDetails"></a>

Details about the EV charge at the current step.

## Contents
<a name="API_RouteChargeStepDetails_Contents"></a>

 ** ArrivalCharge **   <a name="location-Type-RouteChargeStepDetails-ArrivalCharge"></a>
Estimated vehicle battery charge before this step (in kWh).
Type: Double
Valid Range: Minimum value of 0.0.
Required: No

 ** ConsumablePower **   <a name="location-Type-RouteChargeStepDetails-ConsumablePower"></a>
Maximum charging power available to the vehicle.
 **Unit**: `KwH`
Type: Double
Valid Range: Minimum value of 0.0.
Required: No

 ** DesiredCharge **   <a name="location-Type-RouteChargeStepDetails-DesiredCharge"></a>
Details that are specific to a Charge step.
 **Unit**: `KwH`
Type: Double
Valid Range: Minimum value of 0.0.
Required: No

## See Also
<a name="API_RouteChargeStepDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteChargeStepDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteChargeStepDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteChargeStepDetails)
