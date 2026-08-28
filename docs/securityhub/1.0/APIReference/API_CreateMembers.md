---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_CreateMembers.html
---

# CreateMembers
<a name="API_CreateMembers"></a>

Creates a member association in Security Hub CSPM between the specified accounts and the account used to make the request, which is the administrator account. If you are integrated with Organizations, then the administrator account is designated by the organization management account.

 `CreateMembers` is always used to add accounts that are not organization members.

For accounts that are managed using Organizations, `CreateMembers` is only used in the following cases:
+ Security Hub CSPM is not configured to automatically add new organization accounts.
+ The account was disassociated or deleted in Security Hub CSPM.

This action can only be used by an account that has Security Hub CSPM enabled. To enable Security Hub CSPM, you can use the `EnableSecurityHub` operation.

For accounts that are not organization members, you create the account association and then send an invitation to the member account. To send the invitation, you use the `InviteMembers` operation. If the account owner accepts the invitation, the account becomes a member account in Security Hub CSPM.

Accounts that are managed using Organizations don't receive an invitation. They automatically become a member account in Security Hub CSPM.
+ If the organization account does not have Security Hub CSPM enabled, then Security Hub CSPM and the default standards are automatically enabled. Note that Security Hub CSPM cannot be enabled automatically for the organization management account. The organization management account must enable Security Hub CSPM before the administrator account enables it as a member account.
+ For organization accounts that already have Security Hub CSPM enabled, Security Hub CSPM does not make any other changes to those accounts. It does not change their enabled standards or controls.

A permissions policy is added that permits the administrator account to view the findings generated in the member account.

To remove the association between the administrator and member accounts, use the `DisassociateFromMasterAccount` or `DisassociateMembers` operation.

## Request Syntax
<a name="API_CreateMembers_RequestSyntax"></a>

```
POST /members HTTP/1.1
Content-type: application/json

{
   "AccountDetails": [
      {
         "AccountId": "{{string}}",
         "Email": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateMembers_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateMembers_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AccountDetails](#API_CreateMembers_RequestSyntax) **   <a name="securityhub-CreateMembers-request-AccountDetails"></a>
The list of accounts to associate with the Security Hub CSPM administrator account. For each account, the list includes the account ID and optionally the email address.
Type: Array of [AccountDetails](API_AccountDetails.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: Yes

## Response Syntax
<a name="API_CreateMembers_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "UnprocessedAccounts": [
      {
         "AccountId": "string",
         "ProcessingResult": "string"
      }
   ]
}
```

## Response Elements
<a name="API_CreateMembers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [UnprocessedAccounts](#API_CreateMembers_ResponseSyntax) **   <a name="securityhub-CreateMembers-response-UnprocessedAccounts"></a>
The list of AWS accounts that were not processed. For each account, the list includes the account ID and the email address.
Type: Array of [Result](API_Result.md) objects

## Errors
<a name="API_CreateMembers_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action specified in the request.
HTTP Status Code: 403

 ** InternalException **
Internal server error.
HTTP Status Code: 500

 ** InvalidAccessException **
The account doesn't have permission to perform this action.
HTTP Status Code: 401

 ** InvalidInputException **
The request was rejected because you supplied an invalid or out-of-range value for an input parameter.
HTTP Status Code: 400

 ** LimitExceededException **
The request was rejected because it attempted to create resources beyond the current AWS account or throttling limits. The error code describes the limit exceeded.
HTTP Status Code: 429

 ** ResourceConflictException **
The resource specified in the request conflicts with an existing resource.
HTTP Status Code: 409

## See Also
<a name="API_CreateMembers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/CreateMembers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/CreateMembers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/CreateMembers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/CreateMembers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/CreateMembers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/CreateMembers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/CreateMembers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/CreateMembers)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/CreateMembers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/CreateMembers)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
