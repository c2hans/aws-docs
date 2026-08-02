---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteLegGeometry.html
---

# RouteLegGeometry
<a name="API_RouteLegGeometry"></a>

The returned Route leg geometry.

## Contents
<a name="API_RouteLegGeometry_Contents"></a>

 ** LineString **   <a name="location-Type-RouteLegGeometry-LineString"></a>
An ordered list of positions used to plot a route on a map.
LineString and Polyline are mutually exclusive properties.
Type: Array of arrays of doubles
Array Members: Minimum number of 2 items.
Array Members: Fixed number of 2 items.
Required: No

 ** Polyline **   <a name="location-Type-RouteLegGeometry-Polyline"></a>
An ordered list of positions used to plot a route on a map in a lossy compression format.
LineString and Polyline are mutually exclusive properties.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_RouteLegGeometry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteLegGeometry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteLegGeometry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteLegGeometry)
