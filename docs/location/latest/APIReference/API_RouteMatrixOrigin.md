---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteMatrixOrigin.html
---

# RouteMatrixOrigin
<a name="API_RouteMatrixOrigin"></a>

The start position for the route in World Geodetic System (WGS 84) format: [longitude, latitude].

## Contents
<a name="API_RouteMatrixOrigin_Contents"></a>

 ** Position **   <a name="location-Type-RouteMatrixOrigin-Position"></a>
Position in World Geodetic System (WGS 84) format: [longitude, latitude].
Type: Array of doubles
Array Members: Fixed number of 2 items.
Required: Yes

 ** Options **   <a name="location-Type-RouteMatrixOrigin-Options"></a>
 Origin related options. Not supported in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
Type: [RouteMatrixOriginOptions](API_RouteMatrixOriginOptions.md) object
Required: No

## See Also
<a name="API_RouteMatrixOrigin_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteMatrixOrigin)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteMatrixOrigin)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteMatrixOrigin)
