---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_Route.html
---

# Route
<a name="API_Route"></a>

The route.

## Contents
<a name="API_Route_Contents"></a>

 ** Legs **   <a name="location-Type-Route-Legs"></a>
A leg is a section of a route from one waypoint to the next. A leg could be of type Vehicle, Pedestrian or Ferry. Legs of different types could occur together within a single route. For example, a car employing the use of a Ferry will contain Vehicle legs corresponding to journey on land, and Ferry legs corresponding to the journey via Ferry.
Type: Array of [RouteLeg](API_RouteLeg.md) objects
Required: Yes

 ** MajorRoadLabels **   <a name="location-Type-Route-MajorRoadLabels"></a>
Important labels including names and route numbers that differentiate the current route from the alternatives presented.
Type: Array of [RouteMajorRoadLabel](API_RouteMajorRoadLabel.md) objects
Array Members: Minimum number of 0 items. Maximum number of 2 items.
Required: Yes

 ** Summary **   <a name="location-Type-Route-Summary"></a>
Summarized details of the leg.
Type: [RouteSummary](API_RouteSummary.md) object
Required: No

## See Also
<a name="API_Route_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/Route)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/Route)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/Route)
