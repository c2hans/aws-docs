---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_IsolineTruckOptions.html
---

# IsolineTruckOptions
<a name="API_IsolineTruckOptions"></a>

Vehicle characteristics and restrictions that affect which roads can be used when calculating reachable areas for trucks. These details ensure that routes respect physical limitations and legal requirements.

These apply when the provided travel mode is `Truck`

## Contents
<a name="API_IsolineTruckOptions_Contents"></a>

 ** AxleCount **   <a name="location-Type-IsolineTruckOptions-AxleCount"></a>
The total number of axles on the vehicle. Required for certain road restrictions and weight limit calculations.
Type: Integer
Valid Range: Minimum value of 2. Maximum value of 255.
Required: No

 ** EngineType **   <a name="location-Type-IsolineTruckOptions-EngineType"></a>
The type of engine powering the vehicle, which may affect route calculation due to road restrictions or vehicle characteristics.
+  `INTERNAL_COMBUSTION`—Standard gasoline or diesel engine.
+  `ELECTRIC`—Battery electric vehicle.
+  `PLUGIN_HYBRID`—Combination of electric and internal combustion engines with plug-in charging capability.
Type: String
Valid Values: `Electric | InternalCombustion | PluginHybrid`
Required: No

 ** GrossWeight **   <a name="location-Type-IsolineTruckOptions-GrossWeight"></a>
The gross vehicle weight (the maximum weight a vehicle can safely operate at, as specified by the manufacturer) in kilograms. Used to avoid roads with weight restrictions and ensure compliance with maximum allowed vehicle weight regulations.
 **Unit**: `kilograms`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** HazardousCargos **   <a name="location-Type-IsolineTruckOptions-HazardousCargos"></a>
Types of hazardous materials being transported. This affects which roads and tunnels can be used based on local regulations.
+  `Combustible`—Materials that can burn readily
+  `Corrosive`—Materials that can destroy or irreversibly damage other substances
+  `Explosive`—Materials that can produce an explosion by chemical reaction
+  `Flammable`—Materials that can easily ignite
+  `Gas`—Hazardous materials in gaseous form
+  `HarmfulToWater`—Materials that pose a risk to water sources if released
+  `Organic`—Hazardous organic compounds
+  `Other`—Hazardous materials not covered by other categories
+  `Poison`—Toxic materials
+  `PoisonousInhalation`—Materials that are toxic when inhaled
+  `Radioactive`—Materials that emit ionizing radiation
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 11 items.
Valid Values: `Combustible | Corrosive | Explosive | Flammable | Gas | HarmfulToWater | Organic | Other | Poison | PoisonousInhalation | Radioactive`
Required: No

 ** Height **   <a name="location-Type-IsolineTruckOptions-Height"></a>
The vehicle height in centimeters. Used to avoid routes with low bridges or other height restrictions.
 **Unit**: `centimeters`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 5000.
Required: No

 ** HeightAboveFirstAxle **   <a name="location-Type-IsolineTruckOptions-HeightAboveFirstAxle"></a>
The height in centimeters measured from the ground to the highest point above the first axle. Used for specific bridge and tunnel clearance restrictions.
 **Unit**: `centimeters`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 5000.
Required: No

 ** KpraLength **   <a name="location-Type-IsolineTruckOptions-KpraLength"></a>
The kingpin to rear axle (KPRA) length in centimeters. Used to determine if the vehicle can safely navigate turns and intersections.
 **Unit**: `centimeters`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** Length **   <a name="location-Type-IsolineTruckOptions-Length"></a>
The total vehicle length in centimeters. Used to avoid roads with length restrictions and determine if the vehicle can safely navigate turns.
 **Unit**: `centimeters`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 30000.
Required: No

 ** LicensePlate **   <a name="location-Type-IsolineTruckOptions-LicensePlate"></a>
License plate information used in regions where road access or routing restrictions are based on license plate numbers.
Type: [IsolineVehicleLicensePlate](API_IsolineVehicleLicensePlate.md) object
Required: No

 ** MaxSpeed **   <a name="location-Type-IsolineTruckOptions-MaxSpeed"></a>
The maximum speed in kilometers per hour at which the vehicle can or is permitted to travel. This affects travel time calculations and may result in different reachable areas compared to using default speed limits. Value must be between 3.6 and 252 kilometers per hour.
 **Unit**: `kilometers per hour`
Type: Double
Valid Range: Minimum value of 3.6. Maximum value of 252.0.
Required: No

 ** Occupancy **   <a name="location-Type-IsolineTruckOptions-Occupancy"></a>
The number of occupants in the vehicle. This can affect route calculations by enabling the use of high-occupancy vehicle (HOV) lanes where minimum occupancy requirements are met.
Default value: `1`
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** PayloadCapacity **   <a name="location-Type-IsolineTruckOptions-PayloadCapacity"></a>
The maximum cargo weight in kilograms that the vehicle (including attached trailers) is rated to carry.
 **Unit**: `kilograms`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** TireCount **   <a name="location-Type-IsolineTruckOptions-TireCount"></a>
The total number of tires on the vehicle.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 255.
Required: No

 ** Trailer **   <a name="location-Type-IsolineTruckOptions-Trailer"></a>
Optional specifications for attached trailers. When provided, trailer characteristics affect route calculations to ensure compliance with trailer-specific restrictions such as length limits, weight distribution requirements, and access restrictions for multi-trailer configurations.
Type: [IsolineTrailerOptions](API_IsolineTrailerOptions.md) object
Required: No

 ** TruckType **   <a name="location-Type-IsolineTruckOptions-TruckType"></a>
The type of truck: `LightTruck` for smaller delivery vehicles, ` StraightTruck ` for rigid body trucks, or `Tractor` for tractor-trailer combinations.
Type: String
Valid Values: `LightTruck | StraightTruck | Tractor`
Required: No

 ** TunnelRestrictionCode **   <a name="location-Type-IsolineTruckOptions-TunnelRestrictionCode"></a>
The tunnel restriction code.
Tunnel categories in this list indicate the restrictions which apply to certain tunnels in Great Britain. They relate to the types of dangerous goods that can be transported through them.
+  *Tunnel Category B*
  +  *Risk Level*: Limited risk
  +  *Restrictions*: Few restrictions
+  *Tunnel Category C*
  +  *Risk Level*: Medium risk
  +  *Restrictions*: Some restrictions
+  *Tunnel Category D*
  +  *Risk Level*: High risk
  +  *Restrictions*: Many restrictions occur
+  *Tunnel Category E*
  +  *Risk Level*: Very high risk
  +  *Restrictions*: Restricted tunnel
Type: String
Length Constraints: Fixed length of 1.
Required: No

 ** WeightPerAxle **   <a name="location-Type-IsolineTruckOptions-WeightPerAxle"></a>
The heaviest weight per axle in kilograms, regardless of axle type or grouping. Used for roads with axle-weight restrictions in regions where regulations don't distinguish between different axle configurations.
 **Unit**: `kilograms`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** WeightPerAxleGroup **   <a name="location-Type-IsolineTruckOptions-WeightPerAxleGroup"></a>
Specifies the total weight for different axle group configurations. Used in regions where regulations set different weight limits based on axle group types.
 **Unit**: `kilograms`
Type: [WeightPerAxleGroup](API_WeightPerAxleGroup.md) object
Required: No

 ** Width **   <a name="location-Type-IsolineTruckOptions-Width"></a>
The vehicle width in centimeters. Used to avoid routes with width restrictions.
 **Unit**: `centimeters`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 5000.
Required: No

## See Also
<a name="API_IsolineTruckOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/IsolineTruckOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/IsolineTruckOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/IsolineTruckOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
