---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_IsolineConnectionGeometry.html
---

# IsolineConnectionGeometry
<a name="API_IsolineConnectionGeometry"></a>

Represents the geometry of connections between non-contiguous parts of an isoline. These connections can be provided in either coordinate pairs (LineString) or encoded (Polyline) format, matching the format specified in the request.

## Contents
<a name="API_IsolineConnectionGeometry_Contents"></a>

 ** LineString **   <a name="location-Type-IsolineConnectionGeometry-LineString"></a>
A series of `[longitude, latitude]` coordinate pairs defining the connection path when `Simple` geometry format is requested. These coordinates can be directly used as the coordinates array in a GeoJSON LineString without transformation.
LineString and Polyline are mutually exclusive properties.
Type: Array of arrays of doubles
Array Members: Minimum number of 2 items.
Array Members: Fixed number of 2 items.
Required: No

 ** Polyline **   <a name="location-Type-IsolineConnectionGeometry-Polyline"></a>
An encoded representation of the connection path when `FlexiblePolyline` geometry format is requested. This provides a more compact representation suitable for transmission and storage. To convert to GeoJSON, first decode to obtain coordinate pairs, then use those coordinates as the coordinates array in a GeoJSON LineString.
LineString and Polyline are mutually exclusive properties.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_IsolineConnectionGeometry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/IsolineConnectionGeometry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/IsolineConnectionGeometry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/IsolineConnectionGeometry)
