---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_GetAgreementPaymentRequest.html
---

# GetAgreementPaymentRequest
<a name="API_marketplace-agreements_GetAgreementPaymentRequest"></a>

Retrieves detailed information about a specific payment request. Both sellers (proposers) and buyers (acceptors) can use this operation to view payment requests associated with their agreements. The response includes the current status, charge details, timestamps, and the charge ID if the request has been approved.

**Note**
The calling identity must be either the acceptor or proposer of the payment request. A `ResourceNotFoundException` is returned if the payment request does not exist.

## Request Syntax
<a name="API_marketplace-agreements_GetAgreementPaymentRequest_RequestSyntax"></a>

```
{
   "agreementId": "{{string}}",
   "paymentRequestId": "{{string}}"
}
```

## Request Parameters
<a name="API_marketplace-agreements_GetAgreementPaymentRequest_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [agreementId](#API_marketplace-agreements_GetAgreementPaymentRequest_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_GetAgreementPaymentRequest-request-agreementId"></a>
The unique identifier of the agreement associated with the payment request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_/-]+`
Required: Yes

 ** [paymentRequestId](#API_marketplace-agreements_GetAgreementPaymentRequest_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_GetAgreementPaymentRequest-request-paymentRequestId"></a>
The identifier of the payment request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `pr-[a-zA-Z0-9]+`
Required: Yes

## Response Syntax
<a name="API_marketplace-agreements_GetAgreementPaymentRequest_ResponseSyntax"></a>

```
{
   "agreementId": "string",
   "chargeAmount": "string",
   "chargeId": "string",
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
<a name="API_marketplace-agreements_GetAgreementPaymentRequest_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [agreementId](#API_marketplace-agreements_GetAgreementPaymentRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_GetAgreementPaymentRequest-response-agreementId"></a>
The unique identifier of the agreement associated with this payment request. Use `DescribeAgreement` to retrieve full agreement details.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_/-]+`

 ** [chargeAmount](#API_marketplace-agreements_GetAgreementPaymentRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_GetAgreementPaymentRequest-response-chargeAmount"></a>
The amount charged or to be charged to the buyer.
Type: String
Pattern: `[0-9]*(\.[0-9]{0,8})?`

 ** [chargeId](#API_marketplace-agreements_GetAgreementPaymentRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_GetAgreementPaymentRequest-response-chargeId"></a>
The unique identifier of the charge created after the payment request is approved. This field is only present for approved payment requests and follows the pattern `ch-[a-zA-Z0-9]+`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `ch-[a-zA-Z0-9]+`

 ** [createdAt](#API_marketplace-agreements_GetAgreementPaymentRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_GetAgreementPaymentRequest-response-createdAt"></a>
The date and time when the payment request was created.
Type: Timestamp

 ** [currencyCode](#API_marketplace-agreements_GetAgreementPaymentRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_GetAgreementPaymentRequest-response-currencyCode"></a>
The currency code for the charge amount.
Type: String
Length Constraints: Fixed length of 3.
Pattern: `[A-Z]+`

 ** [description](#API_marketplace-agreements_GetAgreementPaymentRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_GetAgreementPaymentRequest-response-description"></a>
The detailed description of the payment request, if provided.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.

 ** [name](#API_marketplace-agreements_GetAgreementPaymentRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_GetAgreementPaymentRequest-response-name"></a>
The descriptive name of the payment request.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 64.
Pattern: `.+`

 ** [paymentRequestId](#API_marketplace-agreements_GetAgreementPaymentRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_GetAgreementPaymentRequest-response-paymentRequestId"></a>
The unique identifier of the payment request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `pr-[a-zA-Z0-9]+`

 ** [status](#API_marketplace-agreements_GetAgreementPaymentRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_GetAgreementPaymentRequest-response-status"></a>
The current status of the payment request. Possible values include:
+  `VALIDATING` – The payment request is being validated against agreement terms.
+  `VALIDATION_FAILED` – The payment request failed validation.
+  `PENDING_APPROVAL` – The payment request is awaiting buyer action.
+  `APPROVED` – The buyer has approved the payment request.
+  `REJECTED` – The buyer has rejected the payment request.
+  `CANCELLED` – The seller has cancelled the payment request.
Type: String
Valid Values: `VALIDATING | VALIDATION_FAILED | PENDING_APPROVAL | APPROVED | REJECTED | CANCELLED`

 ** [statusMessage](#API_marketplace-agreements_GetAgreementPaymentRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_GetAgreementPaymentRequest-response-statusMessage"></a>
An optional message providing additional context about the payment request status, such as a rejection reason or validation failure details.
Type: String

 ** [updatedAt](#API_marketplace-agreements_GetAgreementPaymentRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_GetAgreementPaymentRequest-response-updatedAt"></a>
The date and time when the payment request was last updated.
Type: Timestamp

## Errors
<a name="API_marketplace-agreements_GetAgreementPaymentRequest_Errors"></a>

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
<a name="API_marketplace-agreements_GetAgreementPaymentRequest_Examples"></a>

### Sample request
<a name="API_marketplace-agreements_GetAgreementPaymentRequest_Example_1"></a>

This example illustrates one usage of GetAgreementPaymentRequest.

```
{
    "paymentRequestId": "prEXAMPLE-1bb7-5f53-9826-7b2EXAMPLE06",
    "agreementId": "fEXAMPLE-0aa6-4e42-8715-6a1EXAMPLE95"
}
```

### Sample response
<a name="API_marketplace-agreements_GetAgreementPaymentRequest_Example_2"></a>

This example illustrates one usage of GetAgreementPaymentRequest.

```
{
    "paymentRequestId": "prEXAMPLE-1bb7-5f53-9826-7b2EXAMPLE06",
    "agreementId": "fEXAMPLE-0aa6-4e42-8715-6a1EXAMPLE95",
    "status": "APPROVED",
    "name": "Q1 2024 Usage Charges",
    "description": "Payment request for Q1 2024 usage charges for premium support services",
    "chargeId": "chEXAMPLE-4dd9-7h75-1048-9d4EXAMPLE28",
    "chargeAmount": "1250.50",
    "currencyCode": "USD",
    "createdAt": 1705314600,
    "updatedAt": 1705405500
}
```

## See Also
<a name="API_marketplace-agreements_GetAgreementPaymentRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/marketplace-agreement-2020-03-01/GetAgreementPaymentRequest)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/marketplace-agreement-2020-03-01/GetAgreementPaymentRequest)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/GetAgreementPaymentRequest)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/marketplace-agreement-2020-03-01/GetAgreementPaymentRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/GetAgreementPaymentRequest)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/marketplace-agreement-2020-03-01/GetAgreementPaymentRequest)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/marketplace-agreement-2020-03-01/GetAgreementPaymentRequest)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/marketplace-agreement-2020-03-01/GetAgreementPaymentRequest)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/marketplace-agreement-2020-03-01/GetAgreementPaymentRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/GetAgreementPaymentRequest)
