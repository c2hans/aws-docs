---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteMatrixBoundaryGeometry.html
---

# RouteMatrixBoundaryGeometry
<a name="API_RouteMatrixBoundaryGeometry"></a>

Geometry of the routing boundary.

## Contents
<a name="API_RouteMatrixBoundaryGeometry_Contents"></a>

 ** AutoCircle **   <a name="location-Type-RouteMatrixBoundaryGeometry-AutoCircle"></a>
 `AutoCircle` requests the route matrix service to define a `Circle` boundary that best attempts to include most waypoints (`Origins` and `Destinations`) using the `AutoCircle` settings. Any waypoints outside of the auto-defined `Circle` boundary will be considered out of the routing boundary, which results in a route matrix entry error.
 `AutoCircle` is only used in the request to configure a `Circle` for the route calculation. The derived `Circle` will also be provided in the response.
Type: [RouteMatrixAutoCircle](API_RouteMatrixAutoCircle.md) object
Required: No

 ** BoundingBox **   <a name="location-Type-RouteMatrixBoundaryGeometry-BoundingBox"></a>
Geometry defined as a bounding box. The first pair represents the X and Y coordinates (longitude and latitude,) of the southwest corner of the bounding box; the second pair represents the X and Y coordinates (longitude and latitude) of the northeast corner.
Diagonal distance of the bounding box must be less than or equal to 400,000 meters.
Type: Array of doubles
Array Members: Fixed number of 4 items.
Required: No

 ** Circle **   <a name="location-Type-RouteMatrixBoundaryGeometry-Circle"></a>
Geometry defined as a circle. The circle defines the routing boundary area. Any waypoints outside the circle will result in a route matrix entry error.
You can specify a `Circle` directly in the request, or it will be auto-derived when `AutoCircle` is used. When `AutoCircle` is set in the request, the response routing boundary will return `Circle` derived from the `AutoCircle` settings.
Type: [Circle](API_Circle.md) object
Required: No

 ** Polygon **   <a name="location-Type-RouteMatrixBoundaryGeometry-Polygon"></a>
Geometry defined as a polygon with only one linear ring. A linear ring is a closed sequence of four or more coordinates. The first and last coordinates are the same, forming a closed boundary. Each coordinate is a position in [longitude, latitude] format.
The structure is an array of linear rings (only 1 allowed). Each linear ring is an array of coordinates (minimum 4), and each coordinate is an array of two doubles [longitude, latitude].
Maximum distance between any two vertices must be less than or equal to 400,000 meters.
Type: Array of arrays of arrays of doubles
Array Members: Fixed number of 1 item.
Array Members: Minimum number of 4 items.
Array Members: Fixed number of 2 items.
Required: No

## See Also
<a name="API_RouteMatrixBoundaryGeometry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteMatrixBoundaryGeometry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteMatrixBoundaryGeometry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteMatrixBoundaryGeometry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
