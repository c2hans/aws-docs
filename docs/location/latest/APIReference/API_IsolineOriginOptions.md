---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_IsolineOriginOptions.html
---

# IsolineOriginOptions
<a name="API_IsolineOriginOptions"></a>

Options that control how the origin point is interpreted when calculating reachable areas. These options affect which roads are considered accessible from the starting point and how initial routing decisions are made.

## Contents
<a name="API_IsolineOriginOptions_Contents"></a>

 ** AvoidActionsForDistance **   <a name="location-Type-IsolineOriginOptions-AvoidActionsForDistance"></a>
The distance in meters from the origin point within which certain routing actions (such as U-turns or left turns across traffic) are restricted. This helps generate more practical routes by avoiding potentially dangerous maneuvers near the starting point.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** Heading **   <a name="location-Type-IsolineOriginOptions-Heading"></a>
Initial direction of travel in degrees (0-360, where 0 is north). This affects which road segments are considered accessible from the starting point and is particularly useful when the origin is on a divided road or at a complex intersection.
Type: Double
Valid Range: Minimum value of 0.0. Maximum value of 360.0.
Required: No

 ** Matching **   <a name="location-Type-IsolineOriginOptions-Matching"></a>
Controls how the origin point is matched to the road network, including search radius and matching strategy.
Type: [IsolineMatchingOptions](API_IsolineMatchingOptions.md) object
Required: No

 ** SideOfStreet **   <a name="location-Type-IsolineOriginOptions-SideOfStreet"></a>
Controls which side of the street is considered accessible from the origin point, particularly important for divided roads where building entrances or parking access may only be available from one direction.
Type: [IsolineSideOfStreetOptions](API_IsolineSideOfStreetOptions.md) object
Required: No

## See Also
<a name="API_IsolineOriginOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/IsolineOriginOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/IsolineOriginOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/IsolineOriginOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
