---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_RejectAgreementPaymentRequest.html
---

# RejectAgreementPaymentRequest
<a name="API_marketplace-agreements_RejectAgreementPaymentRequest"></a>

Allows buyers (acceptors) to reject a payment request that is in `PENDING_APPROVAL` status. Once rejected, the payment request transitions to `REJECTED` status and cannot be accepted. Buyers can optionally provide a reason for the rejection.

**Note**
Only payment requests in `PENDING_APPROVAL` status can be rejected. A `ConflictException` is thrown if the payment request is in any other status.

## Request Syntax
<a name="API_marketplace-agreements_RejectAgreementPaymentRequest_RequestSyntax"></a>

```
{
   "agreementId": "{{string}}",
   "paymentRequestId": "{{string}}",
   "rejectionReason": "{{string}}"
}
```

## Request Parameters
<a name="API_marketplace-agreements_RejectAgreementPaymentRequest_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [agreementId](#API_marketplace-agreements_RejectAgreementPaymentRequest_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_RejectAgreementPaymentRequest-request-agreementId"></a>
The unique identifier of the agreement associated with the payment request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_/-]+`
Required: Yes

 ** [paymentRequestId](#API_marketplace-agreements_RejectAgreementPaymentRequest_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_RejectAgreementPaymentRequest-request-paymentRequestId"></a>
The unique identifier of the payment request to reject.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `pr-[a-zA-Z0-9]+`
Required: Yes

 ** [rejectionReason](#API_marketplace-agreements_RejectAgreementPaymentRequest_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_RejectAgreementPaymentRequest-request-rejectionReason"></a>
An optional reason for rejecting the payment request (1-250 characters). This message is visible to the seller.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 250.
Required: No

## Response Syntax
<a name="API_marketplace-agreements_RejectAgreementPaymentRequest_ResponseSyntax"></a>

```
{
   "agreementId": "string",
   "chargeAmount": "string",
   "createdAt": number,
   "currencyCode": "string",
   "description": "string",
   "name": "string",
   "paymentRequestId": "string",
   "status": "string",
   "statusMessage": "string",
   "updatedAt": number
}
```

## Response Elements
<a name="API_marketplace-agreements_RejectAgreementPaymentRequest_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [agreementId](#API_marketplace-agreements_RejectAgreementPaymentRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_RejectAgreementPaymentRequest-response-agreementId"></a>
The unique identifier of the agreement associated with this payment request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_/-]+`

 ** [chargeAmount](#API_marketplace-agreements_RejectAgreementPaymentRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_RejectAgreementPaymentRequest-response-chargeAmount"></a>
The amount that was requested to be charged.
Type: String
Pattern: `[0-9]*(\.[0-9]{0,8})?`

 ** [createdAt](#API_marketplace-agreements_RejectAgreementPaymentRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_RejectAgreementPaymentRequest-response-createdAt"></a>
The date and time when the payment request was originally created.
Type: Timestamp

 ** [currencyCode](#API_marketplace-agreements_RejectAgreementPaymentRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_RejectAgreementPaymentRequest-response-currencyCode"></a>
The currency code for the charge amount.
Type: String
Length Constraints: Fixed length of 3.
Pattern: `[A-Z]+`

 ** [description](#API_marketplace-agreements_RejectAgreementPaymentRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_RejectAgreementPaymentRequest-response-description"></a>
The detailed description of the payment request, if provided.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.

 ** [name](#API_marketplace-agreements_RejectAgreementPaymentRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_RejectAgreementPaymentRequest-response-name"></a>
The descriptive name of the payment request.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 64.
Pattern: `.+`

 ** [paymentRequestId](#API_marketplace-agreements_RejectAgreementPaymentRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_RejectAgreementPaymentRequest-response-paymentRequestId"></a>
The unique identifier of the rejected payment request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `pr-[a-zA-Z0-9]+`

 ** [status](#API_marketplace-agreements_RejectAgreementPaymentRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_RejectAgreementPaymentRequest-response-status"></a>
The updated status of the payment request, which is `REJECTED`.
Type: String
Valid Values: `VALIDATING | VALIDATION_FAILED | PENDING_APPROVAL | APPROVED | REJECTED | CANCELLED`

 ** [statusMessage](#API_marketplace-agreements_RejectAgreementPaymentRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_RejectAgreementPaymentRequest-response-statusMessage"></a>
The rejection reason provided by the buyer, if any.
Type: String

 ** [updatedAt](#API_marketplace-agreements_RejectAgreementPaymentRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_RejectAgreementPaymentRequest-response-updatedAt"></a>
The date and time when the payment request was rejected.
Type: Timestamp

## Errors
<a name="API_marketplace-agreements_RejectAgreementPaymentRequest_Errors"></a>

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
<a name="API_marketplace-agreements_RejectAgreementPaymentRequest_Examples"></a>

### Sample request
<a name="API_marketplace-agreements_RejectAgreementPaymentRequest_Example_1"></a>

This example illustrates one usage of RejectAgreementPaymentRequest.

```
{
    "paymentRequestId": "prEXAMPLE-1bb7-5f53-9826-7b2EXAMPLE06",
    "agreementId": "fEXAMPLE-0aa6-4e42-8715-6a1EXAMPLE95",
    "rejectionReason": "Charges do not match agreed upon services"
}
```

### Sample response
<a name="API_marketplace-agreements_RejectAgreementPaymentRequest_Example_2"></a>

This example illustrates one usage of RejectAgreementPaymentRequest.

```
{
    "paymentRequestId": "prEXAMPLE-1bb7-5f53-9826-7b2EXAMPLE06",
    "agreementId": "fEXAMPLE-0aa6-4e42-8715-6a1EXAMPLE95",
    "status": "REJECTED",
    "statusMessage": "Charges do not match agreed upon services",
    "name": "Q1 2024 Usage Charges",
    "description": "Payment request for Q1 2024 usage charges for premium support services",
    "chargeAmount": "1250.50",
    "currencyCode": "USD",
    "createdAt": 1705314600,
    "updatedAt": 1705414800
}
```

## See Also
<a name="API_marketplace-agreements_RejectAgreementPaymentRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/marketplace-agreement-2020-03-01/RejectAgreementPaymentRequest)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/marketplace-agreement-2020-03-01/RejectAgreementPaymentRequest)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/RejectAgreementPaymentRequest)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/marketplace-agreement-2020-03-01/RejectAgreementPaymentRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/RejectAgreementPaymentRequest)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/marketplace-agreement-2020-03-01/RejectAgreementPaymentRequest)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/marketplace-agreement-2020-03-01/RejectAgreementPaymentRequest)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/marketplace-agreement-2020-03-01/RejectAgreementPaymentRequest)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/marketplace-agreement-2020-03-01/RejectAgreementPaymentRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/RejectAgreementPaymentRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
