---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_CreateAgreementRequest.html
---

# CreateAgreementRequest
<a name="API_marketplace-agreements_CreateAgreementRequest"></a>

Creates an agreement request that acts as a quote for the terms you want to accept. The agreement request captures the requested terms, calculates charges, and returns a summary. Use `AcceptAgreementRequest` with the returned `agreementRequestId` to finalize the agreement.

## Request Syntax
<a name="API_marketplace-agreements_CreateAgreementRequest_RequestSyntax"></a>

```
{
   "agreementProposalIdentifier": "{{string}}",
   "clientToken": "{{string}}",
   "intent": "{{string}}",
   "requestedTerms": [
      {
         "configuration": { ... },
         "id": "{{string}}"
      }
   ],
   "sourceAgreementIdentifier": "{{string}}",
   "taxConfiguration": {
      "taxEstimation": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_marketplace-agreements_CreateAgreementRequest_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [intent](#API_marketplace-agreements_CreateAgreementRequest_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_CreateAgreementRequest-request-intent"></a>
The purpose and desired outcome of the agreement request. This is a required parameter that determines how the agreement request is processed.
+  `NEW` – Creates a new agreement for terms in the request.
+  `AMEND` – Modifies an existing agreement with terms that are accepted in the request.
+  `REPLACE` – Creates a new agreement with accepted terms and replaces the existing agreement.
Type: String
Valid Values: `NEW | AMEND | REPLACE`
Required: Yes

 ** [requestedTerms](#API_marketplace-agreements_CreateAgreementRequest_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_CreateAgreementRequest-request-requestedTerms"></a>
A list of terms that define what is being accepted as part of the agreement. Some terms require configuration.
Type: Array of [RequestedTerm](API_marketplace-agreements_RequestedTerm.md) objects
Array Members: Minimum number of 1 item. Maximum number of 30 items.
Required: Yes

 ** [agreementProposalIdentifier](#API_marketplace-agreements_CreateAgreementRequest_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_CreateAgreementRequest-request-agreementProposalIdentifier"></a>
The agreement proposal signed by the proposer. The proposal includes the requested resources and the terms that outline an agreement outcome.
 This parameter is required if the intent is not `AMEND`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(at-|ap-)[A-Za-z0-9]+`
Required: No

 ** [clientToken](#API_marketplace-agreements_CreateAgreementRequest_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_CreateAgreementRequest-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`
Required: No

 ** [sourceAgreementIdentifier](#API_marketplace-agreements_CreateAgreementRequest_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_CreateAgreementRequest-request-sourceAgreementIdentifier"></a>
The agreement's identifier that the request acts upon.
 This parameter is required for all non-`NEW` intents (i.e., `AMEND` or `REPLACE`). Don't provide this parameter if the intent is `NEW`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_/-]+`
Required: No

 ** [taxConfiguration](#API_marketplace-agreements_CreateAgreementRequest_RequestSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_CreateAgreementRequest-request-taxConfiguration"></a>
Configuration for tax estimation in the agreement request response.
Type: [TaxConfiguration](API_marketplace-agreements_TaxConfiguration.md) object
Required: No

## Response Syntax
<a name="API_marketplace-agreements_CreateAgreementRequest_ResponseSyntax"></a>

```
{
   "agreementRequestId": "string",
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
   }
}
```

## Response Elements
<a name="API_marketplace-agreements_CreateAgreementRequest_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [agreementRequestId](#API_marketplace-agreements_CreateAgreementRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_CreateAgreementRequest-response-agreementRequestId"></a>
The unique identifier of the agreement request created. Use this identifier with `AcceptAgreementRequest` to accept the agreement.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `ar-[A-Za-z0-9]+`

 ** [chargeSummary](#API_marketplace-agreements_CreateAgreementRequest_ResponseSyntax) **   <a name="AWSMarketplaceService-marketplace-agreements_CreateAgreementRequest-response-chargeSummary"></a>
Provides details of the charges associated with the agreement request. This is only applicable when a request is created for `PurchaseAgreement`.
Type: [ChargeSummary](API_marketplace-agreements_ChargeSummary.md) object

## Errors
<a name="API_marketplace-agreements_CreateAgreementRequest_Errors"></a>

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

 ** ServiceQuotaExceededException **
Request exceeded the maximum allowed limit (quota) for a specific resource or API operation.
 ** message **
Description of the error.
 ** quotaCode **
The code of the quota that was exceeded.
 ** requestId **
The unique identifier for the error.
 ** resourceId **
The unique identifier of the resource that exceeded the quota.
 ** resourceType **
The type of the resource that exceeded the quota.
 ** serviceCode **
The code of the service whose quota was exceeded.
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
<a name="API_marketplace-agreements_CreateAgreementRequest_Examples"></a>

### Sample request
<a name="API_marketplace-agreements_CreateAgreementRequest_Example_1"></a>

This example illustrates one usage of CreateAgreementRequest.

```
{
    "clientToken": "75298638-97dc-4588-bd5b-e7d5a40f1367",
    "intent": "NEW",
    "requestedTerms": [
        {
            "id": "term-EXAMPLE1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d",
            "configuration": {
                "configurableUpfrontPricingTermConfiguration": {
                    "selectorValue": "P12M",
                    "dimensions": [
                        {
                            "dimensionKey": "AdminUsers",
                            "dimensionValue": 5
                        },
                        {
                            "dimensionKey": "ReadOnlyUsers",
                            "dimensionValue": 10
                        }
                    ]
                }
            }
        },
        {
            "id": "term-EXAMPLE2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e",
            "configuration": {
                "renewalTermConfiguration": {
                    "enableAutoRenew": false
                }
            }
        },
        {
            "id": "term-EXAMPLE3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f"
        }
    ],
    "agreementProposalIdentifier": "ap-EXAMPLE6b64-0c26-8e5EXAMPLE12"
}
```

### Sample response
<a name="API_marketplace-agreements_CreateAgreementRequest_Example_2"></a>

This example illustrates one usage of CreateAgreementRequest.

```
{
    "agreementRequestId": "ar-EXAMPLE4a53-9b12-3d4EXAMPLE78",
    "chargeSummary": {
        "currencyCode": "USD",
        "newAgreementValue": "100",
        "expectedCharges": [
            {
                "id": "ch-EXAMPLE4b42-9614-5c3EXAMPLE56",
                "amount": "100",
                "time": null,
                "timing": "ON_ACCEPTANCE"
            },
            {
                "id": "ch-EXAMPLE5c53-0725-6d4EXAMPLE67",
                "amount": null,
                "time": null,
                "timing": "BILLING_PERIOD"
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
    }
}
```

## See Also
<a name="API_marketplace-agreements_CreateAgreementRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/marketplace-agreement-2020-03-01/CreateAgreementRequest)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/marketplace-agreement-2020-03-01/CreateAgreementRequest)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/CreateAgreementRequest)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/marketplace-agreement-2020-03-01/CreateAgreementRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/CreateAgreementRequest)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/marketplace-agreement-2020-03-01/CreateAgreementRequest)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/marketplace-agreement-2020-03-01/CreateAgreementRequest)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/marketplace-agreement-2020-03-01/CreateAgreementRequest)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/marketplace-agreement-2020-03-01/CreateAgreementRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/CreateAgreementRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
