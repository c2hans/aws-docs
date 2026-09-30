---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_ListBusinessSupportSubscriptionHistory.html
---

# ListBusinessSupportSubscriptionHistory
<a name="API_billing_ListBusinessSupportSubscriptionHistory"></a>

Returns the history of Business Support subscription contracts across accounts.

## Request Syntax
<a name="API_billing_ListBusinessSupportSubscriptionHistory_RequestSyntax"></a>

```
{
   "accountId": "{{string}}",
   "billingMonth": "{{string}}",
   "endDate": {{number}},
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "startDate": {{number}}
}
```

## Request Parameters
<a name="API_billing_ListBusinessSupportSubscriptionHistory_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [accountId](#API_billing_ListBusinessSupportSubscriptionHistory_RequestSyntax) **   <a name="awscostmanagement-billing_ListBusinessSupportSubscriptionHistory-request-accountId"></a>
The account ID to filter results to a specific account. If you don't specify a value, the response includes subscription history for all accounts.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** [billingMonth](#API_billing_ListBusinessSupportSubscriptionHistory_RequestSyntax) **   <a name="awscostmanagement-billing_ListBusinessSupportSubscriptionHistory-request-billingMonth"></a>
The billing month to retrieve subscription contracts for, in YYYY-MM format. If you don't specify a value, defaults to the current month.
Type: String
Pattern: `\d{4}-(0[1-9]|1[0-2])`
Required: No

 ** [endDate](#API_billing_ListBusinessSupportSubscriptionHistory_RequestSyntax) **   <a name="awscostmanagement-billing_ListBusinessSupportSubscriptionHistory-request-endDate"></a>
The end date to filter subscription contracts to.
Type: Timestamp
Required: No

 ** [maxResults](#API_billing_ListBusinessSupportSubscriptionHistory_RequestSyntax) **   <a name="awscostmanagement-billing_ListBusinessSupportSubscriptionHistory-request-maxResults"></a>
The maximum number of results to return per page. Default is 100.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_billing_ListBusinessSupportSubscriptionHistory_RequestSyntax) **   <a name="awscostmanagement-billing_ListBusinessSupportSubscriptionHistory-request-nextToken"></a>
The pagination token for the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4095.
Pattern: `[-a-zA-Z0-9+=/_]+`
Required: No

 ** [startDate](#API_billing_ListBusinessSupportSubscriptionHistory_RequestSyntax) **   <a name="awscostmanagement-billing_ListBusinessSupportSubscriptionHistory-request-startDate"></a>
The start date to filter subscription contracts from.
Type: Timestamp
Required: No

## Response Syntax
<a name="API_billing_ListBusinessSupportSubscriptionHistory_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "subscriptionContracts": [
      {
         "accountId": "string",
         "contractEndDate": number,
         "contractStartDate": number,
         "planName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_billing_ListBusinessSupportSubscriptionHistory_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_billing_ListBusinessSupportSubscriptionHistory_ResponseSyntax) **   <a name="awscostmanagement-billing_ListBusinessSupportSubscriptionHistory-response-nextToken"></a>
The pagination token for the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4095.
Pattern: `[-a-zA-Z0-9+=/_]+`

 ** [subscriptionContracts](#API_billing_ListBusinessSupportSubscriptionHistory_ResponseSyntax) **   <a name="awscostmanagement-billing_ListBusinessSupportSubscriptionHistory-response-subscriptionContracts"></a>
The list of Business Support subscription contracts.
Type: Array of [BusinessSupportSubscriptionContract](API_billing_BusinessSupportSubscriptionContract.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1000 items.

## Errors
<a name="API_billing_ListBusinessSupportSubscriptionHistory_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
The request processing failed because of an unknown error, exception, or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
 The specified ARN in the request doesn't exist.
 ** resourceId **
 Value is a list of resource IDs that were not found.
 ** resourceType **
 Value is the type of resource that was not found.
HTTP Status Code: 400

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
<a name="API_billing_ListBusinessSupportSubscriptionHistory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/billing-2023-09-07/ListBusinessSupportSubscriptionHistory)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/billing-2023-09-07/ListBusinessSupportSubscriptionHistory)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/ListBusinessSupportSubscriptionHistory)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/billing-2023-09-07/ListBusinessSupportSubscriptionHistory)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/ListBusinessSupportSubscriptionHistory)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/billing-2023-09-07/ListBusinessSupportSubscriptionHistory)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/billing-2023-09-07/ListBusinessSupportSubscriptionHistory)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/billing-2023-09-07/ListBusinessSupportSubscriptionHistory)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/billing-2023-09-07/ListBusinessSupportSubscriptionHistory)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/ListBusinessSupportSubscriptionHistory)
