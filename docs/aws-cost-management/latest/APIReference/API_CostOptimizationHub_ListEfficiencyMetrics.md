---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_ListEfficiencyMetrics.html
---

# ListEfficiencyMetrics
<a name="API_CostOptimizationHub_ListEfficiencyMetrics"></a>

Returns cost efficiency metrics aggregated over time and optionally grouped by a specified dimension. The metrics provide insights into your cost optimization progress by tracking estimated savings, spending, and measures how effectively you're optimizing your Cloud resources.

The operation supports both daily and monthly time granularities and allows grouping results by account ID, AWS Region. Results are returned as time-series data, enabling you to analyze trends in your cost optimization performance over the specified time period.

## Request Syntax
<a name="API_CostOptimizationHub_ListEfficiencyMetrics_RequestSyntax"></a>

```
{
   "granularity": "{{string}}",
   "groupBy": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "orderBy": {
      "dimension": "{{string}}",
      "order": "{{string}}"
   },
   "timePeriod": {
      "end": "{{string}}",
      "start": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CostOptimizationHub_ListEfficiencyMetrics_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [granularity](#API_CostOptimizationHub_ListEfficiencyMetrics_RequestSyntax) **   <a name="awscostmanagement-CostOptimizationHub_ListEfficiencyMetrics-request-granularity"></a>
The time granularity for the cost efficiency metrics. Specify `Daily` for metrics aggregated by day, or `Monthly` for metrics aggregated by month.
Type: String
Valid Values: `Daily | Monthly`
Required: Yes

 ** [groupBy](#API_CostOptimizationHub_ListEfficiencyMetrics_RequestSyntax) **   <a name="awscostmanagement-CostOptimizationHub_ListEfficiencyMetrics-request-groupBy"></a>
The dimension by which to group the cost efficiency metrics. Valid values include account ID, AWS Region. When no grouping is specified, metrics are aggregated across all resources in the specified time period.
Type: String
Required: No

 ** [maxResults](#API_CostOptimizationHub_ListEfficiencyMetrics_RequestSyntax) **   <a name="awscostmanagement-CostOptimizationHub_ListEfficiencyMetrics-request-maxResults"></a>
The maximum number of groups to return in the response. Valid values range from 0 to 1000. Use in conjunction with `nextToken` to paginate through results when the total number of groups exceeds this limit.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1000.
Required: No

 ** [nextToken](#API_CostOptimizationHub_ListEfficiencyMetrics_RequestSyntax) **   <a name="awscostmanagement-CostOptimizationHub_ListEfficiencyMetrics-request-nextToken"></a>
The token to retrieve the next page of results. This value is returned in the response when the number of groups exceeds the specified `maxResults` value.
Type: String
Required: No

 ** [orderBy](#API_CostOptimizationHub_ListEfficiencyMetrics_RequestSyntax) **   <a name="awscostmanagement-CostOptimizationHub_ListEfficiencyMetrics-request-orderBy"></a>
The ordering specification for the results. Defines which dimension to sort by and whether to sort in ascending or descending order.
Type: [OrderBy](API_CostOptimizationHub_OrderBy.md) object
Required: No

 ** [timePeriod](#API_CostOptimizationHub_ListEfficiencyMetrics_RequestSyntax) **   <a name="awscostmanagement-CostOptimizationHub_ListEfficiencyMetrics-request-timePeriod"></a>
The time period for which to retrieve the cost efficiency metrics. The start date is inclusive and the end date is exclusive. Dates can be specified in either YYYY-MM-DD format or YYYY-MM format depending on the desired granularity.
Type: [TimePeriod](API_CostOptimizationHub_TimePeriod.md) object
Required: Yes

## Response Syntax
<a name="API_CostOptimizationHub_ListEfficiencyMetrics_ResponseSyntax"></a>

```
{
   "efficiencyMetricsByGroup": [
      {
         "group": "string",
         "message": "string",
         "metricsByTime": [
            {
               "savings": number,
               "score": number,
               "spend": number,
               "timestamp": "string"
            }
         ]
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_CostOptimizationHub_ListEfficiencyMetrics_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [efficiencyMetricsByGroup](#API_CostOptimizationHub_ListEfficiencyMetrics_ResponseSyntax) **   <a name="awscostmanagement-CostOptimizationHub_ListEfficiencyMetrics-response-efficiencyMetricsByGroup"></a>
A list of cost efficiency metrics grouped by the specified dimension. Each group contains time-series data points with cost efficiency, potential savings, and optimzable spend for the specified time period.
Type: Array of [EfficiencyMetricsByGroup](API_CostOptimizationHub_EfficiencyMetricsByGroup.md) objects

 ** [nextToken](#API_CostOptimizationHub_ListEfficiencyMetrics_ResponseSyntax) **   <a name="awscostmanagement-CostOptimizationHub_ListEfficiencyMetrics-response-nextToken"></a>
The token to retrieve the next page of results. When this value is present in the response, additional groups are available. Pass this token in the `nextToken` parameter of a subsequent request to retrieve the next page.
Type: String

## Errors
<a name="API_CostOptimizationHub_ListEfficiencyMetrics_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You are not authorized to use this operation with the given parameters.
HTTP Status Code: 400

 ** InternalServerException **
An error on the server occurred during the processing of your request. Try again later.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
 ** fields **
The list of fields that are invalid.
 ** reason **
The reason for the validation exception.
HTTP Status Code: 400

## See Also
<a name="API_CostOptimizationHub_ListEfficiencyMetrics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cost-optimization-hub-2022-07-26/ListEfficiencyMetrics)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cost-optimization-hub-2022-07-26/ListEfficiencyMetrics)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cost-optimization-hub-2022-07-26/ListEfficiencyMetrics)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cost-optimization-hub-2022-07-26/ListEfficiencyMetrics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cost-optimization-hub-2022-07-26/ListEfficiencyMetrics)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cost-optimization-hub-2022-07-26/ListEfficiencyMetrics)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cost-optimization-hub-2022-07-26/ListEfficiencyMetrics)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cost-optimization-hub-2022-07-26/ListEfficiencyMetrics)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cost-optimization-hub-2022-07-26/ListEfficiencyMetrics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cost-optimization-hub-2022-07-26/ListEfficiencyMetrics)
