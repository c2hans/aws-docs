---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_payments_ListFinancialRecords.html
---

# ListFinancialRecords

Lists the financial records on your account, with the newest first by default. A financial record is an invoice or a credit memo. You must specify at least one record type in `types`. You can narrow the results further by settlement status and issue date. This operation returns summaries. To get the details that are specific to a record's type, use `GetFinancialRecord` or `BatchGetFinancialRecord`. Results are paginated. Use `nextToken` to retrieve more results.

To use this operation, you must have AWS Identity and Access Management (IAM) permission for both `payments:ListFinancialRecords` and `payments:GetPaymentStatus`.

## Request Syntax
<a name="API_payments_ListFinancialRecords_RequestSyntax"></a>

```
{
   "issuedAfter": {{number}},
   "issuedBefore": {{number}},
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "settlementStatuses": [ "{{string}}" ],
   "sortBy": "{{string}}",
   "sortOrder": "{{string}}",
   "types": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_payments_ListFinancialRecords_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [issuedAfter](#API_payments_ListFinancialRecords_RequestSyntax) **   <a name="awscostmanagement-payments_ListFinancialRecords-request-issuedAfter"></a>
The earliest date and time to return records for, inclusive. The operation returns the records that were issued at or after this time.
Type: Timestamp
Required: No

 ** [issuedBefore](#API_payments_ListFinancialRecords_RequestSyntax) **   <a name="awscostmanagement-payments_ListFinancialRecords-request-issuedBefore"></a>
The latest date and time to return records for, exclusive. The operation returns the records that were issued before this time. When you specify both `issuedAfter` and `issuedBefore`, `issuedBefore` must be later than `issuedAfter`.
Type: Timestamp
Required: No

 ** [maxResults](#API_payments_ListFinancialRecords_RequestSyntax) **   <a name="awscostmanagement-payments_ListFinancialRecords-request-maxResults"></a>
The maximum number of results to return in one page. The default is 100. A page can contain fewer results even when more remain. Use `nextToken` to find out whether more results are available.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_payments_ListFinancialRecords_RequestSyntax) **   <a name="awscostmanagement-payments_ListFinancialRecords-request-nextToken"></a>
The pagination token from the `nextToken` of the previous response. Omit it to get the first page. Tokens expire. If the token is malformed or expired, or doesn't match the original request, the request fails with `ValidationException` and the reason `INVALID_PAGINATION_TOKEN`. In that case, start again from the first page.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [settlementStatuses](#API_payments_ListFinancialRecords_RequestSyntax) **   <a name="awscostmanagement-payments_ListFinancialRecords-request-settlementStatuses"></a>
The settlement statuses to filter by. `OPEN` returns records whose `status` is `OUTSTANDING` or `PROCESSING`. `CLOSED` returns records whose `status` is `SETTLED` or `CANCELED`. When you omit this member, the operation returns records with both settlement statuses.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Valid Values: `OPEN | CLOSED`
Required: No

 ** [sortBy](#API_payments_ListFinancialRecords_RequestSyntax) **   <a name="awscostmanagement-payments_ListFinancialRecords-request-sortBy"></a>
The field to sort the results by. The default is `ISSUED_AT`, the date and time when the record was issued.
Type: String
Valid Values: `ISSUED_AT`
Required: No

 ** [sortOrder](#API_payments_ListFinancialRecords_RequestSyntax) **   <a name="awscostmanagement-payments_ListFinancialRecords-request-sortOrder"></a>
The order to sort the results in. The default is `DESCENDING`, which returns the newest records first. `ASCENDING` returns the oldest records first.
Type: String
Valid Values: `ASCENDING | DESCENDING`
Required: No

 ** [types](#API_payments_ListFinancialRecords_RequestSyntax) **   <a name="awscostmanagement-payments_ListFinancialRecords-request-types"></a>
The financial record types to return. The following values are valid:
+  `INVOICE` – An invoice: a bill from AWS. Payments and credit memos applied to the invoice settle it.
+  `CREDIT_MEMO` – A credit memo: a credit issued to your account, for example for a billing correction or a service credit. Applying it to one or more invoices settles it.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Valid Values: `INVOICE | CREDIT_MEMO`
Required: Yes

## Response Syntax
<a name="API_payments_ListFinancialRecords_ResponseSyntax"></a>

```
{
   "financialRecordSummaries": [
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
         "id": "string",
         "issuedAt": number,
         "settlementStatus": "string",
         "status": "string",
         "type": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_payments_ListFinancialRecords_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [financialRecordSummaries](#API_payments_ListFinancialRecords_ResponseSyntax) **   <a name="awscostmanagement-payments_ListFinancialRecords-response-financialRecordSummaries"></a>
The financial record summaries that match your filters, in the requested order. This list is empty when no record matches.
Type: Array of [FinancialRecordSummary](API_payments_FinancialRecordSummary.md) objects

 ** [nextToken](#API_payments_ListFinancialRecords_ResponseSyntax) **   <a name="awscostmanagement-payments_ListFinancialRecords-response-nextToken"></a>
The pagination token that indicates the next set of results to retrieve. This value is absent when there are no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_payments_ListFinancialRecords_Errors"></a>

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
<a name="API_payments_ListFinancialRecords_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/payments-2026-09-23/ListFinancialRecords)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/payments-2026-09-23/ListFinancialRecords)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payments-2026-09-23/ListFinancialRecords)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/payments-2026-09-23/ListFinancialRecords)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payments-2026-09-23/ListFinancialRecords)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/payments-2026-09-23/ListFinancialRecords)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/payments-2026-09-23/ListFinancialRecords)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/payments-2026-09-23/ListFinancialRecords)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/payments-2026-09-23/ListFinancialRecords)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payments-2026-09-23/ListFinancialRecords)
