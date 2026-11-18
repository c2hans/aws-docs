---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_SplitCredit.html
---

# SplitCredit
<a name="API_billing_SplitCredit"></a>

Splits the available balance of a credit into 2 to 99 new credits in the same account, and cancels the original credit. The new credits keep the original credit's end date and applicable products.

The available balance is the remaining balance minus any amount reserved for a bill that isn't finalized. The portions must add up to exactly the available balance. Each portion must be at least 100.00 in the currency of the credit. For example, if the credit is in USD, each portion must be at least USD $100.00. A reserved amount stays on the original credit and still applies to that bill.

A credit and every credit split from it count toward a limit of 100 credits. After a split, you can't split or transfer the original credit. You can split or transfer its new credits, and you can split a credit after you transfer it.

You must own the credit or be the payer of the account that owns it. You can't undo a split. This operation is idempotent and supports a dry run.

## Request Syntax
<a name="API_billing_SplitCredit_RequestSyntax"></a>

```
{
   "clientToken": "{{string}}",
   "creditId": "{{string}}",
   "dryRun": {{boolean}},
   "portions": [
      {
         "amount": "{{string}}",
         "description": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_billing_SplitCredit_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [clientToken](#API_billing_SplitCredit_RequestSyntax) **   <a name="awscostmanagement-billing_SplitCredit-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure that the operation completes no more than one time. If you retry a successful request with the same client token and parameters, the retry completes without performing any further actions. If you reuse a client token with different parameters, the request fails with a `ValidationException`.
Type: String
Pattern: `[a-zA-Z0-9-]+`
Required: No

 ** [creditId](#API_billing_SplitCredit_RequestSyntax) **   <a name="awscostmanagement-billing_SplitCredit-request-creditId"></a>
The ID of the credit to split.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[0-9]+`
Required: Yes

 ** [dryRun](#API_billing_SplitCredit_RequestSyntax) **   <a name="awscostmanagement-billing_SplitCredit-request-dryRun"></a>
Specifies whether to validate the request and return the result without changing any credit.
Type: Boolean
Required: No

 ** [portions](#API_billing_SplitCredit_RequestSyntax) **   <a name="awscostmanagement-billing_SplitCredit-request-portions"></a>
The new credits to create, one for each portion, in the order listed.
Type: Array of [SplitPortion](API_billing_SplitPortion.md) objects
Array Members: Minimum number of 2 items. Maximum number of 99 items.
Required: Yes

## Response Syntax
<a name="API_billing_SplitCredit_ResponseSyntax"></a>

```
{
   "childCredits": [
      {
         "amount": "string",
         "creditId": "string"
      }
   ],
   "dryRun": boolean,
   "parentCreditId": "string"
}
```

## Response Elements
<a name="API_billing_SplitCredit_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [childCredits](#API_billing_SplitCredit_ResponseSyntax) **   <a name="awscostmanagement-billing_SplitCredit-response-childCredits"></a>
The new credits, in the order of the requested portions.
Type: Array of [ChildCredit](API_billing_ChildCredit.md) objects
Array Members: Minimum number of 2 items. Maximum number of 99 items.

 ** [dryRun](#API_billing_SplitCredit_ResponseSyntax) **   <a name="awscostmanagement-billing_SplitCredit-response-dryRun"></a>
Specifies whether the request was a dry run. If `true`, the operation didn't change any credit.
Type: Boolean

 ** [parentCreditId](#API_billing_SplitCredit_ResponseSyntax) **   <a name="awscostmanagement-billing_SplitCredit-response-parentCreditId"></a>
The ID of the credit that was split.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[0-9]+`

## Errors
<a name="API_billing_SplitCredit_Errors"></a>

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
<a name="API_billing_SplitCredit_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/billing-2023-09-07/SplitCredit)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/billing-2023-09-07/SplitCredit)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/SplitCredit)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/billing-2023-09-07/SplitCredit)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/SplitCredit)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/billing-2023-09-07/SplitCredit)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/billing-2023-09-07/SplitCredit)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/billing-2023-09-07/SplitCredit)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/billing-2023-09-07/SplitCredit)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/SplitCredit)
