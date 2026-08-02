---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_GetCredits.html
---

# GetCredits
<a name="API_billing_GetCredits"></a>

Returns the list of AWS account credits for the specified account. Each credit includes its identifier, type, monetary amounts, applicable products, expiration, sharing configuration, and current enabled status.

When the caller is the management account of a consolidated billing family and `payerAccountFlag` is `true`, the response aggregates credits across the entire family. Otherwise, the response includes only credits owned by the account specified in `accountId`.

## Request Syntax
<a name="API_billing_GetCredits_RequestSyntax"></a>

```
{
   "accountId": "{{string}}",
   "endDate": {{number}},
   "payerAccountFlag": {{boolean}},
   "startDate": {{number}}
}
```

## Request Parameters
<a name="API_billing_GetCredits_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [accountId](#API_billing_GetCredits_RequestSyntax) **   <a name="awscostmanagement-billing_GetCredits-request-accountId"></a>
The AWS account ID. Must be a 12-digit numeric string.
Type: String
Required: Yes

 ** [endDate](#API_billing_GetCredits_RequestSyntax) **   <a name="awscostmanagement-billing_GetCredits-request-endDate"></a>
The end date for the credit period as Unix epoch seconds. Must not be a future date and must be on or after `startDate`. Defaults to the current date when omitted.
Type: Timestamp
Required: No

 ** [payerAccountFlag](#API_billing_GetCredits_RequestSyntax) **   <a name="awscostmanagement-billing_GetCredits-request-payerAccountFlag"></a>
When `true` and the caller is the management account, the response aggregates credits across the entire consolidated billing family. When `false` or omitted, returns only credits for the specified `accountId`.
Type: Boolean
Required: No

 ** [startDate](#API_billing_GetCredits_RequestSyntax) **   <a name="awscostmanagement-billing_GetCredits-request-startDate"></a>
The start date for the credit period as Unix epoch seconds. Must be a past date that is not more than one year before the current date.
Type: Timestamp
Required: Yes

## Response Syntax
<a name="API_billing_GetCredits_ResponseSyntax"></a>

```
{
   "credits": [
      {
         "accountHasCreditSharingEnabled": boolean,
         "accountId": "string",
         "applicableProductNames": [ "string" ],
         "applicationType": "string",
         "costCategoryArn": "string",
         "creditConsoleVisibility": "string",
         "creditId": "string",
         "creditSharingType": "string",
         "creditStatus": "string",
         "creditType": "string",
         "description": "string",
         "endDate": number,
         "estimatedAmount": {
            "currencyAmount": "string",
            "currencyCode": "string"
         },
         "exhaustDate": number,
         "initialAmount": {
            "currencyAmount": "string",
            "currencyCode": "string"
         },
         "purchaseTypeApplications": [ "string" ],
         "remainingAmount": {
            "currencyAmount": "string",
            "currencyCode": "string"
         },
         "ruleName": "string",
         "shareableAccounts": [ "string" ],
         "startDate": number
      }
   ]
}
```

## Response Elements
<a name="API_billing_GetCredits_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [credits](#API_billing_GetCredits_ResponseSyntax) **   <a name="awscostmanagement-billing_GetCredits-response-credits"></a>
The list of credits matching the request. Returns an empty list when no credits exist.
Type: Array of [CreditData](API_billing_CreditData.md) objects

## Errors
<a name="API_billing_GetCredits_Errors"></a>

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
<a name="API_billing_GetCredits_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/billing-2023-09-07/GetCredits)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/billing-2023-09-07/GetCredits)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/GetCredits)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/billing-2023-09-07/GetCredits)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/GetCredits)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/billing-2023-09-07/GetCredits)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/billing-2023-09-07/GetCredits)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/billing-2023-09-07/GetCredits)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/billing-2023-09-07/GetCredits)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/GetCredits)
