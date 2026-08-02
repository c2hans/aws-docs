---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointOptimizationImpedingWaypoint.html
---

# WaypointOptimizationImpedingWaypoint
<a name="API_WaypointOptimizationImpedingWaypoint"></a>

The impeding waypoint.

## Contents
<a name="API_WaypointOptimizationImpedingWaypoint_Contents"></a>

 ** FailedConstraints **   <a name="location-Type-WaypointOptimizationImpedingWaypoint-FailedConstraints"></a>
Failed constraints for an impeding waypoint.
Type: Array of [WaypointOptimizationFailedConstraint](API_WaypointOptimizationFailedConstraint.md) objects
Required: Yes

 ** Id **   <a name="location-Type-WaypointOptimizationImpedingWaypoint-Id"></a>
The waypoint Id.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[^,;!]+`
Required: Yes

 ** Position **   <a name="location-Type-WaypointOptimizationImpedingWaypoint-Position"></a>
Position in World Geodetic System (WGS 84) format: [longitude, latitude].
Type: Array of doubles
Array Members: Fixed number of 2 items.
Required: Yes

## See Also
<a name="API_WaypointOptimizationImpedingWaypoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/WaypointOptimizationImpedingWaypoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/WaypointOptimizationImpedingWaypoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/WaypointOptimizationImpedingWaypoint)
