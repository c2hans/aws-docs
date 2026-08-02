---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_ListRecommendationSummaries.html
---

# ListRecommendationSummaries
<a name="API_CostOptimizationHub_ListRecommendationSummaries"></a>

Returns a concise representation of savings estimates for resources. Also returns de-duped savings across different types of recommendations.

**Note**
The following filters are not supported for this API: `recommendationIds`, `resourceArns`, and `resourceIds`.

## Request Syntax
<a name="API_CostOptimizationHub_ListRecommendationSummaries_RequestSyntax"></a>

```
{
   "filter": {
      "accountIds": [ "{{string}}" ],
      "actionTypes": [ "{{string}}" ],
      "implementationEfforts": [ "{{string}}" ],
      "recommendationIds": [ "{{string}}" ],
      "regions": [ "{{string}}" ],
      "resourceArns": [ "{{string}}" ],
      "resourceIds": [ "{{string}}" ],
      "resourceTypes": [ "{{string}}" ],
      "restartNeeded": {{boolean}},
      "rollbackPossible": {{boolean}},
      "tags": [
         {
            "key": "{{string}}",
            "value": "{{string}}"
         }
      ]
   },
   "groupBy": "{{string}}",
   "maxResults": {{number}},
   "metrics": [ "{{string}}" ],
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_CostOptimizationHub_ListRecommendationSummaries_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [filter](#API_CostOptimizationHub_ListRecommendationSummaries_RequestSyntax) **   <a name="awscostmanagement-CostOptimizationHub_ListRecommendationSummaries-request-filter"></a>
Describes a filter that returns a more specific list of recommendations. Filters recommendations by different dimensions.
Type: [Filter](API_CostOptimizationHub_Filter.md) object
Required: No

 ** [groupBy](#API_CostOptimizationHub_ListRecommendationSummaries_RequestSyntax) **   <a name="awscostmanagement-CostOptimizationHub_ListRecommendationSummaries-request-groupBy"></a>
The grouping of recommendations by a dimension.
Type: String
Required: Yes

 ** [maxResults](#API_CostOptimizationHub_ListRecommendationSummaries_RequestSyntax) **   <a name="awscostmanagement-CostOptimizationHub_ListRecommendationSummaries-request-maxResults"></a>
The maximum number of recommendations to be returned for the request.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1000.
Required: No

 ** [metrics](#API_CostOptimizationHub_ListRecommendationSummaries_RequestSyntax) **   <a name="awscostmanagement-CostOptimizationHub_ListRecommendationSummaries-request-metrics"></a>
Additional metrics to be returned for the request. The only valid value is `savingsPercentage`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Valid Values: `SavingsPercentage`
Required: No

 ** [nextToken](#API_CostOptimizationHub_ListRecommendationSummaries_RequestSyntax) **   <a name="awscostmanagement-CostOptimizationHub_ListRecommendationSummaries-request-nextToken"></a>
The token to retrieve the next set of results.
Type: String
Required: No

## Response Syntax
<a name="API_CostOptimizationHub_ListRecommendationSummaries_ResponseSyntax"></a>

```
{
   "currencyCode": "string",
   "estimatedTotalDedupedSavings": number,
   "groupBy": "string",
   "items": [
      {
         "estimatedMonthlySavings": number,
         "group": "string",
         "recommendationCount": number
      }
   ],
   "metrics": {
      "savingsPercentage": "string"
   },
   "nextToken": "string"
}
```

## Response Elements
<a name="API_CostOptimizationHub_ListRecommendationSummaries_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [currencyCode](#API_CostOptimizationHub_ListRecommendationSummaries_ResponseSyntax) **   <a name="awscostmanagement-CostOptimizationHub_ListRecommendationSummaries-response-currencyCode"></a>
The currency code used for the recommendation.
Type: String

 ** [estimatedTotalDedupedSavings](#API_CostOptimizationHub_ListRecommendationSummaries_ResponseSyntax) **   <a name="awscostmanagement-CostOptimizationHub_ListRecommendationSummaries-response-estimatedTotalDedupedSavings"></a>
The total overall savings for the aggregated view.
Type: Double

 ** [groupBy](#API_CostOptimizationHub_ListRecommendationSummaries_ResponseSyntax) **   <a name="awscostmanagement-CostOptimizationHub_ListRecommendationSummaries-response-groupBy"></a>
The dimension used to group the recommendations by.
Type: String

 ** [items](#API_CostOptimizationHub_ListRecommendationSummaries_ResponseSyntax) **   <a name="awscostmanagement-CostOptimizationHub_ListRecommendationSummaries-response-items"></a>
A list of all savings recommendations.
Type: Array of [RecommendationSummary](API_CostOptimizationHub_RecommendationSummary.md) objects

 ** [metrics](#API_CostOptimizationHub_ListRecommendationSummaries_ResponseSyntax) **   <a name="awscostmanagement-CostOptimizationHub_ListRecommendationSummaries-response-metrics"></a>
The results or descriptions for the additional metrics, based on whether the metrics were or were not requested.
Type: [SummaryMetricsResult](API_CostOptimizationHub_SummaryMetricsResult.md) object

 ** [nextToken](#API_CostOptimizationHub_ListRecommendationSummaries_ResponseSyntax) **   <a name="awscostmanagement-CostOptimizationHub_ListRecommendationSummaries-response-nextToken"></a>
The token to retrieve the next set of results.
Type: String

## Errors
<a name="API_CostOptimizationHub_ListRecommendationSummaries_Errors"></a>

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
<a name="API_CostOptimizationHub_ListRecommendationSummaries_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cost-optimization-hub-2022-07-26/ListRecommendationSummaries)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cost-optimization-hub-2022-07-26/ListRecommendationSummaries)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cost-optimization-hub-2022-07-26/ListRecommendationSummaries)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cost-optimization-hub-2022-07-26/ListRecommendationSummaries)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cost-optimization-hub-2022-07-26/ListRecommendationSummaries)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cost-optimization-hub-2022-07-26/ListRecommendationSummaries)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cost-optimization-hub-2022-07-26/ListRecommendationSummaries)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cost-optimization-hub-2022-07-26/ListRecommendationSummaries)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cost-optimization-hub-2022-07-26/ListRecommendationSummaries)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cost-optimization-hub-2022-07-26/ListRecommendationSummaries)
