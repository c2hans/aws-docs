---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointOptimizationTruckOptions.html
---

# WaypointOptimizationTruckOptions
<a name="API_WaypointOptimizationTruckOptions"></a>

Travel mode options when the provided travel mode is `Truck`.

## Contents
<a name="API_WaypointOptimizationTruckOptions_Contents"></a>

 ** GrossWeight **   <a name="location-Type-WaypointOptimizationTruckOptions-GrossWeight"></a>
Gross weight of the vehicle including trailers, and goods at capacity.
 **Unit**: `kilograms`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** HazardousCargos **   <a name="location-Type-WaypointOptimizationTruckOptions-HazardousCargos"></a>
List of Hazardous cargo contained in the vehicle.
Type: Array of strings
Valid Values: `Combustible | Corrosive | Explosive | Flammable | Gas | HarmfulToWater | Organic | Other | Poison | PoisonousInhalation | Radioactive`
Required: No

 ** Height **   <a name="location-Type-WaypointOptimizationTruckOptions-Height"></a>
Height of the vehicle.
 **Unit**: `centimeters`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 5000.
Required: No

 ** Length **   <a name="location-Type-WaypointOptimizationTruckOptions-Length"></a>
Length of the vehicle.
 **Unit**: `centimeters`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 30000.
Required: No

 ** Trailer **   <a name="location-Type-WaypointOptimizationTruckOptions-Trailer"></a>
Trailer options corresponding to the vehicle.
Type: [WaypointOptimizationTrailerOptions](API_WaypointOptimizationTrailerOptions.md) object
Required: No

 ** TruckType **   <a name="location-Type-WaypointOptimizationTruckOptions-TruckType"></a>
The type of truck: `LightTruck` for smaller delivery vehicles, ` StraightTruck` for rigid body trucks, or `Tractor` for tractor-trailer combinations.
Type: String
Valid Values: `StraightTruck | Tractor`
Required: No

 ** TunnelRestrictionCode **   <a name="location-Type-WaypointOptimizationTruckOptions-TunnelRestrictionCode"></a>
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

 ** WeightPerAxle **   <a name="location-Type-WaypointOptimizationTruckOptions-WeightPerAxle"></a>
Heaviest weight per axle irrespective of the axle type or the axle group. Meant for usage in countries where the differences in axle types or axle groups are not distinguished.
 **Unit**: `kilograms`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** Width **   <a name="location-Type-WaypointOptimizationTruckOptions-Width"></a>
Width of the vehicle.
 **Unit**: `centimeters`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 5000.
Required: No

## See Also
<a name="API_WaypointOptimizationTruckOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/WaypointOptimizationTruckOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/WaypointOptimizationTruckOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/WaypointOptimizationTruckOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
