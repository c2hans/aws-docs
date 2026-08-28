---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteVehicleIncident.html
---

# RouteVehicleIncident
<a name="API_RouteVehicleIncident"></a>

Incidents corresponding to this leg of the route.

## Contents
<a name="API_RouteVehicleIncident_Contents"></a>

 ** Description **   <a name="location-Type-RouteVehicleIncident-Description"></a>
Brief readable description of the incident.
Type: String
Required: No

 ** EndTime **   <a name="location-Type-RouteVehicleIncident-EndTime"></a>
End timestamp of the incident.
Type: String
Pattern: `([1-2][0-9]{3})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9]|60)(\.[0-9]{0,9})?(Z|[+-]([01][0-9]|2[0-3]):[0-5][0-9])`
Required: No

 ** Severity **   <a name="location-Type-RouteVehicleIncident-Severity"></a>
Severity of the incident Critical - The part of the route the incident affects is unusable. Major- Major impact on the leg duration, for example stop and go Minor- Minor impact on the leg duration, for example traffic jam Low - Low on duration, for example slightly increased traffic
Type: String
Valid Values: `Critical | High | Medium | Low`
Required: No

 ** StartTime **   <a name="location-Type-RouteVehicleIncident-StartTime"></a>
Start time of the incident.
Type: String
Pattern: `([1-2][0-9]{3})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9]|60)(\.[0-9]{0,9})?(Z|[+-]([01][0-9]|2[0-3]):[0-5][0-9])`
Required: No

 ** Type **   <a name="location-Type-RouteVehicleIncident-Type"></a>
Type of the incident.
Type: String
Valid Values: `Accident | Congestion | Construction | DisabledVehicle | LaneRestriction | MassTransit | Other | PlannedEvent | RoadClosure | RoadHazard | Weather`
Required: No

## See Also
<a name="API_RouteVehicleIncident_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteVehicleIncident)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteVehicleIncident)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteVehicleIncident)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
