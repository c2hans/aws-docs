---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_payments_GetFinancialRecord.html
---

# GetFinancialRecord

Retrieves a single financial record, including the details that are specific to its type. Specify exactly one of the following:
+ The ID that AWS Payments issued for the record, in `identifier`.
+ The invoice ID that AWS Invoicing issued for an invoice or a credit memo, in `invoiceIdentifier`.

If you specify both or neither, the request fails with `ValidationException`. If no record on your account matches, the request fails with `ResourceNotFoundException`.

This operation provides strongly consistent reads.

To use this operation, you must have AWS Identity and Access Management (IAM) permission for both `payments:GetFinancialRecord` and `payments:GetPaymentStatus`.

## Request Syntax
<a name="API_payments_GetFinancialRecord_RequestSyntax"></a>

```
{
   "identifier": "{{string}}",
   "invoiceIdentifier": "{{string}}"
}
```

## Request Parameters
<a name="API_payments_GetFinancialRecord_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [identifier](#API_payments_GetFinancialRecord_RequestSyntax) **   <a name="awscostmanagement-payments_GetFinancialRecord-request-identifier"></a>
The ID that AWS Payments issued for the financial record, as returned in `id`.
Type: String
Length Constraints: Minimum length of 17. Maximum length of 23.
Pattern: `[A-Z]{2,3}-[0-9]{4}-[0-9]{4}-[0-9]{4}(-[0-9]{4})?`
Required: No

 ** [invoiceIdentifier](#API_payments_GetFinancialRecord_RequestSyntax) **   <a name="awscostmanagement-payments_GetFinancialRecord-request-invoiceIdentifier"></a>
The invoice ID that AWS Invoicing issued for an invoice or a credit memo. The operation returns the record that has this invoice ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `\S(.*\S)?`
Required: No

## Response Syntax
<a name="API_payments_GetFinancialRecord_ResponseSyntax"></a>

```
{
   "financialRecord": {
      "amount": {
         "currency": "string",
         "value": "string"
      },
      "balances": {
         "canceled": {
            "currency": "string",
            "value": "string"
         },
         "outstanding": {
            "currency": "string",
            "value": "string"
         },
         "processing": {
            "currency": "string",
            "value": "string"
         },
         "settled": {
            "currency": "string",
            "value": "string"
         }
      },
      "businessUnit": {
         "lineOfBusiness": "string",
         "merchantOfRecord": "string"
      },
      "closedAt": number,
      "details": { ... },
      "id": "string",
      "issuedAt": number,
      "settlementStatus": "string",
      "status": "string",
      "type": "string"
   }
}
```

## Response Elements
<a name="API_payments_GetFinancialRecord_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [financialRecord](#API_payments_GetFinancialRecord_ResponseSyntax) **   <a name="awscostmanagement-payments_GetFinancialRecord-response-financialRecord"></a>
The requested financial record.
Type: [FinancialRecord](API_payments_FinancialRecord.md) object

## Errors
<a name="API_payments_GetFinancialRecord_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request is denied because you don't have sufficient access to perform this operation. Verify that you have the required permissions and try again. This error is also returned, instead of `ResourceNotFoundException`, when you aren't authorized for the resource, so the response doesn't reveal whether the resource exists.
 ** reason **
The reason that access was denied. The following values are valid:
+  `NOT_AUTHORIZED` – Your IAM policies don't allow this action.
+  `INVALID_ACCOUNT_STATE` – Your AWS account isn't in a state that allows this action, for example because registration isn't complete or the account is suspended.
+  `OTHER` – Access was denied for another reason.
HTTP Status Code: 400

 ** InternalServerException **
The request processing failed because of an unknown error, exception, or failure. Retry your request.
 ** retryAfterSeconds **
The suggested number of seconds to wait before retrying the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource couldn't be found. Verify that the resource ID is correct. This error is returned only when you're authorized for the resource.
 ** resourceId **
The ID of the resource that wasn't found.
 ** resourceType **
The type of the resource that wasn't found.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling. Reduce the frequency of your requests and try again.
 ** retryAfterSeconds **
The suggested number of seconds to wait before retrying the request.
HTTP Status Code: 400

 ** ValidationException **
The request isn't valid. Check `reason` and `fieldList` for the cause, correct the request, and try again.
 ** fieldList **
The request members that failed validation. This member is populated when `reason` is `FIELD_VALIDATION_FAILED`.
 ** reason **
The reason that validation failed. The following values are valid:
+  `CANNOT_PARSE` – The request body couldn't be parsed, or a value isn't of the expected type.
+  `FIELD_VALIDATION_FAILED` – One or more members failed validation. `fieldList` names them.
+  `INVALID_PAGINATION_TOKEN` – The `nextToken` is malformed or expired, or doesn't match the original request. Start again from the first page.
+  `UNSUPPORTED_ACTION` – The request is well formed, but the action isn't supported for your account, Region, or resource.
+  `OTHER` – The request isn't valid for another reason.
HTTP Status Code: 400

## See Also
<a name="API_payments_GetFinancialRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/payments-2026-09-23/GetFinancialRecord)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/payments-2026-09-23/GetFinancialRecord)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payments-2026-09-23/GetFinancialRecord)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/payments-2026-09-23/GetFinancialRecord)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payments-2026-09-23/GetFinancialRecord)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/payments-2026-09-23/GetFinancialRecord)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/payments-2026-09-23/GetFinancialRecord)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/payments-2026-09-23/GetFinancialRecord)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/payments-2026-09-23/GetFinancialRecord)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payments-2026-09-23/GetFinancialRecord)
