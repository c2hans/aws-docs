---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_Isoline.html
---

# Isoline
<a name="API_Isoline"></a>

Represents a single reachable area calculated for a specific threshold.

## Contents
<a name="API_Isoline_Contents"></a>

 ** Connections **   <a name="location-Type-Isoline-Connections"></a>
Lines connecting separate parts of the reachable area that can be reached within the same threshold. These occur when areas are reachable but not contiguous, such as when separated by water or unroutable areas. When present, these lines represent actual transportation network segments (such as ferry routes or bridges) that connect the separated areas.
Type: Array of [IsolineConnection](API_IsolineConnection.md) objects
Required: Yes

 ** Geometries **   <a name="location-Type-Isoline-Geometries"></a>
The shapes that define the reachable area, provided in the requested geometry format.
Type: Array of [IsolineShapeGeometry](API_IsolineShapeGeometry.md) objects
Required: Yes

 ** DistanceThreshold **   <a name="location-Type-Isoline-DistanceThreshold"></a>
The travel distance in meters used to calculate this isoline, if distance-based thresholds were specified in the request.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** TimeThreshold **   <a name="location-Type-Isoline-TimeThreshold"></a>
The travel time in seconds used to calculate this isoline, if time-based thresholds were specified in the request.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

## See Also
<a name="API_Isoline_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/Isoline)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/Isoline)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/Isoline)
