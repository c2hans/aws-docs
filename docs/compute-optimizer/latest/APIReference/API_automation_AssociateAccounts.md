---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_AssociateAccounts.html
---

# AssociateAccounts
<a name="API_automation_AssociateAccounts"></a>

Associates one or more member accounts with your organization's management account, enabling centralized implementation of optimization actions across those accounts. Once associated, the management account (or a delegated administrator) can apply recommended actions to the member account. When you associate a member account, its organization rule mode is automatically set to "Any allowed," which permits the management account to create Automation rules that automatically apply actions to that account. If the member account has not previously enabled the Automation feature, the association process automatically enables it.

**Note**
Only the management account or a delegated administrator can perform this action.

## Request Syntax
<a name="API_automation_AssociateAccounts_RequestSyntax"></a>

```
{
   "accountIds": [ "{{string}}" ],
   "clientToken": "{{string}}"
}
```

## Request Parameters
<a name="API_automation_AssociateAccounts_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [accountIds](#API_automation_AssociateAccounts_RequestSyntax) **   <a name="computeoptimizer-automation_AssociateAccounts-request-accountIds"></a>
 The IDs of the member accounts to associate. You can specify up to 50 account IDs.
Type: Array of strings
Pattern: `[0-9]{12}`
Required: Yes

 ** [clientToken](#API_automation_AssociateAccounts_RequestSyntax) **   <a name="computeoptimizer-automation_AssociateAccounts-request-clientToken"></a>
 A unique identifier to ensure idempotency of the request. Valid for 24 hours after creation.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,64}`
Required: No

## Response Syntax
<a name="API_automation_AssociateAccounts_ResponseSyntax"></a>

```
{
   "accountIds": [ "string" ],
   "errors": [ "string" ]
}
```

## Response Elements
<a name="API_automation_AssociateAccounts_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [accountIds](#API_automation_AssociateAccounts_ResponseSyntax) **   <a name="computeoptimizer-automation_AssociateAccounts-response-accountIds"></a>
 The IDs of the member accounts that were successfully associated.
Type: Array of strings
Pattern: `[0-9]{12}`

 ** [errors](#API_automation_AssociateAccounts_ResponseSyntax) **   <a name="computeoptimizer-automation_AssociateAccounts-response-errors"></a>
 Any errors that occurred during the association process.
Type: Array of strings

## Errors
<a name="API_automation_AssociateAccounts_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 You do not have sufficient permissions to perform this action.
HTTP Status Code: 400

 ** ForbiddenException **
 You are not authorized to perform this action.
HTTP Status Code: 400

 ** IdempotencyTokenInUseException **
 The specified client token is already in use.
HTTP Status Code: 400

 ** IdempotentParameterMismatchException **
Exception thrown when the same client token is used with different parameters, indicating a mismatch in idempotent request parameters.
HTTP Status Code: 400

 ** InternalServerException **
 An internal error occurred while processing the request.
HTTP Status Code: 500

 ** InvalidParameterValueException **
 One or more parameter values are not valid.
HTTP Status Code: 400

 ** NotManagementAccountException **
 The operation can only be performed by a management account.
HTTP Status Code: 400

 ** OptInRequiredException **
 The account must be opted in to Compute Optimizer Automation before performing this action.
HTTP Status Code: 400

 ** ServiceUnavailableException **
 The service is temporarily unavailable.
HTTP Status Code: 500

 ** ThrottlingException **
 The request was denied due to request throttling.
HTTP Status Code: 400

## See Also
<a name="API_automation_AssociateAccounts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/compute-optimizer-automation-2025-09-22/AssociateAccounts)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/compute-optimizer-automation-2025-09-22/AssociateAccounts)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-automation-2025-09-22/AssociateAccounts)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/compute-optimizer-automation-2025-09-22/AssociateAccounts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-automation-2025-09-22/AssociateAccounts)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/compute-optimizer-automation-2025-09-22/AssociateAccounts)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/compute-optimizer-automation-2025-09-22/AssociateAccounts)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/compute-optimizer-automation-2025-09-22/AssociateAccounts)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/compute-optimizer-automation-2025-09-22/AssociateAccounts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-automation-2025-09-22/AssociateAccounts)
