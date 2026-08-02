---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteTransitOptions.html
---

# RouteTransitOptions
<a name="API_RouteTransitOptions"></a>

Options related to transit routing.

**Note**
Not supported in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.

## Contents
<a name="API_RouteTransitOptions_Contents"></a>

 ** AccessibilityAttributes **   <a name="location-Type-RouteTransitOptions-AccessibilityAttributes"></a>
Accessibility attributes to consider when calculating the route.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Valid Values: `Wheelchair`
Required: No

 ** AllowedModes **   <a name="location-Type-RouteTransitOptions-AllowedModes"></a>
Allowed transit transport modes when calculating the route. By default, all transport modes are allowed. Cannot be used together with `ExcludedModes`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 15 items.
Valid Values: `AerialTramway | Airplane | All | Bus | BusRapidTransit | CityTrain | Ferry | FunicularRailway | HighSpeedTrain | IntercityTrain | InterregionalTrain | LightRail | Monorail | PrivateBus | RegionalTrain | Subway`
Required: No

 ** ExcludedModes **   <a name="location-Type-RouteTransitOptions-ExcludedModes"></a>
Excluded transit transport modes when calculating the route. By default, all transport modes are allowed. Cannot be used together with `AllowedModes`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 15 items.
Valid Values: `AerialTramway | Airplane | All | Bus | BusRapidTransit | CityTrain | Ferry | FunicularRailway | HighSpeedTrain | IntercityTrain | InterregionalTrain | LightRail | Monorail | PrivateBus | RegionalTrain | Subway`
Required: No

 ** MaxTransfers **   <a name="location-Type-RouteTransitOptions-MaxTransfers"></a>
Maximum number of transfers allowed when calculating the route.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 6.
Required: No

 ** Pedestrian **   <a name="location-Type-RouteTransitOptions-Pedestrian"></a>
Options for the pedestrian leg of the transit route.
Type: [RouteTransitPedestrianOptions](API_RouteTransitPedestrianOptions.md) object
Required: No

## See Also
<a name="API_RouteTransitOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteTransitOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteTransitOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteTransitOptions)
