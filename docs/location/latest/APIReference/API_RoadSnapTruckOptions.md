---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RoadSnapTruckOptions.html
---

# RoadSnapTruckOptions
<a name="API_RoadSnapTruckOptions"></a>

Travel mode options when the provided travel mode is `Truck`.

## Contents
<a name="API_RoadSnapTruckOptions_Contents"></a>

 ** GrossWeight **   <a name="location-Type-RoadSnapTruckOptions-GrossWeight"></a>
Gross weight of the vehicle including trailers, and goods at capacity.
 **Unit**: `kilograms`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** HazardousCargos **   <a name="location-Type-RoadSnapTruckOptions-HazardousCargos"></a>
List of Hazardous cargos contained in the vehicle.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 11 items.
Valid Values: `Combustible | Corrosive | Explosive | Flammable | Gas | HarmfulToWater | Organic | Other | Poison | PoisonousInhalation | Radioactive`
Required: No

 ** Height **   <a name="location-Type-RoadSnapTruckOptions-Height"></a>
Height of the vehicle.
 **Unit**: `centimeters`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 5000.
Required: No

 ** Length **   <a name="location-Type-RoadSnapTruckOptions-Length"></a>
Length of the vehicle.
 **Unit**: `centimeters`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 30000.
Required: No

 ** Trailer **   <a name="location-Type-RoadSnapTruckOptions-Trailer"></a>
Trailer options corresponding to the vehicle.
Type: [RoadSnapTrailerOptions](API_RoadSnapTrailerOptions.md) object
Required: No

 ** TunnelRestrictionCode **   <a name="location-Type-RoadSnapTruckOptions-TunnelRestrictionCode"></a>
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

 ** Width **   <a name="location-Type-RoadSnapTruckOptions-Width"></a>
Width of the vehicle in centimeters.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 5000.
Required: No

## See Also
<a name="API_RoadSnapTruckOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RoadSnapTruckOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RoadSnapTruckOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RoadSnapTruckOptions)
