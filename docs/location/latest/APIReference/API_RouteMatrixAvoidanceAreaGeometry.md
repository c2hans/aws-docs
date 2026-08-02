---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteMatrixAvoidanceAreaGeometry.html
---

# RouteMatrixAvoidanceAreaGeometry
<a name="API_RouteMatrixAvoidanceAreaGeometry"></a>

Geometry of the area to be avoided.

## Contents
<a name="API_RouteMatrixAvoidanceAreaGeometry_Contents"></a>

 ** BoundingBox **   <a name="location-Type-RouteMatrixAvoidanceAreaGeometry-BoundingBox"></a>
Geometry defined as a bounding box. The first pair represents the X and Y coordinates (longitude and latitude,) of the southwest corner of the bounding box; the second pair represents the X and Y coordinates (longitude and latitude) of the northeast corner.
Type: Array of doubles
Array Members: Fixed number of 4 items.
Required: No

 ** Polygon **   <a name="location-Type-RouteMatrixAvoidanceAreaGeometry-Polygon"></a>
Geometry defined as a polygon with only one linear ring.
Type: Array of arrays of arrays of doubles
Array Members: Fixed number of 1 item.
Array Members: Minimum number of 4 items.
Array Members: Fixed number of 2 items.
Required: No

 ** PolylinePolygon **   <a name="location-Type-RouteMatrixAvoidanceAreaGeometry-PolylinePolygon"></a>
A list of Isoline PolylinePolygon, for each isoline PolylinePolygon, it contains PolylinePolygon of the first linear ring (the outer ring) and from second item to the last item (the inner rings). For more information on polyline encoding, see [https://github.com/aws-geospatial/polyline](https://github.com/aws-geospatial/polyline).
Type: Array of strings
Array Members: Fixed number of 1 item.
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_RouteMatrixAvoidanceAreaGeometry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteMatrixAvoidanceAreaGeometry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteMatrixAvoidanceAreaGeometry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteMatrixAvoidanceAreaGeometry)
