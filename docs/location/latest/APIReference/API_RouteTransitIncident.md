---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteTransitIncident.html
---

# RouteTransitIncident
<a name="API_RouteTransitIncident"></a>

An incident describes disruptions on the transit route.

## Contents
<a name="API_RouteTransitIncident_Contents"></a>

 ** Effect **   <a name="location-Type-RouteTransitIncident-Effect"></a>
The effect of the incident on the transit service.
Type: String
Valid Values: `Delayed | Detoured | Other | ServiceAdded | ServiceCancelled | ServiceModified | ServiceReduced | StopMoved`
Required: Yes

 ** Type **   <a name="location-Type-RouteTransitIncident-Type"></a>
Type of the incident.
Type: String
Valid Values: `Accident | Construction | Demonstration | Holiday | Maintenance | MedicalEmergency | Other | PoliceActivity | Strike | TechnicalProblem | Weather`
Required: Yes

 ** Description **   <a name="location-Type-RouteTransitIncident-Description"></a>
A human readable description of the incident.
Type: String
Required: No

 ** EndTime **   <a name="location-Type-RouteTransitIncident-EndTime"></a>
The end time of the incident.
Type: String
Pattern: `([1-2][0-9]{3})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9]|60)(\.[0-9]{0,9})?(Z|[+-]([01][0-9]|2[0-3]):[0-5][0-9])`
Required: No

 ** StartTime **   <a name="location-Type-RouteTransitIncident-StartTime"></a>
The start time of the incident.
Type: String
Pattern: `([1-2][0-9]{3})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9]|60)(\.[0-9]{0,9})?(Z|[+-]([01][0-9]|2[0-3]):[0-5][0-9])`
Required: No

 ** Url **   <a name="location-Type-RouteTransitIncident-Url"></a>
URL to the original incident published at the agency website.
Type: String
Required: No

## See Also
<a name="API_RouteTransitIncident_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteTransitIncident)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteTransitIncident)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteTransitIncident)
