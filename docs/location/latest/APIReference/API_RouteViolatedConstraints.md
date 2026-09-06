---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteViolatedConstraints.html
---

# RouteViolatedConstraints
<a name="API_RouteViolatedConstraints"></a>

This property contains a summary of violated constraints.

## Contents
<a name="API_RouteViolatedConstraints_Contents"></a>

 ** HazardousCargos **   <a name="location-Type-RouteViolatedConstraints-HazardousCargos"></a>
List of Hazardous cargo contained in the vehicle.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 11 items.
Valid Values: `Combustible | Corrosive | Explosive | Flammable | Gas | HarmfulToWater | Organic | Other | Poison | PoisonousInhalation | Radioactive`
Required: Yes

 ** AllHazardsRestricted **   <a name="location-Type-RouteViolatedConstraints-AllHazardsRestricted"></a>
This restriction applies to truck cargo, where the resulting route excludes roads on which hazardous materials are prohibited from being transported.
Type: Boolean
Required: No

 ** AxleCount **   <a name="location-Type-RouteViolatedConstraints-AxleCount"></a>
Total number of axles of the vehicle.
Type: [RouteNoticeDetailRange](API_RouteNoticeDetailRange.md) object
Required: No

 ** MaxHeight **   <a name="location-Type-RouteViolatedConstraints-MaxHeight"></a>
The maximum height of the vehicle.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** MaxKpraLength **   <a name="location-Type-RouteViolatedConstraints-MaxKpraLength"></a>
The maximum Kpra length of the vehicle.
 **Unit**: `centimeters`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** MaxLength **   <a name="location-Type-RouteViolatedConstraints-MaxLength"></a>
The maximum length of the vehicle.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** MaxPayloadCapacity **   <a name="location-Type-RouteViolatedConstraints-MaxPayloadCapacity"></a>
The maximum load capacity of the vehicle.
 **Unit**: `kilograms`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** MaxWeight **   <a name="location-Type-RouteViolatedConstraints-MaxWeight"></a>
The maximum weight of the route.
 **Unit**: `kilograms`
Type: [RouteWeightConstraint](API_RouteWeightConstraint.md) object
Required: No

 ** MaxWeightPerAxle **   <a name="location-Type-RouteViolatedConstraints-MaxWeightPerAxle"></a>
The maximum weight per axle of the vehicle.
 **Unit**: `kilograms`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** MaxWeightPerAxleGroup **   <a name="location-Type-RouteViolatedConstraints-MaxWeightPerAxleGroup"></a>
The maximum weight per axle group of the vehicle.
 **Unit**: `kilograms`
Type: [WeightPerAxleGroup](API_WeightPerAxleGroup.md) object
Required: No

 ** MaxWidth **   <a name="location-Type-RouteViolatedConstraints-MaxWidth"></a>
The maximum width of the vehicle.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** Occupancy **   <a name="location-Type-RouteViolatedConstraints-Occupancy"></a>
The number of occupants in the vehicle.
Default value: `1`
Type: [RouteNoticeDetailRange](API_RouteNoticeDetailRange.md) object
Required: No

 ** RestrictedTimes **   <a name="location-Type-RouteViolatedConstraints-RestrictedTimes"></a>
Access radius restrictions based on time.
Type: String
Required: No

 ** TimeDependent **   <a name="location-Type-RouteViolatedConstraints-TimeDependent"></a>
The time dependent constraint.
Type: Boolean
Required: No

 ** TrailerCount **   <a name="location-Type-RouteViolatedConstraints-TrailerCount"></a>
Number of trailers attached to the vehicle.
Default value: `0`
Type: [RouteNoticeDetailRange](API_RouteNoticeDetailRange.md) object
Required: No

 ** TravelMode **   <a name="location-Type-RouteViolatedConstraints-TravelMode"></a>
Travel mode corresponding to the leg.
Type: Boolean
Required: No

 ** TruckRoadType **   <a name="location-Type-RouteViolatedConstraints-TruckRoadType"></a>
Truck road type identifiers. `BK1` through `BK4` apply only to Sweden. `A2,A4,B2,B4,C,D,ET2,ET4` apply only to Mexico.
There are currently no other supported values as of 26th April 2024.
Type: String
Required: No

 ** TruckType **   <a name="location-Type-RouteViolatedConstraints-TruckType"></a>
The type of truck: `LightTruck` for smaller delivery vehicles, ` StraightTruck` for rigid body trucks, or `Tractor` for tractor-trailer combinations.
Type: String
Valid Values: `LightTruck | StraightTruck | Tractor`
Required: No

 ** TunnelRestrictionCode **   <a name="location-Type-RouteViolatedConstraints-TunnelRestrictionCode"></a>
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

## See Also
<a name="API_RouteViolatedConstraints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteViolatedConstraints)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteViolatedConstraints)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteViolatedConstraints)
