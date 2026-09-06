---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_IsolineDestinationOptions.html
---

# IsolineDestinationOptions
<a name="API_IsolineDestinationOptions"></a>

Options that control how the destination point is interpreted and matched to the road network when calculating reachable areas. This affects which roads are considered accessible near the destination and how the final approach is calculated.

## Contents
<a name="API_IsolineDestinationOptions_Contents"></a>

 ** AvoidActionsForDistance **   <a name="location-Type-IsolineDestinationOptions-AvoidActionsForDistance"></a>
The distance in meters from the destination point within which certain routing actions (such as U-turns or left turns across traffic) are restricted. This helps generate more practical routes by avoiding potentially dangerous maneuvers near the endpoint.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** Heading **   <a name="location-Type-IsolineDestinationOptions-Heading"></a>
The initial direction of travel in degrees (0-360, where 0 is north). This can affect which road segments are considered accessible from the starting point.
Type: Double
Valid Range: Minimum value of 0.0. Maximum value of 360.0.
Required: No

 ** Matching **   <a name="location-Type-IsolineDestinationOptions-Matching"></a>
Controls how the destination point is matched to the road network, including search radius and name-based matching preferences.
Type: [IsolineMatchingOptions](API_IsolineMatchingOptions.md) object
Required: No

 ** SideOfStreet **   <a name="location-Type-IsolineDestinationOptions-SideOfStreet"></a>
Specifies which side of the street should be considered accessible, which is important when building entrances or parking access points are only reachable from one side of the road.
Type: [IsolineSideOfStreetOptions](API_IsolineSideOfStreetOptions.md) object
Required: No

## See Also
<a name="API_IsolineDestinationOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/IsolineDestinationOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/IsolineDestinationOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/IsolineDestinationOptions)
