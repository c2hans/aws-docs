---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_GetAgreementApproval.html
---

# GetAgreementApproval

Retrieves detailed information about a specific agreement approval, including its approval levels, the approvers at each level, and the decision of each approver. The acceptor, or the management account or a delegated administrator of the acceptor's AWS organization, can call this operation.

## Request Syntax
<a name="API_marketplace-agreements_GetAgreementApproval_RequestSyntax"></a>

```
{
   "agreementApprovalId": "{{string}}"
}
```

## Request Parameters
<a name="API_marketplace-agreements_GetAgreementApproval_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [agreementApprovalId](#API_marketplace-agreements_GetAgreementApproval_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_GetAgreementApproval-request-agreementApprovalId"></a>
The unique identifier of the agreement approval to retrieve.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `apr-[A-Za-z0-9]+`
Required: Yes

## Response Syntax
<a name="API_marketplace-agreements_GetAgreementApproval_ResponseSyntax"></a>

```
{
   "buyerAgreementApproval": {
      "agreementApprovalId": "string",
      "agreementRequestId": "string",
      "approvalNeededBy": number,
      "approvalType": "string",
      "createdAt": number,
      "expiresAt": number,
      "levels": [
         {
            "groups": [
               {
                  "approvalCriteria": {
                     "requiredApprovalCount": number
                  },
                  "approvers": [
                     { ... }
                  ]
               }
            ],
            "name": "string"
         }
      ],
      "name": "string",
      "planInput": {
         "planReference": "string",
         "requesterNote": "string"
      },
      "proposalSummary": {
         "offerId": "string",
         "offerSetId": "string",
         "resources": [
            {
               "deployedOnAws": "string",
               "id": "string",
               "name": "string",
               "type": "string"
            }
         ],
         "visibilityScope": "string"
      },
      "proposer": {
         "accountId": "string",
         "legalName": "string"
      },
      "requester": {
         "accountId": "string"
      },
      "startedAt": number,
      "status": "string",
      "updatedAt": number
   }
}
```

## Response Elements
<a name="API_marketplace-agreements_GetAgreementApproval_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [buyerAgreementApproval](#API_marketplace-agreements_GetAgreementApproval_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_GetAgreementApproval-response-buyerAgreementApproval"></a>
The details of the agreement approval, when it is a `BUYER_AGREEMENT_APPROVAL`.
Type: [BuyerAgreementApproval](API_marketplace-agreements_BuyerAgreementApproval.md) object

## Errors
<a name="API_marketplace-agreements_GetAgreementApproval_Errors"></a>

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
<a name="API_marketplace-agreements_GetAgreementApproval_Examples"></a>

### Sample request
<a name="API_marketplace-agreements_GetAgreementApproval_Example_1"></a>

This example illustrates one usage of GetAgreementApproval.

```
{
    "agreementApprovalId": "apr-EXAMPLE9s0t1u2v3w4x"
}
```

### Sample response
<a name="API_marketplace-agreements_GetAgreementApproval_Example_2"></a>

This example illustrates one usage of GetAgreementApproval.

```
{
    "buyerAgreementApproval": {
        "approvalType": "BUYER_AGREEMENT_APPROVAL",
        "agreementApprovalId": "apr-EXAMPLE9s0t1u2v3w4x",
        "name": "Example Analytics Platform sold by Example Corp",
        "agreementRequestId": "ar-EXAMPLE4a53-9b12-3d4EXAMPLE78",
        "status": "PENDING_APPROVAL",
        "requester": {
            "accountId": "111122223333"
        },
        "createdAt": 1736935800,
        "updatedAt": 1737022200,
        "startedAt": 1736935800,
        "expiresAt": 1739527800,
        "approvalNeededBy": 1739527800,
        "levels": [
            {
                "name": "Budget owner review",
                "groups": [
                    {
                        "approvalCriteria": {
                            "requiredApprovalCount": 1
                        },
                        "approvers": [
                            {
                                "emailApproverOutcome": {
"approverOutcomeId": "aprout-EXAMPLE5y6z7a8b9c0d",
                                    "emailAddress": "richard_roe@example.com",
                                    "name": "Richard Roe",
                                    "status": "APPROVED",
                                    "note": "Approved. Budget confirmed for this fiscal year.",
                                    "updatedAt": 1737022200,
                                    "purchaseOrders": [
                                        {
                                            "chargeId": "ch-EXAMPLE4b42-9614-5c3EXAMPLE56",
                                            "purchaseOrderReference": "PO-123"
                                        }
                                    ]
                                }
                            },
                            {
                                "awsOrganizationApproverOutcome": {
                                    "approverOutcomeId": "aprout-EXAMPLE1e2f3g4h5i6j",
                                    "status": "SKIPPED",
                                    "updatedAt": 1737022200
                                }
                            }
                        ]
                    }
                ]
            },
            {
                "name": "Procurement review",
                "groups": [
                    {
                        "approvalCriteria": {
                            "requiredApprovalCount": 1
                        },
                        "approvers": [
                            {
                                "procurementToolApproverOutcome": {
"name": "Example procurement system",
                                    "status": "QUEUED",
                                    "updatedAt": 1737022200
                                }
                            }
                        ]
                    }
                ]
            }
        ],
        "planInput": {
            "planReference": "aplan-EXAMPLE7g8h9i0j1k2l",
            "requesterNote": "Annual subscription for the data platform team."
        },
        "proposer": {
            "accountId": "111122223333",
            "legalName": "Example Corp"
        },
        "proposalSummary": {
            "offerId": "ABCDEFGHIJKLMNOP123",
            "resources": [
                {
                    "id": "0EXAMPLE-8ce8-4814-bcf1-636EXAMPLEb5",
                    "type": "SaaSProduct",
                    "name": "Example Analytics Platform",
                    "deployedOnAws": "DEPLOYED"
                }
            ],
            "visibilityScope": "PRIVATE"
        }
    }
}
```

## See Also
<a name="API_marketplace-agreements_GetAgreementApproval_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/marketplace-agreement-2020-03-01/GetAgreementApproval)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/marketplace-agreement-2020-03-01/GetAgreementApproval)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/GetAgreementApproval)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/marketplace-agreement-2020-03-01/GetAgreementApproval)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/GetAgreementApproval)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/marketplace-agreement-2020-03-01/GetAgreementApproval)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/marketplace-agreement-2020-03-01/GetAgreementApproval)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/marketplace-agreement-2020-03-01/GetAgreementApproval)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/marketplace-agreement-2020-03-01/GetAgreementApproval)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/GetAgreementApproval)
