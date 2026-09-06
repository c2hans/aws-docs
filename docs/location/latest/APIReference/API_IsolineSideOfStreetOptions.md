---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_IsolineSideOfStreetOptions.html
---

# IsolineSideOfStreetOptions
<a name="API_IsolineSideOfStreetOptions"></a>

Controls how points are matched to specific sides of streets. This is important when the side of the street matters for accessibility - for example, when building entrances or parking lot access points can only be reached from one side of a divided road.

## Contents
<a name="API_IsolineSideOfStreetOptions_Contents"></a>

 ** Position **   <a name="location-Type-IsolineSideOfStreetOptions-Position"></a>
The `[longitude, latitude]` coordinates of the point that should be matched to a specific side of the street.
Type: Array of doubles
Array Members: Fixed number of 2 items.
Required: Yes

 ** UseWith **   <a name="location-Type-IsolineSideOfStreetOptions-UseWith"></a>
Controls whether side-of-street matching is applied to any street (`AnyStreet`) or only to divided roads (`DividedStreetOnly`). This is important when the exact side of the street matters - for example, if a building entrance is only accessible from one side of a divided highway, or if a parking lot can only be entered from northbound lanes. Without correct side-of-street matching, travel time estimates may be inaccurate because they don't account for necessary U-turns or detours to reach the correct side.
Default value: `DividedStreetOnly`
Type: String
Valid Values: `AnyStreet | DividedStreetOnly`
Required: No

## See Also
<a name="API_IsolineSideOfStreetOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/IsolineSideOfStreetOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/IsolineSideOfStreetOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/IsolineSideOfStreetOptions)
