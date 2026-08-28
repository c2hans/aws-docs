---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_IsolineScooterOptions.html
---

# IsolineScooterOptions
<a name="API_IsolineScooterOptions"></a>

Vehicle characteristics that affect which roads and paths can be used when calculating reachable areas for scooters. This includes areas such as bike lanes, shared paths, and roads where scooters are permitted.

## Contents
<a name="API_IsolineScooterOptions_Contents"></a>

 ** EngineType **   <a name="location-Type-IsolineScooterOptions-EngineType"></a>
The type of engine powering the vehicle, which may affect route calculation due to road restrictions or vehicle characteristics.
+  `INTERNAL_COMBUSTION`—Standard gasoline or diesel engine.
+  `ELECTRIC`—Battery electric vehicle.
+  `PLUGIN_HYBRID`—Combination of electric and internal combustion engines with plug-in charging capability.
Type: String
Valid Values: `Electric | InternalCombustion | PluginHybrid`
Required: No

 ** LicensePlate **   <a name="location-Type-IsolineScooterOptions-LicensePlate"></a>
License plate information used in regions where road access or routing restrictions are based on license plate numbers.
Type: [IsolineVehicleLicensePlate](API_IsolineVehicleLicensePlate.md) object
Required: No

 ** MaxSpeed **   <a name="location-Type-IsolineScooterOptions-MaxSpeed"></a>
The maximum speed of the vehicle in kilometers per hour. When specified, routes will not include roads with higher speed limits. Valid values range from 3.6 km/h (1 m/s) to 252 km/h (70 m/s).
 **Unit**: `kilometers per hour`
Type: Double
Valid Range: Minimum value of 3.6. Maximum value of 252.0.
Required: No

 ** Occupancy **   <a name="location-Type-IsolineScooterOptions-Occupancy"></a>
The number of occupants in the vehicle. This can affect route calculations by enabling the use of high-occupancy vehicle (HOV) lanes where minimum occupancy requirements are met.
Default value: `1`
Type: Integer
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_IsolineScooterOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/IsolineScooterOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/IsolineScooterOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/IsolineScooterOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
