---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteMatrixTravelModeOptions.html
---

# RouteMatrixTravelModeOptions
<a name="API_RouteMatrixTravelModeOptions"></a>

Travel mode related options for the provided travel mode.

## Contents
<a name="API_RouteMatrixTravelModeOptions_Contents"></a>

 ** Car **   <a name="location-Type-RouteMatrixTravelModeOptions-Car"></a>
Travel mode options when the provided travel mode is `Car`.
Type: [RouteMatrixCarOptions](API_RouteMatrixCarOptions.md) object
Required: No

 ** Scooter **   <a name="location-Type-RouteMatrixTravelModeOptions-Scooter"></a>
Travel mode options when the provided travel mode is `Scooter`.
When travel mode is set to `Scooter`, then the avoidance option `ControlledAccessHighways` defaults to `true`.
Type: [RouteMatrixScooterOptions](API_RouteMatrixScooterOptions.md) object
Required: No

 ** Truck **   <a name="location-Type-RouteMatrixTravelModeOptions-Truck"></a>
Travel mode options when the provided travel mode is `Truck`.
Type: [RouteMatrixTruckOptions](API_RouteMatrixTruckOptions.md) object
Required: No

## See Also
<a name="API_RouteMatrixTravelModeOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteMatrixTravelModeOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteMatrixTravelModeOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteMatrixTravelModeOptions)
