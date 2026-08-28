---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteTransitTransportModeDetails.html
---

# RouteTransitTransportModeDetails
<a name="API_RouteTransitTransportModeDetails"></a>

Transport mode details for the transit leg.

## Contents
<a name="API_RouteTransitTransportModeDetails_Contents"></a>

 ** Mode **   <a name="location-Type-RouteTransitTransportModeDetails-Mode"></a>
Mode of the transit transport.
Type: String
Valid Values: `AerialTramway | Airplane | All | Bus | BusRapidTransit | CityTrain | Ferry | FunicularRailway | HighSpeedTrain | IntercityTrain | InterregionalTrain | LightRail | Monorail | PrivateBus | RegionalTrain | Subway`
Required: Yes

 ** Accessibility **   <a name="location-Type-RouteTransitTransportModeDetails-Accessibility"></a>
Wheelchair accessibility information for the transit vehicle.
Type: [RouteAccessibilityAvailabilityDetails](API_RouteAccessibilityAvailabilityDetails.md) object
Required: No

 ** Color **   <a name="location-Type-RouteTransitTransportModeDetails-Color"></a>
Color of the transport polyline and background for the transport name.
Type: String
Pattern: `.*#[0-9A-Fa-f]{6}.*`
Required: No

 ** Headsign **   <a name="location-Type-RouteTransitTransportModeDetails-Headsign"></a>
Transit route headsign.
Type: String
Required: No

 ** LongRouteName **   <a name="location-Type-RouteTransitTransportModeDetails-LongRouteName"></a>
Long name of the transit route.
Type: String
Required: No

 ** RouteName **   <a name="location-Type-RouteTransitTransportModeDetails-RouteName"></a>
Transit route name.
Type: String
Required: No

 ** ShortRouteName **   <a name="location-Type-RouteTransitTransportModeDetails-ShortRouteName"></a>
Short name of the transit route.
Type: String
Required: No

 ** TextColor **   <a name="location-Type-RouteTransitTransportModeDetails-TextColor"></a>
Color of the transport name text.
Type: String
Pattern: `.*#[0-9A-Fa-f]{6}.*`
Required: No

## See Also
<a name="API_RouteTransitTransportModeDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteTransitTransportModeDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteTransitTransportModeDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteTransitTransportModeDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
