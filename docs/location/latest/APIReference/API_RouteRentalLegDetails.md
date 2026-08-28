---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteRentalLegDetails.html
---

# RouteRentalLegDetails
<a name="API_RouteRentalLegDetails"></a>

Populated when the Leg type is Rental, and provides additional information that is specific to rental vehicle travel.

## Contents
<a name="API_RouteRentalLegDetails_Contents"></a>

 ** AfterTravelSteps **   <a name="location-Type-RouteRentalLegDetails-AfterTravelSteps"></a>
Steps of a leg that must be performed after the travel portion of the leg.
Type: Array of [RouteRentalAfterTravelStep](API_RouteRentalAfterTravelStep.md) objects
Required: Yes

 ** Agency **   <a name="location-Type-RouteRentalLegDetails-Agency"></a>
Details about the rental agency.
Type: [RouteRentalAgency](API_RouteRentalAgency.md) object
Required: Yes

 ** Arrival **   <a name="location-Type-RouteRentalLegDetails-Arrival"></a>
Details corresponding to the arrival for the leg.
Type: [RouteRentalArrival](API_RouteRentalArrival.md) object
Required: Yes

 ** Attributions **   <a name="location-Type-RouteRentalLegDetails-Attributions"></a>
List of required attributions to display.
Type: Array of [RouteAttribution](API_RouteAttribution.md) objects
Required: Yes

 ** BeforeTravelSteps **   <a name="location-Type-RouteRentalLegDetails-BeforeTravelSteps"></a>
Steps of a leg that must be performed before the travel portion of the leg.
Type: Array of [RouteRentalBeforeTravelStep](API_RouteRentalBeforeTravelStep.md) objects
Required: Yes

 ** BookingWebLinks **   <a name="location-Type-RouteRentalLegDetails-BookingWebLinks"></a>
Web links to external ticket booking services for the rental.
Type: Array of [RouteWebLink](API_RouteWebLink.md) objects
Required: Yes

 ** Departure **   <a name="location-Type-RouteRentalLegDetails-Departure"></a>
Details corresponding to the departure for the leg.
Type: [RouteRentalDeparture](API_RouteRentalDeparture.md) object
Required: Yes

 ** Transport **   <a name="location-Type-RouteRentalLegDetails-Transport"></a>
Transport mode details for the rental leg.
Type: [RouteRentalTransportModeDetails](API_RouteRentalTransportModeDetails.md) object
Required: Yes

 ** TravelSteps **   <a name="location-Type-RouteRentalLegDetails-TravelSteps"></a>
Steps of a leg that must be performed during the travel portion of the leg.
Type: Array of [RouteRentalTravelStep](API_RouteRentalTravelStep.md) objects
Required: Yes

 ** Summary **   <a name="location-Type-RouteRentalLegDetails-Summary"></a>
Summary of the rental leg.
Type: [RouteRentalSummary](API_RouteRentalSummary.md) object
Required: No

## See Also
<a name="API_RouteRentalLegDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteRentalLegDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteRentalLegDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteRentalLegDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
