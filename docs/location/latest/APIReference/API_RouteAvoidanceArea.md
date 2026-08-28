---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteAvoidanceArea.html
---

# RouteAvoidanceArea
<a name="API_RouteAvoidanceArea"></a>

Areas to be avoided.

## Contents
<a name="API_RouteAvoidanceArea_Contents"></a>

 ** Geometry **   <a name="location-Type-RouteAvoidanceArea-Geometry"></a>
Geometry of the area to be avoided.
Type: [RouteAvoidanceAreaGeometry](API_RouteAvoidanceAreaGeometry.md) object
Required: Yes

 ** Except **   <a name="location-Type-RouteAvoidanceArea-Except"></a>
Exceptions to the provided avoidance geometry, to be included while calculating the route.
Type: Array of [RouteAvoidanceAreaGeometry](API_RouteAvoidanceAreaGeometry.md) objects
Required: No

## See Also
<a name="API_RouteAvoidanceArea_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteAvoidanceArea)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteAvoidanceArea)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteAvoidanceArea)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
