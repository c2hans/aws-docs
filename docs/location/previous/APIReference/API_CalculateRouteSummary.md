---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_CalculateRouteSummary.html
---

# CalculateRouteSummary
<a name="API_CalculateRouteSummary"></a>

A summary of the calculated route.

## Contents
<a name="API_CalculateRouteSummary_Contents"></a>

 ** DataSource **   <a name="location-Type-CalculateRouteSummary-DataSource"></a>
The data provider of traffic and road network data used to calculate the route. Indicates one of the available providers:
+  `Esri`
+  `Grab`
+  `Here`
For more information about data providers, see [Amazon Location Service data providers](https://docs.aws.amazon.com/location/previous/developerguide/what-is-data-provider.html).
Type: String
Required: Yes

 ** Distance **   <a name="location-Type-CalculateRouteSummary-Distance"></a>
The total distance covered by the route. The sum of the distance travelled between every stop on the route.
If Esri is the data source for the route calculator, the route distance can’t be greater than 400 km. If the route exceeds 400 km, the response is a `400 RoutesValidationException` error.
Type: Double
Valid Range: Minimum value of 0.
Required: Yes

 ** DistanceUnit **   <a name="location-Type-CalculateRouteSummary-DistanceUnit"></a>
The unit of measurement for route distances.
Type: String
Valid Values: `Kilometers | Miles`
Required: Yes

 ** DurationSeconds **   <a name="location-Type-CalculateRouteSummary-DurationSeconds"></a>
The total travel time for the route measured in seconds. The sum of the travel time between every stop on the route.
Type: Double
Valid Range: Minimum value of 0.
Required: Yes

 ** RouteBBox **   <a name="location-Type-CalculateRouteSummary-RouteBBox"></a>
Specifies a geographical box surrounding a route. Used to zoom into a route when displaying it in a map. For example, `[min x, min y, max x, max y]`.
The first 2 `bbox` parameters describe the lower southwest corner:
+ The first `bbox` position is the X coordinate or longitude of the lower southwest corner.
+ The second `bbox` position is the Y coordinate or latitude of the lower southwest corner.
The next 2 `bbox` parameters describe the upper northeast corner:
+ The third `bbox` position is the X coordinate, or longitude of the upper northeast corner.
+ The fourth `bbox` position is the Y coordinate, or latitude of the upper northeast corner.
Type: Array of doubles
Array Members: Fixed number of 4 items.
Required: Yes

## See Also
<a name="API_CalculateRouteSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/CalculateRouteSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/CalculateRouteSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/CalculateRouteSummary)
