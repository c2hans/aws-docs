---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteMatchingOptions.html
---

# RouteMatchingOptions
<a name="API_RouteMatchingOptions"></a>

Options related to route matching.

## Contents
<a name="API_RouteMatchingOptions_Contents"></a>

 ** NameHint **   <a name="location-Type-RouteMatchingOptions-NameHint"></a>
Attempts to match the provided position to a road similar to the provided name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Required: No

 ** OnRoadThreshold **   <a name="location-Type-RouteMatchingOptions-OnRoadThreshold"></a>
If the distance to a highway/bridge/tunnel/sliproad is within threshold, the waypoint will be snapped to the highway/bridge/tunnel/sliproad.
 **Unit**: `meters`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** Radius **   <a name="location-Type-RouteMatchingOptions-Radius"></a>
Considers all roads within the provided radius to match the provided destination to. The roads that are considered are determined by the provided Strategy.
 **Unit**: `meters`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** Strategy **   <a name="location-Type-RouteMatchingOptions-Strategy"></a>
Strategy that defines matching of the position onto the road network. MatchAny considers all roads possible, whereas MatchMostSignificantRoad matches to the most significant road.
Type: String
Valid Values: `MatchAny | MatchMostSignificantRoad`
Required: No

## See Also
<a name="API_RouteMatchingOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteMatchingOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteMatchingOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteMatchingOptions)
