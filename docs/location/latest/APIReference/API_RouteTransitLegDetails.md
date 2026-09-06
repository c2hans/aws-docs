---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteTransitLegDetails.html
---

# RouteTransitLegDetails
<a name="API_RouteTransitLegDetails"></a>

Populated when the Leg type is Transit, and provides additional information that is specific to public transit travel.

## Contents
<a name="API_RouteTransitLegDetails_Contents"></a>

 ** AfterTravelSteps **   <a name="location-Type-RouteTransitLegDetails-AfterTravelSteps"></a>
Steps of a leg that must be performed after the travel portion of the leg.
Type: Array of [RouteTransitAfterTravelStep](API_RouteTransitAfterTravelStep.md) objects
Required: Yes

 ** Arrival **   <a name="location-Type-RouteTransitLegDetails-Arrival"></a>
Details corresponding to the arrival for the leg.
Type: [RouteTransitArrival](API_RouteTransitArrival.md) object
Required: Yes

 ** Attributions **   <a name="location-Type-RouteTransitLegDetails-Attributions"></a>
List of required attributions to display.
Type: Array of [RouteAttribution](API_RouteAttribution.md) objects
Required: Yes

 ** BeforeTravelSteps **   <a name="location-Type-RouteTransitLegDetails-BeforeTravelSteps"></a>
Steps of a leg that must be performed before the travel portion of the leg.
Type: Array of [RouteTransitBeforeTravelStep](API_RouteTransitBeforeTravelStep.md) objects
Required: Yes

 ** BookingWebLinks **   <a name="location-Type-RouteTransitLegDetails-BookingWebLinks"></a>
Web links to external ticket booking services for the transit.
Type: Array of [RouteWebLink](API_RouteWebLink.md) objects
Required: Yes

 ** Departure **   <a name="location-Type-RouteTransitLegDetails-Departure"></a>
Details corresponding to the departure for the leg.
Type: [RouteTransitDeparture](API_RouteTransitDeparture.md) object
Required: Yes

 ** Incidents **   <a name="location-Type-RouteTransitLegDetails-Incidents"></a>
Incidents affecting this leg of the transit route.
Type: Array of [RouteTransitIncident](API_RouteTransitIncident.md) objects
Required: Yes

 ** IntermediateStops **   <a name="location-Type-RouteTransitLegDetails-IntermediateStops"></a>
Intermediate stops between departure and destination of the transit route.
Type: Array of [RouteTransitIntermediateStop](API_RouteTransitIntermediateStop.md) objects
Required: Yes

 ** NextDepartures **   <a name="location-Type-RouteTransitLegDetails-NextDepartures"></a>
List of next departures that cover the same section of the route.
Type: Array of [RouteTransitNextDeparture](API_RouteTransitNextDeparture.md) objects
Required: Yes

 ** Notices **   <a name="location-Type-RouteTransitLegDetails-Notices"></a>
List of notices that indicate issues that occurred during route calculation.
Type: Array of [RouteTransitNotice](API_RouteTransitNotice.md) objects
Required: Yes

 ** PassThroughWaypoints **   <a name="location-Type-RouteTransitLegDetails-PassThroughWaypoints"></a>
Waypoints that were passed through during the leg. This includes the waypoints that were configured with the PassThrough option. Not populated when the TravelMode is `Transit` or `Intermodal`.
Type: Array of [RoutePassThroughWaypoint](API_RoutePassThroughWaypoint.md) objects
Required: Yes

 ** Spans **   <a name="location-Type-RouteTransitLegDetails-Spans"></a>
Spans that were computed for the requested SpanAdditionalFeatures. Not populated when the TravelMode is `Transit` or `Intermodal`.
Type: Array of [RouteTransitSpan](API_RouteTransitSpan.md) objects
Required: Yes

 ** Transport **   <a name="location-Type-RouteTransitLegDetails-Transport"></a>
Transport mode details for the transit leg.
Type: [RouteTransitTransportModeDetails](API_RouteTransitTransportModeDetails.md) object
Required: Yes

 ** TravelSteps **   <a name="location-Type-RouteTransitLegDetails-TravelSteps"></a>
Steps of a leg that must be performed during the travel portion of the leg.
Type: Array of [RouteTransitTravelStep](API_RouteTransitTravelStep.md) objects
Required: Yes

 ** Agency **   <a name="location-Type-RouteTransitLegDetails-Agency"></a>
Details about the transit agency.
Type: [RouteTransitAgency](API_RouteTransitAgency.md) object
Required: No

 ** Summary **   <a name="location-Type-RouteTransitLegDetails-Summary"></a>
Summary of the transit leg.
Type: [RouteTransitSummary](API_RouteTransitSummary.md) object
Required: No

## See Also
<a name="API_RouteTransitLegDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteTransitLegDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteTransitLegDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteTransitLegDetails)
