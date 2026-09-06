---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_BillingAndCostManagementRecommendedActions_ListRecommendedActions.html
---

# ListRecommendedActions
<a name="API_BillingAndCostManagementRecommendedActions_ListRecommendedActions"></a>

Returns a list of recommended actions that match the filter criteria.

## Request Syntax
<a name="API_BillingAndCostManagementRecommendedActions_ListRecommendedActions_RequestSyntax"></a>

```
{
   "filter": {
      "actions": [
         {
            "key": "{{string}}",
            "matchOption": "{{string}}",
            "values": [ "{{string}}" ]
         }
      ]
   },
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_BillingAndCostManagementRecommendedActions_ListRecommendedActions_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [filter](#API_BillingAndCostManagementRecommendedActions_ListRecommendedActions_RequestSyntax) **   <a name="awscostmanagement-BillingAndCostManagementRecommendedActions_ListRecommendedActions-request-filter"></a>
The criteria that you want all returned recommended actions to match.
Type: [RequestFilter](API_BillingAndCostManagementRecommendedActions_RequestFilter.md) object
Required: No

 ** [maxResults](#API_BillingAndCostManagementRecommendedActions_ListRecommendedActions_RequestSyntax) **   <a name="awscostmanagement-BillingAndCostManagementRecommendedActions_ListRecommendedActions-request-maxResults"></a>
The maximum number of results to return in the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_BillingAndCostManagementRecommendedActions_ListRecommendedActions_RequestSyntax) **   <a name="awscostmanagement-BillingAndCostManagementRecommendedActions_ListRecommendedActions-request-nextToken"></a>
The pagination token that indicates the next set of results that you want to retrieve.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: `[\S\s]*`
Required: No

## Response Syntax
<a name="API_BillingAndCostManagementRecommendedActions_ListRecommendedActions_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "recommendedActions": [
      {
         "accountId": "string",
         "context": {
            "string" : "string"
         },
         "feature": "string",
         "id": "string",
         "lastUpdatedTimeStamp": "string",
         "nextSteps": [ "string" ],
         "severity": "string",
         "type": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BillingAndCostManagementRecommendedActions_ListRecommendedActions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_BillingAndCostManagementRecommendedActions_ListRecommendedActions_ResponseSyntax) **   <a name="awscostmanagement-BillingAndCostManagementRecommendedActions_ListRecommendedActions-response-nextToken"></a>
The pagination token that indicates the next set of results that you want to retrieve.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Pattern: `[\S\s]*`

 ** [recommendedActions](#API_BillingAndCostManagementRecommendedActions_ListRecommendedActions_ResponseSyntax) **   <a name="awscostmanagement-BillingAndCostManagementRecommendedActions_ListRecommendedActions-response-recommendedActions"></a>
The list of recommended actions that satisfy the filter criteria.
Type: Array of [RecommendedAction](API_BillingAndCostManagementRecommendedActions_RecommendedAction.md) objects

## Errors
<a name="API_BillingAndCostManagementRecommendedActions_ListRecommendedActions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
An unexpected error occurred during the processing of your request.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
 ** fieldList **
Lists each problematic field and why it failed validation.
 ** reason **
Provides a single, overarching explanation for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_BillingAndCostManagementRecommendedActions_ListRecommendedActions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bcm-recommended-actions-2024-11-14/ListRecommendedActions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bcm-recommended-actions-2024-11-14/ListRecommendedActions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-recommended-actions-2024-11-14/ListRecommendedActions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bcm-recommended-actions-2024-11-14/ListRecommendedActions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-recommended-actions-2024-11-14/ListRecommendedActions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bcm-recommended-actions-2024-11-14/ListRecommendedActions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bcm-recommended-actions-2024-11-14/ListRecommendedActions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bcm-recommended-actions-2024-11-14/ListRecommendedActions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bcm-recommended-actions-2024-11-14/ListRecommendedActions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-recommended-actions-2024-11-14/ListRecommendedActions)
