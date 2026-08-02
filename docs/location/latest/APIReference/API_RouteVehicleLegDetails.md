---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteVehicleLegDetails.html
---

# RouteVehicleLegDetails
<a name="API_RouteVehicleLegDetails"></a>

Steps of a leg that correspond to the travel portion of the leg.

## Contents
<a name="API_RouteVehicleLegDetails_Contents"></a>

 ** AfterTravelSteps **   <a name="location-Type-RouteVehicleLegDetails-AfterTravelSteps"></a>
Steps of a leg that must be performed after the travel portion of the leg.
Type: Array of [RouteVehicleAfterTravelStep](API_RouteVehicleAfterTravelStep.md) objects
Required: Yes

 ** Arrival **   <a name="location-Type-RouteVehicleLegDetails-Arrival"></a>
Details corresponding to the arrival for the leg.
Type: [RouteVehicleArrival](API_RouteVehicleArrival.md) object
Required: Yes

 ** Departure **   <a name="location-Type-RouteVehicleLegDetails-Departure"></a>
Details corresponding to the departure for the leg.
Type: [RouteVehicleDeparture](API_RouteVehicleDeparture.md) object
Required: Yes

 ** Incidents **   <a name="location-Type-RouteVehicleLegDetails-Incidents"></a>
 Incidents corresponding to this leg of the route. Not supported in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
Type: Array of [RouteVehicleIncident](API_RouteVehicleIncident.md) objects
Required: Yes

 ** Notices **   <a name="location-Type-RouteVehicleLegDetails-Notices"></a>
 Notices are additional information returned that indicate issues that occurred during route calculation. Not supported in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
Type: Array of [RouteVehicleNotice](API_RouteVehicleNotice.md) objects
Required: Yes

 ** PassThroughWaypoints **   <a name="location-Type-RouteVehicleLegDetails-PassThroughWaypoints"></a>
Waypoints that were passed through during the leg. This includes the waypoints that were configured with the PassThrough option.
Type: Array of [RoutePassThroughWaypoint](API_RoutePassThroughWaypoint.md) objects
Required: Yes

 ** Spans **   <a name="location-Type-RouteVehicleLegDetails-Spans"></a>
 Spans that were computed for the requested SpanAdditionalFeatures. Not supported in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
Type: Array of [RouteVehicleSpan](API_RouteVehicleSpan.md) objects
Required: Yes

 ** Tolls **   <a name="location-Type-RouteVehicleLegDetails-Tolls"></a>
 Toll related options. Not supported in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
Type: Array of [RouteToll](API_RouteToll.md) objects
Required: Yes

 ** TollSystems **   <a name="location-Type-RouteVehicleLegDetails-TollSystems"></a>
 Toll systems are authorities that collect payments for the toll. Not supported in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
Type: Array of [RouteTollSystem](API_RouteTollSystem.md) objects
Required: Yes

 ** TravelSteps **   <a name="location-Type-RouteVehicleLegDetails-TravelSteps"></a>
Steps of a leg that must be performed before the travel portion of the leg.
Type: Array of [RouteVehicleTravelStep](API_RouteVehicleTravelStep.md) objects
Required: Yes

 ** TruckRoadTypes **   <a name="location-Type-RouteVehicleLegDetails-TruckRoadTypes"></a>
 Truck road type identifiers. `BK1` through `BK4` apply only to Sweden. `A2,A4,B2,B4,C,D,ET2,ET4` apply only to Mexico. Not supported in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
There are currently no other supported values as of 26th April 2024.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 12 items.
Length Constraints: Minimum length of 1. Maximum length of 3.
Required: Yes

 ** Zones **   <a name="location-Type-RouteVehicleLegDetails-Zones"></a>
 Zones corresponding to this leg of the route. Not supported in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
Type: Array of [RouteZone](API_RouteZone.md) objects
Required: Yes

 ** Summary **   <a name="location-Type-RouteVehicleLegDetails-Summary"></a>
Summarized details of the leg.
Type: [RouteVehicleSummary](API_RouteVehicleSummary.md) object
Required: No

## See Also
<a name="API_RouteVehicleLegDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteVehicleLegDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteVehicleLegDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteVehicleLegDetails)
