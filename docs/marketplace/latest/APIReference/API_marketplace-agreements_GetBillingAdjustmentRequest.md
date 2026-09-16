---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_GetBillingAdjustmentRequest.html
---

# GetBillingAdjustmentRequest
<a name="API_marketplace-agreements_GetBillingAdjustmentRequest"></a>

Retrieves detailed information about a specific billing adjustment request. Sellers (proposers) can use this operation to view the status and details of a billing adjustment request they submitted.

## Request Syntax
<a name="API_marketplace-agreements_GetBillingAdjustmentRequest_RequestSyntax"></a>

```
{
   "agreementId": "{{string}}",
   "billingAdjustmentRequestId": "{{string}}"
}
```

## Request Parameters
<a name="API_marketplace-agreements_GetBillingAdjustmentRequest_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [agreementId](#API_marketplace-agreements_GetBillingAdjustmentRequest_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_GetBillingAdjustmentRequest-request-agreementId"></a>
The unique identifier of the agreement associated with the billing adjustment request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_/-]+`
Required: Yes

 ** [billingAdjustmentRequestId](#API_marketplace-agreements_GetBillingAdjustmentRequest_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_GetBillingAdjustmentRequest-request-billingAdjustmentRequestId"></a>
The unique identifier of the billing adjustment request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `ba-[a-zA-Z0-9]+`
Required: Yes

## Response Syntax
<a name="API_marketplace-agreements_GetBillingAdjustmentRequest_ResponseSyntax"></a>

```
{
   "adjustmentAmount": "string",
   "adjustmentReasonCode": "string",
   "agreementId": "string",
   "billingAdjustmentRequestId": "string",
   "createdAt": number,
   "currencyCode": "string",
   "description": "string",
   "originalInvoiceId": "string",
   "status": "string",
   "statusMessage": "string",
   "updatedAt": number
}
```

## Response Elements
<a name="API_marketplace-agreements_GetBillingAdjustmentRequest_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [adjustmentAmount](#API_marketplace-agreements_GetBillingAdjustmentRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_GetBillingAdjustmentRequest-response-adjustmentAmount"></a>
The adjustment amount as a string representation of a decimal number.
Type: String
Pattern: `[0-9]*(\.[0-9]{0,8})?`

 ** [adjustmentReasonCode](#API_marketplace-agreements_GetBillingAdjustmentRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_GetBillingAdjustmentRequest-response-adjustmentReasonCode"></a>
The reason code for the billing adjustment.
Type: String
Valid Values: `INCORRECT_TERMS_ACCEPTED | INCORRECT_METERING | TEST_ENVIRONMENT_CHARGES | ALTERNATIVE_PROCUREMENT_CHANNEL | UNINTENDED_RENEWAL | BUYER_DISSATISFACTION | OTHER`

 ** [agreementId](#API_marketplace-agreements_GetBillingAdjustmentRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_GetBillingAdjustmentRequest-response-agreementId"></a>
The unique identifier of the agreement associated with this billing adjustment request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_/-]+`

 ** [billingAdjustmentRequestId](#API_marketplace-agreements_GetBillingAdjustmentRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_GetBillingAdjustmentRequest-response-billingAdjustmentRequestId"></a>
The unique identifier of the billing adjustment request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `ba-[a-zA-Z0-9]+`

 ** [createdAt](#API_marketplace-agreements_GetBillingAdjustmentRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_GetBillingAdjustmentRequest-response-createdAt"></a>
The date and time when the billing adjustment request was created.
Type: Timestamp

 ** [currencyCode](#API_marketplace-agreements_GetBillingAdjustmentRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_GetBillingAdjustmentRequest-response-currencyCode"></a>
The currency code for the adjustment amount (e.g., `USD`).
Type: String
Length Constraints: Fixed length of 3.
Pattern: `[A-Z]+`

 ** [originalInvoiceId](#API_marketplace-agreements_GetBillingAdjustmentRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_GetBillingAdjustmentRequest-response-originalInvoiceId"></a>
The identifier of the original invoice being adjusted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [status](#API_marketplace-agreements_GetBillingAdjustmentRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_GetBillingAdjustmentRequest-response-status"></a>
The current status of the billing adjustment request.
Type: String
Valid Values: `PENDING | VALIDATION_FAILED | COMPLETED`

 ** [updatedAt](#API_marketplace-agreements_GetBillingAdjustmentRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_GetBillingAdjustmentRequest-response-updatedAt"></a>
The date and time when the billing adjustment request was last updated.
Type: Timestamp

 ** [description](#API_marketplace-agreements_GetBillingAdjustmentRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_GetBillingAdjustmentRequest-response-description"></a>
The detailed description of the billing adjustment reason, if provided.
Type: String

 ** [statusMessage](#API_marketplace-agreements_GetBillingAdjustmentRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_GetBillingAdjustmentRequest-response-statusMessage"></a>
A message providing additional context about the billing adjustment request status. This field is populated only when the status is `VALIDATION_FAILED`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.

## Errors
<a name="API_marketplace-agreements_GetBillingAdjustmentRequest_Errors"></a>

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
<a name="API_marketplace-agreements_GetBillingAdjustmentRequest_Examples"></a>

### Sample request
<a name="API_marketplace-agreements_GetBillingAdjustmentRequest_Example_1"></a>

This example illustrates one usage of GetBillingAdjustmentRequest.

```
{
    "billingAdjustmentRequestId": "ba-EXAMPLE1a2b3c4d5e",
    "agreementId": "agmt-EXAMPLESvIzsqYMyQwI3"
}
```

### Sample response
<a name="API_marketplace-agreements_GetBillingAdjustmentRequest_Example_2"></a>

This example illustrates one usage of GetBillingAdjustmentRequest.

```
{
    "billingAdjustmentRequestId": "ba-EXAMPLE1a2b3c4d5e",
    "agreementId": "agmt-EXAMPLESvIzsqYMyQwI3",
    "adjustmentReasonCode": "OTHER",
    "description": "Customer requested adjustment due to service outage",
    "originalInvoiceId": "E2E20230929a108cfae",
    "adjustmentAmount": "500.00",
    "currencyCode": "USD",
    "status": "PENDING",
    "createdAt": 1750793400,
    "updatedAt": 1750793400
}
```

## See Also
<a name="API_marketplace-agreements_GetBillingAdjustmentRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/marketplace-agreement-2020-03-01/GetBillingAdjustmentRequest)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/marketplace-agreement-2020-03-01/GetBillingAdjustmentRequest)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/GetBillingAdjustmentRequest)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/marketplace-agreement-2020-03-01/GetBillingAdjustmentRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/GetBillingAdjustmentRequest)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/marketplace-agreement-2020-03-01/GetBillingAdjustmentRequest)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/marketplace-agreement-2020-03-01/GetBillingAdjustmentRequest)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/marketplace-agreement-2020-03-01/GetBillingAdjustmentRequest)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/marketplace-agreement-2020-03-01/GetBillingAdjustmentRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/GetBillingAdjustmentRequest)
