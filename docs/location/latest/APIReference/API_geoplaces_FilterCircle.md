---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_FilterCircle.html
---

# FilterCircle
<a name="API_geoplaces_FilterCircle"></a>

The `Circle` that all results must be in.

## Contents
<a name="API_geoplaces_FilterCircle_Contents"></a>

 ** Center **   <a name="location-Type-geoplaces_FilterCircle-Center"></a>
The center position in World Geodetic System (WGS 84) format: [longitude, latitude].
Type: Array of doubles
Array Members: Fixed number of 2 items.
Required: Yes

 ** Radius **   <a name="location-Type-geoplaces_FilterCircle-Radius"></a>
 The radius, in meters, of the `FilterCircle`. If you use [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html), the `ap-southeast-1` and `ap-southeast-5` AWS Regions support only up to a maximum value of 300,000.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 21000000.
Required: Yes

## See Also
<a name="API_geoplaces_FilterCircle_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-places-2020-11-19/FilterCircle)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-places-2020-11-19/FilterCircle)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-places-2020-11-19/FilterCircle)
