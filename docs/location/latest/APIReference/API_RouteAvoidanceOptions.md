---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteAvoidanceOptions.html
---

# RouteAvoidanceOptions
<a name="API_RouteAvoidanceOptions"></a>

Specifies options for areas to avoid when calculating the route. This is a best-effort avoidance setting, meaning the router will try to honor the avoidance preferences but may still include restricted areas if no feasible alternative route exists. If avoidance options are not followed, the response will indicate that the avoidance criteria were violated.

## Contents
<a name="API_RouteAvoidanceOptions_Contents"></a>

 ** Areas **   <a name="location-Type-RouteAvoidanceOptions-Areas"></a>
 Areas to be avoided. Not supported in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
Type: Array of [RouteAvoidanceArea](API_RouteAvoidanceArea.md) objects
Required: No

 ** CarShuttleTrains **   <a name="location-Type-RouteAvoidanceOptions-CarShuttleTrains"></a>
 Avoid car-shuttle-trains while calculating the route. Not supported in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
Type: Boolean
Required: No

 ** ControlledAccessHighways **   <a name="location-Type-RouteAvoidanceOptions-ControlledAccessHighways"></a>
Avoid controlled access highways while calculating the route.
Type: Boolean
Required: No

 ** DirtRoads **   <a name="location-Type-RouteAvoidanceOptions-DirtRoads"></a>
 Avoid dirt roads while calculating the route. Not supported in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
Type: Boolean
Required: No

 ** Ferries **   <a name="location-Type-RouteAvoidanceOptions-Ferries"></a>
Avoid ferries while calculating the route.
Type: Boolean
Required: No

 ** SeasonalClosure **   <a name="location-Type-RouteAvoidanceOptions-SeasonalClosure"></a>
 Avoid roads that have seasonal closure while calculating the route. Not supported in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
Type: Boolean
Required: No

 ** TollRoads **   <a name="location-Type-RouteAvoidanceOptions-TollRoads"></a>
Avoids roads where the specified toll transponders are the only mode of payment.
Type: Boolean
Required: No

 ** TollTransponders **   <a name="location-Type-RouteAvoidanceOptions-TollTransponders"></a>
 Avoids roads where the specified toll transponders are the only mode of payment. Not supported in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
Type: Boolean
Required: No

 ** TruckRoadTypes **   <a name="location-Type-RouteAvoidanceOptions-TruckRoadTypes"></a>
 Truck road type identifiers. `BK1` through `BK4` apply only to Sweden. `A2,A4,B2,B4,C,D,ET2,ET4` apply only to Mexico. Not supported in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
There are currently no other supported values as of 26th April 2024.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 12 items.
Length Constraints: Minimum length of 1. Maximum length of 3.
Required: No

 ** Tunnels **   <a name="location-Type-RouteAvoidanceOptions-Tunnels"></a>
 Avoid tunnels while calculating the route. Not supported in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
Type: Boolean
Required: No

 ** UTurns **   <a name="location-Type-RouteAvoidanceOptions-UTurns"></a>
 Avoid U-turns for calculation on highways and motorways. Not supported in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
Type: Boolean
Required: No

 ** ZoneCategories **   <a name="location-Type-RouteAvoidanceOptions-ZoneCategories"></a>
 Zone categories to be avoided. Not supported in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
Type: Array of [RouteAvoidanceZoneCategory](API_RouteAvoidanceZoneCategory.md) objects
Array Members: Minimum number of 0 items. Maximum number of 3 items.
Required: No

## See Also
<a name="API_RouteAvoidanceOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteAvoidanceOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteAvoidanceOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteAvoidanceOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
