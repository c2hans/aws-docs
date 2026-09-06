---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_AcceptAgreementPaymentRequest.html
---

# AcceptAgreementPaymentRequest
<a name="API_marketplace-agreements_AcceptAgreementPaymentRequest"></a>

Allows buyers (acceptors) to accept a payment request that is in `PENDING_APPROVAL` status. Once accepted, the payment request transitions to `APPROVED` status and the charge will be processed. Buyers can optionally provide a purchase order reference for their internal tracking.

**Note**
Only payment requests in `PENDING_APPROVAL` status can be accepted. A `ConflictException` is thrown if the payment request is in any other status.

## Request Syntax
<a name="API_marketplace-agreements_AcceptAgreementPaymentRequest_RequestSyntax"></a>

```
{
   "agreementId": "{{string}}",
   "paymentRequestId": "{{string}}",
   "purchaseOrderReference": "{{string}}"
}
```

## Request Parameters
<a name="API_marketplace-agreements_AcceptAgreementPaymentRequest_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [agreementId](#API_marketplace-agreements_AcceptAgreementPaymentRequest_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_AcceptAgreementPaymentRequest-request-agreementId"></a>
The unique identifier of the agreement associated with the payment request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_/-]+`
Required: Yes

 ** [paymentRequestId](#API_marketplace-agreements_AcceptAgreementPaymentRequest_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_AcceptAgreementPaymentRequest-request-paymentRequestId"></a>
The unique identifier of the payment request to accept.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `pr-[a-zA-Z0-9]+`
Required: Yes

 ** [purchaseOrderReference](#API_marketplace-agreements_AcceptAgreementPaymentRequest_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_AcceptAgreementPaymentRequest-request-purchaseOrderReference"></a>
An optional purchase order reference that buyers can provide to associate the payment request with their internal purchase order system.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## Response Syntax
<a name="API_marketplace-agreements_AcceptAgreementPaymentRequest_ResponseSyntax"></a>

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
   "updatedAt": number
}
```

## Response Elements
<a name="API_marketplace-agreements_AcceptAgreementPaymentRequest_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [agreementId](#API_marketplace-agreements_AcceptAgreementPaymentRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_AcceptAgreementPaymentRequest-response-agreementId"></a>
The unique identifier of the agreement associated with this payment request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_/-]+`

 ** [chargeAmount](#API_marketplace-agreements_AcceptAgreementPaymentRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_AcceptAgreementPaymentRequest-response-chargeAmount"></a>
The amount that was approved to be charged.
Type: String
Pattern: `[0-9]*(\.[0-9]{0,8})?`

 ** [createdAt](#API_marketplace-agreements_AcceptAgreementPaymentRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_AcceptAgreementPaymentRequest-response-createdAt"></a>
The date and time when the payment request was originally created.
Type: Timestamp

 ** [currencyCode](#API_marketplace-agreements_AcceptAgreementPaymentRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_AcceptAgreementPaymentRequest-response-currencyCode"></a>
The currency code for the charge amount.
Type: String
Length Constraints: Fixed length of 3.
Pattern: `[A-Z]+`

 ** [description](#API_marketplace-agreements_AcceptAgreementPaymentRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_AcceptAgreementPaymentRequest-response-description"></a>
The detailed description of the payment request, if provided.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.

 ** [name](#API_marketplace-agreements_AcceptAgreementPaymentRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_AcceptAgreementPaymentRequest-response-name"></a>
The descriptive name of the payment request.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 64.
Pattern: `.+`

 ** [paymentRequestId](#API_marketplace-agreements_AcceptAgreementPaymentRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_AcceptAgreementPaymentRequest-response-paymentRequestId"></a>
The unique identifier of the accepted payment request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `pr-[a-zA-Z0-9]+`

 ** [status](#API_marketplace-agreements_AcceptAgreementPaymentRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_AcceptAgreementPaymentRequest-response-status"></a>
The updated status of the payment request, which is `APPROVED`.
Type: String
Valid Values: `VALIDATING | VALIDATION_FAILED | PENDING_APPROVAL | APPROVED | REJECTED | CANCELLED`

 ** [updatedAt](#API_marketplace-agreements_AcceptAgreementPaymentRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_AcceptAgreementPaymentRequest-response-updatedAt"></a>
The date and time when the payment request was accepted.
Type: Timestamp

## Errors
<a name="API_marketplace-agreements_AcceptAgreementPaymentRequest_Errors"></a>

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
<a name="API_marketplace-agreements_AcceptAgreementPaymentRequest_Examples"></a>

### Sample request
<a name="API_marketplace-agreements_AcceptAgreementPaymentRequest_Example_1"></a>

This example illustrates one usage of AcceptAgreementPaymentRequest.

```
{
    "paymentRequestId": "prEXAMPLE-1bb7-5f53-9826-7b2EXAMPLE06",
    "agreementId": "fEXAMPLE-0aa6-4e42-8715-6a1EXAMPLE95",
    "purchaseOrderReference": "PO-2024-Q1-12345"
}
```

### Sample response
<a name="API_marketplace-agreements_AcceptAgreementPaymentRequest_Example_2"></a>

This example illustrates one usage of AcceptAgreementPaymentRequest.

```
{
    "paymentRequestId": "prEXAMPLE-1bb7-5f53-9826-7b2EXAMPLE06",
    "agreementId": "fEXAMPLE-0aa6-4e42-8715-6a1EXAMPLE95",
    "status": "APPROVED",
    "name": "Q1 2024 Usage Charges",
    "description": "Payment request for Q1 2024 usage charges for premium support services",
    "chargeAmount": "1250.50",
    "currencyCode": "USD",
    "createdAt": 1705314600,
    "updatedAt": 1705405500
}
```

## See Also
<a name="API_marketplace-agreements_AcceptAgreementPaymentRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/marketplace-agreement-2020-03-01/AcceptAgreementPaymentRequest)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/marketplace-agreement-2020-03-01/AcceptAgreementPaymentRequest)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/AcceptAgreementPaymentRequest)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/marketplace-agreement-2020-03-01/AcceptAgreementPaymentRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/AcceptAgreementPaymentRequest)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/marketplace-agreement-2020-03-01/AcceptAgreementPaymentRequest)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/marketplace-agreement-2020-03-01/AcceptAgreementPaymentRequest)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/marketplace-agreement-2020-03-01/AcceptAgreementPaymentRequest)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/marketplace-agreement-2020-03-01/AcceptAgreementPaymentRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/AcceptAgreementPaymentRequest)
