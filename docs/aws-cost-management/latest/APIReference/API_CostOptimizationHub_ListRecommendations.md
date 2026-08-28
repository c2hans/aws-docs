---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_ListRecommendations.html
---

# ListRecommendations
<a name="API_CostOptimizationHub_ListRecommendations"></a>

Returns a list of recommendations.

## Request Syntax
<a name="API_CostOptimizationHub_ListRecommendations_RequestSyntax"></a>

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
   "includeAllRecommendations": {{boolean}},
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "orderBy": {
      "dimension": "{{string}}",
      "order": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CostOptimizationHub_ListRecommendations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [filter](#API_CostOptimizationHub_ListRecommendations_RequestSyntax) **   <a name="awscostmanagement-CostOptimizationHub_ListRecommendations-request-filter"></a>
The constraints that you want all returned recommendations to match.
Type: [Filter](API_CostOptimizationHub_Filter.md) object
Required: No

 ** [includeAllRecommendations](#API_CostOptimizationHub_ListRecommendations_RequestSyntax) **   <a name="awscostmanagement-CostOptimizationHub_ListRecommendations-request-includeAllRecommendations"></a>
List of all recommendations for a resource, or a single recommendation if de-duped by `resourceId`.
Type: Boolean
Required: No

 ** [maxResults](#API_CostOptimizationHub_ListRecommendations_RequestSyntax) **   <a name="awscostmanagement-CostOptimizationHub_ListRecommendations-request-maxResults"></a>
The maximum number of recommendations that are returned for the request.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1000.
Required: No

 ** [nextToken](#API_CostOptimizationHub_ListRecommendations_RequestSyntax) **   <a name="awscostmanagement-CostOptimizationHub_ListRecommendations-request-nextToken"></a>
The token to retrieve the next set of results.
Type: String
Required: No

 ** [orderBy](#API_CostOptimizationHub_ListRecommendations_RequestSyntax) **   <a name="awscostmanagement-CostOptimizationHub_ListRecommendations-request-orderBy"></a>
The ordering of recommendations by a dimension.
Type: [OrderBy](API_CostOptimizationHub_OrderBy.md) object
Required: No

## Response Syntax
<a name="API_CostOptimizationHub_ListRecommendations_ResponseSyntax"></a>

```
{
   "items": [
      {
         "accountId": "string",
         "actionType": "string",
         "currencyCode": "string",
         "currentResourceSummary": "string",
         "currentResourceType": "string",
         "estimatedMonthlyCost": number,
         "estimatedMonthlySavings": number,
         "estimatedSavingsPercentage": number,
         "implementationEffort": "string",
         "lastRefreshTimestamp": number,
         "recommendationId": "string",
         "recommendationLookbackPeriodInDays": number,
         "recommendedResourceSummary": "string",
         "recommendedResourceType": "string",
         "region": "string",
         "resourceArn": "string",
         "resourceId": "string",
         "restartNeeded": boolean,
         "rollbackPossible": boolean,
         "source": "string",
         "tags": [
            {
               "key": "string",
               "value": "string"
            }
         ]
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_CostOptimizationHub_ListRecommendations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_CostOptimizationHub_ListRecommendations_ResponseSyntax) **   <a name="awscostmanagement-CostOptimizationHub_ListRecommendations-response-items"></a>
List of all savings recommendations.
Type: Array of [Recommendation](API_CostOptimizationHub_Recommendation.md) objects

 ** [nextToken](#API_CostOptimizationHub_ListRecommendations_ResponseSyntax) **   <a name="awscostmanagement-CostOptimizationHub_ListRecommendations-response-nextToken"></a>
The token to retrieve the next set of results.
Type: String

## Errors
<a name="API_CostOptimizationHub_ListRecommendations_Errors"></a>

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
<a name="API_CostOptimizationHub_ListRecommendations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cost-optimization-hub-2022-07-26/ListRecommendations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cost-optimization-hub-2022-07-26/ListRecommendations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cost-optimization-hub-2022-07-26/ListRecommendations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cost-optimization-hub-2022-07-26/ListRecommendations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cost-optimization-hub-2022-07-26/ListRecommendations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cost-optimization-hub-2022-07-26/ListRecommendations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cost-optimization-hub-2022-07-26/ListRecommendations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cost-optimization-hub-2022-07-26/ListRecommendations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cost-optimization-hub-2022-07-26/ListRecommendations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cost-optimization-hub-2022-07-26/ListRecommendations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
