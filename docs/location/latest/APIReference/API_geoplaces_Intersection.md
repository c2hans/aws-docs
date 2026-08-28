---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_Intersection.html
---

# Intersection
<a name="API_geoplaces_Intersection"></a>

All Intersections that are near the provided address.

## Contents
<a name="API_geoplaces_Intersection_Contents"></a>

 ** PlaceId **   <a name="location-Type-geoplaces_Intersection-PlaceId"></a>
The `PlaceId` of the place result.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: Yes

 ** Title **   <a name="location-Type-geoplaces_Intersection-Title"></a>
The localized display name of this result item based on request parameter `language`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Required: Yes

 ** AccessPoints **   <a name="location-Type-geoplaces_Intersection-AccessPoints"></a>
Position of the access point in World Geodetic System (WGS 84) format: [longitude, latitude].
Type: Array of [AccessPoint](API_geoplaces_AccessPoint.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** Address **   <a name="location-Type-geoplaces_Intersection-Address"></a>
The place address.
Type: [Address](API_geoplaces_Address.md) object
Required: No

 ** Distance **   <a name="location-Type-geoplaces_Intersection-Distance"></a>
The distance in meters from the QueryPosition.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** MapView **   <a name="location-Type-geoplaces_Intersection-MapView"></a>
The bounding box enclosing the geometric shape (area or line) that an individual result covers.
The bounding box formed is defined as a set of four coordinates: `[{westward lng}, {southern lat}, {eastward lng}, {northern lat}]`
Type: Array of doubles
Array Members: Fixed number of 4 items.
Required: No

 ** Position **   <a name="location-Type-geoplaces_Intersection-Position"></a>
The position in World Geodetic System (WGS 84) format: [longitude, latitude].
Type: Array of doubles
Array Members: Fixed number of 2 items.
Required: No

 ** RouteDistance **   <a name="location-Type-geoplaces_Intersection-RouteDistance"></a>
The distance from the routing position of the nearby address to the street result.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

## See Also
<a name="API_geoplaces_Intersection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-places-2020-11-19/Intersection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-places-2020-11-19/Intersection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-places-2020-11-19/Intersection)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
