---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_payments_ListPaymentInstruments.html
---

# ListPaymentInstruments

Lists the payment instruments on your account. This operation returns summaries. To get the details that are specific to an instrument's payment method, use `GetPaymentInstrument`. Results are paginated. Use `nextToken` to retrieve more results.

To use this operation, you must have AWS Identity and Access Management (IAM) permission for `payments:ListPaymentInstruments`.

## Request Syntax
<a name="API_payments_ListPaymentInstruments_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_payments_ListPaymentInstruments_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_payments_ListPaymentInstruments_RequestSyntax) **   <a name="awscostmanagement-payments_ListPaymentInstruments-request-maxResults"></a>
The maximum number of payment instruments to return in one page. The default is 25. A page can contain fewer payment instruments even when more remain. Use `nextToken` to find out whether more payment instruments are available.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 25.
Required: No

 ** [nextToken](#API_payments_ListPaymentInstruments_RequestSyntax) **   <a name="awscostmanagement-payments_ListPaymentInstruments-request-nextToken"></a>
The pagination token from the `nextToken` of the previous response. Omit it to get the first page. Tokens expire. If the token is malformed or expired, or doesn't match the original request, the request fails with `ValidationException` and the reason `INVALID_PAGINATION_TOKEN`. In that case, start again from the first page.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_payments_ListPaymentInstruments_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "paymentInstrumentSummaries": [
      {
         "arn": "string",
         "createdAt": number,
         "id": "string",
         "paymentMethod": "string",
         "status": "string",
         "updatedAt": number
      }
   ]
}
```

## Response Elements
<a name="API_payments_ListPaymentInstruments_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_payments_ListPaymentInstruments_ResponseSyntax) **   <a name="awscostmanagement-payments_ListPaymentInstruments-response-nextToken"></a>
The pagination token that indicates the next set of results to retrieve. This value is absent when there are no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [paymentInstrumentSummaries](#API_payments_ListPaymentInstruments_ResponseSyntax) **   <a name="awscostmanagement-payments_ListPaymentInstruments-response-paymentInstrumentSummaries"></a>
The payment instruments on your account, one summary for each instrument. This list is empty when your account has no payment instruments.
Type: Array of [PaymentInstrumentSummary](API_payments_PaymentInstrumentSummary.md) objects
Array Members: Minimum number of 0 items. Maximum number of 25 items.

## Errors
<a name="API_payments_ListPaymentInstruments_Errors"></a>

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
<a name="API_payments_ListPaymentInstruments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/payments-2026-09-23/ListPaymentInstruments)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/payments-2026-09-23/ListPaymentInstruments)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payments-2026-09-23/ListPaymentInstruments)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/payments-2026-09-23/ListPaymentInstruments)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payments-2026-09-23/ListPaymentInstruments)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/payments-2026-09-23/ListPaymentInstruments)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/payments-2026-09-23/ListPaymentInstruments)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/payments-2026-09-23/ListPaymentInstruments)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/payments-2026-09-23/ListPaymentInstruments)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payments-2026-09-23/ListPaymentInstruments)
