---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_SendAgreementCancellationRequest.html
---

# SendAgreementCancellationRequest
<a name="API_marketplace-agreements_SendAgreementCancellationRequest"></a>

Allows sellers (proposers) to submit a cancellation request for an active agreement. The cancellation request is created in `PENDING_APPROVAL` status, at which point the buyer can review it.

## Request Syntax
<a name="API_marketplace-agreements_SendAgreementCancellationRequest_RequestSyntax"></a>

```
{
   "agreementId": "{{string}}",
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "reasonCode": "{{string}}"
}
```

## Request Parameters
<a name="API_marketplace-agreements_SendAgreementCancellationRequest_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [agreementId](#API_marketplace-agreements_SendAgreementCancellationRequest_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_SendAgreementCancellationRequest-request-agreementId"></a>
The unique identifier of the agreement for which the cancellation request is being submitted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_/-]+`
Required: Yes

 ** [reasonCode](#API_marketplace-agreements_SendAgreementCancellationRequest_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_SendAgreementCancellationRequest-request-reasonCode"></a>
The reason code for the cancellation request.
Type: String
Valid Values: `INCORRECT_TERMS_ACCEPTED | REPLACING_AGREEMENT | TEST_AGREEMENT | ALTERNATIVE_PROCUREMENT_CHANNEL | PRODUCT_DISCONTINUED | UNINTENDED_RENEWAL | BUYER_DISSATISFACTION | OTHER`
Required: Yes

 ** [clientToken](#API_marketplace-agreements_SendAgreementCancellationRequest_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_SendAgreementCancellationRequest-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`
Required: No

 ** [description](#API_marketplace-agreements_SendAgreementCancellationRequest_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_SendAgreementCancellationRequest-request-description"></a>
An optional detailed description of the cancellation reason (1-2000 characters).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Required: No

## Response Syntax
<a name="API_marketplace-agreements_SendAgreementCancellationRequest_ResponseSyntax"></a>

```
{
   "agreementCancellationRequestId": "string",
   "agreementId": "string",
   "createdAt": number,
   "description": "string",
   "reasonCode": "string",
   "status": "string",
   "updatedAt": number
}
```

## Response Elements
<a name="API_marketplace-agreements_SendAgreementCancellationRequest_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [agreementCancellationRequestId](#API_marketplace-agreements_SendAgreementCancellationRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_SendAgreementCancellationRequest-response-agreementCancellationRequestId"></a>
The unique identifier for the created cancellation request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `acr-[a-zA-Z0-9]+`

 ** [agreementId](#API_marketplace-agreements_SendAgreementCancellationRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_SendAgreementCancellationRequest-response-agreementId"></a>
The unique identifier of the agreement.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_/-]+`

 ** [createdAt](#API_marketplace-agreements_SendAgreementCancellationRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_SendAgreementCancellationRequest-response-createdAt"></a>
The time when the cancellation request was created.
Type: Timestamp

 ** [description](#API_marketplace-agreements_SendAgreementCancellationRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_SendAgreementCancellationRequest-response-description"></a>
The detailed description of the cancellation reason, if provided.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.

 ** [reasonCode](#API_marketplace-agreements_SendAgreementCancellationRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_SendAgreementCancellationRequest-response-reasonCode"></a>
The reason code provided for the cancellation.
Type: String
Valid Values: `INCORRECT_TERMS_ACCEPTED | REPLACING_AGREEMENT | TEST_AGREEMENT | ALTERNATIVE_PROCUREMENT_CHANNEL | PRODUCT_DISCONTINUED | UNINTENDED_RENEWAL | BUYER_DISSATISFACTION | OTHER`

 ** [status](#API_marketplace-agreements_SendAgreementCancellationRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_SendAgreementCancellationRequest-response-status"></a>
The current status of the cancellation request. The initial status is `PENDING_APPROVAL`.
Type: String
Valid Values: `PENDING_APPROVAL | APPROVED | REJECTED | CANCELLED | VALIDATION_FAILED`

 ** [updatedAt](#API_marketplace-agreements_SendAgreementCancellationRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_SendAgreementCancellationRequest-response-updatedAt"></a>
The time when the cancellation request was last updated.
Type: Timestamp

## Errors
<a name="API_marketplace-agreements_SendAgreementCancellationRequest_Errors"></a>

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
<a name="API_marketplace-agreements_SendAgreementCancellationRequest_Examples"></a>

### Sample request
<a name="API_marketplace-agreements_SendAgreementCancellationRequest_Example_1"></a>

This example illustrates one usage of SendAgreementCancellationRequest.

```
{
    "agreementId": "agmt-EXAMPLE752jqvg74yo7k",
    "reasonCode": "OTHER",
    "description": "Due to budget constraints, we are unable to continue with our current subscription",
    "clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
}
```

### Sample response
<a name="API_marketplace-agreements_SendAgreementCancellationRequest_Example_2"></a>

This example illustrates one usage of SendAgreementCancellationRequest.

```
{
    "agreementId": "agmt-EXAMPLE752jqvg74yo7k",
    "agreementCancellationRequestId": "acr-EXAMPLE752jqvg74yo7k",
    "status": "PENDING_APPROVAL",
    "reasonCode": "OTHER",
    "description": "Due to budget constraints, we are unable to continue with our current subscription",
    "createdAt": 1736935800,
    "updatedAt": 1736935800
}
```

## See Also
<a name="API_marketplace-agreements_SendAgreementCancellationRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/marketplace-agreement-2020-03-01/SendAgreementCancellationRequest)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/marketplace-agreement-2020-03-01/SendAgreementCancellationRequest)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/SendAgreementCancellationRequest)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/marketplace-agreement-2020-03-01/SendAgreementCancellationRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/SendAgreementCancellationRequest)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/marketplace-agreement-2020-03-01/SendAgreementCancellationRequest)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/marketplace-agreement-2020-03-01/SendAgreementCancellationRequest)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/marketplace-agreement-2020-03-01/SendAgreementCancellationRequest)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/marketplace-agreement-2020-03-01/SendAgreementCancellationRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/SendAgreementCancellationRequest)
