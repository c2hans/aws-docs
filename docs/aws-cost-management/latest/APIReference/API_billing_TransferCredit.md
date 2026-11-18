---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_TransferCredit.html
---

# TransferCredit
<a name="API_billing_TransferCredit"></a>

Moves a credit to another account in the same consolidated billing family. The credit keeps its ID, balance, end date, and applicable products. Only the account that owns the credit changes.

The transfer removes the credit's sharing settings. The new owner or the payer can set them again. Any amount reserved for a bill that isn't finalized moves with the credit and still applies to that bill.

You must be the payer of both accounts. You can't transfer a credit that has ended, has no available balance, or is the original credit of a split. A transfer creates no credit, so it doesn't count toward the split limit, and the payer can transfer the credit back. This operation is idempotent and supports a dry run.

## Request Syntax
<a name="API_billing_TransferCredit_RequestSyntax"></a>

```
{
   "clientToken": "{{string}}",
   "creditId": "{{string}}",
   "destinationAccountId": "{{string}}",
   "dryRun": {{boolean}}
}
```

## Request Parameters
<a name="API_billing_TransferCredit_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [clientToken](#API_billing_TransferCredit_RequestSyntax) **   <a name="awscostmanagement-billing_TransferCredit-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure that the operation completes no more than one time. If you retry a successful request with the same client token and parameters, the retry completes without performing any further actions. If you reuse a client token with different parameters, the request fails with a `ValidationException`.
Type: String
Pattern: `[a-zA-Z0-9-]+`
Required: No

 ** [creditId](#API_billing_TransferCredit_RequestSyntax) **   <a name="awscostmanagement-billing_TransferCredit-request-creditId"></a>
The ID of the credit to transfer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[0-9]+`
Required: Yes

 ** [destinationAccountId](#API_billing_TransferCredit_RequestSyntax) **   <a name="awscostmanagement-billing_TransferCredit-request-destinationAccountId"></a>
The AWS account ID that becomes the owner of the credit. The account must be in your consolidated billing family and must not be the current owner.
Type: String
Pattern: `[0-9]{12}`
Required: Yes

 ** [dryRun](#API_billing_TransferCredit_RequestSyntax) **   <a name="awscostmanagement-billing_TransferCredit-request-dryRun"></a>
Specifies whether to validate the request and return the result without changing the credit.
Type: Boolean
Required: No

## Response Syntax
<a name="API_billing_TransferCredit_ResponseSyntax"></a>

```
{
   "amount": "string",
   "destinationAccountId": "string",
   "dryRun": boolean,
   "newCreditId": "string",
   "sourceCreditId": "string"
}
```

## Response Elements
<a name="API_billing_TransferCredit_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [amount](#API_billing_TransferCredit_ResponseSyntax) **   <a name="awscostmanagement-billing_TransferCredit-response-amount"></a>
The available balance of the credit, which is its remaining balance minus any amount reserved for a bill that isn't finalized.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[0-9]{1,25}(\.[0-9]{1,6})?`

 ** [destinationAccountId](#API_billing_TransferCredit_ResponseSyntax) **   <a name="awscostmanagement-billing_TransferCredit-response-destinationAccountId"></a>
The AWS account ID that owns the credit after the transfer.
Type: String
Pattern: `[0-9]{12}`

 ** [dryRun](#API_billing_TransferCredit_ResponseSyntax) **   <a name="awscostmanagement-billing_TransferCredit-response-dryRun"></a>
Specifies whether the request was a dry run. If `true`, the operation didn't change the credit.
Type: Boolean

 ** [newCreditId](#API_billing_TransferCredit_ResponseSyntax) **   <a name="awscostmanagement-billing_TransferCredit-response-newCreditId"></a>
Always the same as `sourceCreditId`, because a transfer moves the credit and creates no new one. A dry run omits this field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[0-9]+`

 ** [sourceCreditId](#API_billing_TransferCredit_ResponseSyntax) **   <a name="awscostmanagement-billing_TransferCredit-response-sourceCreditId"></a>
The ID of the transferred credit. The credit keeps this ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[0-9]+`

## Errors
<a name="API_billing_TransferCredit_Errors"></a>

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

 ** ServiceQuotaExceededException **
 You've reached the limit of resources you can create, or exceeded the size of an individual resource.
 ** quotaCode **
 The container for the `quotaCode`.
 ** resourceId **
 The ID of the resource.
 ** resourceType **
 The type of AWS resource.
 ** serviceCode **
 The container for the `serviceCode`.
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
<a name="API_billing_TransferCredit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/billing-2023-09-07/TransferCredit)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/billing-2023-09-07/TransferCredit)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/TransferCredit)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/billing-2023-09-07/TransferCredit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/TransferCredit)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/billing-2023-09-07/TransferCredit)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/billing-2023-09-07/TransferCredit)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/billing-2023-09-07/TransferCredit)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/billing-2023-09-07/TransferCredit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/TransferCredit)
