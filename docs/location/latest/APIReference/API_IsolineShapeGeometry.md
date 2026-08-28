---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_IsolineShapeGeometry.html
---

# IsolineShapeGeometry
<a name="API_IsolineShapeGeometry"></a>

Represents the shape of a reachable area. The geometry can be provided either as coordinate pairs (`Polygon`) or in encoded format (`PolylinePolygon`), matching the format specified in the request.

## Contents
<a name="API_IsolineShapeGeometry_Contents"></a>

 ** Polygon **   <a name="location-Type-IsolineShapeGeometry-Polygon"></a>
A series of coordinate rings defining the reachable area when Simple geometry format is requested. Each ring is a list of `[longitude, latitude]` coordinate pairs. The first ring defines the outer boundary; subsequent rings define holes representing unreachable areas.
Polygon and PolylinePolygon are mutually exclusive properties.
Type: Array of arrays of arrays of doubles
Array Members: Minimum number of 1 item.
Array Members: Minimum number of 4 items.
Array Members: Fixed number of 2 items.
Required: No

 ** PolylinePolygon **   <a name="location-Type-IsolineShapeGeometry-PolylinePolygon"></a>
An encoded representation of the reachable area when FlexiblePolyline geometry format is requested. Provides a compact representation suitable for transmission and storage. The first string defines the outer boundary; subsequent strings define holes representing unreachable areas. For more information on polyline encoding, see [https://github.com/aws-geospatial/polyline](https://github.com/aws-geospatial/polyline).
Polygon and PolylinePolygon are mutually exclusive properties.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_IsolineShapeGeometry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/IsolineShapeGeometry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/IsolineShapeGeometry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/IsolineShapeGeometry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
