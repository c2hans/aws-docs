---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_GetBillingPreferences.html
---

# GetBillingPreferences
<a name="API_billing_GetBillingPreferences"></a>

Retrieves billing preferences for the specified feature. Each feature controls a distinct billing capability: which accounts can share Reserved Instances or credits, whether billing alerts are enabled, the historical record of sharing changes, and per-credit options.

## Request Syntax
<a name="API_billing_GetBillingPreferences_RequestSyntax"></a>

```
{
   "features": [ "{{string}}" ],
   "filters": [
      {
         "name": "{{string}}",
         "value": [ "{{string}}" ]
      }
   ],
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_billing_GetBillingPreferences_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [features](#API_billing_GetBillingPreferences_RequestSyntax) **   <a name="awscostmanagement-billing_GetBillingPreferences-request-features"></a>
The feature to retrieve. Specify exactly one value. Valid values: `BILLING_ALERTS`, `RI_SHARING`, `RI_SHARING_HISTORY`, `CREDIT_SHARING`, `CREDIT_SHARING_HISTORY`, `CREDIT_LEVEL_SHARING`, `CREDIT_PREFERENCE_OPTIONS`.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `RI_SHARING | RI_SHARING_HISTORY | CREDIT_SHARING | CREDIT_SHARING_HISTORY | CREDIT_LEVEL_SHARING | BILLING_ALERTS | CREDIT_PREFERENCE_OPTIONS`
Required: Yes

 ** [filters](#API_billing_GetBillingPreferences_RequestSyntax) **   <a name="awscostmanagement-billing_GetBillingPreferences-request-filters"></a>
Filters to narrow results. Specify exactly one filter when supplied. The supported filter name is `PREFERENCE_KEY`, which accepts 1 to 10 values to match preference keys.
Type: Array of [BillingFeatureFilter](API_billing_BillingFeatureFilter.md) objects
Array Members: Fixed number of 1 item.
Required: No

 ** [maxResults](#API_billing_GetBillingPreferences_RequestSyntax) **   <a name="awscostmanagement-billing_GetBillingPreferences-request-maxResults"></a>
The maximum number of records to return per page. Range: 1 to 50. Default: 50.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [nextToken](#API_billing_GetBillingPreferences_RequestSyntax) **   <a name="awscostmanagement-billing_GetBillingPreferences-request-nextToken"></a>
Pagination token from a previous response. Pass the value returned in `nextToken` to retrieve the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4095.
Pattern: `[-a-zA-Z0-9+=/_]+`
Required: No

## Response Syntax
<a name="API_billing_GetBillingPreferences_ResponseSyntax"></a>

```
{
   "billingPreferences": [
      {
         "accountId": "string",
         "accountName": "string",
         "billingPeriod": {
            "month": number,
            "year": number
         },
         "feature": "string",
         "key": "string",
         "value": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_billing_GetBillingPreferences_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [billingPreferences](#API_billing_GetBillingPreferences_ResponseSyntax) **   <a name="awscostmanagement-billing_GetBillingPreferences-response-billingPreferences"></a>
The list of preference entries matching the request.
Type: Array of [BillingPreferenceSummary](API_billing_BillingPreferenceSummary.md) objects

 ** [nextToken](#API_billing_GetBillingPreferences_ResponseSyntax) **   <a name="awscostmanagement-billing_GetBillingPreferences-response-nextToken"></a>
Pagination token. Present when more pages are available; `null` when there are no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4095.
Pattern: `[-a-zA-Z0-9+=/_]+`

## Errors
<a name="API_billing_GetBillingPreferences_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
The request processing failed because of an unknown error, exception, or failure.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
 ** fieldList **
The input fails to satisfy the constraints specified by an AWS service.
 ** reason **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_billing_GetBillingPreferences_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/billing-2023-09-07/GetBillingPreferences)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/billing-2023-09-07/GetBillingPreferences)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/GetBillingPreferences)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/billing-2023-09-07/GetBillingPreferences)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/GetBillingPreferences)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/billing-2023-09-07/GetBillingPreferences)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/billing-2023-09-07/GetBillingPreferences)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/billing-2023-09-07/GetBillingPreferences)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/billing-2023-09-07/GetBillingPreferences)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/GetBillingPreferences)
