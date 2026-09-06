---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteMatrixBoundary.html
---

# RouteMatrixBoundary
<a name="API_RouteMatrixBoundary"></a>

Boundary within which the matrix is to be calculated. All data, origins and destinations outside the boundary are considered invalid.

## Contents
<a name="API_RouteMatrixBoundary_Contents"></a>

 ** Geometry **   <a name="location-Type-RouteMatrixBoundary-Geometry"></a>
Geometry of the area to be avoided.
Type: [RouteMatrixBoundaryGeometry](API_RouteMatrixBoundaryGeometry.md) object
Required: No

 ** Unbounded **   <a name="location-Type-RouteMatrixBoundary-Unbounded"></a>
No restrictions in terms of a routing boundary, and is typically used for longer routes.
Type: Boolean
Required: No

## See Also
<a name="API_RouteMatrixBoundary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteMatrixBoundary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteMatrixBoundary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteMatrixBoundary)
