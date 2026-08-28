---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_SendAgreementPaymentRequest.html
---

# SendAgreementPaymentRequest
<a name="API_marketplace-agreements_SendAgreementPaymentRequest"></a>

Allows sellers (proposers) to submit a payment request to buyers (acceptors) for a specific charge amount for an agreement that includes a `VariablePaymentTerm`. The payment request is created in `PENDING_APPROVAL` status, at which point the buyer can accept or reject it.

**Note**
The agreement must be active and have a `VariablePaymentTerm` to support payment requests. The `chargeAmount` must not exceed the remaining available balance under the `VariablePaymentTerm` `maxTotalChargeAmount`.

## Request Syntax
<a name="API_marketplace-agreements_SendAgreementPaymentRequest_RequestSyntax"></a>

```
{
   "agreementId": "{{string}}",
   "chargeAmount": "{{string}}",
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "name": "{{string}}",
   "termId": "{{string}}"
}
```

## Request Parameters
<a name="API_marketplace-agreements_SendAgreementPaymentRequest_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [agreementId](#API_marketplace-agreements_SendAgreementPaymentRequest_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_SendAgreementPaymentRequest-request-agreementId"></a>
The unique identifier of the agreement for which the payment request is being submitted. Use `GetAgreementTerms` to retrieve agreement term details.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_/-]+`
Required: Yes

 ** [chargeAmount](#API_marketplace-agreements_SendAgreementPaymentRequest_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_SendAgreementPaymentRequest-request-chargeAmount"></a>
The amount requested to be charged to the buyer, positive decimal value in the currency of the accepted term.
A `ValidationException` is returned if the `chargeAmount` exceeds the available balance, if the agreement doesn't have an active `VariablePaymentTerm`, or if the `termId` is invalid.
Type: String
Pattern: `[0-9]*(\.[0-9]{0,8})?`
Required: Yes

 ** [name](#API_marketplace-agreements_SendAgreementPaymentRequest_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_SendAgreementPaymentRequest-request-name"></a>
A descriptive name for the payment request (5-64 characters).
Type: String
Length Constraints: Minimum length of 5. Maximum length of 64.
Pattern: `.+`
Required: Yes

 ** [termId](#API_marketplace-agreements_SendAgreementPaymentRequest_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_SendAgreementPaymentRequest-request-termId"></a>
The unique identifier of the `VariablePaymentTerm` for the agreement that the payment request is being sent for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9+=;,.@\-_]+`
Required: Yes

 ** [clientToken](#API_marketplace-agreements_SendAgreementPaymentRequest_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_SendAgreementPaymentRequest-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`
Required: No

 ** [description](#API_marketplace-agreements_SendAgreementPaymentRequest_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_SendAgreementPaymentRequest-request-description"></a>
An optional detailed description of the payment request (1-2000 characters).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Required: No

## Response Syntax
<a name="API_marketplace-agreements_SendAgreementPaymentRequest_ResponseSyntax"></a>

```
{
   "agreementId": "string",
   "chargeAmount": "string",
   "createdAt": number,
   "currencyCode": "string",
   "description": "string",
   "name": "string",
   "paymentRequestId": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_marketplace-agreements_SendAgreementPaymentRequest_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [agreementId](#API_marketplace-agreements_SendAgreementPaymentRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_SendAgreementPaymentRequest-response-agreementId"></a>
The agreement identifier for this payment request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_/-]+`

 ** [chargeAmount](#API_marketplace-agreements_SendAgreementPaymentRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_SendAgreementPaymentRequest-response-chargeAmount"></a>
The amount being charged to the buyer.
Type: String
Pattern: `[0-9]*(\.[0-9]{0,8})?`

 ** [createdAt](#API_marketplace-agreements_SendAgreementPaymentRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_SendAgreementPaymentRequest-response-createdAt"></a>
The time when the payment request was created.
Type: Timestamp

 ** [currencyCode](#API_marketplace-agreements_SendAgreementPaymentRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_SendAgreementPaymentRequest-response-currencyCode"></a>
The currency code for the charge amount (e.g., `USD`).
Type: String
Length Constraints: Fixed length of 3.
Pattern: `[A-Z]+`

 ** [description](#API_marketplace-agreements_SendAgreementPaymentRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_SendAgreementPaymentRequest-response-description"></a>
The detailed description of the payment request, if provided.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.

 ** [name](#API_marketplace-agreements_SendAgreementPaymentRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_SendAgreementPaymentRequest-response-name"></a>
The descriptive name of the payment request.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 64.
Pattern: `.+`

 ** [paymentRequestId](#API_marketplace-agreements_SendAgreementPaymentRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_SendAgreementPaymentRequest-response-paymentRequestId"></a>
The unique identifier for the sent payment request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `pr-[a-zA-Z0-9]+`

 ** [status](#API_marketplace-agreements_SendAgreementPaymentRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_SendAgreementPaymentRequest-response-status"></a>
The current status of the payment request. The initial status is `PENDING_APPROVAL`.
Type: String
Valid Values: `VALIDATING | VALIDATION_FAILED | PENDING_APPROVAL | APPROVED | REJECTED | CANCELLED`

## Errors
<a name="API_marketplace-agreements_SendAgreementPaymentRequest_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
 ** message **
Description of the error.
 ** reason **
The reason for the access denied exception.
 ** requestId **
The unique identifier for the error.
HTTP Status Code: 400

 ** ConflictException **
Request was denied due to a resource conflict.
 ** message **
Description of the error.
 ** requestId **
The unique identifier for the error.
 ** resourceId **
The unique identifier of the resource involved in the conflict.
 ** resourceType **
The type of the resource involved in the conflict.
HTTP Status Code: 400

 ** InternalServerException **
Unexpected error during processing of request.
 ** message **
Description of the error.
 ** requestId **
The unique identifier for the error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Request references a resource which does not exist.
 ** message **
Description of the error.
 ** requestId **
The unique identifier for the error.
 ** resourceId **
The unique identifier for the resource.
 ** resourceType **
The type of resource.
HTTP Status Code: 400

 ** ThrottlingException **
Request was denied due to request throttling.
 ** message **
Description of the error.
 ** requestId **
The unique identifier for the error.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by the service.
 ** fields **
The fields associated with the error.
 ** message **
Description of the error.
 ** reason **
The reason associated with the error.
 ** requestId **
The unique identifier associated with the error.
HTTP Status Code: 400

## Examples
<a name="API_marketplace-agreements_SendAgreementPaymentRequest_Examples"></a>

### Sample request
<a name="API_marketplace-agreements_SendAgreementPaymentRequest_Example_1"></a>

This example illustrates one usage of SendAgreementPaymentRequest.

```
{
    "clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "agreementId": "fEXAMPLE-0aa6-4e42-8715-6a1EXAMPLE95",
    "termId": "termEXAMPLE-3cc8-6g64-0937-8c3EXAMPLE17",
    "name": "Q1 2024 Usage Charges",
    "chargeAmount": "1250.50",
    "description": "Payment request for Q1 2024 usage charges for premium support services"
}
```

### Sample response
<a name="API_marketplace-agreements_SendAgreementPaymentRequest_Example_2"></a>

This example illustrates one usage of SendAgreementPaymentRequest.

```
{
    "paymentRequestId": "prEXAMPLE-1bb7-5f53-9826-7b2EXAMPLE06",
    "agreementId": "fEXAMPLE-0aa6-4e42-8715-6a1EXAMPLE95",
    "status": "PENDING_APPROVAL",
    "name": "Q1 2024 Usage Charges",
    "description": "Payment request for Q1 2024 usage charges for premium support services",
    "chargeAmount": "1250.50",
    "currencyCode": "USD",
    "createdAt": 1705314600
}
```

## See Also
<a name="API_marketplace-agreements_SendAgreementPaymentRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/marketplace-agreement-2020-03-01/SendAgreementPaymentRequest)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/marketplace-agreement-2020-03-01/SendAgreementPaymentRequest)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/SendAgreementPaymentRequest)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/marketplace-agreement-2020-03-01/SendAgreementPaymentRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/SendAgreementPaymentRequest)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/marketplace-agreement-2020-03-01/SendAgreementPaymentRequest)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/marketplace-agreement-2020-03-01/SendAgreementPaymentRequest)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/marketplace-agreement-2020-03-01/SendAgreementPaymentRequest)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/marketplace-agreement-2020-03-01/SendAgreementPaymentRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/SendAgreementPaymentRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
