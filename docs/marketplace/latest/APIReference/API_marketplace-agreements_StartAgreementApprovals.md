---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_StartAgreementApprovals.html
---

# StartAgreementApprovals

Allows buyers (acceptors) to start the approvals that their organization requires for an agreement request. You start one agreement approval for each approval plan that you specify. Use `GetAgreementRequestApprovalPlans` to retrieve the approval plans of the agreement request. Once the agreement approvals start, the agreement request transitions to `PENDING_APPROVAL` status.

## Request Syntax
<a name="API_marketplace-agreements_StartAgreementApprovals_RequestSyntax"></a>

```
{
   "agreementRequestId": "{{string}}",
   "planInputs": [
      { ... }
   ],
   "purchaseOrders": [
      {
         "chargeId": "{{string}}",
         "purchaseOrderReference": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_marketplace-agreements_StartAgreementApprovals_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [agreementRequestId](#API_marketplace-agreements_StartAgreementApprovals_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_StartAgreementApprovals-request-agreementRequestId"></a>
The unique identifier of the agreement request to start approvals for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `ar-[A-Za-z0-9]+`
Required: Yes

 ** [planInputs](#API_marketplace-agreements_StartAgreementApprovals_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_StartAgreementApprovals-request-planInputs"></a>
The approval plans to start agreement approvals for.
Type: Array of [AgreementApprovalPlanInput](API_marketplace-agreements_AgreementApprovalPlanInput.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

 ** [purchaseOrders](#API_marketplace-agreements_StartAgreementApprovals_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_StartAgreementApprovals-request-purchaseOrders"></a>
An optional list of purchase order references to associate with charges on the agreement request.
Type: Array of [AgreementApprovalPurchaseOrder](API_marketplace-agreements_AgreementApprovalPurchaseOrder.md) objects
Array Members: Minimum number of 1 item. Maximum number of 86 items.
Required: No

## Response Syntax
<a name="API_marketplace-agreements_StartAgreementApprovals_ResponseSyntax"></a>

```
{
   "approvalSummaries": [
      {
         "agreementApprovalId": "string",
         "agreementRequestId": "string",
         "approvalNeededBy": number,
         "approvalType": "string",
         "createdAt": number,
         "expiresAt": number,
         "name": "string",
         "startedAt": number,
         "status": "string",
         "updatedAt": number
      }
   ]
}
```

## Response Elements
<a name="API_marketplace-agreements_StartAgreementApprovals_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [approvalSummaries](#API_marketplace-agreements_StartAgreementApprovals_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_StartAgreementApprovals-response-approvalSummaries"></a>
An array of `AgreementApprovalSummary` objects, one for each agreement approval that was started.
Type: Array of [AgreementApprovalSummary](API_marketplace-agreements_AgreementApprovalSummary.md) objects

## Errors
<a name="API_marketplace-agreements_StartAgreementApprovals_Errors"></a>

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
<a name="API_marketplace-agreements_StartAgreementApprovals_Examples"></a>

### Sample request
<a name="API_marketplace-agreements_StartAgreementApprovals_Example_1"></a>

This example illustrates one usage of StartAgreementApprovals.

```
{
    "agreementRequestId": "ar-EXAMPLE4a53-9b12-3d4EXAMPLE78",
    "planInputs": [
        {
            "buyerAgreementApprovalPlanInput": {
                "planReference": "aplan-EXAMPLE7g8h9i0j1k2l",
                "requesterNote": "Annual subscription for the data platform team."
            }
        }
    ],
    "purchaseOrders": [
        {
            "chargeId": "ch-EXAMPLE4b42-9614-5c3EXAMPLE56",
            "purchaseOrderReference": "PO-123"
        }
    ]
}
```

### Sample response
<a name="API_marketplace-agreements_StartAgreementApprovals_Example_2"></a>

This example illustrates one usage of StartAgreementApprovals.

```
{
    "approvalSummaries": [
        {
            "approvalType": "BUYER_AGREEMENT_APPROVAL",
            "agreementRequestId": "ar-EXAMPLE4a53-9b12-3d4EXAMPLE78",
            "agreementApprovalId": "apr-EXAMPLE9s0t1u2v3w4x",
            "name": "Example Analytics Platform sold by Example Corp",
            "status": "PENDING_APPROVAL",
            "createdAt": 1736935800,
            "updatedAt": 1736935800,
            "startedAt": 1736935800,
            "expiresAt": 1739527800,
            "approvalNeededBy": 1739527800
        }
    ]
}
```

## See Also
<a name="API_marketplace-agreements_StartAgreementApprovals_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/marketplace-agreement-2020-03-01/StartAgreementApprovals)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/marketplace-agreement-2020-03-01/StartAgreementApprovals)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/StartAgreementApprovals)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/marketplace-agreement-2020-03-01/StartAgreementApprovals)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/StartAgreementApprovals)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/marketplace-agreement-2020-03-01/StartAgreementApprovals)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/marketplace-agreement-2020-03-01/StartAgreementApprovals)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/marketplace-agreement-2020-03-01/StartAgreementApprovals)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/marketplace-agreement-2020-03-01/StartAgreementApprovals)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/StartAgreementApprovals)
