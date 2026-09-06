---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_IsolineConnection.html
---

# IsolineConnection
<a name="API_IsolineConnection"></a>

Represents a segment of the transportation network that connects separate parts of a reachable area. These connections show how discontinuous areas are linked, such as by ferry routes or bridges crossing unroutable terrain.

## Contents
<a name="API_IsolineConnection_Contents"></a>

 ** FromPolygonIndex **   <a name="location-Type-IsolineConnection-FromPolygonIndex"></a>
The index of the starting polygon in the isoline's `Geometries` list.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** Geometry **   <a name="location-Type-IsolineConnection-Geometry"></a>
The shape of the connection, representing the actual path through the transportation network that links the polygons.
Type: [IsolineConnectionGeometry](API_IsolineConnectionGeometry.md) object
Required: Yes

 ** ToPolygonIndex **   <a name="location-Type-IsolineConnection-ToPolygonIndex"></a>
The index of the ending polygon in the isoline's `Geometries` list.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

## See Also
<a name="API_IsolineConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/IsolineConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/IsolineConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/IsolineConnection)
