---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_Circle.html
---

# Circle
<a name="API_Circle"></a>

A circle on the earth, as defined by a center point and a radius.

## Contents
<a name="API_Circle_Contents"></a>

 ** Center **   <a name="location-Type-Circle-Center"></a>
A single point geometry, specifying the center of the circle, using [WGS 84](https://gisgeography.com/wgs84-world-geodetic-system/) coordinates, in the form `[longitude, latitude]`.
Type: Array of doubles
Array Members: Fixed number of 2 items.
Required: Yes

 ** Radius **   <a name="location-Type-Circle-Radius"></a>
The radius of the circle in meters. Must be greater than zero and no larger than 100,000 (100 kilometers).
Type: Double
Required: Yes

## See Also
<a name="API_Circle_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/Circle)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/Circle)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/Circle)
