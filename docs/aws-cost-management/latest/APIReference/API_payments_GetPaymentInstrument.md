---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_payments_GetPaymentInstrument.html
---

# GetPaymentInstrument

Retrieves a payment instrument on your account, including the details that are specific to its payment method, such as a card's last four digits. Identify the instrument by its Amazon Resource Name (ARN) or by its ID. `ListPaymentInstruments` returns both.

To use this operation, you must have AWS Identity and Access Management (IAM) permission for `payments:GetPaymentInstrument`. You can scope this permission to the instrument's ARN.

## Request Syntax
<a name="API_payments_GetPaymentInstrument_RequestSyntax"></a>

```
{
   "identifier": "{{string}}"
}
```

## Request Parameters
<a name="API_payments_GetPaymentInstrument_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [identifier](#API_payments_GetPaymentInstrument_RequestSyntax) **   <a name="awscostmanagement-payments_GetPaymentInstrument-request-identifier"></a>
The instrument to retrieve. Specify one of the following:
+ The Amazon Resource Name (ARN) of the instrument, as `ListPaymentInstruments` returns in `arn`. The ARN must be for an instrument on your account.
+ The ID of the instrument, as `ListPaymentInstruments` returns in `id`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(arn:[a-z0-9-]+:payments::[0-9]{12}:payment-instrument:[a-z0-9-]{1,64}|[a-z0-9-]{1,64})`
Required: Yes

## Response Syntax
<a name="API_payments_GetPaymentInstrument_ResponseSyntax"></a>

```
{
   "paymentInstrument": {
      "arn": "string",
      "createdAt": number,
      "details": { ... },
      "paymentMethod": "string",
      "status": "string",
      "updatedAt": number
   }
}
```

## Response Elements
<a name="API_payments_GetPaymentInstrument_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [paymentInstrument](#API_payments_GetPaymentInstrument_ResponseSyntax) **   <a name="awscostmanagement-payments_GetPaymentInstrument-response-paymentInstrument"></a>
The payment instrument, including the details that are specific to its payment method.
Type: [PaymentInstrument](API_payments_PaymentInstrument.md) object

## Errors
<a name="API_payments_GetPaymentInstrument_Errors"></a>

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
<a name="API_payments_GetPaymentInstrument_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/payments-2026-09-23/GetPaymentInstrument)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/payments-2026-09-23/GetPaymentInstrument)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payments-2026-09-23/GetPaymentInstrument)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/payments-2026-09-23/GetPaymentInstrument)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payments-2026-09-23/GetPaymentInstrument)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/payments-2026-09-23/GetPaymentInstrument)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/payments-2026-09-23/GetPaymentInstrument)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/payments-2026-09-23/GetPaymentInstrument)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/payments-2026-09-23/GetPaymentInstrument)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payments-2026-09-23/GetPaymentInstrument)
