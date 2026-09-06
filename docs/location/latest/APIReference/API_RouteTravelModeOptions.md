---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteTravelModeOptions.html
---

# RouteTravelModeOptions
<a name="API_RouteTravelModeOptions"></a>

Travel mode related options for the provided travel mode.

## Contents
<a name="API_RouteTravelModeOptions_Contents"></a>

 ** Car **   <a name="location-Type-RouteTravelModeOptions-Car"></a>
Travel mode options when the provided travel mode is `Car`.
Type: [RouteCarOptions](API_RouteCarOptions.md) object
Required: No

 ** Intermodal **   <a name="location-Type-RouteTravelModeOptions-Intermodal"></a>
Travel mode options when the provided travel mode is `Intermodal`.
Not supported in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
Type: [RouteIntermodalOptions](API_RouteIntermodalOptions.md) object
Required: No

 ** Pedestrian **   <a name="location-Type-RouteTravelModeOptions-Pedestrian"></a>
Travel mode options when the provided travel mode is `Pedestrian`.
Type: [RoutePedestrianOptions](API_RoutePedestrianOptions.md) object
Required: No

 ** Scooter **   <a name="location-Type-RouteTravelModeOptions-Scooter"></a>
Travel mode options when the provided travel mode is `Scooter`.
When travel mode is set to `Scooter`, then the avoidance option `ControlledAccessHighways` defaults to `true`.
Type: [RouteScooterOptions](API_RouteScooterOptions.md) object
Required: No

 ** Transit **   <a name="location-Type-RouteTravelModeOptions-Transit"></a>
Travel mode options when the provided travel mode is `Transit`.
Not supported in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
Type: [RouteTransitOptions](API_RouteTransitOptions.md) object
Required: No

 ** Truck **   <a name="location-Type-RouteTravelModeOptions-Truck"></a>
Travel mode options when the provided travel mode is `Truck`.
Type: [RouteTruckOptions](API_RouteTruckOptions.md) object
Required: No

## See Also
<a name="API_RouteTravelModeOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteTravelModeOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteTravelModeOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteTravelModeOptions)
