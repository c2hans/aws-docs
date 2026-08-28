---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteAvoidanceAreaGeometry.html
---

# RouteAvoidanceAreaGeometry
<a name="API_RouteAvoidanceAreaGeometry"></a>

Geometry of the area to be avoided.

## Contents
<a name="API_RouteAvoidanceAreaGeometry_Contents"></a>

 ** BoundingBox **   <a name="location-Type-RouteAvoidanceAreaGeometry-BoundingBox"></a>
Geometry defined as a bounding box. The first pair represents the X and Y coordinates (longitude and latitude,) of the southwest corner of the bounding box; the second pair represents the X and Y coordinates (longitude and latitude) of the northeast corner.
Type: Array of doubles
Array Members: Fixed number of 4 items.
Required: No

 ** Corridor **   <a name="location-Type-RouteAvoidanceAreaGeometry-Corridor"></a>
Geometry defined as a corridor - a LineString with a radius that defines the width of the corridor.
Type: [Corridor](API_Corridor.md) object
Required: No

 ** Polygon **   <a name="location-Type-RouteAvoidanceAreaGeometry-Polygon"></a>
Geometry defined as a polygon with only one linear ring.
Type: Array of arrays of arrays of doubles
Array Members: Fixed number of 1 item.
Array Members: Minimum number of 4 items.
Array Members: Fixed number of 2 items.
Required: No

 ** PolylineCorridor **   <a name="location-Type-RouteAvoidanceAreaGeometry-PolylineCorridor"></a>
Geometry defined as an encoded corridor - an encoded polyline with a radius that defines the width of the corridor.
Type: [PolylineCorridor](API_PolylineCorridor.md) object
Required: No

 ** PolylinePolygon **   <a name="location-Type-RouteAvoidanceAreaGeometry-PolylinePolygon"></a>
A list of Isoline PolylinePolygon, for each isoline PolylinePolygon, it contains PolylinePolygon of the first linear ring (the outer ring) and from 2nd item to the last item (the inner rings). For more information on polyline encoding, see [https://github.com/aws-geospatial/polyline](https://github.com/aws-geospatial/polyline).
Type: Array of strings
Array Members: Fixed number of 1 item.
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_RouteAvoidanceAreaGeometry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteAvoidanceAreaGeometry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteAvoidanceAreaGeometry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteAvoidanceAreaGeometry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
