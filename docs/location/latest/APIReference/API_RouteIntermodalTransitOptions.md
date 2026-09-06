---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteIntermodalTransitOptions.html
---

# RouteIntermodalTransitOptions
<a name="API_RouteIntermodalTransitOptions"></a>

Options for the transit leg of the intermodal route.

## Contents
<a name="API_RouteIntermodalTransitOptions_Contents"></a>

 ** AllowedModes **   <a name="location-Type-RouteIntermodalTransitOptions-AllowedModes"></a>
Allowed transit transport modes when calculating the route. By default, all transport modes are allowed. Cannot be used together with `ExcludedModes`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 15 items.
Valid Values: `AerialTramway | Airplane | All | Bus | BusRapidTransit | CityTrain | Ferry | FunicularRailway | HighSpeedTrain | IntercityTrain | InterregionalTrain | LightRail | Monorail | PrivateBus | RegionalTrain | Subway`
Required: No

 ** EnabledFor **   <a name="location-Type-RouteIntermodalTransitOptions-EnabledFor"></a>
Specifies the portion of the route for which this leg type is enabled. By default, the leg type is enabled for all legs. Valid values:
+  `FirstLeg` - Enable this leg type for the first non-pedestrian leg of the route.
+  `LastLeg` - Enable this leg type for the last non-pedestrian leg of the route.
+  `EntireRoute` - Enable this leg type for the entire route.
+  `None` - Disable this leg type entirely.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Valid Values: `FirstLeg | LastLeg | EntireRoute | None`
Required: No

 ** ExcludedModes **   <a name="location-Type-RouteIntermodalTransitOptions-ExcludedModes"></a>
Excluded transit transport modes when calculating the route. By default, all transport modes are allowed. Cannot be used together with `AllowedModes`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 15 items.
Valid Values: `AerialTramway | Airplane | All | Bus | BusRapidTransit | CityTrain | Ferry | FunicularRailway | HighSpeedTrain | IntercityTrain | InterregionalTrain | LightRail | Monorail | PrivateBus | RegionalTrain | Subway`
Required: No

## See Also
<a name="API_RouteIntermodalTransitOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteIntermodalTransitOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteIntermodalTransitOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteIntermodalTransitOptions)
