---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_PolylineCorridor.html
---

# PolylineCorridor
<a name="API_PolylineCorridor"></a>

Geometry defined as an encoded corridor - an encoded polyline with a radius that defines the width of the corridor.

## Contents
<a name="API_PolylineCorridor_Contents"></a>

 ** Polyline **   <a name="location-Type-PolylineCorridor-Polyline"></a>
An ordered list of positions used to plot a route on a map in a lossy compression format.
LineString and Polyline are mutually exclusive properties.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** Radius **   <a name="location-Type-PolylineCorridor-Radius"></a>
Considers all roads within the provided radius to match the provided destination to. The roads that are considered are determined by the provided Strategy.
 **Unit**: `meters`
Type: Integer
Required: Yes

## See Also
<a name="API_PolylineCorridor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/PolylineCorridor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/PolylineCorridor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/PolylineCorridor)
