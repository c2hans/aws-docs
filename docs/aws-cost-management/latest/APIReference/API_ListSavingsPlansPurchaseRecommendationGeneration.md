---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ListSavingsPlansPurchaseRecommendationGeneration.html
---

# ListSavingsPlansPurchaseRecommendationGeneration
<a name="API_ListSavingsPlansPurchaseRecommendationGeneration"></a>

Retrieves a list of your historical recommendation generations within the past 30 days.

## Request Syntax
<a name="API_ListSavingsPlansPurchaseRecommendationGeneration_RequestSyntax"></a>

```
{
   "GenerationStatus": "{{string}}",
   "NextPageToken": "{{string}}",
   "PageSize": {{number}},
   "RecommendationIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_ListSavingsPlansPurchaseRecommendationGeneration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [GenerationStatus](#API_ListSavingsPlansPurchaseRecommendationGeneration_RequestSyntax) **   <a name="awscostmanagement-ListSavingsPlansPurchaseRecommendationGeneration-request-GenerationStatus"></a>
The status of the recommendation generation.
Type: String
Valid Values: `SUCCEEDED | PROCESSING | FAILED`
Required: No

 ** [NextPageToken](#API_ListSavingsPlansPurchaseRecommendationGeneration_RequestSyntax) **   <a name="awscostmanagement-ListSavingsPlansPurchaseRecommendationGeneration-request-NextPageToken"></a>
The token to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[\S\s]*`
Required: No

 ** [PageSize](#API_ListSavingsPlansPurchaseRecommendationGeneration_RequestSyntax) **   <a name="awscostmanagement-ListSavingsPlansPurchaseRecommendationGeneration-request-PageSize"></a>
The number of recommendations that you want returned in a single response object.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 6000.
Required: No

 ** [RecommendationIds](#API_ListSavingsPlansPurchaseRecommendationGeneration_RequestSyntax) **   <a name="awscostmanagement-ListSavingsPlansPurchaseRecommendationGeneration-request-RecommendationIds"></a>
The IDs for each specific recommendation.
Type: Array of strings
Length Constraints: Fixed length of 36.
Pattern: `^[\S\s]{8}-[\S\s]{4}-[\S\s]{4}-[\S\s]{4}-[\S\s]{12}$`
Required: No

## Response Syntax
<a name="API_ListSavingsPlansPurchaseRecommendationGeneration_ResponseSyntax"></a>

```
{
   "GenerationSummaryList": [
      {
         "EstimatedCompletionTime": "string",
         "GenerationCompletionTime": "string",
         "GenerationStartedTime": "string",
         "GenerationStatus": "string",
         "RecommendationId": "string"
      }
   ],
   "NextPageToken": "string"
}
```

## Response Elements
<a name="API_ListSavingsPlansPurchaseRecommendationGeneration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GenerationSummaryList](#API_ListSavingsPlansPurchaseRecommendationGeneration_ResponseSyntax) **   <a name="awscostmanagement-ListSavingsPlansPurchaseRecommendationGeneration-response-GenerationSummaryList"></a>
The list of historical recommendation generations.
Type: Array of [GenerationSummary](API_GenerationSummary.md) objects

 ** [NextPageToken](#API_ListSavingsPlansPurchaseRecommendationGeneration_ResponseSyntax) **   <a name="awscostmanagement-ListSavingsPlansPurchaseRecommendationGeneration-response-NextPageToken"></a>
The token to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[\S\s]*`

## Errors
<a name="API_ListSavingsPlansPurchaseRecommendationGeneration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DataUnavailableException **
The requested data is unavailable.
HTTP Status Code: 400

 ** InvalidNextTokenException **
The pagination token is invalid. Try again without a pagination token.
HTTP Status Code: 400

 ** LimitExceededException **
You made too many calls in a short period of time. Try again later.
HTTP Status Code: 400

## See Also
<a name="API_ListSavingsPlansPurchaseRecommendationGeneration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ce-2017-10-25/ListSavingsPlansPurchaseRecommendationGeneration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ce-2017-10-25/ListSavingsPlansPurchaseRecommendationGeneration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/ListSavingsPlansPurchaseRecommendationGeneration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ce-2017-10-25/ListSavingsPlansPurchaseRecommendationGeneration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/ListSavingsPlansPurchaseRecommendationGeneration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ce-2017-10-25/ListSavingsPlansPurchaseRecommendationGeneration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ce-2017-10-25/ListSavingsPlansPurchaseRecommendationGeneration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ce-2017-10-25/ListSavingsPlansPurchaseRecommendationGeneration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ce-2017-10-25/ListSavingsPlansPurchaseRecommendationGeneration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/ListSavingsPlansPurchaseRecommendationGeneration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
