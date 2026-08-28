---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_IsolineAvoidanceAreaGeometry.html
---

# IsolineAvoidanceAreaGeometry
<a name="API_IsolineAvoidanceAreaGeometry"></a>

Defines an area to avoid during calculations using one of several supported geometry types. The service will prefer routes that avoid these areas when possible.

## Contents
<a name="API_IsolineAvoidanceAreaGeometry_Contents"></a>

 ** BoundingBox **   <a name="location-Type-IsolineAvoidanceAreaGeometry-BoundingBox"></a>
A rectangular area defined by its southwest and northeast corners: `[min longitude, min latitude, max longitude, max latitude]`.
Type: Array of doubles
Array Members: Fixed number of 4 items.
Required: No

 ** Corridor **   <a name="location-Type-IsolineAvoidanceAreaGeometry-Corridor"></a>
A buffer zone around a line, defined by a series of coordinates and a radius in meters.
Type: [Corridor](API_Corridor.md) object
Required: No

 ** Polygon **   <a name="location-Type-IsolineAvoidanceAreaGeometry-Polygon"></a>
A polygon defined by a list of coordinate rings. The first ring defines the outer boundary; subsequent rings will be ignored.
Type: Array of arrays of arrays of doubles
Array Members: Fixed number of 1 item.
Array Members: Minimum number of 4 items.
Array Members: Fixed number of 2 items.
Required: No

 ** PolylineCorridor **   <a name="location-Type-IsolineAvoidanceAreaGeometry-PolylineCorridor"></a>
A buffer zone around a compressed polyline, defined by an encoded polyline string and a radius in meters. For more information on polyline encoding, see [https://github.com/aws-geospatial/polyline](https://github.com/aws-geospatial/polyline).
Type: [PolylineCorridor](API_PolylineCorridor.md) object
Required: No

 ** PolylinePolygon **   <a name="location-Type-IsolineAvoidanceAreaGeometry-PolylinePolygon"></a>
A polygon defined by encoded polyline strings. The first string defines the outer boundary; subsequent strings will be ignored. For more information on polyline encoding, see [https://github.com/aws-geospatial/polyline](https://github.com/aws-geospatial/polyline).
Type: Array of strings
Array Members: Fixed number of 1 item.
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_IsolineAvoidanceAreaGeometry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/IsolineAvoidanceAreaGeometry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/IsolineAvoidanceAreaGeometry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/IsolineAvoidanceAreaGeometry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
