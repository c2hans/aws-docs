---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteTruckOptions.html
---

# RouteTruckOptions
<a name="API_RouteTruckOptions"></a>

 Travel mode options when the provided travel mode is `Truck`. Not supported in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.

## Contents
<a name="API_RouteTruckOptions_Contents"></a>

 ** AxleCount **   <a name="location-Type-RouteTruckOptions-AxleCount"></a>
Total number of axles of the vehicle.
Type: Integer
Valid Range: Minimum value of 2. Maximum value of 255.
Required: No

 ** EngineType **   <a name="location-Type-RouteTruckOptions-EngineType"></a>
Engine type of the vehicle.
Type: String
Valid Values: `Electric | InternalCombustion | PluginHybrid`
Required: No

 ** GrossWeight **   <a name="location-Type-RouteTruckOptions-GrossWeight"></a>
Gross weight of the vehicle including trailers, and goods at capacity.
 **Unit**: `kilograms`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** HazardousCargos **   <a name="location-Type-RouteTruckOptions-HazardousCargos"></a>
List of Hazardous cargo contained in the vehicle.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 11 items.
Valid Values: `Combustible | Corrosive | Explosive | Flammable | Gas | HarmfulToWater | Organic | Other | Poison | PoisonousInhalation | Radioactive`
Required: No

 ** Height **   <a name="location-Type-RouteTruckOptions-Height"></a>
Height of the vehicle.
 **Unit**: `centimeters`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 5000.
Required: No

 ** HeightAboveFirstAxle **   <a name="location-Type-RouteTruckOptions-HeightAboveFirstAxle"></a>
Height of the vehicle above its first axle.
 **Unit**: `centimeters`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 5000.
Required: No

 ** KpraLength **   <a name="location-Type-RouteTruckOptions-KpraLength"></a>
Kingpin to rear axle length of the vehicle.
 **Unit**: `centimeters`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** Length **   <a name="location-Type-RouteTruckOptions-Length"></a>
Length of the vehicle.
 **Unit**: `c`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 30000.
Required: No

 ** LicensePlate **   <a name="location-Type-RouteTruckOptions-LicensePlate"></a>
The vehicle License Plate.
Type: [RouteVehicleLicensePlate](API_RouteVehicleLicensePlate.md) object
Required: No

 ** MaxSpeed **   <a name="location-Type-RouteTruckOptions-MaxSpeed"></a>
Maximum speed
 **Unit**: `kilometers per hour`
Type: Double
Valid Range: Minimum value of 3.6. Maximum value of 252.0.
Required: No

 ** Occupancy **   <a name="location-Type-RouteTruckOptions-Occupancy"></a>
The number of occupants in the vehicle.
Default value: `1`
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** PayloadCapacity **   <a name="location-Type-RouteTruckOptions-PayloadCapacity"></a>
Payload capacity of the vehicle and trailers attached.
 **Unit**: `kilograms`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** TireCount **   <a name="location-Type-RouteTruckOptions-TireCount"></a>
Number of tires on the vehicle.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 255.
Required: No

 ** Trailer **   <a name="location-Type-RouteTruckOptions-Trailer"></a>
Trailer options corresponding to the vehicle.
Type: [RouteTrailerOptions](API_RouteTrailerOptions.md) object
Required: No

 ** TruckType **   <a name="location-Type-RouteTruckOptions-TruckType"></a>
The type of truck: `LightTruck` for smaller delivery vehicles, ` StraightTruck` for rigid body trucks, or `Tractor` for tractor-trailer combinations.
Type: String
Valid Values: `LightTruck | StraightTruck | Tractor`
Required: No

 ** TunnelRestrictionCode **   <a name="location-Type-RouteTruckOptions-TunnelRestrictionCode"></a>
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
Length Constraints: Minimum length of 0. Maximum length of 20.
Required: No

 ** WeightPerAxle **   <a name="location-Type-RouteTruckOptions-WeightPerAxle"></a>
Heaviest weight per axle irrespective of the axle type or the axle group. Meant for usage in countries where the differences in axle types or axle groups are not distinguished.
 **Unit**: `kilograms`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** WeightPerAxleGroup **   <a name="location-Type-RouteTruckOptions-WeightPerAxleGroup"></a>
Specifies the total weight for the specified axle group. Meant for usage in countries that have different regulations based on the axle group type.
 **Unit**: `kilograms`
Type: [WeightPerAxleGroup](API_WeightPerAxleGroup.md) object
Required: No

 ** Width **   <a name="location-Type-RouteTruckOptions-Width"></a>
Width of the vehicle.
 **Unit**: `centimeters`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 5000.
Required: No

## See Also
<a name="API_RouteTruckOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteTruckOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteTruckOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteTruckOptions)
