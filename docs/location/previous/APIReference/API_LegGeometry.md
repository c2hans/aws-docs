---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_LegGeometry.html
---

# LegGeometry
<a name="API_LegGeometry"></a>

Contains the geometry details for each path between a pair of positions. Used in plotting a route leg on a map.

## Contents
<a name="API_LegGeometry_Contents"></a>

 ** LineString **   <a name="location-Type-LegGeometry-LineString"></a>
An ordered list of positions used to plot a route on a map.
The first position is closest to the start position for the leg, and the last position is the closest to the end position for the leg.
+ For example, `[[-123.117, 49.284],[-123.115, 49.285],[-123.115, 49.285]]`
Type: Array of arrays of doubles
Array Members: Minimum number of 2 items.
Array Members: Fixed number of 2 items.
Required: No

## See Also
<a name="API_LegGeometry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/LegGeometry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/LegGeometry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/LegGeometry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
