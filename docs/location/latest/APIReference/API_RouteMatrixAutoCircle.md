---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteMatrixAutoCircle.html
---

# RouteMatrixAutoCircle
<a name="API_RouteMatrixAutoCircle"></a>

 `AutoCircle` requests the route matrix service to define a `Circle` boundary that best attempts to include most waypoints (`Origins` and `Destinations`) using the `AutoCircle` settings. Any waypoints outside of the auto-defined `Circle` boundary will be considered out of the routing boundary, which results in a route matrix entry error.

 `AutoCircle` is only used in the request to configure a `Circle` for the route calculation. The derived `Circle` will also be provided in the response.

## Contents
<a name="API_RouteMatrixAutoCircle_Contents"></a>

 ** Margin **   <a name="location-Type-RouteMatrixAutoCircle-Margin"></a>
The minimal distance, in meters, between any waypoint and the perimeter of the circle auto-defined for the boundary. Some margin is usually recommended so that the routing has enough leeway to travel from one waypoint to another optimally without conflicting with the routing boundary.
The total of `MaxRadius` and `Margin` must be less than or equal to 200,000 meters.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 200000.
Required: No

 ** MaxRadius **   <a name="location-Type-RouteMatrixAutoCircle-MaxRadius"></a>
The maximum radius, in meters, that the auto-defined `Circle` boundary should have, before the `Margin` distance is added to the circle.
The total of `MaxRadius` and `Margin` must be less than or equal to 200,000 meters.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 200000.
Required: No

## See Also
<a name="API_RouteMatrixAutoCircle_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteMatrixAutoCircle)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteMatrixAutoCircle)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteMatrixAutoCircle)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
