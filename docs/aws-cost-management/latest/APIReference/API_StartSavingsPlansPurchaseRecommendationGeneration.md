---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_StartSavingsPlansPurchaseRecommendationGeneration.html
---

# StartSavingsPlansPurchaseRecommendationGeneration
<a name="API_StartSavingsPlansPurchaseRecommendationGeneration"></a>

Requests a Savings Plans recommendation generation. This enables you to calculate a fresh set of Savings Plans recommendations that takes your latest usage data and current Savings Plans inventory into account. You can refresh Savings Plans recommendations up to three times daily for a consolidated billing family.

**Note**
 `StartSavingsPlansPurchaseRecommendationGeneration` has no request syntax because no input parameters are needed to support this operation.

## Response Syntax
<a name="API_StartSavingsPlansPurchaseRecommendationGeneration_ResponseSyntax"></a>

```
{
   "EstimatedCompletionTime": "string",
   "GenerationStartedTime": "string",
   "RecommendationId": "string"
}
```

## Response Elements
<a name="API_StartSavingsPlansPurchaseRecommendationGeneration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EstimatedCompletionTime](#API_StartSavingsPlansPurchaseRecommendationGeneration_ResponseSyntax) **   <a name="awscostmanagement-StartSavingsPlansPurchaseRecommendationGeneration-response-EstimatedCompletionTime"></a>
The estimated time for when the recommendation generation will complete.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 25.
Pattern: `^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(([+-]\d\d:\d\d)|Z)$`

 ** [GenerationStartedTime](#API_StartSavingsPlansPurchaseRecommendationGeneration_ResponseSyntax) **   <a name="awscostmanagement-StartSavingsPlansPurchaseRecommendationGeneration-response-GenerationStartedTime"></a>
The start time of the recommendation generation.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 25.
Pattern: `^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d(([+-]\d\d:\d\d)|Z)$`

 ** [RecommendationId](#API_StartSavingsPlansPurchaseRecommendationGeneration_ResponseSyntax) **   <a name="awscostmanagement-StartSavingsPlansPurchaseRecommendationGeneration-response-RecommendationId"></a>
The ID for this specific recommendation.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[\S\s]{8}-[\S\s]{4}-[\S\s]{4}-[\S\s]{4}-[\S\s]{12}$`

## Errors
<a name="API_StartSavingsPlansPurchaseRecommendationGeneration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DataUnavailableException **
The requested data is unavailable.
HTTP Status Code: 400

 ** GenerationExistsException **
A request to generate a recommendation or analysis is already in progress.
HTTP Status Code: 400

 ** LimitExceededException **
You made too many calls in a short period of time. Try again later.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
 You've reached the limit on the number of resources you can create, or exceeded the size of an individual resource.
HTTP Status Code: 400

## See Also
<a name="API_StartSavingsPlansPurchaseRecommendationGeneration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ce-2017-10-25/StartSavingsPlansPurchaseRecommendationGeneration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ce-2017-10-25/StartSavingsPlansPurchaseRecommendationGeneration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/StartSavingsPlansPurchaseRecommendationGeneration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ce-2017-10-25/StartSavingsPlansPurchaseRecommendationGeneration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/StartSavingsPlansPurchaseRecommendationGeneration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ce-2017-10-25/StartSavingsPlansPurchaseRecommendationGeneration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ce-2017-10-25/StartSavingsPlansPurchaseRecommendationGeneration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ce-2017-10-25/StartSavingsPlansPurchaseRecommendationGeneration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ce-2017-10-25/StartSavingsPlansPurchaseRecommendationGeneration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/StartSavingsPlansPurchaseRecommendationGeneration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
