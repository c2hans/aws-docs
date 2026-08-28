---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteMatrixOriginOptions.html
---

# RouteMatrixOriginOptions
<a name="API_RouteMatrixOriginOptions"></a>

Origin related options.

## Contents
<a name="API_RouteMatrixOriginOptions_Contents"></a>

 ** AvoidActionsForDistance **   <a name="location-Type-RouteMatrixOriginOptions-AvoidActionsForDistance"></a>
Avoids actions for the provided distance. This is typically to consider for users in moving vehicles who may not have sufficient time to make an action at an origin or a destination.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** Heading **   <a name="location-Type-RouteMatrixOriginOptions-Heading"></a>
GPS Heading at the position.
Type: Double
Valid Range: Minimum value of 0.0. Maximum value of 360.0.
Required: No

 ** Matching **   <a name="location-Type-RouteMatrixOriginOptions-Matching"></a>
Options to configure matching the provided position to the road network.
Type: [RouteMatrixMatchingOptions](API_RouteMatrixMatchingOptions.md) object
Required: No

 ** SideOfStreet **   <a name="location-Type-RouteMatrixOriginOptions-SideOfStreet"></a>
Options to configure matching the provided position to a side of the street.
Type: [RouteMatrixSideOfStreetOptions](API_RouteMatrixSideOfStreetOptions.md) object
Required: No

## See Also
<a name="API_RouteMatrixOriginOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteMatrixOriginOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteMatrixOriginOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteMatrixOriginOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
