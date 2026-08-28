---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_CalculateRouteMatrixSummary.html
---

# CalculateRouteMatrixSummary
<a name="API_CalculateRouteMatrixSummary"></a>

A summary of the calculated route matrix.

## Contents
<a name="API_CalculateRouteMatrixSummary_Contents"></a>

 ** DataSource **   <a name="location-Type-CalculateRouteMatrixSummary-DataSource"></a>
The data provider of traffic and road network data used to calculate the routes. Indicates one of the available providers:
+  `Esri`
+  `Grab`
+  `Here`
For more information about data providers, see [Amazon Location Service data providers](https://docs.aws.amazon.com/location/previous/developerguide/what-is-data-provider.html).
Type: String
Required: Yes

 ** DistanceUnit **   <a name="location-Type-CalculateRouteMatrixSummary-DistanceUnit"></a>
The unit of measurement for route distances.
Type: String
Valid Values: `Kilometers | Miles`
Required: Yes

 ** ErrorCount **   <a name="location-Type-CalculateRouteMatrixSummary-ErrorCount"></a>
The count of error results in the route matrix. If this number is 0, all routes were calculated successfully.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 160000.
Required: Yes

 ** RouteCount **   <a name="location-Type-CalculateRouteMatrixSummary-RouteCount"></a>
The count of cells in the route matrix. Equal to the number of `DeparturePositions` multiplied by the number of `DestinationPositions`.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 160000.
Required: Yes

## See Also
<a name="API_CalculateRouteMatrixSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/CalculateRouteMatrixSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/CalculateRouteMatrixSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/CalculateRouteMatrixSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
