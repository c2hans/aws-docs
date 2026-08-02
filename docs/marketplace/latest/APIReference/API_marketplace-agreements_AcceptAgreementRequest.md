---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_AcceptAgreementRequest.html
---

# AcceptAgreementRequest
<a name="API_marketplace-agreements_AcceptAgreementRequest"></a>

Accepts an agreement request to finalize the agreement. The acceptor can optionally provide purchase orders to associate with the agreement charges.

## Request Syntax
<a name="API_marketplace-agreements_AcceptAgreementRequest_RequestSyntax"></a>

```
{
   "agreementRequestId": "{{string}}",
   "purchaseOrders": [
      {
         "agreementId": "{{string}}",
         "chargeId": "{{string}}",
         "chargeRevision": {{number}},
         "purchaseOrderReference": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_marketplace-agreements_AcceptAgreementRequest_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [agreementRequestId](#API_marketplace-agreements_AcceptAgreementRequest_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_AcceptAgreementRequest-request-agreementRequestId"></a>
The unique identifier of the agreement request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `ar-[A-Za-z0-9]+`
Required: Yes

 ** [purchaseOrders](#API_marketplace-agreements_AcceptAgreementRequest_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_AcceptAgreementRequest-request-purchaseOrders"></a>
A list of purchase orders associated with accepting a marketplace agreement request.
Type: Array of [PurchaseOrder](API_marketplace-agreements_PurchaseOrder.md) objects
Array Members: Minimum number of 1 item. Maximum number of 86 items.
Required: No

## Response Syntax
<a name="API_marketplace-agreements_AcceptAgreementRequest_ResponseSyntax"></a>

```
{
   "agreementId": "string"
}
```

## Response Elements
<a name="API_marketplace-agreements_AcceptAgreementRequest_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [agreementId](#API_marketplace-agreements_AcceptAgreementRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_AcceptAgreementRequest-response-agreementId"></a>
The unique identifier of the agreement created or modified by accepting the agreement request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_/-]+`

## Errors
<a name="API_marketplace-agreements_AcceptAgreementRequest_Errors"></a>

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
<a name="API_marketplace-agreements_AcceptAgreementRequest_Examples"></a>

### Sample request
<a name="API_marketplace-agreements_AcceptAgreementRequest_Example_1"></a>

This example illustrates one usage of AcceptAgreementRequest.

```
{
    "agreementRequestId": "arEXAMPLE-0cc8-4a53-9b12-3d4EXAMPLE78",
    "purchaseOrders": [
        {
            "chargeId": "chEXAMPLE-1aa7-4b42-9614-5c3EXAMPLE56",
            "purchaseOrderReference": "PO-123"
        }
    ]
}
```

### Sample response
<a name="API_marketplace-agreements_AcceptAgreementRequest_Example_2"></a>

This example illustrates one usage of AcceptAgreementRequest.

```
{
    "agreementId": "fEXAMPLE-0aa6-4e42-8715-6a1EXAMPLE95"
}
```

## See Also
<a name="API_marketplace-agreements_AcceptAgreementRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/marketplace-agreement-2020-03-01/AcceptAgreementRequest)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/marketplace-agreement-2020-03-01/AcceptAgreementRequest)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/AcceptAgreementRequest)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/marketplace-agreement-2020-03-01/AcceptAgreementRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/AcceptAgreementRequest)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/marketplace-agreement-2020-03-01/AcceptAgreementRequest)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/marketplace-agreement-2020-03-01/AcceptAgreementRequest)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/marketplace-agreement-2020-03-01/AcceptAgreementRequest)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/marketplace-agreement-2020-03-01/AcceptAgreementRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/AcceptAgreementRequest)
