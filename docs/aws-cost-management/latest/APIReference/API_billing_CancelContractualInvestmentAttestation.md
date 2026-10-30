---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_CancelContractualInvestmentAttestation.html
---

# CancelContractualInvestmentAttestation
<a name="API_billing_CancelContractualInvestmentAttestation"></a>

Cancels a contractual investment attestation. This operation is idempotent, so retrying is safe. You can cancel an attestation only while it is still pending (its `isCancellable` value is `true`).

## Request Syntax
<a name="API_billing_CancelContractualInvestmentAttestation_RequestSyntax"></a>

```
{
   "attestationId": "{{string}}",
   "contractArn": "{{string}}",
   "reason": "{{string}}"
}
```

## Request Parameters
<a name="API_billing_CancelContractualInvestmentAttestation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [attestationId](#API_billing_CancelContractualInvestmentAttestation_RequestSyntax) **   <a name="awscostmanagement-billing_CancelContractualInvestmentAttestation-request-attestationId"></a>
The identifier of the investment attestation to cancel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `[a-zA-Z0-9_\-]+`
Required: Yes

 ** [contractArn](#API_billing_CancelContractualInvestmentAttestation_RequestSyntax) **   <a name="awscostmanagement-billing_CancelContractualInvestmentAttestation-request-contractArn"></a>
The Amazon Resource Name (ARN) of the contract that contains the attested investment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Pattern: `arn:aws[a-z-]*:billing::[0-9]{12}:contract/[a-zA-Z0-9_\+=\.\@-]{0,70}[a-zA-Z0-9]`
Required: Yes

 ** [reason](#API_billing_CancelContractualInvestmentAttestation_RequestSyntax) **   <a name="awscostmanagement-billing_CancelContractualInvestmentAttestation-request-reason"></a>
The reason for the cancellation. This value can be 1 to 80 characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 80.
Required: Yes

## Response Elements
<a name="API_billing_CancelContractualInvestmentAttestation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_billing_CancelContractualInvestmentAttestation_Errors"></a>

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
<a name="API_billing_CancelContractualInvestmentAttestation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/billing-2023-09-07/CancelContractualInvestmentAttestation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/billing-2023-09-07/CancelContractualInvestmentAttestation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/CancelContractualInvestmentAttestation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/billing-2023-09-07/CancelContractualInvestmentAttestation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/CancelContractualInvestmentAttestation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/billing-2023-09-07/CancelContractualInvestmentAttestation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/billing-2023-09-07/CancelContractualInvestmentAttestation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/billing-2023-09-07/CancelContractualInvestmentAttestation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/billing-2023-09-07/CancelContractualInvestmentAttestation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/CancelContractualInvestmentAttestation)
