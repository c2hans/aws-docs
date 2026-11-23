---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_RejectAgreementApproval.html
---

# RejectAgreementApproval

Allows the management account or a delegated administrator of the buyer's AWS organization to reject an agreement approval that is in `PENDING_APPROVAL` status, as the organization administrator approver or on behalf of another approver. Once rejected, the agreement approval and its agreement request transition to `REJECTED` status. You must provide a reason for the rejection.

## Request Syntax
<a name="API_marketplace-agreements_RejectAgreementApproval_RequestSyntax"></a>

```
{
   "buyerAgreementApprovalRejectionInput": {
      "agreementApprovalId": "{{string}}",
      "approverOutcomeIdToOverride": "{{string}}",
      "note": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_marketplace-agreements_RejectAgreementApproval_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [buyerAgreementApprovalRejectionInput](#API_marketplace-agreements_RejectAgreementApproval_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_RejectAgreementApproval-request-buyerAgreementApprovalRejectionInput"></a>
The rejection decision for an agreement approval that the buyer's organization requires.
Type: [BuyerAgreementApprovalRejectionInput](API_marketplace-agreements_BuyerAgreementApprovalRejectionInput.md) object
Required: No

## Response Elements
<a name="API_marketplace-agreements_RejectAgreementApproval_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_marketplace-agreements_RejectAgreementApproval_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
 ** message **
Description of the error.
 ** reason **
The reason for the access denied exception.
 ** requestId **
The unique identifier for the error.
HTTP Status Code: 403

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
HTTP Status Code: 409

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
HTTP Status Code: 404

 ** ThrottlingException **
Request was denied due to request throttling.
 ** message **
Description of the error.
 ** requestId **
The unique identifier for the error.
HTTP Status Code: 429

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
<a name="API_marketplace-agreements_RejectAgreementApproval_Examples"></a>

### Sample request
<a name="API_marketplace-agreements_RejectAgreementApproval_Example_1"></a>

This example illustrates one usage of RejectAgreementApproval.

```
{
    "buyerAgreementApprovalRejectionInput": {
        "agreementApprovalId": "apr-EXAMPLE9s0t1u2v3w4x",
        "note": "Rejected. This purchase isn't in the approved budget."
    }
}
```

### Sample response
<a name="API_marketplace-agreements_RejectAgreementApproval_Example_2"></a>

This example illustrates one usage of RejectAgreementApproval.

```
{}
```

## See Also
<a name="API_marketplace-agreements_RejectAgreementApproval_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/marketplace-agreement-2020-03-01/RejectAgreementApproval)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/marketplace-agreement-2020-03-01/RejectAgreementApproval)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/RejectAgreementApproval)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/marketplace-agreement-2020-03-01/RejectAgreementApproval)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/RejectAgreementApproval)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/marketplace-agreement-2020-03-01/RejectAgreementApproval)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/marketplace-agreement-2020-03-01/RejectAgreementApproval)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/marketplace-agreement-2020-03-01/RejectAgreementApproval)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/marketplace-agreement-2020-03-01/RejectAgreementApproval)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/RejectAgreementApproval)
