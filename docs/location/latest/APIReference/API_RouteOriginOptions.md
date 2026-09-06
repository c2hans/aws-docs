---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteOriginOptions.html
---

# RouteOriginOptions
<a name="API_RouteOriginOptions"></a>

Origin related options.

## Contents
<a name="API_RouteOriginOptions_Contents"></a>

 ** AvoidActionsForDistance **   <a name="location-Type-RouteOriginOptions-AvoidActionsForDistance"></a>
Avoids actions for the provided distance. This is typically to consider for users in moving vehicles who may not have sufficient time to make an action at an origin or a destination.
Type: Long
Valid Range: Maximum value of 2000.
Required: No

 ** AvoidUTurns **   <a name="location-Type-RouteOriginOptions-AvoidUTurns"></a>
Avoid U-turns for calculation on highways and motorways.
Type: Boolean
Required: No

 ** Heading **   <a name="location-Type-RouteOriginOptions-Heading"></a>
GPS Heading at the position.
Type: Double
Valid Range: Minimum value of 0.0. Maximum value of 360.0.
Required: No

 ** Matching **   <a name="location-Type-RouteOriginOptions-Matching"></a>
Options to configure matching the provided position to the road network.
Type: [RouteMatchingOptions](API_RouteMatchingOptions.md) object
Required: No

 ** SideOfStreet **   <a name="location-Type-RouteOriginOptions-SideOfStreet"></a>
Options to configure matching the provided position to a side of the street.
Type: [RouteSideOfStreetOptions](API_RouteSideOfStreetOptions.md) object
Required: No

## See Also
<a name="API_RouteOriginOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteOriginOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteOriginOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteOriginOptions)
