---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteDestinationOptions.html
---

# RouteDestinationOptions
<a name="API_RouteDestinationOptions"></a>

Options related to the destination.

## Contents
<a name="API_RouteDestinationOptions_Contents"></a>

 ** AvoidActionsForDistance **   <a name="location-Type-RouteDestinationOptions-AvoidActionsForDistance"></a>
The distance in meters from the destination point within which certain routing actions (such as U-turns or left turns across traffic) are restricted. This helps generate more practical routes by avoiding potentially dangerous maneuvers near the endpoint.
Type: Long
Valid Range: Maximum value of 2000.
Required: No

 ** AvoidUTurns **   <a name="location-Type-RouteDestinationOptions-AvoidUTurns"></a>
Avoid U-turns for calculation on highways and motorways.
Type: Boolean
Required: No

 ** Heading **   <a name="location-Type-RouteDestinationOptions-Heading"></a>
GPS Heading at the position.
Type: Double
Valid Range: Minimum value of 0.0. Maximum value of 360.0.
Required: No

 ** Matching **   <a name="location-Type-RouteDestinationOptions-Matching"></a>
Options to configure matching the provided position to the road network.
Type: [RouteMatchingOptions](API_RouteMatchingOptions.md) object
Required: No

 ** SideOfStreet **   <a name="location-Type-RouteDestinationOptions-SideOfStreet"></a>
Options to configure matching the provided position to a side of the street.
Type: [RouteSideOfStreetOptions](API_RouteSideOfStreetOptions.md) object
Required: No

 ** StopDuration **   <a name="location-Type-RouteDestinationOptions-StopDuration"></a>
Duration of the stop.
 **Unit**: `seconds`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

## See Also
<a name="API_RouteDestinationOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteDestinationOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteDestinationOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteDestinationOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
