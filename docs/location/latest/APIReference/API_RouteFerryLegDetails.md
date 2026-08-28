---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteFerryLegDetails.html
---

# RouteFerryLegDetails
<a name="API_RouteFerryLegDetails"></a>

 FerryLegDetails is populated when the Leg type is Ferry, and provides additional information that is specific to ferry travel.

## Contents
<a name="API_RouteFerryLegDetails_Contents"></a>

 ** AfterTravelSteps **   <a name="location-Type-RouteFerryLegDetails-AfterTravelSteps"></a>
Steps of a leg that must be performed after the travel portion of the leg.
Type: Array of [RouteFerryAfterTravelStep](API_RouteFerryAfterTravelStep.md) objects
Required: Yes

 ** Arrival **   <a name="location-Type-RouteFerryLegDetails-Arrival"></a>
Details corresponding to the arrival for the leg.
Type: [RouteFerryArrival](API_RouteFerryArrival.md) object
Required: Yes

 ** BeforeTravelSteps **   <a name="location-Type-RouteFerryLegDetails-BeforeTravelSteps"></a>
Steps of a leg that must be performed before the travel portion of the leg.
Type: Array of [RouteFerryBeforeTravelStep](API_RouteFerryBeforeTravelStep.md) objects
Required: Yes

 ** Departure **   <a name="location-Type-RouteFerryLegDetails-Departure"></a>
Details corresponding to the departure for the leg.
Type: [RouteFerryDeparture](API_RouteFerryDeparture.md) object
Required: Yes

 ** Notices **   <a name="location-Type-RouteFerryLegDetails-Notices"></a>
Notices are additional information returned that indicate issues that occurred during route calculation.
Type: Array of [RouteFerryNotice](API_RouteFerryNotice.md) objects
Required: Yes

 ** PassThroughWaypoints **   <a name="location-Type-RouteFerryLegDetails-PassThroughWaypoints"></a>
Waypoints that were passed through during the leg. This includes the waypoints that were configured with the PassThrough option.
Type: Array of [RoutePassThroughWaypoint](API_RoutePassThroughWaypoint.md) objects
Required: Yes

 ** Spans **   <a name="location-Type-RouteFerryLegDetails-Spans"></a>
Spans that were computed for the requested SpanAdditionalFeatures.
Type: Array of [RouteFerrySpan](API_RouteFerrySpan.md) objects
Required: Yes

 ** TravelSteps **   <a name="location-Type-RouteFerryLegDetails-TravelSteps"></a>
Steps of a leg that must be performed before the travel portion of the leg.
Type: Array of [RouteFerryTravelStep](API_RouteFerryTravelStep.md) objects
Required: Yes

 ** RouteName **   <a name="location-Type-RouteFerryLegDetails-RouteName"></a>
Route name of the ferry line.
Type: String
Required: No

 ** Summary **   <a name="location-Type-RouteFerryLegDetails-Summary"></a>
Summarized details of the leg.
Type: [RouteFerrySummary](API_RouteFerrySummary.md) object
Required: No

## See Also
<a name="API_RouteFerryLegDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteFerryLegDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteFerryLegDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteFerryLegDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
