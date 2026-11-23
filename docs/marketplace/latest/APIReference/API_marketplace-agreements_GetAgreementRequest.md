---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_GetAgreementRequest.html
---

# GetAgreementRequest

Retrieves detailed information about a specific agreement request, including its status, intent, approval requirement, and charges. The acceptor, or the management account or a delegated administrator of the acceptor's AWS organization, can call this operation.

## Request Syntax
<a name="API_marketplace-agreements_GetAgreementRequest_RequestSyntax"></a>

```
{
   "agreementRequestId": "{{string}}"
}
```

## Request Parameters
<a name="API_marketplace-agreements_GetAgreementRequest_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [agreementRequestId](#API_marketplace-agreements_GetAgreementRequest_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_GetAgreementRequest-request-agreementRequestId"></a>
The unique identifier of the agreement request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `ar-[A-Za-z0-9]+`
Required: Yes

## Response Syntax
<a name="API_marketplace-agreements_GetAgreementRequest_ResponseSyntax"></a>

```
{
   "agreementId": "string",
   "agreementRequestId": "string",
   "agreementType": "string",
   "approvalRequirement": "string",
   "chargeSummary": {
      "currencyCode": "string",
      "estimatedTaxes": {
         "breakdown": [
            {
               "amount": "string",
               "rate": "string",
               "type": "string"
            }
         ],
         "totalAmount": "string"
      },
      "expectedCharges": [
         {
            "amount": "string",
            "amountAfterTax": "string",
            "estimatedTaxes": {
               "breakdown": [
                  {
                     "amount": "string",
                     "rate": "string",
                     "type": "string"
                  }
               ],
               "totalAmount": "string"
            },
            "id": "string",
            "purchaseOrderReference": "string",
            "time": number,
            "timing": "string"
         }
      ],
      "invoicingEntity": {
         "branchName": "string",
         "legalName": "string"
      },
      "itemizedCharges": [
         {
            "chargeReference": "string",
            "dimensionKey": "string",
            "incrementalChargeAmount": "string",
            "newQuantity": number,
            "oldQuantity": number
         }
      ],
      "newAgreementValue": "string",
      "newAgreementValueAfterTax": "string"
   },
   "createdAt": number,
   "intent": "string",
   "proposalSummary": {
      "offerId": "string",
      "offerSetId": "string",
      "resources": [
         {
            "id": "string",
            "type": "string"
         }
      ]
   },
   "proposer": {
      "accountId": "string"
   },
   "status": "string"
}
```

## Response Elements
<a name="API_marketplace-agreements_GetAgreementRequest_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [agreementId](#API_marketplace-agreements_GetAgreementRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_GetAgreementRequest-response-agreementId"></a>
The unique identifier of the agreement that the agreement request is for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_/-]+`

 ** [agreementRequestId](#API_marketplace-agreements_GetAgreementRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_GetAgreementRequest-response-agreementRequestId"></a>
The unique identifier of the agreement request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `ar-[A-Za-z0-9]+`

 ** [agreementType](#API_marketplace-agreements_GetAgreementRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_GetAgreementRequest-response-agreementType"></a>
The type of agreement (for example, `PurchaseAgreement`).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z]+`

 ** [approvalRequirement](#API_marketplace-agreements_GetAgreementRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_GetAgreementRequest-response-approvalRequirement"></a>
Indicates whether the agreement request requires approval before it can be accepted. Values are `REQUIRED` and `NOT_REQUIRED`.
Type: String
Valid Values: `REQUIRED | NOT_REQUIRED`

 ** [chargeSummary](#API_marketplace-agreements_GetAgreementRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_GetAgreementRequest-response-chargeSummary"></a>
Provides details of the charges associated with the agreement request. This is only applicable when a request is created for `PurchaseAgreement`.
Type: [ChargeSummary](API_marketplace-agreements_ChargeSummary.md) object

 ** [createdAt](#API_marketplace-agreements_GetAgreementRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_GetAgreementRequest-response-createdAt"></a>
The date and time when the agreement request was created.
Type: Timestamp

 ** [intent](#API_marketplace-agreements_GetAgreementRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_GetAgreementRequest-response-intent"></a>
The purpose and desired outcome of the agreement request.
+  `NEW` – Creates a new agreement for terms in the request.
+  `AMEND` – Modifies an existing agreement with terms that are accepted in the request.
+  `REPLACE` – Creates a new agreement with accepted terms and replaces the existing agreement.
Type: String
Valid Values: `NEW | AMEND | REPLACE`

 ** [proposalSummary](#API_marketplace-agreements_GetAgreementRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_GetAgreementRequest-response-proposalSummary"></a>
A summary of the proposal received from the proposer.
Type: [ProposalSummary](API_marketplace-agreements_ProposalSummary.md) object

 ** [proposer](#API_marketplace-agreements_GetAgreementRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_GetAgreementRequest-response-proposer"></a>
The details of the party proposing the agreement terms. This is commonly the seller for `PurchaseAgreement`.
Type: [Proposer](API_marketplace-agreements_Proposer.md) object

 ** [status](#API_marketplace-agreements_GetAgreementRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_GetAgreementRequest-response-status"></a>
The current status of the agreement request. Possible values include:
+  `DRAFT` – The agreement request has been created but not yet submitted for approval.
+  `PENDING_APPROVAL` – The agreement request is waiting for one or more approvers to decide.
+  `APPROVED` – All required approvals have been granted, but the agreement request wasn't accepted automatically. Call `AcceptAgreementRequest` to accept it. If the call fails, its error explains why.
+  `ACCEPTED` – The agreement request has been accepted and the resulting agreement has been created.
+  `REJECTED` – At least one approver rejected the agreement request. It won't proceed.
+  `CANCELLED` – The agreement request was cancelled before completion, by the acceptor or because the acceptor's account left its AWS organization.
Type: String
Valid Values: `DRAFT | PENDING_APPROVAL | APPROVED | ACCEPTED | REJECTED | CANCELLED`

## Errors
<a name="API_marketplace-agreements_GetAgreementRequest_Errors"></a>

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
<a name="API_marketplace-agreements_GetAgreementRequest_Examples"></a>

### Sample request
<a name="API_marketplace-agreements_GetAgreementRequest_Example_1"></a>

This example illustrates one usage of GetAgreementRequest.

```
{
    "agreementRequestId": "ar-EXAMPLE4a53-9b12-3d4EXAMPLE78"
}
```

### Sample response
<a name="API_marketplace-agreements_GetAgreementRequest_Example_2"></a>

This example illustrates one usage of GetAgreementRequest.

```
{
    "agreementRequestId": "ar-EXAMPLE4a53-9b12-3d4EXAMPLE78",
    "agreementType": "PurchaseAgreement",
    "status": "PENDING_APPROVAL",
    "approvalRequirement": "REQUIRED",
    "intent": "NEW",
    "createdAt": 1736935800,
    "chargeSummary": {
        "currencyCode": "USD",
        "newAgreementValue": "100",
        "expectedCharges": [
            {
                "id": "ch-EXAMPLE4b42-9614-5c3EXAMPLE56",
                "purchaseOrderReference": "PO-123",
                "amount": "100",
                "timing": "ON_ACCEPTANCE"
            }
        ],
        "itemizedCharges": [
            {
                "dimensionKey": "AdminUsers",
                "newQuantity": 5,
                "oldQuantity": 0,
                "incrementalChargeAmount": "50",
                "chargeReference": "ch-EXAMPLE4b42-9614-5c3EXAMPLE56"
            },
            {
                "dimensionKey": "ReadOnlyUsers",
                "newQuantity": 10,
                "oldQuantity": 0,
                "incrementalChargeAmount": "50",
                "chargeReference": "ch-EXAMPLE4b42-9614-5c3EXAMPLE56"
            }
        ]
    },
    "proposer": {
        "accountId": "111122223333"
    },
    "proposalSummary": {
        "resources": [
            {
                "id": "0EXAMPLE-8ce8-4814-bcf1-636EXAMPLEb5",
                "type": "SaaSProduct"
            }
        ],
        "offerId": "ABCDEFGHIJKLMNOP123"
    }
}
```

## See Also
<a name="API_marketplace-agreements_GetAgreementRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/marketplace-agreement-2020-03-01/GetAgreementRequest)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/marketplace-agreement-2020-03-01/GetAgreementRequest)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/GetAgreementRequest)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/marketplace-agreement-2020-03-01/GetAgreementRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/GetAgreementRequest)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/marketplace-agreement-2020-03-01/GetAgreementRequest)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/marketplace-agreement-2020-03-01/GetAgreementRequest)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/marketplace-agreement-2020-03-01/GetAgreementRequest)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/marketplace-agreement-2020-03-01/GetAgreementRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/GetAgreementRequest)
