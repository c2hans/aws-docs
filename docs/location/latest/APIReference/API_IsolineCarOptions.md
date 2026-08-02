---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_IsolineCarOptions.html
---

# IsolineCarOptions
<a name="API_IsolineCarOptions"></a>

Vehicle characteristics and preferences that affect routing for passenger cars. This includes vehicle type, occupancy, and speed restrictions that may influence which roads can be used and expected travel times.

## Contents
<a name="API_IsolineCarOptions_Contents"></a>

 ** EngineType **   <a name="location-Type-IsolineCarOptions-EngineType"></a>
The type of engine powering the vehicle, which may affect route calculation due to road restrictions or vehicle characteristics.
+  `INTERNAL_COMBUSTION`—Standard gasoline or diesel engine.
+  `ELECTRIC`—Battery electric vehicle.
+  `PLUGIN_HYBRID`—Combination of electric and internal combustion engines with plug-in charging capability.
Type: String
Valid Values: `Electric | InternalCombustion | PluginHybrid`
Required: No

 ** LicensePlate **   <a name="location-Type-IsolineCarOptions-LicensePlate"></a>
License plate information used in regions where road access or routing restrictions are based on license plate numbers.
Type: [IsolineVehicleLicensePlate](API_IsolineVehicleLicensePlate.md) object
Required: No

 ** MaxSpeed **   <a name="location-Type-IsolineCarOptions-MaxSpeed"></a>
The maximum speed of the vehicle in kilometers per hour. When specified, routes will not include roads with higher speed limits. Valid values range from 3.6 km/h (1 m/s) to 252 km/h (70 m/s).
 **Unit**: `kilometers per hour`
Type: Double
Valid Range: Minimum value of 3.6. Maximum value of 252.0.
Required: No

 ** Occupancy **   <a name="location-Type-IsolineCarOptions-Occupancy"></a>
The number of occupants in the vehicle. This can affect route calculations by enabling the use of high-occupancy vehicle (HOV) lanes where minimum occupancy requirements are met.
Default value: `1`
Type: Integer
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_IsolineCarOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/IsolineCarOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/IsolineCarOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/IsolineCarOptions)
