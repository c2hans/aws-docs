---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_Corridor.html
---

# Corridor
<a name="API_Corridor"></a>

Geometry defined as a corridor - a LineString with a radius that defines the width of the corridor.

## Contents
<a name="API_Corridor_Contents"></a>

 ** LineString **   <a name="location-Type-Corridor-LineString"></a>
An ordered list of positions used to plot a route on a map.
LineString and Polyline are mutually exclusive properties.
Type: Array of arrays of doubles
Array Members: Minimum number of 2 items.
Array Members: Fixed number of 2 items.
Required: Yes

 ** Radius **   <a name="location-Type-Corridor-Radius"></a>
Radius that defines the width of the corridor.
Type: Integer
Required: Yes

## See Also
<a name="API_Corridor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/Corridor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/Corridor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/Corridor)
