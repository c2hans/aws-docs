---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RoutePedestrianLegDetails.html
---

# RoutePedestrianLegDetails
<a name="API_RoutePedestrianLegDetails"></a>

Details that are specific to a pedestrian leg.

## Contents
<a name="API_RoutePedestrianLegDetails_Contents"></a>

 ** AfterTravelSteps **   <a name="location-Type-RoutePedestrianLegDetails-AfterTravelSteps"></a>
Steps of a leg that must be performed after the travel portion of the leg.
Type: Array of [RoutePedestrianAfterTravelStep](API_RoutePedestrianAfterTravelStep.md) objects
Required: Yes

 ** Arrival **   <a name="location-Type-RoutePedestrianLegDetails-Arrival"></a>
Details corresponding to the arrival for the leg.
Type: [RoutePedestrianArrival](API_RoutePedestrianArrival.md) object
Required: Yes

 ** Departure **   <a name="location-Type-RoutePedestrianLegDetails-Departure"></a>
Details corresponding to the departure for the leg.
Type: [RoutePedestrianDeparture](API_RoutePedestrianDeparture.md) object
Required: Yes

 ** Notices **   <a name="location-Type-RoutePedestrianLegDetails-Notices"></a>
 Notices are additional information returned that indicate issues that occurred during route calculation. Not supported in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
Type: Array of [RoutePedestrianNotice](API_RoutePedestrianNotice.md) objects
Required: Yes

 ** PassThroughWaypoints **   <a name="location-Type-RoutePedestrianLegDetails-PassThroughWaypoints"></a>
Waypoints that were passed through during the leg. This includes the waypoints that were configured with the PassThrough option.
Type: Array of [RoutePassThroughWaypoint](API_RoutePassThroughWaypoint.md) objects
Required: Yes

 ** Spans **   <a name="location-Type-RoutePedestrianLegDetails-Spans"></a>
 Spans that were computed for the requested SpanAdditionalFeatures. Not supported in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
Type: Array of [RoutePedestrianSpan](API_RoutePedestrianSpan.md) objects
Required: Yes

 ** TravelSteps **   <a name="location-Type-RoutePedestrianLegDetails-TravelSteps"></a>
Steps of a leg that must be performed before the travel portion of the leg.
Type: Array of [RoutePedestrianTravelStep](API_RoutePedestrianTravelStep.md) objects
Required: Yes

 ** Summary **   <a name="location-Type-RoutePedestrianLegDetails-Summary"></a>
Summarized details of the leg.
Type: [RoutePedestrianSummary](API_RoutePedestrianSummary.md) object
Required: No

## See Also
<a name="API_RoutePedestrianLegDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RoutePedestrianLegDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RoutePedestrianLegDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RoutePedestrianLegDetails)
