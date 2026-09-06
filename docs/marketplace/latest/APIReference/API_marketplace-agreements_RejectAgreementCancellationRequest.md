---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_RejectAgreementCancellationRequest.html
---

# RejectAgreementCancellationRequest
<a name="API_marketplace-agreements_RejectAgreementCancellationRequest"></a>

Allows buyers (acceptors) to reject a cancellation request that is in `PENDING_APPROVAL` status. Once rejected, the cancellation request transitions to `REJECTED` status and the agreement remains active. Buyers must provide a reason for the rejection.

**Note**
Only cancellation requests in `PENDING_APPROVAL` status can be rejected. A `ConflictException` is thrown if the cancellation request is in any other status.

## Request Syntax
<a name="API_marketplace-agreements_RejectAgreementCancellationRequest_RequestSyntax"></a>

```
{
   "agreementCancellationRequestId": "{{string}}",
   "agreementId": "{{string}}",
   "rejectionReason": "{{string}}"
}
```

## Request Parameters
<a name="API_marketplace-agreements_RejectAgreementCancellationRequest_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [agreementCancellationRequestId](#API_marketplace-agreements_RejectAgreementCancellationRequest_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_RejectAgreementCancellationRequest-request-agreementCancellationRequestId"></a>
The unique identifier of the cancellation request to reject.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `acr-[a-zA-Z0-9]+`
Required: Yes

 ** [agreementId](#API_marketplace-agreements_RejectAgreementCancellationRequest_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_RejectAgreementCancellationRequest-request-agreementId"></a>
The unique identifier of the agreement associated with the cancellation request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_/-]+`
Required: Yes

 ** [rejectionReason](#API_marketplace-agreements_RejectAgreementCancellationRequest_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_RejectAgreementCancellationRequest-request-rejectionReason"></a>
The reason for rejecting the cancellation request (1-2000 characters). This message is visible to the seller.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.
Required: Yes

## Response Syntax
<a name="API_marketplace-agreements_RejectAgreementCancellationRequest_ResponseSyntax"></a>

```
{
   "agreementCancellationRequestId": "string",
   "agreementId": "string",
   "createdAt": number,
   "description": "string",
   "reasonCode": "string",
   "status": "string",
   "statusMessage": "string",
   "updatedAt": number
}
```

## Response Elements
<a name="API_marketplace-agreements_RejectAgreementCancellationRequest_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [agreementCancellationRequestId](#API_marketplace-agreements_RejectAgreementCancellationRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_RejectAgreementCancellationRequest-response-agreementCancellationRequestId"></a>
The unique identifier of the rejected cancellation request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `acr-[a-zA-Z0-9]+`

 ** [agreementId](#API_marketplace-agreements_RejectAgreementCancellationRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_RejectAgreementCancellationRequest-response-agreementId"></a>
The unique identifier of the agreement associated with this cancellation request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_/-]+`

 ** [createdAt](#API_marketplace-agreements_RejectAgreementCancellationRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_RejectAgreementCancellationRequest-response-createdAt"></a>
The date and time when the cancellation request was originally created.
Type: Timestamp

 ** [description](#API_marketplace-agreements_RejectAgreementCancellationRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_RejectAgreementCancellationRequest-response-description"></a>
The detailed description of the cancellation reason, if provided.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.

 ** [reasonCode](#API_marketplace-agreements_RejectAgreementCancellationRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_RejectAgreementCancellationRequest-response-reasonCode"></a>
The original reason code provided when the cancellation request was created.
Type: String
Valid Values: `INCORRECT_TERMS_ACCEPTED | REPLACING_AGREEMENT | TEST_AGREEMENT | ALTERNATIVE_PROCUREMENT_CHANNEL | PRODUCT_DISCONTINUED | UNINTENDED_RENEWAL | BUYER_DISSATISFACTION | OTHER`

 ** [status](#API_marketplace-agreements_RejectAgreementCancellationRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_RejectAgreementCancellationRequest-response-status"></a>
The updated status of the cancellation request, which is `REJECTED`.
Type: String
Valid Values: `PENDING_APPROVAL | APPROVED | REJECTED | CANCELLED | VALIDATION_FAILED`

 ** [statusMessage](#API_marketplace-agreements_RejectAgreementCancellationRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_RejectAgreementCancellationRequest-response-statusMessage"></a>
The rejection reason provided by the buyer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2000.

 ** [updatedAt](#API_marketplace-agreements_RejectAgreementCancellationRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_RejectAgreementCancellationRequest-response-updatedAt"></a>
The date and time when the cancellation request was rejected.
Type: Timestamp

## Errors
<a name="API_marketplace-agreements_RejectAgreementCancellationRequest_Errors"></a>

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
<a name="API_marketplace-agreements_RejectAgreementCancellationRequest_Examples"></a>

### Sample request
<a name="API_marketplace-agreements_RejectAgreementCancellationRequest_Example_1"></a>

This example illustrates one usage of RejectAgreementCancellationRequest.

```
{
    "agreementCancellationRequestId": "acr-EXAMPLE752jqvg74yo7k",
    "agreementId": "agmt-EXAMPLE752jqvg74yo7k",
    "rejectionReason": "Still using the product"
}
```

### Sample response
<a name="API_marketplace-agreements_RejectAgreementCancellationRequest_Example_2"></a>

This example illustrates one usage of RejectAgreementCancellationRequest.

```
{
    "agreementCancellationRequestId": "acr-EXAMPLE752jqvg74yo7k",
    "agreementId": "agmt-EXAMPLE752jqvg74yo7k",
    "reasonCode": "PRODUCT_DISCONTINUED",
    "description": "Product is being discontinued and no longer supported",
    "status": "REJECTED",
    "statusMessage": "Still using the product",
    "createdAt": 1736935800,
    "updatedAt": 1737022200
}
```

## See Also
<a name="API_marketplace-agreements_RejectAgreementCancellationRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/marketplace-agreement-2020-03-01/RejectAgreementCancellationRequest)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/marketplace-agreement-2020-03-01/RejectAgreementCancellationRequest)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/RejectAgreementCancellationRequest)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/marketplace-agreement-2020-03-01/RejectAgreementCancellationRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/RejectAgreementCancellationRequest)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/marketplace-agreement-2020-03-01/RejectAgreementCancellationRequest)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/marketplace-agreement-2020-03-01/RejectAgreementCancellationRequest)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/marketplace-agreement-2020-03-01/RejectAgreementCancellationRequest)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/marketplace-agreement-2020-03-01/RejectAgreementCancellationRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/RejectAgreementCancellationRequest)
