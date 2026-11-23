---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_payments_BatchGetFinancialRecord.html
---

# BatchGetFinancialRecord

Retrieves up to 100 financial records in one request, including the details that are specific to each record's type. Identify each record by its ID or by its invoice ID. Results can be partial: each key that you request appears once in the response, either as a record in `financialRecords` or as an error in `errors`. A key that matches no record on your account is returned in `errors` and doesn't fail the request. This operation provides strongly consistent reads.

To use this operation, you must have AWS Identity and Access Management (IAM) permission for both `payments:BatchGetFinancialRecord` and `payments:GetPaymentStatus`.

## Request Syntax
<a name="API_payments_BatchGetFinancialRecord_RequestSyntax"></a>

```
{
   "keys": [
      { ... }
   ]
}
```

## Request Parameters
<a name="API_payments_BatchGetFinancialRecord_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [keys](#API_payments_BatchGetFinancialRecord_RequestSyntax) **   <a name="awscostmanagement-payments_BatchGetFinancialRecord-request-keys"></a>
The keys of the financial records to retrieve. Each key is either the record's ID or its invoice ID.
Type: Array of [FinancialRecordKey](API_payments_FinancialRecordKey.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: Yes

## Response Syntax
<a name="API_payments_BatchGetFinancialRecord_ResponseSyntax"></a>

```
{
   "errors": [
      {
         "code": "string",
         "key": { ... },
         "message": "string"
      }
   ],
   "financialRecords": [
      {
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
   ]
}
```

## Response Elements
<a name="API_payments_BatchGetFinancialRecord_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [errors](#API_payments_BatchGetFinancialRecord_ResponseSyntax) **   <a name="awscostmanagement-payments_BatchGetFinancialRecord-response-errors"></a>
The errors for the records that the operation couldn't retrieve, one for each record, with the key as you requested it and the reason. This list is empty when the operation retrieved every record.
Type: Array of [FinancialRecordError](API_payments_FinancialRecordError.md) objects

 ** [financialRecords](#API_payments_BatchGetFinancialRecord_ResponseSyntax) **   <a name="awscostmanagement-payments_BatchGetFinancialRecord-response-financialRecords"></a>
The financial records that the operation retrieved, in no particular order. This list contains fewer records than you requested when `errors` names one or more keys.
Type: Array of [FinancialRecord](API_payments_FinancialRecord.md) objects

## Errors
<a name="API_payments_BatchGetFinancialRecord_Errors"></a>

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
<a name="API_payments_BatchGetFinancialRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/payments-2026-09-23/BatchGetFinancialRecord)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/payments-2026-09-23/BatchGetFinancialRecord)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payments-2026-09-23/BatchGetFinancialRecord)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/payments-2026-09-23/BatchGetFinancialRecord)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payments-2026-09-23/BatchGetFinancialRecord)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/payments-2026-09-23/BatchGetFinancialRecord)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/payments-2026-09-23/BatchGetFinancialRecord)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/payments-2026-09-23/BatchGetFinancialRecord)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/payments-2026-09-23/BatchGetFinancialRecord)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payments-2026-09-23/BatchGetFinancialRecord)
