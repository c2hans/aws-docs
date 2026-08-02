---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteMatrixTruckOptions.html
---

# RouteMatrixTruckOptions
<a name="API_RouteMatrixTruckOptions"></a>

Travel mode options when the provided travel mode is `Truck`.

## Contents
<a name="API_RouteMatrixTruckOptions_Contents"></a>

 ** AxleCount **   <a name="location-Type-RouteMatrixTruckOptions-AxleCount"></a>
Total number of axles of the vehicle.
Type: Integer
Valid Range: Minimum value of 2. Maximum value of 255.
Required: No

 ** GrossWeight **   <a name="location-Type-RouteMatrixTruckOptions-GrossWeight"></a>
Gross weight of the vehicle including trailers, and goods at capacity.
 **Unit**: `kilograms`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** HazardousCargos **   <a name="location-Type-RouteMatrixTruckOptions-HazardousCargos"></a>
List of Hazardous cargo contained in the vehicle.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 11 items.
Valid Values: `Combustible | Corrosive | Explosive | Flammable | Gas | HarmfulToWater | Organic | Other | Poison | PoisonousInhalation | Radioactive`
Required: No

 ** Height **   <a name="location-Type-RouteMatrixTruckOptions-Height"></a>
Height of the vehicle.
 **Unit**: `centimeters`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 5000.
Required: No

 ** KpraLength **   <a name="location-Type-RouteMatrixTruckOptions-KpraLength"></a>
Kingpin to rear axle length of the vehicle
 **Unit**: `centimeters`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** Length **   <a name="location-Type-RouteMatrixTruckOptions-Length"></a>
Length of the vehicle.
 **Unit**: `centimeters`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 30000.
Required: No

 ** LicensePlate **   <a name="location-Type-RouteMatrixTruckOptions-LicensePlate"></a>
The vehicle License Plate.
Type: [RouteMatrixVehicleLicensePlate](API_RouteMatrixVehicleLicensePlate.md) object
Required: No

 ** MaxSpeed **   <a name="location-Type-RouteMatrixTruckOptions-MaxSpeed"></a>
Maximum speed
 **Unit**: `kilometers per hour`
Type: Double
Valid Range: Minimum value of 3.6. Maximum value of 252.0.
Required: No

 ** Occupancy **   <a name="location-Type-RouteMatrixTruckOptions-Occupancy"></a>
The number of occupants in the vehicle.
Default value: `1`
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** PayloadCapacity **   <a name="location-Type-RouteMatrixTruckOptions-PayloadCapacity"></a>
Payload capacity of the vehicle and trailers attached.
 **Unit**: `kilograms`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** Trailer **   <a name="location-Type-RouteMatrixTruckOptions-Trailer"></a>
Trailer options corresponding to the vehicle.
Type: [RouteMatrixTrailerOptions](API_RouteMatrixTrailerOptions.md) object
Required: No

 ** TruckType **   <a name="location-Type-RouteMatrixTruckOptions-TruckType"></a>
The type of truck: `LightTruck` for smaller delivery vehicles, ` StraightTruck` for rigid body trucks, or `Tractor` for tractor-trailer combinations.
Type: String
Valid Values: `LightTruck | StraightTruck | Tractor`
Required: No

 ** TunnelRestrictionCode **   <a name="location-Type-RouteMatrixTruckOptions-TunnelRestrictionCode"></a>
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

 ** WeightPerAxle **   <a name="location-Type-RouteMatrixTruckOptions-WeightPerAxle"></a>
Heaviest weight per axle irrespective of the axle type or the axle group. Meant for usage in countries where the differences in axle types or axle groups are not distinguished.
 **Unit**: `kilograms`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** WeightPerAxleGroup **   <a name="location-Type-RouteMatrixTruckOptions-WeightPerAxleGroup"></a>
Specifies the total weight for the specified axle group. Meant for usage in countries that have different regulations based on the axle group type.
Type: [WeightPerAxleGroup](API_WeightPerAxleGroup.md) object
Required: No

 ** Width **   <a name="location-Type-RouteMatrixTruckOptions-Width"></a>
Width of the vehicle.
 **Unit**: `centimeters`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 5000.
Required: No

## See Also
<a name="API_RouteMatrixTruckOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteMatrixTruckOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteMatrixTruckOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteMatrixTruckOptions)
