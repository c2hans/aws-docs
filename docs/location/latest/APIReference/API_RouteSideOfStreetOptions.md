---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteSideOfStreetOptions.html
---

# RouteSideOfStreetOptions
<a name="API_RouteSideOfStreetOptions"></a>

Options to configure matching the provided position to a side of the street.

## Contents
<a name="API_RouteSideOfStreetOptions_Contents"></a>

 ** Position **   <a name="location-Type-RouteSideOfStreetOptions-Position"></a>
Position in World Geodetic System (WGS 84) format: [longitude, latitude].
Type: Array of doubles
Array Members: Fixed number of 2 items.
Required: Yes

 ** UseWith **   <a name="location-Type-RouteSideOfStreetOptions-UseWith"></a>
Strategy that defines when the side of street position should be used.
Default value: `DividedStreetOnly`
Type: String
Valid Values: `AnyStreet | DividedStreetOnly`
Required: No

## See Also
<a name="API_RouteSideOfStreetOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteSideOfStreetOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteSideOfStreetOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteSideOfStreetOptions)
