---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointOptimizationAvoidanceOptions.html
---

# WaypointOptimizationAvoidanceOptions
<a name="API_WaypointOptimizationAvoidanceOptions"></a>

Specifies options for areas to avoid. This is a best-effort avoidance setting, meaning the router will try to honor the avoidance preferences but may still include restricted areas if no feasible alternative route exists. If avoidance options are not followed, the response will indicate that the avoidance criteria were violated.

## Contents
<a name="API_WaypointOptimizationAvoidanceOptions_Contents"></a>

 ** Areas **   <a name="location-Type-WaypointOptimizationAvoidanceOptions-Areas"></a>
Areas to be avoided.
Type: Array of [WaypointOptimizationAvoidanceArea](API_WaypointOptimizationAvoidanceArea.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** CarShuttleTrains **   <a name="location-Type-WaypointOptimizationAvoidanceOptions-CarShuttleTrains"></a>
Avoidance options for cars-shuttles-trains.
Type: Boolean
Required: No

 ** ControlledAccessHighways **   <a name="location-Type-WaypointOptimizationAvoidanceOptions-ControlledAccessHighways"></a>
Avoid controlled access highways while calculating the route.
Type: Boolean
Required: No

 ** DirtRoads **   <a name="location-Type-WaypointOptimizationAvoidanceOptions-DirtRoads"></a>
Avoid dirt roads while calculating the route.
Type: Boolean
Required: No

 ** Ferries **   <a name="location-Type-WaypointOptimizationAvoidanceOptions-Ferries"></a>
Avoidance options for ferries.
Type: Boolean
Required: No

 ** TollRoads **   <a name="location-Type-WaypointOptimizationAvoidanceOptions-TollRoads"></a>
Avoids roads where the specified toll transponders are the only mode of payment.
Type: Boolean
Required: No

 ** Tunnels **   <a name="location-Type-WaypointOptimizationAvoidanceOptions-Tunnels"></a>
Avoid tunnels while calculating the route.
Type: Boolean
Required: No

 ** UTurns **   <a name="location-Type-WaypointOptimizationAvoidanceOptions-UTurns"></a>
Avoid U-turns for calculation on highways and motorways.
Type: Boolean
Required: No

## See Also
<a name="API_WaypointOptimizationAvoidanceOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/WaypointOptimizationAvoidanceOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/WaypointOptimizationAvoidanceOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/WaypointOptimizationAvoidanceOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
