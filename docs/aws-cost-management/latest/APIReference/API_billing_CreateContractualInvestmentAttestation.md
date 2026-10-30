---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_CreateContractualInvestmentAttestation.html
---

# CreateContractualInvestmentAttestation
<a name="API_billing_CreateContractualInvestmentAttestation"></a>

Creates an attestation that claims an investment award for a completed milestone or outcome within a private pricing contract. Supply a `clientToken` to make the request idempotent so a safe retry does not create a duplicate attestation. This operation starts an asynchronous review and returns an `attestationId` while the attestation is pending.

## Request Syntax
<a name="API_billing_CreateContractualInvestmentAttestation_RequestSyntax"></a>

```
{
   "additionalRecipients": [
      {
         "email": "{{string}}"
      }
   ],
   "approverDetails": {
      "email": "{{string}}",
      "name": "{{string}}",
      "title": "{{string}}"
   },
   "attestationDetails": {
      "attestationValue": { ... },
      "investmentDistributions": [
         {
            "accountId": "{{string}}",
            "investmentAmount": {
               "currencyAmount": "{{string}}",
               "currencyCode": "{{string}}"
            }
         }
      ]
   },
   "clientToken": "{{string}}",
   "contractArn": "{{string}}",
   "contractDocumentId": "{{string}}",
   "investmentDisbursedAt": {{number}},
   "investmentId": "{{string}}",
   "investmentSummaryId": "{{string}}"
}
```

## Request Parameters
<a name="API_billing_CreateContractualInvestmentAttestation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [additionalRecipients](#API_billing_CreateContractualInvestmentAttestation_RequestSyntax) **   <a name="awscostmanagement-billing_CreateContractualInvestmentAttestation-request-additionalRecipients"></a>
The email addresses to copy as viewers on the executive approval request.
Type: Array of [AdditionalRecipient](API_billing_AdditionalRecipient.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** [approverDetails](#API_billing_CreateContractualInvestmentAttestation_RequestSyntax) **   <a name="awscostmanagement-billing_CreateContractualInvestmentAttestation-request-approverDetails"></a>
The details of the executive who authorized the attestation, under the terms of the private pricing contract. The executive receives a click-to-accept email to confirm the attestation.
Type: [ApproverDetails](API_billing_ApproverDetails.md) object
Required: Yes

 ** [attestationDetails](#API_billing_CreateContractualInvestmentAttestation_RequestSyntax) **   <a name="awscostmanagement-billing_CreateContractualInvestmentAttestation-request-attestationDetails"></a>
The details of the attestation, including the value being claimed and how the resulting investment is distributed across investment accounts.
Type: [AttestationDetails](API_billing_AttestationDetails.md) object
Required: Yes

 ** [clientToken](#API_billing_CreateContractualInvestmentAttestation_RequestSyntax) **   <a name="awscostmanagement-billing_CreateContractualInvestmentAttestation-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry completes without performing any further actions.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[!-~]+`
Required: No

 ** [contractArn](#API_billing_CreateContractualInvestmentAttestation_RequestSyntax) **   <a name="awscostmanagement-billing_CreateContractualInvestmentAttestation-request-contractArn"></a>
The Amazon Resource Name (ARN) of the contract that contains the investment being attested.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Pattern: `arn:aws[a-z-]*:billing::[0-9]{12}:contract/[a-zA-Z0-9_\+=\.\@-]{0,70}[a-zA-Z0-9]`
Required: Yes

 ** [contractDocumentId](#API_billing_CreateContractualInvestmentAttestation_RequestSyntax) **   <a name="awscostmanagement-billing_CreateContractualInvestmentAttestation-request-contractDocumentId"></a>
The contract ID from the contract document, located in the top-right corner of the private pricing contract pages. This value confirms that you have access to the contract.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Required: Yes

 ** [investmentDisbursedAt](#API_billing_CreateContractualInvestmentAttestation_RequestSyntax) **   <a name="awscostmanagement-billing_CreateContractualInvestmentAttestation-request-investmentDisbursedAt"></a>
The date on which the investment is disbursed to the investment accounts. The disbursement date is subject to review timelines.
Type: Timestamp
Required: No

 ** [investmentId](#API_billing_CreateContractualInvestmentAttestation_RequestSyntax) **   <a name="awscostmanagement-billing_CreateContractualInvestmentAttestation-request-investmentId"></a>
The identifier of the investment (outcome) being attested.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `[a-zA-Z0-9_\-]+`
Required: Yes

 ** [investmentSummaryId](#API_billing_CreateContractualInvestmentAttestation_RequestSyntax) **   <a name="awscostmanagement-billing_CreateContractualInvestmentAttestation-request-investmentSummaryId"></a>
The identifier of the investment summary being attested. This is the parent to the investmentId.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `[a-zA-Z0-9_\-]+`
Required: Yes

## Response Syntax
<a name="API_billing_CreateContractualInvestmentAttestation_ResponseSyntax"></a>

```
{
   "attestationId": "string"
}
```

## Response Elements
<a name="API_billing_CreateContractualInvestmentAttestation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [attestationId](#API_billing_CreateContractualInvestmentAttestation_ResponseSyntax) **   <a name="awscostmanagement-billing_CreateContractualInvestmentAttestation-response-attestationId"></a>
The identifier of the submitted attestation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `[a-zA-Z0-9_\-]+`

## Errors
<a name="API_billing_CreateContractualInvestmentAttestation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action.
HTTP Status Code: 400

 ** ConflictException **
 The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.
 ** resourceId **
 The identifier for the service resource associated with the request.
 ** resourceType **
 The type of resource associated with the request.
HTTP Status Code: 400

 ** InternalServerException **
The request processing failed because of an unknown error, exception, or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
 The specified ARN in the request doesn't exist.
 ** resourceId **
 Value is a list of resource IDs that were not found.
 ** resourceType **
 Value is the type of resource that was not found.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
 ** fieldList **
The input fails to satisfy the constraints specified by an AWS service.
 ** reason **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_billing_CreateContractualInvestmentAttestation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/billing-2023-09-07/CreateContractualInvestmentAttestation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/billing-2023-09-07/CreateContractualInvestmentAttestation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/CreateContractualInvestmentAttestation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/billing-2023-09-07/CreateContractualInvestmentAttestation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/CreateContractualInvestmentAttestation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/billing-2023-09-07/CreateContractualInvestmentAttestation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/billing-2023-09-07/CreateContractualInvestmentAttestation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/billing-2023-09-07/CreateContractualInvestmentAttestation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/billing-2023-09-07/CreateContractualInvestmentAttestation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/CreateContractualInvestmentAttestation)
