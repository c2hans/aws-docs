---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteMatrixAvoidanceOptions.html
---

# RouteMatrixAvoidanceOptions
<a name="API_RouteMatrixAvoidanceOptions"></a>

Specifies options for areas to avoid when calculating the route. This is a best-effort avoidance setting, meaning the router will try to honor the avoidance preferences but may still include restricted areas if no feasible alternative route exists. If avoidance options are not followed, the response will indicate that the avoidance criteria were violated.

## Contents
<a name="API_RouteMatrixAvoidanceOptions_Contents"></a>

 ** Areas **   <a name="location-Type-RouteMatrixAvoidanceOptions-Areas"></a>
Areas to be avoided.
Type: Array of [RouteMatrixAvoidanceArea](API_RouteMatrixAvoidanceArea.md) objects
Array Members: Minimum number of 0 items. Maximum number of 250 items.
Required: No

 ** CarShuttleTrains **   <a name="location-Type-RouteMatrixAvoidanceOptions-CarShuttleTrains"></a>
Avoid car-shuttle-trains while calculating the route.
Type: Boolean
Required: No

 ** ControlledAccessHighways **   <a name="location-Type-RouteMatrixAvoidanceOptions-ControlledAccessHighways"></a>
Avoid controlled access highways while calculating the route.
Type: Boolean
Required: No

 ** DirtRoads **   <a name="location-Type-RouteMatrixAvoidanceOptions-DirtRoads"></a>
Avoid dirt roads while calculating the route.
Type: Boolean
Required: No

 ** Ferries **   <a name="location-Type-RouteMatrixAvoidanceOptions-Ferries"></a>
Avoid ferries while calculating the route.
Type: Boolean
Required: No

 ** TollRoads **   <a name="location-Type-RouteMatrixAvoidanceOptions-TollRoads"></a>
Avoids roads where the specified toll transponders are the only mode of payment.
Type: Boolean
Required: No

 ** TollTransponders **   <a name="location-Type-RouteMatrixAvoidanceOptions-TollTransponders"></a>
Avoids roads where the specified toll transponders are the only mode of payment.
Type: Boolean
Required: No

 ** TruckRoadTypes **   <a name="location-Type-RouteMatrixAvoidanceOptions-TruckRoadTypes"></a>
Truck road type identifiers. `BK1` through `BK4` apply only to Sweden. `A2,A4,B2,B4,C,D,ET2,ET4` apply only to Mexico.
There are currently no other supported values as of 26th April 2024.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 12 items.
Length Constraints: Minimum length of 1. Maximum length of 3.
Required: No

 ** Tunnels **   <a name="location-Type-RouteMatrixAvoidanceOptions-Tunnels"></a>
Avoid tunnels while calculating the route.
Type: Boolean
Required: No

 ** UTurns **   <a name="location-Type-RouteMatrixAvoidanceOptions-UTurns"></a>
Avoid U-turns for calculation on highways and motorways.
Type: Boolean
Required: No

 ** ZoneCategories **   <a name="location-Type-RouteMatrixAvoidanceOptions-ZoneCategories"></a>
Zone categories to be avoided.
Type: Array of [RouteMatrixAvoidanceZoneCategory](API_RouteMatrixAvoidanceZoneCategory.md) objects
Array Members: Minimum number of 0 items. Maximum number of 3 items.
Required: No

## See Also
<a name="API_RouteMatrixAvoidanceOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteMatrixAvoidanceOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteMatrixAvoidanceOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteMatrixAvoidanceOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
