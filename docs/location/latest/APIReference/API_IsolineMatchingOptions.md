---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_IsolineMatchingOptions.html
---

# IsolineMatchingOptions
<a name="API_IsolineMatchingOptions"></a>

Controls how origin and destination points are matched to the road network when they don't fall exactly on a road. Matching options help ensure realistic routing by connecting points to appropriate roads.

## Contents
<a name="API_IsolineMatchingOptions_Contents"></a>

 ** NameHint **   <a name="location-Type-IsolineMatchingOptions-NameHint"></a>
The expected street name near the point. Helps disambiguate matching when multiple roads are within range.
Type: String
Required: No

 ** OnRoadThreshold **   <a name="location-Type-IsolineMatchingOptions-OnRoadThreshold"></a>
The maximum distance in meters that a point can be from a road while still being considered "on" that road. Points further than this distance require explicit matching.
 **Unit**: `meters`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** Radius **   <a name="location-Type-IsolineMatchingOptions-Radius"></a>
The maximum distance in meters to search for roads to match to. Points with no roads within this radius will fail to match. The roads that are considered within this radius are determined by the specified `Strategy`
 **Unit**: `meters`
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

 ** Strategy **   <a name="location-Type-IsolineMatchingOptions-Strategy"></a>
Determines how points are matched to the road network. `MatchAny` finds the nearest viable road segment, while `MatchMostSignificantRoad` prioritizes major roads.
Type: String
Valid Values: `MatchAny | MatchMostSignificantRoad`
Required: No

## See Also
<a name="API_IsolineMatchingOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/IsolineMatchingOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/IsolineMatchingOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/IsolineMatchingOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
