---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_ListRecommendedActions.html
---

# ListRecommendedActions
<a name="API_automation_ListRecommendedActions"></a>

 Lists the recommended actions based that match specified filters.

**Note**
Management accounts and delegated administrators can retrieve recommended actions that include associated member accounts. You can associate a member account using `AssociateAccounts`.

## Request Syntax
<a name="API_automation_ListRecommendedActions_RequestSyntax"></a>

```
{
   "filters": [
      {
         "name": "{{string}}",
         "values": [ "{{string}}" ]
      }
   ],
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_automation_ListRecommendedActions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [filters](#API_automation_ListRecommendedActions_RequestSyntax) **   <a name="computeoptimizer-automation_ListRecommendedActions-request-filters"></a>
 The filters to apply to the list of recommended actions.
Type: Array of [RecommendedActionFilter](API_automation_RecommendedActionFilter.md) objects
Required: No

 ** [maxResults](#API_automation_ListRecommendedActions_RequestSyntax) **   <a name="computeoptimizer-automation_ListRecommendedActions-request-maxResults"></a>
The maximum number of recommended actions to return in a single response. Valid range is 1-1000.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_automation_ListRecommendedActions_RequestSyntax) **   <a name="computeoptimizer-automation_ListRecommendedActions-request-nextToken"></a>
A token used for pagination to retrieve the next set of results when the response is truncated.
Type: String
Pattern: `[A-Za-z0-9+/=]+`
Required: No

## Response Syntax
<a name="API_automation_ListRecommendedActions_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "recommendedActions": [
      {
         "accountId": "string",
         "currentResourceDetails": { ... },
         "currentResourceSummary": "string",
         "estimatedMonthlySavings": {
            "afterDiscountSavings": number,
            "beforeDiscountSavings": number,
            "currency": "string",
            "savingsEstimationMode": "string"
         },
         "lookBackPeriodInDays": number,
         "recommendedActionId": "string",
         "recommendedActionType": "string",
         "recommendedResourceDetails": { ... },
         "recommendedResourceSummary": "string",
         "region": "string",
         "resourceArn": "string",
         "resourceId": "string",
         "resourceTags": [
            {
               "key": "string",
               "value": "string"
            }
         ],
         "resourceType": "string",
         "restartNeeded": boolean
      }
   ]
}
```

## Response Elements
<a name="API_automation_ListRecommendedActions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_automation_ListRecommendedActions_ResponseSyntax) **   <a name="computeoptimizer-automation_ListRecommendedActions-response-nextToken"></a>
A token used for pagination. If present, indicates there are more results available and can be used in subsequent requests.
Type: String
Pattern: `[A-Za-z0-9+/=]+`

 ** [recommendedActions](#API_automation_ListRecommendedActions_ResponseSyntax) **   <a name="computeoptimizer-automation_ListRecommendedActions-response-recommendedActions"></a>
 The list of recommended actions that match the specified criteria.
Type: Array of [RecommendedAction](API_automation_RecommendedAction.md) objects

## Errors
<a name="API_automation_ListRecommendedActions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 You do not have sufficient permissions to perform this action.
HTTP Status Code: 400

 ** ForbiddenException **
 You are not authorized to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
 An internal error occurred while processing the request.
HTTP Status Code: 500

 ** InvalidParameterValueException **
 One or more parameter values are not valid.
HTTP Status Code: 400

 ** OptInRequiredException **
 The account must be opted in to Compute Optimizer Automation before performing this action.
HTTP Status Code: 400

 ** ServiceUnavailableException **
 The service is temporarily unavailable.
HTTP Status Code: 500

 ** ThrottlingException **
 The request was denied due to request throttling.
HTTP Status Code: 400

## See Also
<a name="API_automation_ListRecommendedActions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/compute-optimizer-automation-2025-09-22/ListRecommendedActions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/compute-optimizer-automation-2025-09-22/ListRecommendedActions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-automation-2025-09-22/ListRecommendedActions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/compute-optimizer-automation-2025-09-22/ListRecommendedActions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-automation-2025-09-22/ListRecommendedActions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/compute-optimizer-automation-2025-09-22/ListRecommendedActions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/compute-optimizer-automation-2025-09-22/ListRecommendedActions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/compute-optimizer-automation-2025-09-22/ListRecommendedActions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/compute-optimizer-automation-2025-09-22/ListRecommendedActions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-automation-2025-09-22/ListRecommendedActions)
