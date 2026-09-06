---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteCarOptions.html
---

# RouteCarOptions
<a name="API_RouteCarOptions"></a>

 Travel mode options when the provided travel mode is `Car`. For [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers, `ap-southeast-1` and `ap-southeast-5` regions support only `LicensePlate` options.

## Contents
<a name="API_RouteCarOptions_Contents"></a>

 ** EngineType **   <a name="location-Type-RouteCarOptions-EngineType"></a>
 Engine type of the vehicle. Not supported in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
Type: String
Valid Values: `Electric | InternalCombustion | PluginHybrid`
Required: No

 ** LicensePlate **   <a name="location-Type-RouteCarOptions-LicensePlate"></a>
The vehicle License Plate.
Type: [RouteVehicleLicensePlate](API_RouteVehicleLicensePlate.md) object
Required: No

 ** MaxSpeed **   <a name="location-Type-RouteCarOptions-MaxSpeed"></a>
 Maximum speed specified. Not supported in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
 **Unit**: `kilometers per hour`
Type: Double
Valid Range: Minimum value of 3.6. Maximum value of 252.0.
Required: No

 ** Occupancy **   <a name="location-Type-RouteCarOptions-Occupancy"></a>
 The number of occupants in the vehicle. Not supported in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
Default value: `1`
Type: Integer
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_RouteCarOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteCarOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteCarOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteCarOptions)
