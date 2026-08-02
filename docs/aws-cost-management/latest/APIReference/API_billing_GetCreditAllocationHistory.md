---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_GetCreditAllocationHistory.html
---

# GetCreditAllocationHistory
<a name="API_billing_GetCreditAllocationHistory"></a>

Returns the per-billing-month allocation history for credits applied to an AWS account's bills. Traverses the consolidated billing family to capture cross-account credit applications. Supports pagination and optional filtering to a single credit.

## Request Syntax
<a name="API_billing_GetCreditAllocationHistory_RequestSyntax"></a>

```
{
   "accountId": "{{string}}",
   "creditId": {{number}},
   "endDate": {{number}},
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "startDate": {{number}}
}
```

## Request Parameters
<a name="API_billing_GetCreditAllocationHistory_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [accountId](#API_billing_GetCreditAllocationHistory_RequestSyntax) **   <a name="awscostmanagement-billing_GetCreditAllocationHistory-request-accountId"></a>
The AWS account ID whose allocation history to retrieve. Must be a 12-digit numeric string.
Type: String
Pattern: `[0-9]{12}`
Required: Yes

 ** [creditId](#API_billing_GetCreditAllocationHistory_RequestSyntax) **   <a name="awscostmanagement-billing_GetCreditAllocationHistory-request-creditId"></a>
Filters the result to a single credit. When omitted, returns allocation entries for all credits.
Type: Long
Required: No

 ** [endDate](#API_billing_GetCreditAllocationHistory_RequestSyntax) **   <a name="awscostmanagement-billing_GetCreditAllocationHistory-request-endDate"></a>
Inclusive end date as Unix epoch seconds.
Type: Timestamp
Required: Yes

 ** [maxResults](#API_billing_GetCreditAllocationHistory_RequestSyntax) **   <a name="awscostmanagement-billing_GetCreditAllocationHistory-request-maxResults"></a>
The maximum number of records to return per page. Range: 1 to 1000. Default: 100.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_billing_GetCreditAllocationHistory_RequestSyntax) **   <a name="awscostmanagement-billing_GetCreditAllocationHistory-request-nextToken"></a>
Pagination token from a previous response. Pass the value returned in `nextToken` to retrieve the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4095.
Pattern: `[-a-zA-Z0-9+=/_]+`
Required: No

 ** [startDate](#API_billing_GetCreditAllocationHistory_RequestSyntax) **   <a name="awscostmanagement-billing_GetCreditAllocationHistory-request-startDate"></a>
Inclusive start date as Unix epoch seconds. Must be on or before `endDate`. The range from `startDate` to `endDate` cannot exceed 24 billing months.
Type: Timestamp
Required: Yes

## Response Syntax
<a name="API_billing_GetCreditAllocationHistory_ResponseSyntax"></a>

```
{
   "creditAllocationHistoryList": [
      {
         "accountId": "string",
         "appliedServiceName": "string",
         "billingMonth": "string",
         "creditAmount": {
            "currencyAmount": "string",
            "currencyCode": "string"
         },
         "creditId": "string",
         "description": "string",
         "isEstimatedBill": boolean
      }
   ],
   "failedMonths": [ "string" ],
   "nextToken": "string",
   "partialResults": boolean
}
```

## Response Elements
<a name="API_billing_GetCreditAllocationHistory_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [creditAllocationHistoryList](#API_billing_GetCreditAllocationHistory_ResponseSyntax) **   <a name="awscostmanagement-billing_GetCreditAllocationHistory-response-creditAllocationHistoryList"></a>
Allocation entries sorted by `billingMonth` in descending order.
Type: Array of [CreditAllocationHistoryEntry](API_billing_CreditAllocationHistoryEntry.md) objects

 ** [failedMonths](#API_billing_GetCreditAllocationHistory_ResponseSyntax) **   <a name="awscostmanagement-billing_GetCreditAllocationHistory-response-failedMonths"></a>
Billing months in `YYYY-MM` format that failed to return data. Non-empty only when `partialResults` is `true`.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 7.

 ** [nextToken](#API_billing_GetCreditAllocationHistory_ResponseSyntax) **   <a name="awscostmanagement-billing_GetCreditAllocationHistory-response-nextToken"></a>
Pagination token. Present when more pages are available; `null` when there are no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4095.
Pattern: `[-a-zA-Z0-9+=/_]+`

 ** [partialResults](#API_billing_GetCreditAllocationHistory_ResponseSyntax) **   <a name="awscostmanagement-billing_GetCreditAllocationHistory-response-partialResults"></a>
 `true` when data could not be retrieved for one or more billing months. The `failedMonths` field lists which months are missing.
Type: Boolean

## Errors
<a name="API_billing_GetCreditAllocationHistory_Errors"></a>

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
<a name="API_billing_GetCreditAllocationHistory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/billing-2023-09-07/GetCreditAllocationHistory)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/billing-2023-09-07/GetCreditAllocationHistory)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/GetCreditAllocationHistory)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/billing-2023-09-07/GetCreditAllocationHistory)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/GetCreditAllocationHistory)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/billing-2023-09-07/GetCreditAllocationHistory)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/billing-2023-09-07/GetCreditAllocationHistory)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/billing-2023-09-07/GetCreditAllocationHistory)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/billing-2023-09-07/GetCreditAllocationHistory)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/GetCreditAllocationHistory)
