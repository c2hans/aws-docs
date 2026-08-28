---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_WaypointOptimizationSideOfStreetOptions.html
---

# WaypointOptimizationSideOfStreetOptions
<a name="API_WaypointOptimizationSideOfStreetOptions"></a>

Options to configure matching the provided position to a side of the street.

## Contents
<a name="API_WaypointOptimizationSideOfStreetOptions_Contents"></a>

 ** Position **   <a name="location-Type-WaypointOptimizationSideOfStreetOptions-Position"></a>
Position in World Geodetic System (WGS 84) format: [longitude, latitude].
Type: Array of doubles
Array Members: Fixed number of 2 items.
Required: Yes

 ** UseWith **   <a name="location-Type-WaypointOptimizationSideOfStreetOptions-UseWith"></a>
Strategy that defines when the side of street position should be used. AnyStreet will always use the provided position.
Default value: `DividedStreetOnly`
Type: String
Valid Values: `AnyStreet | DividedStreetOnly`
Required: No

## See Also
<a name="API_WaypointOptimizationSideOfStreetOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/WaypointOptimizationSideOfStreetOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/WaypointOptimizationSideOfStreetOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/WaypointOptimizationSideOfStreetOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
