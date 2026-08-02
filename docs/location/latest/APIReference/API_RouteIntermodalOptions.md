---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteIntermodalOptions.html
---

# RouteIntermodalOptions
<a name="API_RouteIntermodalOptions"></a>

Options related to intermodal routing.

**Note**
Not supported in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.

## Contents
<a name="API_RouteIntermodalOptions_Contents"></a>

 ** AccessibilityAttributes **   <a name="location-Type-RouteIntermodalOptions-AccessibilityAttributes"></a>
Accessibility attributes to consider when calculating the route.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Valid Values: `Wheelchair`
Required: No

 ** MaxTransfers **   <a name="location-Type-RouteIntermodalOptions-MaxTransfers"></a>
Maximum number of transfers allowed when calculating the route.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 6.
Required: No

 ** Pedestrian **   <a name="location-Type-RouteIntermodalOptions-Pedestrian"></a>
Options for the pedestrian leg of the intermodal route.
Type: [RouteIntermodalPedestrianOptions](API_RouteIntermodalPedestrianOptions.md) object
Required: No

 ** Rental **   <a name="location-Type-RouteIntermodalOptions-Rental"></a>
Options for the rental leg of the intermodal route.
Type: [RouteIntermodalRentalOptions](API_RouteIntermodalRentalOptions.md) object
Required: No

 ** Taxi **   <a name="location-Type-RouteIntermodalOptions-Taxi"></a>
Options for the taxi leg of the intermodal route.
Type: [RouteIntermodalTaxiOptions](API_RouteIntermodalTaxiOptions.md) object
Required: No

 ** Transit **   <a name="location-Type-RouteIntermodalOptions-Transit"></a>
Options for the transit leg of the intermodal route.
Type: [RouteIntermodalTransitOptions](API_RouteIntermodalTransitOptions.md) object
Required: No

 ** Vehicle **   <a name="location-Type-RouteIntermodalOptions-Vehicle"></a>
Options for the vehicle leg of the intermodal route.
Type: [RouteIntermodalVehicleOptions](API_RouteIntermodalVehicleOptions.md) object
Required: No

## See Also
<a name="API_RouteIntermodalOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteIntermodalOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteIntermodalOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteIntermodalOptions)
