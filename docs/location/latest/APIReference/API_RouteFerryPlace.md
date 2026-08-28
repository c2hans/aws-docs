---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteFerryPlace.html
---

# RouteFerryPlace
<a name="API_RouteFerryPlace"></a>

Position provided in the request.

## Contents
<a name="API_RouteFerryPlace_Contents"></a>

 ** Position **   <a name="location-Type-RouteFerryPlace-Position"></a>
Position in World Geodetic System (WGS 84) format: [longitude, latitude].
Type: Array of doubles
Array Members: Minimum number of 2 items. Maximum number of 3 items.
Required: Yes

 ** Name **   <a name="location-Type-RouteFerryPlace-Name"></a>
The name of the place.
Type: String
Required: No

 ** OriginalPosition **   <a name="location-Type-RouteFerryPlace-OriginalPosition"></a>
Position provided in the request.
Type: Array of doubles
Array Members: Minimum number of 2 items. Maximum number of 3 items.
Required: No

 ** WaypointIndex **   <a name="location-Type-RouteFerryPlace-WaypointIndex"></a>
Index of the waypoint in the request.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_RouteFerryPlace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteFerryPlace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteFerryPlace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteFerryPlace)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
