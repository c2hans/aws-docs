---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteRoad.html
---

# RouteRoad
<a name="API_RouteRoad"></a>

The road on the route.

## Contents
<a name="API_RouteRoad_Contents"></a>

 ** RoadName **   <a name="location-Type-RouteRoad-RoadName"></a>
Name of the road (localized).
Type: Array of [LocalizedString](API_LocalizedString.md) objects
Required: Yes

 ** RouteNumber **   <a name="location-Type-RouteRoad-RouteNumber"></a>
Route number of the road.
Type: Array of [RouteNumber](API_RouteNumber.md) objects
Required: Yes

 ** Towards **   <a name="location-Type-RouteRoad-Towards"></a>
Names of destinations that can be reached when traveling on the road.
Type: Array of [LocalizedString](API_LocalizedString.md) objects
Required: Yes

 ** Type **   <a name="location-Type-RouteRoad-Type"></a>
The type of road.
Type: String
Valid Values: `Highway | Rural | Urban`
Required: No

## See Also
<a name="API_RouteRoad_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteRoad)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteRoad)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteRoad)
