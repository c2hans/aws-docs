---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteTaxiLegDetails.html
---

# RouteTaxiLegDetails
<a name="API_RouteTaxiLegDetails"></a>

Populated when the Leg type is Taxi, and provides additional information that is specific to taxi travel.

## Contents
<a name="API_RouteTaxiLegDetails_Contents"></a>

 ** AfterTravelSteps **   <a name="location-Type-RouteTaxiLegDetails-AfterTravelSteps"></a>
Steps of a leg that must be performed after the travel portion of the leg.
Type: Array of [RouteTaxiAfterTravelStep](API_RouteTaxiAfterTravelStep.md) objects
Required: Yes

 ** Agency **   <a name="location-Type-RouteTaxiLegDetails-Agency"></a>
Details about the taxi agency.
Type: [RouteTaxiAgency](API_RouteTaxiAgency.md) object
Required: Yes

 ** Arrival **   <a name="location-Type-RouteTaxiLegDetails-Arrival"></a>
Details corresponding to the arrival for the leg.
Type: [RouteTaxiArrival](API_RouteTaxiArrival.md) object
Required: Yes

 ** Attributions **   <a name="location-Type-RouteTaxiLegDetails-Attributions"></a>
List of required attributions to display.
Type: Array of [RouteAttribution](API_RouteAttribution.md) objects
Required: Yes

 ** BeforeTravelSteps **   <a name="location-Type-RouteTaxiLegDetails-BeforeTravelSteps"></a>
Steps of a leg that must be performed before the travel portion of the leg.
Type: Array of [RouteTaxiBeforeTravelStep](API_RouteTaxiBeforeTravelStep.md) objects
Required: Yes

 ** BookingWebLinks **   <a name="location-Type-RouteTaxiLegDetails-BookingWebLinks"></a>
Web links to external ticket booking services for the taxi.
Type: Array of [RouteWebLink](API_RouteWebLink.md) objects
Required: Yes

 ** Departure **   <a name="location-Type-RouteTaxiLegDetails-Departure"></a>
Details corresponding to the departure for the leg.
Type: [RouteTaxiDeparture](API_RouteTaxiDeparture.md) object
Required: Yes

 ** Notices **   <a name="location-Type-RouteTaxiLegDetails-Notices"></a>
List of notices that indicate issues that occurred during route calculation.
Type: Array of [RouteTaxiNotice](API_RouteTaxiNotice.md) objects
Required: Yes

 ** Transport **   <a name="location-Type-RouteTaxiLegDetails-Transport"></a>
Transport mode details for the taxi leg.
Type: [RouteTaxiTransportModeDetails](API_RouteTaxiTransportModeDetails.md) object
Required: Yes

 ** TravelSteps **   <a name="location-Type-RouteTaxiLegDetails-TravelSteps"></a>
Steps of a leg that must be performed during the travel portion of the leg.
Type: Array of [RouteTaxiTravelStep](API_RouteTaxiTravelStep.md) objects
Required: Yes

 ** Summary **   <a name="location-Type-RouteTaxiLegDetails-Summary"></a>
Summary of the taxi leg.
Type: [RouteTaxiSummary](API_RouteTaxiSummary.md) object
Required: No

## See Also
<a name="API_RouteTaxiLegDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteTaxiLegDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteTaxiLegDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteTaxiLegDetails)
